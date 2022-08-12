from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget, QApplication, QHBoxLayout, QListWidget, QLineEdit, QTextEdit
import json
# Cоздание окна и приложения
app = QApplication([])
window = QWidget()



text_edit_countries = QTextEdit()
line_head = QHBoxLayout()
line_countries = QVBoxLayout()
line_label = QVBoxLayout()

list_dict = {}

with open('countries.json', 'w', encoding='utf-8') as file:
    json.dump(list_dict, file)

country_add = QLineEdit()
button_add_country = QPushButton("Добавить книгу")
button_clear = QPushButton('Очистить')
button_del = QPushButton('Удалить книгу')
button_edit = QPushButton('Изменить данные')
country_add.setPlaceholderText('Введите книгу для добавления')
line_buttons = QHBoxLayout()



widget_countries = QListWidget()
with open('countries.json', 'r', encoding='utf-8') as file:
    dict_countries = json.load(file)
    widget_countries.addItems(dict_countries.keys())

line_countries.addWidget(widget_countries)
line_label.addWidget(text_edit_countries, stretch = 2)
line_label.addWidget(country_add, stretch=1)
line_buttons.addWidget(button_add_country, alignment=Qt.AlignCenter, stretch=1)
line_buttons.addWidget(button_del, alignment=Qt.AlignCenter, stretch=1)
line_buttons.addWidget(button_edit, alignment=Qt.AlignCenter, stretch=1)
line_buttons.addWidget(button_clear, alignment=Qt.AlignCenter, stretch=1)
line_label.addLayout(line_buttons, stretch=1)
line_head.addLayout(line_countries, stretch=2)
line_head.addLayout(line_label, stretch=3)
window.setLayout(line_head)

def info_country():
    country = widget_countries.currentItem().text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
        text_edit_countries.setText(dict_countries[country])

def add_country():
    dict_countries = ''
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
    with open('countries.json', 'w', encoding='utf-8') as file:
        country = country_add.text()
        dict_countries[country] = text_edit_countries.toPlainText()
        json.dump(dict_countries, file)
        widget_countries.clear()
        widget_countries.addItems(dict_countries.keys())

def clear_widgets():
    country_add.clear()
    text_edit_countries.clear()

def delete_country():
    country = widget_countries.currentItem().text()
    dict_countries = ''
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
    del dict_countries[country]
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(dict_countries, file)
        clear_widgets()
        widget_countries.clear()
        widget_countries.addItems(dict_countries.keys())

def edit_country():
    country = widget_countries.currentItem().text()
    description = text_edit_countries.toPlainText()
    dict_countries = ''
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
    with open('countries.json', 'w', encoding='utf-8') as file:
        dict_countries[country] = description
        json.dump(dict_countries, file)
        clear_widgets()
        widget_countries.clear()
        widget_countries.addItems(dict_countries.keys())
    

button_add_country.clicked.connect(add_country)
button_del.clicked.connect(delete_country)
button_clear.clicked.connect(clear_widgets)
button_edit.clicked.connect(edit_country)
widget_countries.itemClicked.connect(info_country)

window.show()
app.exec()