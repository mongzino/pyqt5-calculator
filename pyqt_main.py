import sys
import numpy as np
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_button = QGridLayout()
        layout_equation = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("")
        self.equation = QLineEdit("")

        ### layout_equation 레이아웃에 수식, 답 위젯을 추가
        layout_equation.addRow(label_equation, self.equation)

        ### button 
        btnList = ["%","CE","C","del","1/x","x^2","√x","/","7","8","9","*","4","5","6","-","1","2","3","+","+/-","0",".","="]
        button_dict = {}
        for num in range(0, 24):
            button_dict[num] = QPushButton(btnList[num])
            x,y = divmod(num, 4)
            layout_button.addWidget(button_dict[num],x,y)
            if (0<num<3):
                button_dict[num].clicked.connect(self.button_clear_clicked)
            if (num == 3):
                button_dict[num].clicked.connect(self.button_backspace_clicked)
            if (num == 4):
                button_dict[num].clicked.connect(self.button_reciprocal_clicked)
            if (num == 5):
                button_dict[num].clicked.connect(self.button_square_clicked)
            if (num == 6):
                button_dict[num].clicked.connect(self.button_root_clicked)
            if (num == 23):
                button_dict[num].clicked.connect(self.button_equal_clicked)
            elif(num!=0 or num!=20 ):
                button_dict[num].clicked.connect(lambda state, operation = btnList[num]: self.button_operation_clicked(operation))


        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation)
        main_layout.addLayout(layout_button)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        equation = eval(equation)
        self.equation.setText(str(equation))
        
    def button_clear_clicked(self):
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

    def button_reciprocal_clicked(self):
        equation = self.equation.text()
        number = float(equation)
        number = np.reciprocal(number)
        equation = str(number)
        self.equation.setText(equation)

    def button_square_clicked(self):
        equation = self.equation.text()
        number = float(equation)
        number **= 2
        equation = str(number)
        self.equation.setText(equation)

    def button_root_clicked(self):
        equation = self.equation.text()
        number = float(equation)
        number **= 1/2
        equation = str(number)
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())