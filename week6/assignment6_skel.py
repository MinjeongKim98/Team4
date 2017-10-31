import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        lblName = QLabel("Name")
        self.editName = QLineEdit()
        Age = QLabel("Age")
        self.editAge = QLineEdit()
        Score = QLabel("Score")
        self.editScore = QLineEdit()
        Amount = QLabel("Amount")
        self.editAmount = QLineEdit()
        Key = QLabel("Key")
        self.cb = QComboBox(self)
        self.cb.addItem("Name")
        self.cb.addItem("Score")
        self.cb.addItem("Age")
        self.btnAdd = QPushButton("Add")

        self.btnAdd.clicked.connect(lambda :self.Add(self.editName.text(), self.editAge.text(), self.editScore.text()))
        self.btnDel = QPushButton("Del")
        self.btnDel.clicked.connect(self.dell)
        self.btnFind = QPushButton("Find")
        self.btnFind.clicked.connect(self.find)
        self.btnInc = QPushButton("Inc")
        self.btnInc.clicked.connect(self.Incc)
        self.btnshow = QPushButton("Show")
        self.btnshow.clicked.connect(lambda : self.showScoreDB(str(self.cb.currentText())))
        Result = QLabel("Result")
        self.ResultEdit  = QTextEdit()

        # 레이아웃
        layout = QVBoxLayout()
        layout0 = QHBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()

        layout0.addWidget(lblName)
        layout0.addWidget(self.editName)
        layout0.addWidget(Age)
        layout0.addWidget(self.editAge)
        layout0.addWidget(Score)
        layout0.addWidget(self.editScore)
        layout1.addWidget(Amount)
        layout1.addWidget(self.editAmount)
        layout1.addWidget(Key)
        layout1.addWidget(self.cb)
        layout2.addWidget(self.btnAdd)
        layout2.addWidget(self.btnDel)
        layout2.addWidget(self.btnFind)
        layout2.addWidget(self.btnInc)
        layout2.addWidget(self.btnshow)
        layout3.addWidget(Result)
        layout4.addWidget(self.ResultEdit, 5)

        # 다이얼로그에 레이아웃 지정
        layout.addLayout(layout0)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)

        self.setLayout(layout)

        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB('Name')
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname):
        print(keyname)
        msg = ""
        for p in sorted(self.scoredb, key=lambda person: str(person[keyname])):
            for attr in sorted(p):

                msg+=str(str(attr) + " = " + str(p[attr]) + " ")
            msg+="\n"
        self.ResultEdit.setPlainText(msg)

    def Add(self, a, b, c):
        record = {'Name': a, 'Age': b, 'Score': c}
        self.scoredb += [record]
        self.showScoreDB(str(self.cb.currentText()))

    def Incc(self):
        for p in self.scoredb:
            if p['Name'] == self.editName.text():
                p['Score'] = str(int(p['Score']) + int(self.editAmount.text()))
        self.showScoreDB(str(self.cb.currentText()))


    def dell(self):
        t = len(self.scoredb)
        for l in range(len(self.scoredb)):
            p = self.scoredb[t - l - 1]
            if p['Name'] == self.editName.text():
                self.scoredb.remove(p)
        self.showScoreDB(str(self.cb.currentText()))


    def find(self):
        msg = ""
        for j in self.scoredb:
            if j['Name'] == self.editName.text():
                msg += str("Age" + " = " + str(j['Age']) + " " + "Name" + " = " + str(j['Name']) + " " + "Score" + " = " + str(j['Score'])+"\n")


        self.ResultEdit.setPlainText(msg)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





