from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils

import sys
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap

import os
import numpy as np

# import matplotlib.pyplot as plt
from utility import *
global filename
filename=""
# nuce_img = NUCE(img) 

def NUCE(img):
    #natural-based underwater image color enhancement
    
    #superior based underwater color cast neutralization
    neu_img = neutralize_image(img)
    #Dual-intensity images fusion based on average of mean and median values
    img1, img2 = Stretching(neu_img)
    dual_img = enhanced_image(img1, img2)
    #Swarm-intelligence based mean equalization
    pso_res = pso_image(dual_img)
    #Unsharp masking
    nuce_img = unsharp_masking(pso_res)
    return nuce_img

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('imageProcessingUi.ui', self)
        self.SelectButton.clicked.connect(self.loadImage)
        self.ProcessButton.clicked.connect(self.Process)
        self.show()
        
    def loadImage(self):
        global filename
        filename, _ = QFileDialog.getOpenFileName(self)
        print('filename ' , filename)
        self.image=cv2.imread(filename)
        
        # cv2.imshow("img",img)
        self.setPhoto(self.image)

    def setPhoto(self,image):
        global filename
        self.tmp = image
        image = imutils.resize(image,width=640,height=480)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.ImageToShow.setPixmap(QtGui.QPixmap.fromImage(image))


    
    def Process(self):
        global filename
        print(filename)
        img = cv2.imread(filename)
        # cv2.imshow('sss',img)
        nuce_img = NUCE(img) 
        self.setPhoto(nuce_img)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()