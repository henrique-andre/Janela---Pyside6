from modulos_qt_core import *
from gui.images.icons import *

class Ui_application_page(object):
    def setupUi(self, application_page):
        if not application_page.objectName():
            application_page.setObjectName(u"application_page")
        application_page.resize(846, 726)
        self.page_1_cm = QWidget()
        self.page_1_cm.setObjectName(u"page_1_cm")
        self.frame_1 = QFrame(self.page_1_cm)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setGeometry(QRect(130, 40, 250, 70))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy)
        self.frame_1.setMinimumSize(QSize(250, 50))
        self.frame_1.setMaximumSize(QSize(250, 70))
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.label_hardware = QLabel(self.frame_1)
        self.label_hardware.setObjectName(u"label_hardware")
        self.label_hardware.setGeometry(QRect(10, 10, 230, 22))
        self.label_hardware.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_hardware = QPushButton(self.frame_1)
        self.btn_hardware.setObjectName(u"btn_hardware")
        self.btn_hardware.setEnabled(True)
        self.btn_hardware.setGeometry(QRect(10, 38, 100, 30))
        self.btn_hardware.setMinimumSize(QSize(100, 30))
        self.btn_hardware.setMaximumSize(QSize(100, 30))
        self.btn_hardware.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(r"gui\images\icons\hard-drive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_hardware.setIcon(icon)
        self.btn_hardware.setIconSize(QSize(20, 18))
        self.frame_2 = QFrame(self.page_1_cm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(130, 144, 250, 70))
        self.frame_2.setMinimumSize(QSize(250, 70))
        self.frame_2.setMaximumSize(QSize(250, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_tef = QLabel(self.frame_2)
        self.label_tef.setObjectName(u"label_tef")
        self.label_tef.setGeometry(QRect(10, 0, 241, 26))
        self.label_tef.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_prd = QPushButton(self.frame_2)
        self.btn_prd.setObjectName(u"btn_prd")
        self.btn_prd.setGeometry(QRect(120, 40, 100, 30))
        self.btn_prd.setMinimumSize(QSize(100, 30))
        self.btn_prd.setMaximumSize(QSize(100, 30))
        self.btn_prd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(r"gui\images\icons\Lane3000.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prd.setIcon(icon1)
        self.btn_prd.setIconSize(QSize(27, 29))
        self.btn_hml = QPushButton(self.frame_2)
        self.btn_hml.setObjectName(u"btn_hml")
        self.btn_hml.setGeometry(QRect(10, 40, 100, 30))
        self.btn_hml.setMinimumSize(QSize(100, 30))
        self.btn_hml.setMaximumSize(QSize(100, 30))
        self.btn_hml.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_hml.setIcon(icon1)
        self.btn_hml.setIconSize(QSize(27, 29))
        self.frame_3 = QFrame(self.page_1_cm)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(130, 248, 250, 70))
        self.frame_3.setMinimumSize(QSize(250, 70))
        self.frame_3.setMaximumSize(QSize(250, 70))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_version = QLabel(self.frame_3)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(10, 10, 230, 22))
        self.label_version.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_version = QPushButton(self.frame_3)
        self.btn_version.setObjectName(u"btn_version")
        self.btn_version.setGeometry(QRect(10, 38, 100, 30))
        self.btn_version.setMinimumSize(QSize(100, 30))
        self.btn_version.setMaximumSize(QSize(100, 30))
        self.btn_version.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(r"gui\images\icons\cm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_version.setIcon(icon2)
        self.btn_version.setIconSize(QSize(38, 25))
        self.frame_4 = QFrame(self.page_1_cm)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(130, 352, 250, 70))
        self.frame_4.setMinimumSize(QSize(250, 70))
        self.frame_4.setMaximumSize(QSize(250, 70))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_servicos = QLabel(self.frame_4)
        self.label_servicos.setObjectName(u"label_servicos")
        self.label_servicos.setGeometry(QRect(10, 10, 230, 22))
        self.label_servicos.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_servicos = QPushButton(self.frame_4)
        self.btn_servicos.setObjectName(u"btn_servicos")
        self.btn_servicos.setGeometry(QRect(10, 38, 100, 30))
        self.btn_servicos.setMinimumSize(QSize(100, 30))
        self.btn_servicos.setMaximumSize(QSize(100, 30))
        self.btn_servicos.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(r"gui\images\icons\cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_servicos.setIcon(icon3)
        self.frame_5 = QFrame(self.page_1_cm)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(130, 456, 250, 70))
        self.frame_5.setMinimumSize(QSize(250, 70))
        self.frame_5.setMaximumSize(QSize(250, 70))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_perifericos = QLabel(self.frame_5)
        self.label_perifericos.setObjectName(u"label_perifericos")
        self.label_perifericos.setGeometry(QRect(10, 10, 230, 22))
        self.label_perifericos.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_perifericos = QPushButton(self.frame_5)
        self.btn_perifericos.setObjectName(u"btn_perifericos")
        self.btn_perifericos.setGeometry(QRect(10, 38, 100, 30))
        self.btn_perifericos.setMinimumSize(QSize(100, 30))
        self.btn_perifericos.setMaximumSize(QSize(100, 30))
        self.btn_perifericos.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(r"gui\images\icons\printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_perifericos.setIcon(icon4)
        self.frame_6 = QFrame(self.page_1_cm)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(130, 560, 250, 70))
        self.frame_6.setMinimumSize(QSize(250, 70))
        self.frame_6.setMaximumSize(QSize(250, 70))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_loja = QLabel(self.frame_6)
        self.label_loja.setObjectName(u"label_loja")
        self.label_loja.setGeometry(QRect(10, 10, 230, 22))
        self.label_loja.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_loja = QPushButton(self.frame_6)
        self.btn_loja.setObjectName(u"btn_loja")
        self.btn_loja.setGeometry(QRect(10, 38, 100, 30))
        self.btn_loja.setMinimumSize(QSize(100, 30))
        self.btn_loja.setMaximumSize(QSize(100, 30))
        self.btn_loja.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(r"gui\images\icons\shopping-bag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_loja.setIcon(icon5)
        self.line = QFrame(self.page_1_cm)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(450, 70, 20, 651))
        self.line.setStyleSheet(u"rgb:(255, 255, 255)")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.page_1_cm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(410, 10, 111, 61))
        self.label.setPixmap(QPixmap(r"gui\images\icons\cm.png"))
        self.label.setScaledContents(True)
        application_page.addWidget(self.page_1_cm)
        self.page_2_linx = QWidget()
        self.page_2_linx.setObjectName(u"page_2_linx")
        self.frame = QFrame(self.page_2_linx)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 88, 250, 70))
        self.frame.setMinimumSize(QSize(250, 50))
        self.frame.setMaximumSize(QSize(250, 70))
        self.frame.setSizeIncrement(QSize(250, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_hardware_2 = QLabel(self.frame)
        self.label_hardware_2.setObjectName(u"label_hardware_2")
        self.label_hardware_2.setGeometry(QRect(0, 0, 230, 22))
        self.label_hardware_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_hardware_2 = QPushButton(self.frame)
        self.btn_hardware_2.setObjectName(u"btn_hardware_2")
        self.btn_hardware_2.setEnabled(True)
        self.btn_hardware_2.setGeometry(QRect(10, 30, 100, 30))
        self.btn_hardware_2.setMinimumSize(QSize(100, 30))
        self.btn_hardware_2.setMaximumSize(QSize(100, 30))
        self.btn_hardware_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_hardware_2.setIcon(icon)
        self.btn_hardware_2.setIconSize(QSize(20, 18))
        self.frame_7 = QFrame(self.page_2_linx)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(120, 168, 250, 70))
        self.frame_7.setMinimumSize(QSize(250, 70))
        self.frame_7.setMaximumSize(QSize(250, 70))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_tef_2 = QLabel(self.frame_7)
        self.label_tef_2.setObjectName(u"label_tef_2")
        self.label_tef_2.setGeometry(QRect(10, 0, 241, 26))
        self.label_tef_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_prd_2 = QPushButton(self.frame_7)
        self.btn_prd_2.setObjectName(u"btn_prd_2")
        self.btn_prd_2.setGeometry(QRect(120, 40, 100, 30))
        self.btn_prd_2.setMinimumSize(QSize(100, 30))
        self.btn_prd_2.setMaximumSize(QSize(100, 30))
        self.btn_prd_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_prd_2.setIcon(icon1)
        self.btn_prd_2.setIconSize(QSize(27, 29))
        self.btn_hml_2 = QPushButton(self.frame_7)
        self.btn_hml_2.setObjectName(u"btn_hml_2")
        self.btn_hml_2.setGeometry(QRect(10, 40, 100, 30))
        self.btn_hml_2.setMinimumSize(QSize(100, 30))
        self.btn_hml_2.setMaximumSize(QSize(100, 30))
        self.btn_hml_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_hml_2.setIcon(icon1)
        self.btn_hml_2.setIconSize(QSize(27, 29))
        self.frame_8 = QFrame(self.page_2_linx)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(120, 278, 250, 70))
        self.frame_8.setMinimumSize(QSize(250, 70))
        self.frame_8.setMaximumSize(QSize(250, 70))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_version_2 = QLabel(self.frame_8)
        self.label_version_2.setObjectName(u"label_version_2")
        self.label_version_2.setGeometry(QRect(10, 10, 230, 22))
        self.label_version_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_version_2 = QPushButton(self.frame_8)
        self.btn_version_2.setObjectName(u"btn_version_2")
        self.btn_version_2.setGeometry(QRect(10, 38, 100, 30))
        self.btn_version_2.setMinimumSize(QSize(100, 30))
        self.btn_version_2.setMaximumSize(QSize(100, 30))
        self.btn_version_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(r"gui\images\icons\linx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_version_2.setIcon(icon6)
        self.btn_version_2.setIconSize(QSize(38, 25))
        self.frame_9 = QFrame(self.page_2_linx)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(120, 368, 250, 70))
        self.frame_9.setMinimumSize(QSize(250, 70))
        self.frame_9.setMaximumSize(QSize(250, 70))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_servicos_2 = QLabel(self.frame_9)
        self.label_servicos_2.setObjectName(u"label_servicos_2")
        self.label_servicos_2.setGeometry(QRect(10, 10, 230, 22))
        self.label_servicos_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_servicos_2 = QPushButton(self.frame_9)
        self.btn_servicos_2.setObjectName(u"btn_servicos_2")
        self.btn_servicos_2.setGeometry(QRect(10, 38, 100, 30))
        self.btn_servicos_2.setMinimumSize(QSize(100, 30))
        self.btn_servicos_2.setMaximumSize(QSize(100, 30))
        self.btn_servicos_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_servicos_2.setIcon(icon3)
        self.frame_10 = QFrame(self.page_2_linx)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(120, 458, 250, 70))
        self.frame_10.setMinimumSize(QSize(250, 70))
        self.frame_10.setMaximumSize(QSize(250, 70))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_perifericos_2 = QLabel(self.frame_10)
        self.label_perifericos_2.setObjectName(u"label_perifericos_2")
        self.label_perifericos_2.setGeometry(QRect(10, 10, 230, 22))
        self.label_perifericos_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_perifericos_2 = QPushButton(self.frame_10)
        self.btn_perifericos_2.setObjectName(u"btn_perifericos_2")
        self.btn_perifericos_2.setGeometry(QRect(10, 38, 100, 30))
        self.btn_perifericos_2.setMinimumSize(QSize(100, 30))
        self.btn_perifericos_2.setMaximumSize(QSize(100, 30))
        self.btn_perifericos_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_perifericos_2.setIcon(icon4)
        self.frame_12 = QFrame(self.page_2_linx)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(120, 556, 250, 70))
        self.frame_12.setMinimumSize(QSize(250, 70))
        self.frame_12.setMaximumSize(QSize(250, 70))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_loja_2 = QLabel(self.frame_12)
        self.label_loja_2.setObjectName(u"label_loja_2")
        self.label_loja_2.setGeometry(QRect(10, 10, 230, 22))
        self.label_loja_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_loja_2 = QPushButton(self.frame_12)
        self.btn_loja_2.setObjectName(u"btn_loja_2")
        self.btn_loja_2.setGeometry(QRect(10, 38, 100, 30))
        self.btn_loja_2.setMinimumSize(QSize(100, 30))
        self.btn_loja_2.setMaximumSize(QSize(100, 30))
        self.btn_loja_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_loja_2.setIcon(icon5)
        self.line_2 = QFrame(self.page_2_linx)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(410, 70, 20, 651))
        self.line_2.setStyleSheet(u"rgb:(255, 255, 255)")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.page_2_linx)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 10, 61, 61))
        self.label_2.setPixmap(QPixmap(r"gui\images\icons\linx.png"))
        self.label_2.setScaledContents(True)
        application_page.addWidget(self.page_2_linx)
        self.page_3_totvs = QWidget()
        self.page_3_totvs.setObjectName(u"page_3_totvs")
        self.frame_13 = QFrame(self.page_3_totvs)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(110, 90, 250, 70))
        self.frame_13.setMinimumSize(QSize(250, 70))
        self.frame_13.setMaximumSize(QSize(250, 70))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.btn_hardware_3 = QPushButton(self.frame_13)
        self.btn_hardware_3.setObjectName(u"btn_hardware_3")
        self.btn_hardware_3.setEnabled(True)
        self.btn_hardware_3.setGeometry(QRect(10, 40, 100, 30))
        self.btn_hardware_3.setMinimumSize(QSize(100, 30))
        self.btn_hardware_3.setMaximumSize(QSize(100, 30))
        self.btn_hardware_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_hardware_3.setIcon(icon)
        self.btn_hardware_3.setIconSize(QSize(20, 18))
        self.label_hardware_3 = QLabel(self.frame_13)
        self.label_hardware_3.setObjectName(u"label_hardware_3")
        self.label_hardware_3.setGeometry(QRect(10, 10, 230, 22))
        self.label_hardware_3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame_14 = QFrame(self.page_3_totvs)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(110, 180, 250, 70))
        self.frame_14.setMinimumSize(QSize(250, 70))
        self.frame_14.setMaximumSize(QSize(250, 70))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_tef_4 = QLabel(self.frame_14)
        self.label_tef_4.setObjectName(u"label_tef_4")
        self.label_tef_4.setGeometry(QRect(10, 0, 241, 26))
        self.label_tef_4.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_prd_4 = QPushButton(self.frame_14)
        self.btn_prd_4.setObjectName(u"btn_prd_4")
        self.btn_prd_4.setGeometry(QRect(120, 40, 100, 30))
        self.btn_prd_4.setMinimumSize(QSize(100, 30))
        self.btn_prd_4.setMaximumSize(QSize(100, 30))
        self.btn_prd_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_prd_4.setIcon(icon1)
        self.btn_prd_4.setIconSize(QSize(27, 29))
        self.btn_hml_4 = QPushButton(self.frame_14)
        self.btn_hml_4.setObjectName(u"btn_hml_4")
        self.btn_hml_4.setGeometry(QRect(10, 40, 100, 30))
        self.btn_hml_4.setMinimumSize(QSize(100, 30))
        self.btn_hml_4.setMaximumSize(QSize(100, 30))
        self.btn_hml_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_hml_4.setIcon(icon1)
        self.btn_hml_4.setIconSize(QSize(27, 29))
        self.frame_15 = QFrame(self.page_3_totvs)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(110, 280, 250, 70))
        self.frame_15.setMinimumSize(QSize(250, 70))
        self.frame_15.setMaximumSize(QSize(250, 70))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_version_3 = QLabel(self.frame_15)
        self.label_version_3.setObjectName(u"label_version_3")
        self.label_version_3.setGeometry(QRect(10, 10, 230, 22))
        self.label_version_3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_version_3 = QPushButton(self.frame_15)
        self.btn_version_3.setObjectName(u"btn_version_3")
        self.btn_version_3.setGeometry(QRect(10, 38, 100, 30))
        self.btn_version_3.setMinimumSize(QSize(100, 30))
        self.btn_version_3.setMaximumSize(QSize(100, 30))
        self.btn_version_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(r"gui\images\icons\totvs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_version_3.setIcon(icon7)
        self.btn_version_3.setIconSize(QSize(38, 25))
        self.frame_16 = QFrame(self.page_3_totvs)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(110, 370, 250, 70))
        self.frame_16.setMinimumSize(QSize(250, 70))
        self.frame_16.setMaximumSize(QSize(250, 70))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_servicos_3 = QLabel(self.frame_16)
        self.label_servicos_3.setObjectName(u"label_servicos_3")
        self.label_servicos_3.setGeometry(QRect(10, 10, 230, 22))
        self.label_servicos_3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_servicos_3 = QPushButton(self.frame_16)
        self.btn_servicos_3.setObjectName(u"btn_servicos_3")
        self.btn_servicos_3.setGeometry(QRect(10, 38, 100, 30))
        self.btn_servicos_3.setMinimumSize(QSize(100, 30))
        self.btn_servicos_3.setMaximumSize(QSize(100, 30))
        self.btn_servicos_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_servicos_3.setIcon(icon3)
        self.frame_17 = QFrame(self.page_3_totvs)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(110, 460, 250, 70))
        self.frame_17.setMinimumSize(QSize(250, 70))
        self.frame_17.setMaximumSize(QSize(250, 70))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_perifericos_4 = QLabel(self.frame_17)
        self.label_perifericos_4.setObjectName(u"label_perifericos_4")
        self.label_perifericos_4.setGeometry(QRect(10, 10, 230, 22))
        self.label_perifericos_4.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_perifericos_4 = QPushButton(self.frame_17)
        self.btn_perifericos_4.setObjectName(u"btn_perifericos_4")
        self.btn_perifericos_4.setGeometry(QRect(10, 38, 100, 30))
        self.btn_perifericos_4.setMinimumSize(QSize(100, 30))
        self.btn_perifericos_4.setMaximumSize(QSize(100, 30))
        self.btn_perifericos_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_perifericos_4.setIcon(icon4)
        self.frame_18 = QFrame(self.page_3_totvs)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(110, 550, 250, 70))
        self.frame_18.setMinimumSize(QSize(250, 70))
        self.frame_18.setMaximumSize(QSize(250, 70))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_loja_3 = QLabel(self.frame_18)
        self.label_loja_3.setObjectName(u"label_loja_3")
        self.label_loja_3.setGeometry(QRect(10, 10, 230, 22))
        self.label_loja_3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btn_loja_3 = QPushButton(self.frame_18)
        self.btn_loja_3.setObjectName(u"btn_loja_3")
        self.btn_loja_3.setGeometry(QRect(10, 38, 100, 30))
        self.btn_loja_3.setMinimumSize(QSize(100, 30))
        self.btn_loja_3.setMaximumSize(QSize(100, 30))
        self.btn_loja_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.btn_loja_3.setIcon(icon5)
        self.line_3 = QFrame(self.page_3_totvs)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(400, 80, 20, 641))
        self.line_3.setStyleSheet(u"rgb:(255, 255, 255)")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.page_3_totvs)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 20, 61, 61))
        self.label_3.setPixmap(QPixmap(r"gui\images\icons\totvs.png"))
        self.label_3.setScaledContents(True)
        application_page.addWidget(self.page_3_totvs)
        self.page_4_config = QWidget()
        self.page_4_config.setObjectName(u"page_4_config")
        self.verticalLayout_5 = QVBoxLayout(self.page_4_config)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_4_config)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        application_page.addWidget(self.page_4_config)

        self.retranslateUi(application_page)

        application_page.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(application_page)
    # setupUi

    def retranslateUi(self, application_page):
        application_page.setWindowTitle(QCoreApplication.translate("application_page", u"StackedWidget", None))
        self.label_hardware.setText(QCoreApplication.translate("application_page", u"Informa\u00e7\u00f5es de hardware:", None))
        self.btn_hardware.setText(QCoreApplication.translate("application_page", u"Hardware", None))
        self.label_tef.setText(QCoreApplication.translate("application_page", u"Selecione o TEF desejado:", None))
        self.btn_prd.setText(QCoreApplication.translate("application_page", u"PRD", None))
        self.btn_hml.setText(QCoreApplication.translate("application_page", u"HML", None))
        self.label_version.setText(QCoreApplication.translate("application_page", u"Vers\u00e3o de CM instalada:", None))
        self.btn_version.setText(QCoreApplication.translate("application_page", u"Vers\u00e3o", None))
        self.label_servicos.setText(QCoreApplication.translate("application_page", u"Status de servi\u00e7os:", None))
        self.btn_servicos.setText(QCoreApplication.translate("application_page", u"Servi\u00e7os", None))
        self.label_perifericos.setText(QCoreApplication.translate("application_page", u"Verificar perif\u00e9ricos:", None))
        self.btn_perifericos.setText(QCoreApplication.translate("application_page", u"Perif\u00e9ricos ", None))
        self.label_loja.setText(QCoreApplication.translate("application_page", u"Informa\u00e7\u00f5es de Loja/UF:", None))
        self.btn_loja.setText(QCoreApplication.translate("application_page", u"Loja", None))
        self.label.setText("")
        self.label_hardware_2.setText(QCoreApplication.translate("application_page", u"Informa\u00e7\u00f5es de hardware:", None))
        self.btn_hardware_2.setText(QCoreApplication.translate("application_page", u"Hardware", None))
        self.label_tef_2.setText(QCoreApplication.translate("application_page", u"Selecione o TEF desejado:", None))
        self.btn_prd_2.setText(QCoreApplication.translate("application_page", u"PRD", None))
        self.btn_hml_2.setText(QCoreApplication.translate("application_page", u"HML", None))
        self.label_version_2.setText(QCoreApplication.translate("application_page", u"Vers\u00f5es Linx instalada:", None))
        self.btn_version_2.setText(QCoreApplication.translate("application_page", u"Vers\u00e3o", None))
        self.label_servicos_2.setText(QCoreApplication.translate("application_page", u"Status de servi\u00e7os:", None))
        self.btn_servicos_2.setText(QCoreApplication.translate("application_page", u"Servi\u00e7os", None))
        self.label_perifericos_2.setText(QCoreApplication.translate("application_page", u"Verificar perif\u00e9ricos:", None))
        self.btn_perifericos_2.setText(QCoreApplication.translate("application_page", u"Perif\u00e9ricos ", None))
        self.label_loja_2.setText(QCoreApplication.translate("application_page", u"Informa\u00e7\u00f5es de Loja/UF:", None))
        self.btn_loja_2.setText(QCoreApplication.translate("application_page", u"Loja", None))
        self.label_2.setText("")
        self.btn_hardware_3.setText(QCoreApplication.translate("application_page", u"Hardware", None))
        self.label_hardware_3.setText(QCoreApplication.translate("application_page", u"Informa\u00e7\u00f5es de hardware:", None))
        self.label_tef_4.setText(QCoreApplication.translate("application_page", u"Selecione o TEF desejado:", None))
        self.btn_prd_4.setText(QCoreApplication.translate("application_page", u"PRD", None))
        self.btn_hml_4.setText(QCoreApplication.translate("application_page", u"HML", None))
        self.label_version_3.setText(QCoreApplication.translate("application_page", u"Vers\u00f5es Totvs instaladas:", None))
        self.btn_version_3.setText(QCoreApplication.translate("application_page", u"Vers\u00e3o", None))
        self.label_servicos_3.setText(QCoreApplication.translate("application_page", u"Status de servi\u00e7os:", None))
        self.btn_servicos_3.setText(QCoreApplication.translate("application_page", u"Servi\u00e7os", None))
        self.label_perifericos_4.setText(QCoreApplication.translate("application_page", u"Verificar perif\u00e9ricos:", None))
        self.btn_perifericos_4.setText(QCoreApplication.translate("application_page", u"Perif\u00e9ricos ", None))
        self.label_loja_3.setText(QCoreApplication.translate("application_page", u"Informa\u00e7\u00f5es de Loja/UF:", None))
        self.btn_loja_3.setText(QCoreApplication.translate("application_page", u"Loja", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("application_page", u"Pagina 4", None))
    # retranslateUi

