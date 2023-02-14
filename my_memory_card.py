from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QButtonGroup, QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QMessageBox,QRadioButton,QGroupBox
from random import*
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def next_question():
    win.total+=1
    cur_question = randint(0,len(question_list)-1)
    ask(question_list[cur_question])    
def click_OK():
    if  button.text()=='Ответить':
        check_answer()
    else:
        next_question()
def show_question():
    box.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    box.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        win.score+=1
        print('Статистика\n-Всего вопросов:',win.total,'\n-Правильных ответов:',win.score)
        print('Рейтинг:',(win.score/win.total*100),'%')
        show_correct('Правильно!')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        print('Статистика\n-Всего вопросов:',win.total,'\n-Правильных ответов:',win.score)
        print('Рейтинг:',(win.score/win.total*100),'%')
        show_correct('Неверно')
app = QApplication([])
win = QWidget()
win.setWindowTitle('Memory Card')
label=QLabel('Какой национальности не существует')
button=QPushButton('Ответить')
box = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()
layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)
layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)
box.setLayout(layout_1)
AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct,alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line_1 = QHBoxLayout()
layout_line_2 = QHBoxLayout()
layout_line_3 = QHBoxLayout()
layout_line_1.addWidget(label, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line_2.addWidget(box)
layout_line_2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line_3.addStretch(1)
layout_line_3.addWidget(button, stretch=2)
layout_line_3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line_1, stretch=2)
layout_card.addLayout(layout_line_2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line_3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
win.setLayout(layout_card)
question_list=list()
question_list.append(Question('Какой национальности не существует','Смурфы','Энцы','Алеуты','Чулымцы'))
question_list.append(Question('Чему равен 0!','1','0','-1','-0'))
question_list.append(Question('Стихия Итто','гео','анемо','пиро','гидро'))


button.clicked.connect(click_OK)
win.score=0
win.total=0
next_question()
win.show()
app.exec()
