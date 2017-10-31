import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
<<<<<<< HEAD
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

=======
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


>>>>>>> 9473b25bd0bdc0cfca5d1c3643f307ddd25620cf
class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
<<<<<<< HEAD
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        self.doScoreDB()
        self.writeScoreDB()

        
    def initUI(self):
        self.name = QLabel('Name:')
        self.age = QLabel('Age:')
        self.score = QLabel('Score:')
        self.amount = QLabel('Amount:')
        self.key = QLabel('Key:')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        self.combo = QComboBox(self)
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")

        # grid = QGridLayout()
        # grid.setSpacing(10)

        # grid.addWidget(name, 1, 0)
        # grid.addWidget(nameEdit, 1, 1)

        # grid.addWidget(age, 1, 2)
        # grid.addWidget(ageEdit, 1, 3)

        # grid.addWidget(score, 1, 4)
        # grid.addWidget(scoreEdit, 1, 5)

        # grid.addWidget(amount, 2, 2)
        # grid.addWidget(amountEdit, 2, 3)

        # grid.addWidget(key, 2, 4)
        # grid.addWidget(self.combo, 2, 5)

        self.addbtn = QPushButton('Add', self)
        # grid.addWidget(addbtn, 3, 1)

        self.delbtn = QPushButton('Del', self)
        # grid.addWidget(delbtn, 3, 2)

        self.findbtn = QPushButton('Find', self)
        # grid.addWidget(findbtn, 3, 3)

        self.incbtn = QPushButton('Inc', self)
        # grid.addWidget(incbtn, 3, 4)

        self.showbtn = QPushButton('Show', self)
        # grid.addWidget(showbtn, 3, 5)

        self.result = QLabel('Result:')
        # grid.addWidget(result, 4, 0)

        self.resultEdit = QTextEdit()
        # grid.addWidget(resultEdit, 5, 0, 5, 6)

        # self.setLayout(grid)

        #self.addbtn = ScoreDB()
        self.addbtn.clicked.connect(self.buttonClicked)
        #self.delbtn = ScoreDB
        self.delbtn.clicked.connect(self.buttonClicked)
        #self.findbtn = ScoreDB
        self.findbtn.clicked.connect(self.buttonClicked)
        self.incbtn.clicked.connect(self.buttonClicked)
        self.incbtn.clicked.connect(self.buttonClicked)
        self.showbtn.clicked.connect(self.buttonClicked)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.name)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(self.age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(self.score)
        hbox.addWidget(self.scoreEdit)
        # hbox.addWidget(name)
        # hbox.addWidget(cancelButton)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addStretch(1)
        hbox1.addWidget(self.amount)
        hbox1.addWidget(self.amountEdit)
        hbox1.addWidget(self.key)
        hbox1.addWidget(self.combo)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.addbtn)
        hbox2.addWidget(self.delbtn)
        hbox2.addWidget(self.findbtn)
        hbox2.addWidget(self.incbtn)
        hbox2.addWidget(self.showbtn)

        hbox3 = QHBoxLayout()
        # hbox3.addStretch(1)
        hbox3.addWidget(self.result)

        hbox4 = QHBoxLayout()
        # hbox4.addStretch(1)
        hbox4.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)
        vbox.addLayout(hbox1)
        # vbox.addStretch(1)
        vbox.addLayout(hbox2)
        # vbox.addStretch(1)
        vbox.addLayout(hbox3)
        # vbox.addStretch(1)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)


        self.setLayout(vbox)


        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        self.show()

    def buttonClicked(self):
        sender = self.sender()


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):

        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            return []

        try:
            self.scoredb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()
        return self.scoredb

    #write the data into person db
=======
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
>>>>>>> 9473b25bd0bdc0cfca5d1c3643f307ddd25620cf
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

<<<<<<< HEAD
    def doScoreDB(self):
        # try: #try except -> fix all error
        try:
            if self.sender == self.addbtn:
                    record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
                    self.scoredb += [record]
                    self.showScoreDB()

        except IndexError:
            print("Index is out of range, check and enter again")


        try:
            if self.sender() is self.delbtn:
                for k in len(self.scoredb):
                    for p in self.scoredb:
                        #if self.delbtn.clicked:
                        self.scoredb.remove(p)
                        self.showScoreDB()

        except IndexError:
            print("Index error, check and try again")

        try:
            if self.sender is self.showbtn:
                    #sortKey = self.combo.currentIndex()
                    #self.textEdit.setText(self.scoredb)
                    self.showScoreDB()

        except IndexError:
            print("Index Error check and try again")

        try:
            if self.sender is self.findbtn:
                if len(self.findEdit.text()) > 1:
                    print("unnecessary things were written")
                else:
                    for i in self.scoredb:
                        if self.findEdit.text() == i['Name']:
                            print(i)
                            self.showScoreDB()


        except IndexError:
            print("Index is out of range check and try again")

        try:
            if self.sender is self.incbtn:
                for i in self.scoredb:
                    if i['Name'] == self.findEdit.text():  # find name in the list scdb
                        if len(self.findEdit.text()) > 2:
                            print("unnecessary things exist")
                        else:
                            i['Score'] = int(self.incEdit.text()) + int(i['Score'])  # list is string so change them as integer
                    else:  # enter the word that does not exist
                        print("That name does not exist")
                    self.showScoreDB()

        except IndexError:  # tell they are wrong and make program work again
            print("Out of range. try again please")

    def showScoreDB(self):
        st = ''
        sortKey = self.combo.currentIndex()
        for p in sorted(self.scoredb, key=lambda person: sortKey):
            for attr in sorted(p):
                st += attr + " = " + str(p[attr])
            st += '\n'
        self.resultEdit.setText(st)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    #scoredb = readScoreDB(self)
    #doScoreDB(scoredb)
    #writeScoreDB(scoredb)
=======
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
>>>>>>> 9473b25bd0bdc0cfca5d1c3643f307ddd25620cf
    ex = ScoreDB()
    sys.exit(app.exec_())





