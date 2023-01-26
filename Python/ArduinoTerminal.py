import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, 
QComboBox, QVBoxLayout, QHBoxLayout, QGridLayout)

from PyQt6.QtSerialPort import (QSerialPort, QSerialPortInfo)
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon

class Windows(QWidget):
   def __init__(self):
      super(Windows,self).__init__()
      self.initUI()
      
   def initUI(self):
      self.setWindowIcon(QIcon("Python/led-icon.png"))
      self.setWindowTitle("Serial LED Control")
      self.setContentsMargins(20, 20, 20, 20)
      # self.resize(400, 170)
      self.setFixedSize(420,150)

      layout = QVBoxLayout()
      self.setLayout(layout)

      horizontalBox = QHBoxLayout()
      horizontalBox.setSpacing(5)
      layout.addLayout(horizontalBox)
      
      self.availablePorts = QComboBox()
      self.availablePorts.addItems([comPorts.portName() for comPorts in QSerialPortInfo().availablePorts()])
      self.availablePorts.setMaximumWidth(80)
      self.availablePorts.setMinimumWidth(80)
      
      self.baudrateComPort = QComboBox()
      self.baudrateComPort.addItems(["9600", "19200", "115200"])
      self.baudrateComPort.setMaximumWidth(80)
      self.baudrateComPort.setMinimumWidth(80)
      
      self.serialPort = QSerialPort()

      self.refreshButton = QPushButton("R")
      self.refreshButton.setMaximumWidth(25)
      self.refreshButton.setMinimumWidth(25)
      self.refreshButton.clicked.connect(self.refreshComPortEvent)
      
      self.connectButton = QPushButton("Connect")
      self.connectButton.setMaximumWidth(80)
      self.connectButton.setMinimumWidth(80)
      self.connectButton.clicked.connect(self.connectButtonEvent)
      
      self.desconnectButton = QPushButton("Desconnect")
      self.desconnectButton.setMaximumWidth(80)
      self.desconnectButton.setMinimumWidth(80)
      self.desconnectButton.clicked.connect(self.desconnectButtonEvent)
      self.desconnectButton.setEnabled(False)

      horizontalBox.addWidget(self.availablePorts)
      horizontalBox.addWidget(self.refreshButton)
      horizontalBox.addWidget(self.baudrateComPort)
      horizontalBox.addWidget(self.connectButton)
      horizontalBox.addWidget(self.desconnectButton)

      verticalBox = QVBoxLayout()
      verticalBox.setSpacing(5)
      layout.addLayout(verticalBox)

      self.onLedButton = QPushButton("LED ON")
      self.onLedButton.clicked.connect(self.onButtonEvent)
      self.onLedButton.setEnabled(False)

      self.offLedButton = QPushButton("LED OFF")
      self.offLedButton.clicked.connect(self.offButtonEvent)
      self.offLedButton.setEnabled(False)

      self.serialReadLabel = QLabel()

      verticalBox.addWidget(self.onLedButton)
      verticalBox.addWidget(self.offLedButton)
      
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
      self.desconnectButton.setEnabled(True)
      self.onLedButton.setEnabled(True)
      self.offLedButton.setEnabled(True)

   def desconnectButtonEvent(self):
      self.serialPort.close()

      self.connectButton.setEnabled(True)
      self.refreshButton.setEnabled(True)
      self.availablePorts.setEnabled(True)
      self.baudrateComPort.setEnabled(True)
      self.desconnectButton.setEnabled(False)
      self.onLedButton.setEnabled(False)
      self.offLedButton.setEnabled(False)

   def onButtonEvent(self):
      self.serialPort.write("on".encode())
   
   def offButtonEvent(self):
      self.serialPort.write("off".encode())

def window():
   applicationWindow = QApplication(sys.argv)
   windowApp = Windows()

   windowApp.show()

   sys.exit(applicationWindow.exec())

window()