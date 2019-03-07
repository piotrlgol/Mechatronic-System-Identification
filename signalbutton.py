from PyQt5.QtWidgets import QPushButton

class SignalButton(QPushButton):
    def __init__():
        super().__init__()

    def on_clicked(self, bool):
        self.bool = not self.bool
        self.isclicked.emit(self.bool, self)