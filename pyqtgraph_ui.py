# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import pyaudio
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.audiocapture()
        
    # Function to capture the audio data
    def audiocapture(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 14100
        self.CHUNK = 1024
        self.MAX_PLOT_SIZE = self.CHUNK * 50
         
        # setup audio recording
        self.audio = pyaudio.PyAudio()
        
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                        rate=self.RATE, input=True,
                        frames_per_buffer= self.CHUNK)
        
        self.win = self.graphicsView
        
        # create a plot for the time domain data
        self.data_plot = self.win.addPlot(title="Audio Signal Vs Time")
        self.data_plot.setXRange(0 ,self.MAX_PLOT_SIZE)
        self.data_plot.showGrid(True, True)
        self.data_plot.addLegend()
        self.time_curve = self.data_plot.plot(pen=(24,215,248), name = "Time Domain Audio")
        
        # create a plot for the frequency domain data
        self.win.nextRow()
        self.fft_plot = self.win.addPlot(title="Power Vs Frequency Domain") 
        self.fft_plot.addLegend()
        self.fft_curve = self.fft_plot.plot(pen='y', name = "Power Spectrum")
        
        self.fft_plot.showGrid(True, True)
        self.total_data = []
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0)
    #upate chunk of audio data
    def update(self):

            # read data
            raw_data = self.stream.read(self.CHUNK)
            
            # convert raw bytes into integers
            data_sample = np.frombuffer(raw_data, dtype=np.int16)
            self.total_data = np.concatenate([self.total_data, data_sample ])
            
            # remove old data
            if len(self.total_data) > self.MAX_PLOT_SIZE:
                self.total_data = self.total_data[self.CHUNK:]
            self.time_curve.setData(self.total_data)
            
            # calculate the FFT
            fft_data = data_sample * np.hanning(len(data_sample))
            power_spectrum = 20 * np.log10(np.abs(np.fft.rfft(fft_data))/len(fft_data))
            self.fft_curve.setData(power_spectrum)
            self.fft_plot.enableAutoRange('xy', False)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Live Power Spectrum"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from pyqtgraph import GraphicsLayoutWidget
