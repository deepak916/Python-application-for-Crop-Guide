from PyQt5 import QtCore, QtGui, QtWidgets#import widgets from pyqt5 
import sqlite3#import for databse
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 854)#to resize the window size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(110, 10, 1000, 111))#to increase the size of the widget
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")#change the font
        font.setPointSize(36)#increase the font
        font.setBold(True)#to make it bold
        font.setWeight(75)#increase the font weight
        self.label_heading.setFont(font)
        self.label_heading.setStyleSheet("background-color: rgb(255, 255, 0);")#to change the color of the widget
        self.label_heading.setObjectName("label_heading")
        self.label_season = QtWidgets.QLabel(self.centralwidget)
        self.label_season.setGeometry(QtCore.QRect(150, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_season.setFont(font)
        self.label_season.setObjectName("label_season")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 210, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")#add elemnts to the combobox and add the text in retranslateUi function
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_state = QtWidgets.QLabel(self.centralwidget)
        self.label_state.setGeometry(QtCore.QRect(150, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 330, 220, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_Acres = QtWidgets.QLabel(self.centralwidget)
        self.label_Acres.setGeometry(QtCore.QRect(150, 440, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Acres.setFont(font)
        self.label_Acres.setObjectName("label_Acres")
        self.line_Acres = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Acres.setGeometry(QtCore.QRect(320, 450, 151, 41))
        self.line_Acres.setObjectName("line_Acres")
        self.label_Budget = QtWidgets.QLabel(self.centralwidget)
        self.label_Budget.setGeometry(QtCore.QRect(150, 540, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Budget.setFont(font)
        self.label_Budget.setObjectName("label_Budget")
        self.line_Budget = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Budget.setGeometry(QtCore.QRect(320, 550, 151, 41))
        self.line_Budget.setObjectName("line_Budget")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(280, 600, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit.setFont(font)
        self.button_submit.setObjectName("button_submit")
        self.button_submit.clicked.connect(self.Submit)#connect to the function submit

        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(550, 130, 791, 451))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("img//main.png"))#add the image to the label
        self.label_image.setObjectName("label_image")
        self.text_info = QtWidgets.QTextEdit(self.centralwidget)
        self.text_info.setGeometry(QtCore.QRect(550, 520, 400, 150))
        self.text_info.setObjectName("text_info")
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.text_info.setFont(font)
 
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "                            CROP GUIDE"))#change the title name
        self.label_season.setText(_translate("MainWindow", "Season"))#change the label name
        self.comboBox.setItemText(0, _translate("MainWindow", "Kharif"))#change the label name
        self.comboBox.setItemText(1, _translate("MainWindow", "Rabi"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Zaid"))
        self.label_state.setText(_translate("MainWindow", "State"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Chandigarh"))#add element to the combox
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Delhi"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Haryana"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Himachal Pradesh"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Jammu  Kashmir"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Ladakh"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Punjab"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Rajasthan"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Uttarakhand"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Uttar Pradesh"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Madhya Pradesh"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "West Bengal"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Bihar"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Gujarat"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Andhra Pradesh"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Karnataka"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Kerala"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "Lakshadweep"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "Puducherry"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "Tamil Nadu"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "Telangana"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "Chennai"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "Bengaluru"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "Hyderabad"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "Kochi"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "Warangal"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "Thiruvananthapuram"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "Coimbatore"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "Visakhapatanam"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "Mysuru"))
        self.comboBox_2.setItemText(30, _translate("MainWindow", "Madurai"))
        self.comboBox_2.setItemText(31, _translate("MainWindow", "Vijayawada"))
        self.comboBox_2.setItemText(32, _translate("MainWindow", "Kozhikode"))
        self.label_Acres.setText(_translate("MainWindow", "Acres"))
        self.label_Budget.setText(_translate("MainWindow", "Budget"))
        self.button_submit.setText(_translate("MainWindow", "SUBMIT"))
    

    def Submit(self):
        #dict "res" had key has cropname and value has Pesticides
        res={'Sugarcane': 'insecticides and fungi- cides', 'Rice': 'Lambda-cyhalothrin, malathion and zeta-cypermethrin', 'Cotton': 'Pyrethroids and Organophosphates', 'Maize': ' herbicides, atrazine', 'Wheat': 'organochlorines, organophosphates', 'Mustard seed': 'Plasmodiophora brassicae', 'Banana': 'Chlorpyrifos,Thiabendazole', 'Mango': 'Imidacloprid, Endosulfan', 'Cucumber': 'Carbaryl and Dichlorvos (DDVP)', 'Jute': 'Endosulfan and fenpropathrin', 'Pumpkin': 'Sevin (carbaryl), Furadan', 'Tomato': 'permethrin, bifenthrin'}    
        conn = sqlite3.connect('crop_guide.sqlite')
        cur = conn.cursor()
        ans=cur.execute("SELECT * FROM crop WHERE northern IS NOT NULL")#get all the values in the column in the database
        ans=cur.fetchall()#fetch the output
        ans=list(ans[0][5:-1])#remove null values by converting into a list and using slice operator
        se = self.comboBox.currentText()#get text from the user(input) in case of combobox
        sta =  self.comboBox_2.currentText()
        money = int(self.line_Budget.text())#get text from the user(input) in case of line_edit
        acers = int(self.line_Acres.text())

        ns=sta in ans[0]#in operator return bool values
        

        if ns:
        
            if money>=50000 and acers>=10:

                
                cur.execute("SELECT nh FROM crop WHERE season=?",[se])#fetch data from nh column to the w.r.t season
                dd = cur.fetchall() #fetch the output
                dd=str(dd[0])[2:-3]
                print(dd)
 
                self.label_image.setPixmap(QtGui.QPixmap("img//"+dd+".png"))#add image
                result ="Pesticides used are "+res[dd]#"+" used to concat
                self.text_info.setText(result)#add text to the line_edit
                
              
            
            else:

        
                cur.execute("SELECT nl FROM crop WHERE season=?",[se])
                dd = cur.fetchall()
                dd=str(dd[0])[2:-3]
                print(dd)
                
                self.label_image.setPixmap(QtGui.QPixmap("img//"+dd+".png"))
                self.text_info.setText(dd)
                result ="Pesticides used are "+res[dd]
                self.text_info.setText(result)
                
          

            
        
        else:
            if money>=50000 and acers>=10:
        

                cur.execute("SELECT sh FROM crop WHERE season=?",[se])
                dd = cur.fetchall() 
                dd=str(dd[0])[2:-3]
                print(dd)

                self.label_image.setPixmap(QtGui.QPixmap("img//"+dd+".png"))
                self.text_info.setText(dd)
                result ="Pesticides used are "+res[dd]
                self.text_info.setText(result)
                
            
            else:
                cur.execute("SELECT sl FROM crop WHERE season=?",[se])
                dd = cur.fetchall() 
                dd=str(dd[0])[2:-3]
                print(dd)

                self.label_image.setPixmap(QtGui.QPixmap("img//"+dd+".png"))
                self.text_info.setText(dd)
                result ="Pesticides used are "+res[dd]
                self.text_info.setText(result)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
