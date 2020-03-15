# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 660)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(320, 660))
        MainWindow.setMinimumSize(QtCore.QSize(320, 660))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: #ffdd61\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setGeometry(QtCore.QRect(10, 10, 301, 91))
        self.lcd.setAutoFillBackground(False)
        self.lcd.setStyleSheet("QLCDNumber{\n"
"    background-color :#e3e3e3\n"
"}")
        self.lcd.setObjectName("lcd")
        self.spectrogramButton = QtWidgets.QPushButton(self.centralwidget)
        self.spectrogramButton.setGeometry(QtCore.QRect(10, 340, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.spectrogramButton.setFont(font)
        self.spectrogramButton.setStyleSheet("QPushButton{\n"
"    background-color: #000000;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff5457;\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"}")
        self.spectrogramButton.setObjectName("spectrogramButton")
        self.recordButton = QtWidgets.QPushButton(self.centralwidget)
        self.recordButton.setGeometry(QtCore.QRect(10, 160, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.recordButton.setFont(font)
        self.recordButton.setStyleSheet("QPushButton{\n"
"    background-color: #000000;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #dadbde, stop: 1#ff5457);\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"}")
        self.recordButton.setObjectName("recordButton")
        self.spectrumButton = QtWidgets.QPushButton(self.centralwidget)
        self.spectrumButton.setGeometry(QtCore.QRect(10, 280, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.spectrumButton.setFont(font)
        self.spectrumButton.setStyleSheet("QPushButton{\n"
"    background-color: #000000;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff5457;\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"}")
        self.spectrumButton.setObjectName("spectrumButton")
        self.spectralButton = QtWidgets.QPushButton(self.centralwidget)
        self.spectralButton.setGeometry(QtCore.QRect(10, 460, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.spectralButton.setFont(font)
        self.spectralButton.setStyleSheet("QPushButton{\n"
"    background-color: #000000;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff5457;\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"}")
        self.spectralButton.setObjectName("spectralButton")
        self.zcrButton = QtWidgets.QPushButton(self.centralwidget)
        self.zcrButton.setGeometry(QtCore.QRect(10, 400, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.zcrButton.setFont(font)
        self.zcrButton.setStyleSheet("QPushButton{\n"
"    background-color: #000000;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff5457;\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"}")
        self.zcrButton.setObjectName("zcrButton")
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(10, 110, 301, 41))
        self.slider.setAutoFillBackground(False)
        self.slider.setStyleSheet("QSlider{\n"
"    background-color:  #ffdd61\n"
"}")
        self.slider.setMaximum(10)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 600, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton{\n"
"    background-color:  #ff5457;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #f6f7fa;\n"
"    background-color: #000000;\n"
"    font-size: 22px;\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.chromaButton = QtWidgets.QPushButton(self.centralwidget)
        self.chromaButton.setGeometry(QtCore.QRect(10, 520, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.chromaButton.setFont(font)
        self.chromaButton.setStyleSheet("QPushButton{\n"
"    background-color: #000000;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ff5457;\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"}")
        self.chromaButton.setObjectName("chromaButton")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(10, 220, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("QPushButton{\n"
"    background-color: #000000;\n"
"    border-width: 20px;\n"
"    border-radius : 25px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #dadbde, stop: 1#ff5457);\n"
"    color: #000000;\n"
"    font-size: 20px;\n"
"}")
        self.playButton.setObjectName("playButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.slider.valueChanged['int'].connect(self.lcd.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Spectrum Analyzer"))
        self.spectrogramButton.setText(_translate("MainWindow", "SPECTROGRAM"))
        self.recordButton.setText(_translate("MainWindow", "RECORD"))
        self.spectrumButton.setText(_translate("MainWindow", "LIVE POWER SPECTRUM"))
        self.spectralButton.setText(_translate("MainWindow", "SPECTRAL CENTROID"))
        self.zcrButton.setText(_translate("MainWindow", "ZERO CROSSING RATIO"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.chromaButton.setText(_translate("MainWindow", "CHROMA FREQUENCIES"))
        self.playButton.setText(_translate("MainWindow", "PLAY"))

