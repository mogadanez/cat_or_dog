from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
import numpy as np
from keras.preprocessing import image

import sys

       

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        self.initUI()
        self.show()
        self. classifier = load_model("cat_or_dog.h5")

 

    def initUI(self):
        self.setWindowTitle("My Program")
        self.pixmap.setScaledContents(True)
        self.pushButton.clicked.connect(self.openFileDialog)

    # ------ PART 1 : MENU BAR --------

    def openFileDialog(self): # File -> Exit
        dialog = QtWidgets.QFileDialog()
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile);
        dialog.setNameFilters(["Image files (*.png *.jpg *.jpeg)"]);
        if(dialog.exec()):
            fileName = dialog.selectedFiles()[0]
            imageObject = QImage()
            imageObject.load(fileName)
            self.pixmap.setPixmap(QPixmap.fromImage(imageObject));

            test_image = image.load_img(fileName, target_size=(64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            result = self.classifier.predict(test_image)
            if result[0][0] == 1:
                prediction = 'dog'
            else:
                prediction = 'cat'
            self.txtResult.setText(prediction )
        
       



    # ------ PART 2 : GUI --------

    def slider_update(self):
        cel = self.horizontalSlider.value()
        self.lcdNumber_2.display(int(cel*3))

       


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater) # if using IPython Console
    window = Ui()
    sys.exit(app.exec_())


