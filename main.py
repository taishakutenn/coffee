import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


class CoffeInformation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("main.ui", self)
        self.getCoffeeInfoButton.clicked.connect(self.get_coffee_information)

    def get_coffee_information(self):
        self.showCoffeeInfoList.clear()
        conn = sqlite3.connect("coffee.sqlite")
        cur = conn.cursor()
        sql = '''SELECT * FROM coffe'''
        response = cur.execute(sql).fetchall()
        self.show_coffe(response)
        conn.close()

    def show_coffe(self, response):
        for i in response:
            self.showCoffeeInfoList.addItem(f"id: {i[0]}\nНазвание сорта: {i[1]}\nСтепень обжарки: {i[2]}"
                                            f"\nМолотый или нет: {i[3]}\nОписание вкуса: {i[4]}\nЦена: {i[5]} руб. за {i[6]} г.\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CoffeInformation()
    win.show()
    sys.exit(app.exec())