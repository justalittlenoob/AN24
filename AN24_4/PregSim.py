# -*- coding: utf-8 -*-

"""
Module implementing PregSim.
"""

import PyQt4, sys, random
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import (pyqtSignature, QTimer, SIGNAL)
from Ui_PregSim import Ui_PregSim
from Holter import *
from OpenCsv import *
from BasCal import *


class PregSim(QDialog, Ui_PregSim):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.start(250)
        QtCore.QObject.connect(self.timer, SIGNAL("timeout()"),self.ShowHr)
        
    
    
    @pyqtSignature("bool")
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if DlgHolter.isVisible():
            DlgHolter.setVisible(False)
        else:
            DlgHolter.setVisible(True)
        DlgPregSim.setVisible(False)            
        self.Bulb.setStyleSheet("background-image: url(:/picture/imgs/BulbOn.png);\n"
"background-repeat: no-repeat")
    
    def ShowHr(self):
        """
        display the heatrate of mother and children 
        """
        x = random.randint(60, 120)
        y = random.randint(120, 180)
        self.MoHrNum.setText(str(x))
        self.ChHrNum.setText(str(y))





if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    path="E:/5-HOLTER/new/long.csv"
    Time, FHR, MHR, EHG= OpenCsv(path)
    Baseline=CalBaseline(FHR)
    print len(Baseline)
    DlgHolter=Holter()
    DlgPregSim=PregSim()
    Holter.FHRR=FHR
    Holter.Baseline=Baseline
        
    DlgPregSim.show()
    sys.exit(app.exec_())
