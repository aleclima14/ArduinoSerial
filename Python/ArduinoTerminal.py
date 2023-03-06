import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
QComboBox, QVBoxLayout, QHBoxLayout)

from PyQt6.QtSerialPort import (QSerialPort, QSerialPortInfo)
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon

class Windows(QWidget):
   def __init__(self):
      super(Windows,self).__init__()
      self.initUI()
      
   def initUI(self):
      self.setWindowIcon(QIcon("led-icon.png"))
      self.setWindowTitle("Serial LED Control")
      self.setContentsMargins(20, 20, 20, 20)
      self.setFixedSize(420, 180)

      self.serialReadLabel = QLabel()
      self.availablePorts = QComboBox()
      self.baudrateComPort = QComboBox()
      self.serialPort = QSerialPort()
      self.refreshButton = QPushButton("R")
      self.connectButton = QPushButton("Connect")
      self.disconnectButton = QPushButton("Disconnect")
      self.onLedButton = QPushButton("LED ON")
      self.offLedButton = QPushButton("LED OFF")

      layout = QVBoxLayout()
      horizontalBox = QHBoxLayout()
      verticalBox = QVBoxLayout()

      self.setLayout(layout)    
      horizontalBox.setSpacing(5)
      layout.addLayout(horizontalBox)
      verticalBox.setSpacing(5)
      layout.addLayout(verticalBox)
      
      self.availablePorts.addItems([comPorts.portName() for comPorts in QSerialPortInfo().availablePorts()])
      self.availablePorts.setMaximumWidth(80)
      self.availablePorts.setMinimumWidth(80)
      
      self.baudrateComPort.addItems(["9600", "19200", "115200"])
      self.baudrateComPort.setMaximumWidth(80)
      self.baudrateComPort.setMinimumWidth(80)  

      self.refreshButton.setMaximumWidth(25)
      self.refreshButton.setMinimumWidth(25)
      self.refreshButton.clicked.connect(self.refreshComPortEvent)
      
      self.connectButton.setMaximumWidth(80)
      self.connectButton.setMinimumWidth(80)
      self.connectButton.clicked.connect(self.connectButtonEvent)
      
      self.disconnectButton.setMaximumWidth(80)
      self.disconnectButton.setMinimumWidth(80)
      self.disconnectButton.clicked.connect(self.disconnectButtonEvent)
      self.disconnectButton.setEnabled(False)
      
      self.onLedButton.clicked.connect(self.onButtonEvent)
      self.onLedButton.setEnabled(False)

      self.offLedButton.clicked.connect(self.offButtonEvent)
      self.offLedButton.setEnabled(False)

      horizontalBox.addWidget(self.availablePorts)
      horizontalBox.addWidget(self.refreshButton)
      horizontalBox.addWidget(self.baudrateComPort)
      horizontalBox.addWidget(self.connectButton)
      horizontalBox.addWidget(self.disconnectButton)

      verticalBox.addWidget(self.onLedButton)
      verticalBox.addWidget(self.offLedButton)
      verticalBox.addWidget(self.serialReadLabel)
      
   def refreshComPortEvent(self):
      self.availablePorts.clear()
      self.availablePorts.addItems([comPorts.portName() for comPorts in QSerialPortInfo().availablePorts()])
   
   def connectButtonEvent(self):
      self.serialPort.setPortName(self.availablePorts.currentText())
      self.serialPort.setBaudRate(int(self.baudrateComPort.currentText()), QSerialPort.Direction.AllDirections)

      self.serialPort.open(QtCore.QIODeviceBase.OpenModeFlag.ReadWrite)

      self.connectButton.setEnabled(False)
      self.refreshButton.setEnabled(False)
      self.availablePorts.setEnabled(False)
      self.baudrateComPort.setEnabled(False)
      self.disconnectButton.setEnabled(True)
      self.onLedButton.setEnabled(True)
      self.offLedButton.setEnabled(True)

   def disconnectButtonEvent(self):
      self.serialPort.close()

      self.connectButton.setEnabled(True)
      self.refreshButton.setEnabled(True)
      self.availablePorts.setEnabled(True)
      self.baudrateComPort.setEnabled(True)
      self.disconnectButton.setEnabled(False)
      self.onLedButton.setEnabled(False)
      self.offLedButton.setEnabled(False)

   def onButtonEvent(self):
      self.serialPort.write("on".encode())
      self.readStatusLed()
   
   def offButtonEvent(self):
      self.serialPort.write("off".encode())
      self.readStatusLed()
     
   def readStatusLed(self):
      valorLido = self.serialPort.readLine()
      self.serialReadLabel.setText(str(valorLido, 'utf-8'))
      valorLido = ""

def window():
   applicationWindow = QApplication(sys.argv)
   windowApp = Windows()
   windowApp.show()
   sys.exit(applicationWindow.exec())

window()