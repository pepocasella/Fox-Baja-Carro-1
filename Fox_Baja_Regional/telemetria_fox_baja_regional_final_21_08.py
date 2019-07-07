# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:24:30 2018

@author: Pedro Casella
"""

"""Imports"""
from datetime import datetime
import RPi.GPIO as GPIO
from PyQt5 import QtCore, QtGui, QtWidgets
import time


from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

"""Setup Pinos RaspBerry Pi 3"""

#Sensor Bateria GPIOs
pinoBat_led_verde_3 = 14
pinoBat_led_verde_2 = 15
pinoBat_led_verde_1 = 18
pinoBat_led_amarelo = 23
pinoBat_led_vermelho = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoBat_led_verde_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoBat_led_verde_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoBat_led_verde_3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoBat_led_amarelo, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoBat_led_vermelho, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Sensor Gasolina GPIOs
pinoGas_led_verde_1 = 22
pinoGas_led_verde_2 = 10
#pinoBat_led_vermelho = 

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoGas_led_verde_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoGas_led_verde_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(pinoGas_led_vermelho, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 310, 53, 53))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("led_laranja_apagado.png"))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 370, 53, 53))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("led_vermelho_apagado.png"))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 190, 53, 53))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 130, 53, 53))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 270, 101, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(660, 330, 101, 21))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(660, 390, 101, 21))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 246, 128))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Projeto_Python_Baja/IHM/logo_fox_baja.png"))
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 190, 283, 229))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../Projeto_Python_Baja/IHM/mascote_fox_baja.png"))
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(70, 30, 124, 94))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("battery_icon_2.png"))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(620, 90, 87, 140))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("gas_icon.png"))
        self.label_17.setObjectName("label_17")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(590, 370, 53, 53))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("led_vermelho_apagado.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(590, 250, 53, 53))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        self.label_13.setObjectName("label_13")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(590, 310, 53, 53))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        self.label_18.setObjectName("label_18")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 250, 53, 53))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.counter =1
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()



    '''
    pinoBat_led_verde_3 = 14
    pinoBat_led_verde_2 = 15
    pinoBat_led_verde_1 = 18
    pinoBat_led_amarelo = 23
    pinoBat_led_vermelho = 24

    pinoGas_led_verde_1 = 22
    pinoBat_led_verde_2 = 10
    '''

    '''
    label_3 = Bat_led_vermelho
    label_4 = Bat_led_amarelo
    label_5 = Bat_led_verde_1
    label_5 = Bat_led_verde_2
    label_6 = Bat_led_verde_3

    label_7 = Gas_led_verde_2
    label_8 = Gas_led_verde_1
    label_9 = Gas_led_vermelho_empty
    '''
 def recurring_timer(self):

        #loop check bateria
        if GPIO.input(14) == GPIO.HIGH:
            print('Bat_led_verde_3 - apagado')
            self.label_7.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        else:
        #elif GPIO.input(14) == GPIO.LOW:
            print('Bat_led_verde_3 - aceso')
            self.label_7.setPixmap(QtGui.QPixmap("led_verde_aceso.png"))

        if GPIO.input(15) == GPIO.HIGH:
            print('Bat_led_verde_2 - apagado')
            self.label_6.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        else:
        #elif GPIO.input(15) == GPIO.LOW:
            print('Bat_led_verde_2 - aceso')
            self.label_6.setPixmap(QtGui.QPixmap("led_verde_aceso.png"))

        if GPIO.input(18) == GPIO.HIGH:
            print('Bat_led_verde_1 - apagado')
            self.label_5.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))
        else:
        #elif GPIO.input(18) == GPIO.LOW:
            print('Bat_led_verde_1 - aceso')
            self.label_5.setPixmap(QtGui.QPixmap("led_verde_aceso.png"))

        if GPIO.input(23) == GPIO.HIGH:
            print('Bat_led_amarelo - apagado')
            self.label_4.setPixmap(QtGui.QPixmap("led_laranja_apagado.png"))
        else:
        #elif GPIO.input(23) == GPIO.LOW:
            print('Bat_led_amarelo - aceso')
            self.label_4.setPixmap(QtGui.QPixmap("led_laranja_aceso.png"))

        if GPIO.input(24) == GPIO.HIGH:
            print('Bat_led_vermelho - apagado')
            self.label_3.setPixmap(QtGui.QPixmap("led_vermelho_apagado.png"))
        else:
        #elif GPIO.input(24) == GPIO.LOW:
            print('Bat_led_vermelho - aceso')
            self.label_3.setPixmap(QtGui.QPixmap("led_vermelho_aceso.png"))


        #loop check gasolina
        if GPIO.input(22) == GPIO.HIGH:
            print('Bat_led_verde_2 - aceso')
            self.label_13.setPixmap(QtGui.QPixmap("led_verde_aceso.png"))
        else:
        #elif GPIO.input(22) == GPIO.LOW:
            print('Bat_led_verde_2 - apagado')
            self.label_13.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))

        if GPIO.input(10) == GPIO.HIGH:
            print('Bat_led_verde_1 - aceso')
            self.label_18.setPixmap(QtGui.QPixmap("led_verde_aceso.png"))
        else:
        #elif GPIO.input(10) == GPIO.LOW:
            print('Bat_led_verde_1 - apagado')
            self.label_18.setPixmap(QtGui.QPixmap("led_verde_apagado.png"))

        if GPIO.input(22) or GPIO.input(10):
            print('Bat_led_vermelho - aceso')
            self.label_12.setPixmap(QtGui.QPixmap("led_vermelho_apagado.png"))
        else:
            print('Bat_led_vermelho - apagado')
            self.label_12.setPixmap(QtGui.QPixmap("led_vermelho_aceso.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Full"))
        self.label_14.setText(_translate("MainWindow", "1/2"))
        self.label_15.setText(_translate("MainWindow", "Empty"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

