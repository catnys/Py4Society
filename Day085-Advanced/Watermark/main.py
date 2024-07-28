import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Watermarker')

        # Layout setup
        mainLayout = QVBoxLayout()

        # Button to select image
        self.selectImageButton = QPushButton('Select Image', self)
        self.selectImageButton.clicked.connect(self.selectImage)
        mainLayout.addWidget(self.selectImageButton)

        # Label to display selected image
        self.imageLabel = QLabel(self)
        mainLayout.addWidget(self.imageLabel)

        # Field to enter watermark text
        self.watermarkText = QLineEdit(self)
        mainLayout.addWidget(self.watermarkText)

        # Button to apply watermark
        self.applyWatermarkButton = QPushButton('Apply Watermark', self)
        self.applyWatermarkButton.clicked.connect(self.applyWatermark)
        mainLayout.addWidget(self.applyWatermarkButton)

        # Label to display watermarked image
        self.watermarkedImageLabel = QLabel(self)
        mainLayout.addWidget(self.watermarkedImageLabel)

        self.setLayout(mainLayout)

    def selectImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Images (*.png *.xpm *.jpg)", options=options)
        if fileName:
            pixmap = QPixmap(fileName)
            self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio))
            self.currentImage = fileName

    def applyWatermark(self):
        if hasattr(self, 'currentImage'):
            watermarkText = self.watermarkText.text()
            image = Image.open(self.currentImage)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 15)
            textwidth, textheight = draw.textsize(watermarkText, font)
            width, height = image.size
            x = width / 2 - textwidth / 2
            y = height / 2 - textheight / 2
            draw.text((x, y), watermarkText, fill="white", font=font)
            image.save("watermarked_image.jpg")
            self.displayWatermarkedImage()

    def displayWatermarkedImage(self):
        pixmap = QPixmap("watermarked_image.jpg")
        self.watermarkedImageLabel.setPixmap(pixmap.scaled(self.watermarkedImageLabel.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WatermarkApp()
    ex.show()
    sys.exit(app.exec_())
