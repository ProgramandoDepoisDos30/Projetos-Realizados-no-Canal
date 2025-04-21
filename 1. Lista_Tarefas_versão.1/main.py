import sys  # Módulo para interagir com o sistema
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel, QListWidgetItem  # Widgets do PyQt5
from PyQt5.QtGui import QPixmap, QPalette, QColor, QBrush  # Usado para imagem e cores
from PyQt5.QtCore import Qt  # Usado para alinhamento

# Classe principal do aplicativo
class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()  # Inicializa a superclasse QWidget

        # Configuração da janela
        self.setWindowTitle("To-Do List Dark")  # Título da janela
        self.setGeometry(100, 100, 300, 400)  # Define posição e tamanho da janela

        self.layout = QVBoxLayout()  # Cria um layout vertical
        self.setLayout(self.layout)  # Aplica o layout à janela

        # === Avatar no topo ===
        self.avatar_label = QLabel()  # Cria o espaço para exibir a imagem
        self.avatar_pixmap = QPixmap("avatar.png")  # Carrega a imagem do avatar
        self.avatar_pixmap = self.avatar_pixmap.scaledToWidth(100)  # Redimensiona a imagem para largura de 100px
        self.avatar_label.setPixmap(self.avatar_pixmap)  # Define a imagem no label
        self.avatar_label.setAlignment(Qt.AlignCenter)  # Centraliza a imagem no topo
        self.layout.addWidget(self.avatar_label)  # Adiciona o label ao layout

        # === Campo de entrada de tarefas ===
        self.task_input = QLineEdit()  # Campo de texto para digitar a tarefa
        self.task_input.setPlaceholderText("Digite uma nova tarefa...")  # Texto de dica
        self.layout.addWidget(self.task_input)  # Adiciona o campo ao layout

        # === Botão de adicionar tarefa ===
        self.add_button = QPushButton("Adicionar")  # Cria o botão
        self.layout.addWidget(self.add_button)  # Adiciona o botão ao layout

        # === Lista de tarefas ===
        self.task_list = QListWidget()  # Cria a lista de tarefas
        self.layout.addWidget(self.task_list)  # Adiciona a lista ao layout

        # === Conecta o clique do botão à função de adicionar tarefa ===
        self.add_button.clicked.connect(self.add_task)

    # Função para adicionar tarefa na lista
    def add_task(self):
        task = self.task_input.text()  # Pega o texto digitado
        if task:  # Se não estiver vazio
            item = QListWidgetItem(task)
            item.setForeground(QBrush(Qt.white))  # Define o texto da tarefa como branco
            self.task_list.addItem(item)  # Adiciona o item à lista
            self.task_input.clear()  # Limpa o campo de texto

# Código que roda a aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Cria a aplicação

    # === Tema Dark ===
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(30, 30, 30))  # Cor do fundo da janela
    dark_palette.setColor(QPalette.WindowText, Qt.white)        # Cor do texto
    dark_palette.setColor(QPalette.Base, QColor(20, 20, 20))    # Fundo dos campos de entrada
    dark_palette.setColor(QPalette.Text, Qt.black)              # Texto dos campos
    dark_palette.setColor(QPalette.Button, QColor(45, 45, 45))  # Fundo dos botões
    dark_palette.setColor(QPalette.ButtonText, Qt.black)        # Texto dos botões
    dark_palette.setColor(QPalette.Highlight, QColor(60, 60, 60))  # Seleção na lista
    dark_palette.setColor(QPalette.HighlightedText, Qt.white)   # Texto selecionado

    app.setPalette(dark_palette)

    window = ToDoApp()  # Cria a janela
    window.show()  # Mostra a janela
    sys.exit(app.exec_())  # Executa a aplicação e finaliza ao fechar
