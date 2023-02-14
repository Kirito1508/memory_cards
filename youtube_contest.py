from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QMessageBox,QRadioButton
def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно!\nвы выграли гироскутер')
    victory_win.exec()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Нет, в 2015 году\nВы выйграли фирменный плакат')
    victory_win.exec()


app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс от Crazy People')
question = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
layoutV=QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
win.setLayout(layoutV)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)
#отображение окна приложения 
win.show()
app.exec()