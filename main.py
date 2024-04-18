# IMPORTAR MÓDULOS
import sys
import os

# IMPORTAR MÓDULOS QT CORE
from modulos_qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *

# MAIN WINDOW
class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckConfig PDV")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.ocultar_menu.clicked.connect(self.ocultar_menu)

        # Btn CM
        self.ui.btn_cm.clicked.connect(self.pagina_1)

        # Btn Linx
        self.ui.btn_linx.clicked.connect(self.pagina_2)

        # Btn Totvs
        self.ui.btn_totvs.clicked.connect(self.pagina_3)

        # Btn Configurações
        self.ui.settings_btn.clicked.connect(self.pagina_4)

        # EXIBI A NOSSA APLICAÇÃO
        self.show()

    # Redefinir seleção do botão
    def reset_selection(self):
        for btn in self.ui.menu_esquerdo.findChildren(QPushButton):
            try:
                btn.set_active(True)
            except:
                pass

    # Change text - Home Page
    def pagina_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1_cm)
        self.ui.btn_cm.set_active(True)

    def pagina_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2_linx)
        self.ui.btn_linx.set_active(True) 

    def pagina_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3_totvs)
        self.ui.btn_totvs.set_active(True)  

    def pagina_4(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4_config)
        self.ui.settings_btn.set_active(True)     

    # Toggle button
    def ocultar_menu(self):
        # Get menu width
        largura_do_menu = self.ui.menu_esquerdo.width()

        # Verificar a largura
        largura = 50
        if largura_do_menu == 50:
            largura = 150

        # Estartar animação
        self.animation = QPropertyAnimation(self.ui.menu_esquerdo, b"minimumWidth")
        self.animation.setStartValue(largura_do_menu)
        self.animation.setEndValue(largura)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("gui\images\icons\logo_boti.ico"))
    window = Janela()
    sys.exit(app.exec())