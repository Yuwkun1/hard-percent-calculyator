from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel) 

def calc_hard_percent(summa_input, percent_input, years_input, layout):
    summa = int(summa_input.text())
    percent = int(percent_input.text())
    years = int(years_input.text())
    percent = percent/100+1
    for i in range(years) :
        summa*=percent
    str_summa = str(summa)
    index_dot = str_summa.find(".")
    result = "В итоге сумма вклада составит: " + str_summa[0:index_dot+3]
    layout.addWidget(QLabel(result))
    lable = QLabel(result)
    lable.setStyleSheet("font-size:25px;font-color:green;")
    layout.addWidget(lable)

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setStyleSheet("background:white;border:2px dashed black;")

lable_title = QLabel("Калькулятор вклада")
lable_title.setStyleSheet("color:black;font-size:35px;")
layout.addWidget(lable_title)

lable_summa = QLabel("Введите сумму:")
lable_summa.setStyleSheet("color:orange;font-size:24px;")
layout.addWidget(lable_summa)
summa_input = QLineEdit()
summa_input.setStyleSheet("color:red;font-size:18px;")
layout.addWidget(summa_input)

lable_years = QLabel("Введите процент:")
lable_years.setStyleSheet("color:pink;font-size:24px;")
layout.addWidget(lable_years)
percent_input = QLineEdit()
percent_input.setStyleSheet("color:blue;font-size:18px;")
layout.addWidget(percent_input)

lable_percent = QLabel("Введите срок в годах:")
lable_percent.setStyleSheet("color:dark_green;font-size:20px;")
layout.addWidget(lable_percent)
years_input = QLineEdit()
years_input.setStyleSheet("color:blue;font-size:18px;")
layout.addWidget(years_input)

btn_submit = QPushButton("Рассчитать")
btn_submit.setStyleSheet("color:grey;font-size:25px;font-weight:400;")
btn_submit.clicked.connect(lambda: calc_hard_percent(summa_input, percent_input, years_input, layout))
layout.addWidget(btn_submit)

window.setLayout(layout)
window.show()
app.exec_()
