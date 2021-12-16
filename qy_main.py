import PyQt6.QtWidgets as Manager
from PyQt6.QtCore import Qt
import sys

# app = QApplication(sys.argv)
#
# window = QWidget()
# button = QPushButton('Push me')
# window.setWindowTitle('My First Win')
# window.setC
# window.setGeometry(400, 200, 400, 400)
# window.show()
# app.exec()
from PyQt6.QtGui import QPixmap


class MainWindow(Manager.QMainWindow):
    def __init__(self, title='My Window'):

        super().__init__()
        #  --------------------------------------------------------------------- #
        #  Setting Main window
        self.setWindowTitle(title)
        # self.setFixedSize(400, 400)
        self.setGeometry(400, 200, 400, 400)
        self.setMinimumSize(350, 400)
        self.setMaximumSize(800, 800)

        #  --------------------------------------------------------------------- #
        # Creating Button
        self.button = Manager.QPushButton('Press me')
        self.click_count = 0

        self.button.setCheckable(True)
        self.button.clicked.connect(self.handle_click)

        #  --------------------------------------------------------------------- #
        # Creating label
        self.label = Manager.QLabel('Default label Text')

        # setting label font
        font = self.label.font()
        font.setPointSize(15)
        self.label.setFont(font)

        # creating label with image
        self.img_label = Manager.QLabel('')

        #  --------------------------------------------------------------------- #
        #  Creating check-box

        self.chk_box = Manager.QCheckBox('Hey! I am Checkbox')
        # self.chk_box.setCheckState(Qt.CheckState.Checked)
        self.chk_box.stateChanged.connect(self.check_handle)

        #  --------------------------------------------------------------------- #
        # creating button to show image
        self.btn_img = Manager.QPushButton('show image')
        self.btn_img.setCheckable(True)
        self.btn_img.clicked.connect(self.handle_btn_img)

        #  --------------------------------------------------------------------- #
        # creating input
        self.input = Manager.QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        #  --------------------------------------------------------------------- #
        # Creating ComboBox
        self.combo_box = Manager.QComboBox()
        self.combo_box.addItems(['Apple', 'Banana', 'Mango'])

        # self.combo_box.currentIndexChanged()

        #  --------------------------------------------------------------------- #
        # setting layout
        self.layout = Manager.QVBoxLayout()
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.btn_img)
        self.layout.addWidget(self.img_label)
        self.layout.addWidget(self.chk_box)
        self.layout.addWidget(self.combo_box)

        #  --------------------------------------------------------------------- #

        #  --------------------------------------------------------------------- #
        #  Setting container
        self.container = Manager.QWidget()
        self.container.setLayout(self.layout)

        #  --------------------------------------------------------------------- #

        #  --------------------------------------------------------------------- #
        # Set the central widget of the Window.
        self.setCentralWidget(self.container)

        #  --------------------------------------------------------------------- #

    #  -------------------------------------------------------------------------------- #

    def handle_click(self):

        # self.button.setEnabled(False)
        self.setWindowTitle('Clicked Done')
        self.click_count += 1
        self.button.setText(f'{self.click_count} clicks')
        print(self.label.text())

    def again_click(self, checked):
        print('you click again butoon ', checked)

    #  --------------------------------------------------------------------- #

    def handle_btn_img(self, checked):

        if checked:
            self.img_label.setPixmap(QPixmap('gator.jpg'))
            self.btn_img.setText('Hide Image')

        else:
            self.img_label.setPixmap(QPixmap())
            self.btn_img.setText('Show Image')

    #  --------------------------------------------------------------------- #

    def check_handle(self, state):
        if state:
            self.chk_box.setText('I am Enable')
        else:
            self.chk_box.setText('I am Disable')


app = Manager.QApplication(sys.argv)
window = MainWindow('I AM WINDOW')
window.show()
app.exec()
