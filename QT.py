import sys
import time
from PyQt5.QtWidgets import *
from formula import *
from cala import *
from file_operate import *
class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()
        self.fs=''
        self.anss=''

    def initUI(self):
        self.setWindowTitle('四则运算生成')
        self.resize(300,800)
        layout = QGridLayout()
        self.edit=QLineEdit()
        self.edit2=QLineEdit()
        self.edit3=QLineEdit()
        self.text=QTextEdit()
        self.button=QPushButton('确认')
        self.button1=QPushButton('生成')
        self.button2=QPushButton('批改')
        self.button3=QPushButton('导出题目')

        self.edit.setPlaceholderText('输入比10小的数作为上限(默认为9)')
        self.edit2.setPlaceholderText('输入比10小的数作为下限(默认为1)')
        self.edit3.setPlaceholderText('生成题目数量(默认为1)')
        self.button.clicked.connect(self.setting)
        self.button2.clicked.connect(self.check_answer)
        self.button3.clicked.connect(self.save_question)

        layout.addWidget(self.button1,1,1)
        layout.addWidget(self.button2,1,2)
        layout.addWidget(self.edit,2,1,1,2)
        layout.addWidget(self.edit2,3,1,1,2)
        layout.addWidget(self.edit3,4,1,1,2)
        layout.addWidget(self.button,5,1,1,2)
        layout.addWidget(self.text,6,1,10,2)
        layout.addWidget(self.button3,16,1,1,2)
        self.setLayout(layout)
    def setting(self):
        a = self.edit.text()
        b = self.edit2.text()
        if self.edit.text()=="":
            a="9"
            self.edit.setText("9")
        if self.edit2.text()=="":
            b="1"
            self.edit2.setText("1")
        if self.edit3.text()=="":
            self.edit3.setText("1")
        if a>=b and int(a)<10:
            self.product()
        if int(a) >= 10:
            self.edit.setText("")
            self.edit.setFocus()
            self.edit.setPlaceholderText('上限大于10')
        if a < b:
            self.edit2.setText("")
            self.edit2.setFocus()
            self.edit2.setPlaceholderText('上限不能比下限小')


    def product(self):
        start=time.time()
        a = self.edit.text()
        b = self.edit2.text()
        c = self.edit3.text()
        min=int(b)
        max=int(a)
        n=int(c)
        f=formula(max,min)
        count=0
        coun=0
        while count<n:
            fs=f.generate_formula()
            ans=cala(fs)
            disassemble(fs)
            if fs!=False and ans>=0:
                list1=[self.fs,fs,'\n']
                self.fs=''.join(list1)
                list2=[self.anss,str(ans),'\n']
                self.anss=''.join(list2)
                count+=1
            coun+=1
            if coun>n+1000:
                break
        self.text.setPlainText(self.fs)
        end=time.time()
        run=end-start
        print('程序运行时间',run)
    def check_answer(self):
        corrent,wrong,c,w=check()
        s=''
        s=s+'corrent:'+str(c)+corrent+'\n'+'wrong:'+str(w)+wrong
        self.text.setPlainText(s)
    def save_question(self):
        save_answer(self.anss)
        save_question(self.fs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())