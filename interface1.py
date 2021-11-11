# -*- coding: utf-8 -*-


#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from python_speech_features import mfcc
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import wave
import DTW
import Comparaison as c


audio=c.comparaison()
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Projet Traitement de la Parole")
        Form.resize(774, 607)
        Form.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_image = QtWidgets.QLabel(Form)
        self.label_image.setGeometry(QtCore.QRect(150, 20, 81, 81))
        self.label_image.setStyleSheet("image: url(C:/Users/Lenovo/PycharmProjects/Parole_Projet/micro.png);")
        self.label_image.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.label_titre = QtWidgets.QLabel(Form)
        self.label_titre.setGeometry(QtCore.QRect(240, 20, 431, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_titre.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(20)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 150, 261, 231))
        self.label.setStyleSheet("color :rgb(0, 0, 127);")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 390, 151, 31))
        palette = QtGui.QPalette()

        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 80, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(45, 80, 206);\n"
"color:rgb(255, 255, 255);\n"
"border-raduis:5%\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 150, 261, 231))
        self.label_2.setStyleSheet("color :rgb(0, 0, 127);")
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 390, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(45, 80, 206);\n"
"color:rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.calcul_button = QtWidgets.QPushButton(Form)
        self.calcul_button.setGeometry(QtCore.QRect(230, 490, 321, 41))
        palette = QtGui.QPalette()

        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.calcul_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.calcul_button.setFont(font)
        self.calcul_button.setStyleSheet("background-color:rgb(77, 231, 231);\n"
"color:rgb(0, 0, 177)")
        self.calcul_button.setAutoDefault(False)
        self.calcul_button.setObjectName("calcul_button")
        self.label_Nom = QtWidgets.QLabel(Form)
        self.label_Nom.setGeometry(QtCore.QRect(10, 580, 231, 18))
        self.label_Nom.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_Nom.setObjectName("label_Nom")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(160, 540, 550, 41))
        self.result.setStyleSheet("color: rgb(0, 0, 127);font-size:15px;align:center;")
        self.result.setObjectName("result")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_titre.setText(_translate("Form", "Comparer des mots isolés  avec DTW"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\""
                                              " font-size:20pt; font-weight:600;\">Veuillez"
                                              " choisir</span></p><p align=\"center\"><span style=\""
                                              " font-size:20pt; font-weight:600;\">l\'audio N°1 </span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "audio N° 1"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">"
                                                "<span style=\" font-size:20pt; font-weight:600;\""
                                                ">Veuillez choisir</span></p><p align=\"center\"><span"
                                                " style=\" font-size:20pt; font-weight:600;\">l\'audio "
                                                "N°2</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "audio N° 2"))
        self.calcul_button.setText(_translate("Form", "Comparer les deux audios"))
        self.label_Nom.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:11pt;\">Réaliser par :El hammiouy Salima</span></p></body></html>"))

        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton_handler2)
        self.calcul_button.clicked.connect(self.comparaison)

    def pushButton_handler(self):
        a=1
        print("Button 1 pressed")
        self.open_dialog_box()

    def pushButton_handler2(self):
        a=2
        print("Button 2 pressed")
        self.open_dialog_box2()

    def open_dialog_box(self):
        _translate = QtCore.QCoreApplication.translate
        filename = QFileDialog.getOpenFileName(None, "", "","audio (*.wav)")
        path = filename[0]
        audio.audio1=path
        print(path)
        self.label.setText("")
        self.label.setStyleSheet("image: url(./check.jpg);")
        return path

    def open_dialog_box2(self):
        _translate = QtCore.QCoreApplication.translate
        filename = QFileDialog.getOpenFileName(None, "", "","audio (*.wav)")
        path2 = filename[0]
        audio.audio2 = path2
        print(path2)
        self.label_2.setText("")
        self.label_2.setStyleSheet("image: url(./check.jpg);")
        return path2

    def comparaison(self):
        self.result.setText(audio.Comparer2Mot())





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
