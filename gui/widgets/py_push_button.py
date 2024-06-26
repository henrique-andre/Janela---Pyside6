# IMPORTS
import os

# IMPORT QT CORE
from modulos_qt_core import *

class PyPushButton(QPushButton):
    def __init__(
        self,
        texto = "",
        altura = 40,
        largura_mínima = 50,
        text_padding = 55,
        cor_texto = "#c3ccdf",
        icon_path = "",
        cor_icone = "white",
        btn_color = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_active = False
    ):
        super().__init__()

        # Definir parâmetros padrão
        self.setText(texto)
        self.setMaximumHeight(altura)
        self.setMinimumHeight(altura)
        self.setCursor(Qt.PointingHandCursor)

        # Parâmetros personalizados
        self.minimum_width = largura_mínima
        self.text_padding = text_padding
        self.text_color = cor_texto
        self.icon_path = icon_path
        self.icon_color = cor_icone
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Definir estilo
        self.definir_estilo(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
    
    def set_active(self, is_active_menu):
        self.definir_estilo(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )

    def definir_estilo(
        self,
        text_padding = 55,
        text_color = "#c3ccdf",
        btn_color = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_active = False
    ):
        estilo = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        ativar_estilo = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid #282a36;
        }}
        """
        if not is_active:
            self.setStyleSheet(estilo)
        else:
            self.setStyleSheet(estilo + ativar_estilo)

    def paintEvent(self, event):
        # Retornar estilo padrão
        QPushButton.paintEvent(self, event)

        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())

        self. desenhar_ícone(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def  desenhar_ícone(self, qp, image, rect, color):
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Ícone de desenho
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()