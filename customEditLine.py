from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def move_cursor_left(self):
        cursor_pos = self.cursorPosition()
        if cursor_pos > 0:
            self.setCursorPosition(cursor_pos - 1)

    def move_cursor_right(self):
        cursor_pos = self.cursorPosition()
        if cursor_pos < len(self.text()):
            self.setCursorPosition(cursor_pos + 1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.move_cursor_left()
        elif event.key() == Qt.Key_Right:
            self.move_cursor_right()
        else:
            super().keyPressEvent(event)
