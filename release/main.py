import sys
import sqlite3

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from addEditCoffeeForm import Ui_Form
from main_ui import Ui_MainWindow


class CoffeInformation(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.getCoffeeInfoButton.clicked.connect(self.get_coffee_information)
        self.changeCoffeeInformationButton.clicked.connect(self.change_information)

    def get_coffee_information(self):
        self.showCoffeeInfoList.clear()
        conn = sqlite3.connect("data/coffee.sqlite")
        cur = conn.cursor()
        sql = '''SELECT * FROM coffe'''
        response = cur.execute(sql).fetchall()
        self.show_coffe(response)
        conn.close()

    def show_coffe(self, response):
        for i in response:
            self.showCoffeeInfoList.addItem(f"id: {i[0]}\nНазвание сорта: {i[1]}\nСтепень обжарки: {i[2]}"
                                            f"\nМолотый или нет: {i[3]}\nОписание вкуса: {i[4]}\nЦена: {i[5]} руб. за {i[6]} г.\n")

    def change_information(self):
        self.new_win = ChangingCoffeeInformation()
        self.new_win.show()


class ChangingCoffeeInformation(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createNewCoffeInfoButton.clicked.connect(self.create_new_info)
        self.changeCoffeeInfoButton.clicked.connect(self.change_info)

    def create_new_info(self):
        info = (self.nameSortEdit.text(), self.objarkaEdit.text(), self.molotiOrZernaButton.text(),
                self.descriptionButton.text(), self.priceEdit.text(), self.volumeButton.text())
        conn = sqlite3.connect("data/coffee.sqlite")
        cur = conn.cursor()
        sql = '''INSERT INTO coffe(variety_name, degree_doneness, ground_or_grains, description_taste, price, packaging_volume)
                 VALUES (?, ?, ?, ?, ?, ?)'''
        cur.execute(sql, info)
        conn.commit()
        conn.close()
        self.close()

    def change_info(self):
        info = (self.nameSortEdit.text(), self.objarkaEdit.text(), self.molotiOrZernaButton.text(),
                self.descriptionButton.text(), self.priceEdit.text(), self.volumeButton.text(), self.idEdit.text())
        conn = sqlite3.connect("data/coffee.sqlite")
        cur = conn.cursor()
        sql = '''UPDATE coffe
                 SET variety_name = ?,
                 degree_doneness = ?,
                 ground_or_grains = ?, 
                 description_taste = ?,
                 price = ?,
                 packaging_volume = ?
                 WHERE id = ?'''
        cur.execute(sql, info)
        conn.commit()
        conn.close()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CoffeInformation()
    win.show()
    sys.exit(app.exec())
