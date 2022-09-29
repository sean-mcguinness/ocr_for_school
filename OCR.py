from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QTextEdit, QLineEdit, QComboBox
from PyQt5 import uic
from PIL import Image
import sys
import config
import pytesseract
import ImageProcessing
import ImageProcessing
from ImageProcessing import imagefilter

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# TODO implement advanced Settings Page/Buttons, fix function adv settings

class UI(QMainWindow):

    # Initialization Method
    def __init__(self):
        super(UI, self).__init__()

        # Load ui file
        uic.loadUi("ui.ui", self)

        # Define Widgets
        self.selectBtn = self.findChild(QPushButton, "selectImage")
        self.runBtn = self.findChild(QPushButton, "runScript")
        self.textDisplay = self.findChild(QTextEdit, "textDisplay")
        self.inputPath = self.findChild(QLineEdit, "inputPath")
        self.selLang = self.findChild(QComboBox, "selLang")
        self.advSettings = self.findChild(QPushButton, "advSettings")

        # Events
        self.selectBtn.clicked.connect(self.fileselect)
        self.runBtn.clicked.connect(self.runscript)

        #to debug
        self.advSettings.clicked.connect(ImageProcessing.imagefilter())

        # Show App
        self.show()

    # Method to select file and store its path
    def fileselect(self):
        # get Filepath from Explorer selection
        fname = QFileDialog.getOpenFileName(self, 'Datei wählen', 'C:\Desktop')

        # Display Path and set filepath
        self.inputPath.setText(fname[0])

        config.filepath = self.inputPath.text()

        # self.optimizeImage()
        return config.filepath

        # Method for OpenCV image processing

    # Method to convert image to string and displaying it
    def runscript(self):

        # Dictionary for language selection
        langdict = {"Deutsch": "DEU",
                    "English": "ENG",

                    # TODO2 ADD Languages to Dictionary
                    "Other": "*"

                    }

        # get File Path
        config.filepath = self.inputPath.text()

        # find selected Language
        selectedlang = str(self.selLang.currentText())
        # get Language
        strlang = langdict[selectedlang]
        # store image in variable
        im = Image.open(config.filepath)
        # convert image to string
        config.outstring = pytesseract.image_to_string(im, lang=strlang)
        # display text
        self.textDisplay.setText(config.outstring)

        return config.outstring

# Initialize/Run App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
