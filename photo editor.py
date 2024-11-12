#step 1: import modules
#pyqt5 -> buat app
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#PIL -> python image library
from PIL import ImageFilter
from PIL.ImageFilter import *
from PIL import Image
from PIL.Image import *

#upload folder
import os #operation system

#step 2: bikin app
#screen
width = 500
height = 500
app = QApplication([])
screen = QWidget()
screen.resize(width,height) #ganti ukuran
screen.setWindowTitle("Photo Editor Ynzz") #ganti sesuaiin kalian

#label image -> nampung imagenya
lb_image = QLabel("Image")
#list files photo
list_files = QListWidget()
#btn
#upload
btn_upload = QPushButton("upload a folder")
#filter
#bnw, puter kanan, puter kiri, flip, mirror, sharp, blur
#minimal 5
btn_bnw = QPushButton("Hitam dan Putih")
btn_flip = QPushButton("Flip")
btn_mirror = QPushButton("Mirror")
btn_sharp = QPushButton("Mempertajam/HD")
btn_blur = QPushButton("Buram/Kabur")

main_layout = QHBoxLayout()
kolom1 = QVBoxLayout()

kolom1.addWidget(list_files)
kolom1.addWidget(btn_upload)

layout_btn = QHBoxLayout()
layout_btn.addWidget(btn_bnw)
layout_btn.addWidget(btn_blur)
layout_btn.addWidget(btn_sharp)
layout_btn.addWidget(btn_mirror)
layout_btn.addWidget(btn_mirror)

kolom2 = QVBoxLayout()

kolom2.addLayout(layout_btn)
kolom2.addWidget(lb_image, 95)

main_layout.addLayout(kolom1, 40)
main_layout.addLayout(kolom2, 60)

screen.setLayout(main_layout)
screen.show