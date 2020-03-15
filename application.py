import sys
from PyQt5 import QtCore
from PyQt5 import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from record_play import recordAudio, setTimer, playAudio
from audio_feature_extraction import *
from pyqtgraph_ui import Ui_MainWindow1

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, sl_value = 0):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon1.png'))
        self.exitButton.clicked.connect(qApp.quit)
        self.slider.valueChanged['int'].connect(self.lcd.display)
        self.recordButton.clicked.connect(recordAudio)
        self.playButton.clicked.connect(playAudio)
        self.spectrumButton.clicked.connect(self.second_win)
        self.spectrogramButton.clicked.connect(spectrogram)
        self.zcrButton.clicked.connect(zcr)
        self.spectralButton.clicked.connect(spectralcentroid)
        self.chromaButton.clicked.connect(chromafrequencies)
        self.slider.setValue(sl_value)
        self.slider.valueChanged[int].connect(self.valuechange)
        print(sl_value)
        
    
    def second_win(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    def valuechange(self, value):
        self.__init__(value)
        setTimer(value)
    def spectrum(self):
       print('Spectrum button clicked')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()