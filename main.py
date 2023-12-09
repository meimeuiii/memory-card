import random

from PyQt5.QtWidgets import*
app = QApplication([])
window = QWidget()
window.resize(700, 500)

menu_btn = QPushButton("Меню")
menu_btn = QGroupBox("Варіанти відповідей")
menu_btn = QGroupBox("Вікно")
group_box = QGroupBox()
question_lbl = QLabel("Яблоко")
answer1_btn = QRadioButton("building")
answer2_btn = QRadioButton ("home")
answer3_btn = QRadioButton("application")
answer4_btn = QRadioButton("apple")

answers = [answer1_btn, answer2_btn, answer3_btn, answer4_btn]
random.shuffle(answers)
vidpovistu_btn = QPushButton("Відповісти")
main_line = QVBoxLayout()

h1  = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addStretch(1)
main_line.addLayout(h1)

main_line.addWidget(question_lbl)

group_line = QVBoxLayout()
group_line.addWidget()
QWidget(answer1_btn)
group_line.addWidget()
QWidget(answer2_btn)
group_line.addWidget()
QWidget(answer3_btn)
group_line.addWidget(answer4_btn)
group_box.setLayout(group_line)

main_line.addWidget(group_box)

window.setLayout(main_line)
window.show()
app.exec()