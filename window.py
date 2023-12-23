from PyQt5.QtWidgets import*
import database
def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Введіть правильну відповідь")
    quest_edit = QLineEdit()
    right_ans_edit = QLineEdit()
    add_quest_btn = QPushButton

    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)

    window.setLayout(main_line)
    window.exec()