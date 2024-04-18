# IMPORTAR QT CORE
from modulos_qt_core import *

from gui.pages.ui_pages import Ui_application_page
from gui.widgets.py_push_button import PyPushButton

# MAIN - JANELA
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")


        # DEFINIR PARÂMETROS INICIAIS
        # ///////////////////////////////////////////////////////////////
        parent.resize(960, 700)
        parent.setMinimumSize(960, 700)


        # CRIAR WIDGET CENTRAL
        # ///////////////////////////////////////////////////////////////
        self.central_frame = QFrame()


        # CRIAR LAYOUT PRINCIPAL
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)


        # MENU ESQUERDO
        # ///////////////////////////////////////////////////////////////
        self.menu_esquerdo = QFrame()
        self.menu_esquerdo.setStyleSheet("background-color: #44475a")
        self.menu_esquerdo.setMaximumWidth(50)
        self.menu_esquerdo.setMinimumWidth(50)


        # LAYOUT MENU ESQUERDO
        self.layout_menu_esquerdo = QVBoxLayout(self.menu_esquerdo)
        self.layout_menu_esquerdo.setContentsMargins(0,0,0,0)
        self.layout_menu_esquerdo.setSpacing(0)


        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red; }")


        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)


        # BOTÃO NO TOP
        self.ocultar_menu = PyPushButton(
            texto="Ocultar menu",
            icon_path="align-justify.svg"
        )
        self.btn_cm = PyPushButton(
            texto = "CM", 
            icon_path= "archive.svg",
            is_active= True
        )
        self.btn_linx = PyPushButton(
            texto = "Linx",
            icon_path= "airplay.svg",
            is_active= True
        )
        self.btn_totvs = PyPushButton(
            texto = "Totvs",
            icon_path= "package.svg",
            is_active= True
        )

        # ADICIONAR BOTÕES AO LAYOUT
        self.left_menu_top_layout.addWidget(self.ocultar_menu)
        self.left_menu_top_layout.addWidget(self.btn_cm)
        self.left_menu_top_layout.addWidget(self.btn_linx)
        self.left_menu_top_layout.addWidget(self.btn_totvs)


        # ESPAÇO NO MENU 
        # ///////////////////////////////////////////////////////////////
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)


        # BOTTOM FRAME MENU
        # ///////////////////////////////////////////////////////////////
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")


        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        # BOTÃO CONFIGURAÇÕES
        self.settings_btn = PyPushButton(
            texto = "Configurações",
            icon_path="icon_settings.svg",
            is_active= True
        )

        # ADICIONANDO AO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)


        # VERSÃO - RODAPÉ
        # ///////////////////////////////////////////////////////////////
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: white")


        # ADIONANDO TODOS AO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.layout_menu_esquerdo.addWidget(self.left_menu_top_frame)
        self.layout_menu_esquerdo.addItem(self.left_menu_spacer)
        self.layout_menu_esquerdo.addWidget(self.left_menu_bottom_frame)
        self.layout_menu_esquerdo.addWidget(self.left_menu_label_version)


        # CONTENT
        # ///////////////////////////////////////////////////////////////
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")


        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)


        # TOP BAR
        # ///////////////////////////////////////////////////////////////
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)


        # Left label
        self.top_label_left = QLabel("Aplicação para checar parametros neste PDV")


        # Top spacer
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        # Right label
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")


        # Add to layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.bottom_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)


        # Application pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;")
        self.ui_pages = Ui_application_page()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1_cm)


        # BOTTOM BAR
        # ///////////////////////////////////////////////////////////////
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")


        # BOTTOM BAR
        # ///////////////////////////////////////////////////////////////
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)

        # Left label
        self.bottom_label_left = QLabel("Testando aplicação")

        # Top spacer
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        # Right label
        self.bottom_bar_label_right = QLabel("| 2023")


        # Add to layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_bar_label_right)


        # Add to content layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)


        # ADD WIDGETS TO APP
        # ///////////////////////////////////////////////////////////////
        self.main_layout.addWidget(self.menu_esquerdo)
        self.main_layout.addWidget(self.content)


        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)





