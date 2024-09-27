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

    def move_cursor_up(self):
        # Logic for moving the cursor up
        # Assuming multiline text; this moves the cursor to the start of the previous line
        current_line = self.text().count('\n', 0, self.cursorPosition())
        if current_line > 0:
            previous_line_start = self.text().rfind('\n', 0, self.cursorPosition()) + 1
            previous_line_end = self.text().find('\n', previous_line_start)
            if previous_line_end == -1:  # Last line
                previous_line_end = len(self.text())
            new_cursor_pos = previous_line_start + max(0, min(self.cursorPosition() - previous_line_start, previous_line_end - previous_line_start))
            self.setCursorPosition(new_cursor_pos)

    def move_cursor_down(self):
        # Logic for moving the cursor down
        # Assuming multiline text; this moves the cursor to the start of the next line
        current_line_end = self.text().find('\n', self.cursorPosition())
        if current_line_end != -1:
            next_line_start = current_line_end + 1
            next_line_end = self.text().find('\n', next_line_start)
            if next_line_end == -1:  # Last line
                next_line_end = len(self.text())
            new_cursor_pos = next_line_start + max(0, min(self.cursorPosition() - next_line_start, next_line_end - next_line_start))
            self.setCursorPosition(new_cursor_pos)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.move_cursor_left()
        elif event.key() == Qt.Key_Right:
            self.move_cursor_right()
        elif event.key() == Qt.Key_Up:
            self.move_cursor_up()
        elif event.key() == Qt.Key_Down:
            self.move_cursor_down()
        else:
            super().keyPressEvent(event)
