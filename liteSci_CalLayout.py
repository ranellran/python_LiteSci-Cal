from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QGridLayout, QLabel, QPushButton, QSpacerItem, QLineEdit
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QColor
from customEditLine import CustomLineEdit  # This is custom line edit

class SciCalcLayout(QWidget):
    # my global buttons
    sci_button = None
    num_button = None
    equal_button = None



    def __init__(self):
        super().__init__()
        self.create_global_buttons()  # Call to create global buttons
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LiteSci-Cal')
        self.setFixedSize(500, 800)

        # Create the main layout
        mainLayout = QVBoxLayout()  # Using QVBoxLayout for simplicity
        mainLayout.setContentsMargins(0, 10, 0, 0)  # Remove margins
        mainLayout.setSpacing(0)  # Remove spacing between widgets

        # Set the layout to the widget
        self.setLayout(mainLayout)

        # Create a background widget and set its layout
        background_widget = QWidget()
        background_widget.setStyleSheet("""
            background-color: #163E64;
            border-radius: 15px;
        """)
        background_layout = QVBoxLayout()
        background_layout.setContentsMargins(int(20), int(20), int(20), int(20))  # Remove margins
        background_layout.setSpacing(0)  # Remove spacing
        background_widget.setLayout(background_layout)

        # Add background widget to the main layout
        mainLayout.addWidget(background_widget)

        # Upper section
        upperSection = QWidget()
        upperSection.setFixedHeight(int(0.42 * 800))  # 40% of the height
        upperSection.setStyleSheet("""
            
            border-radius: 5px;
        """)
        background_layout.addWidget(upperSection)

        # Lower section
        lowerSection = QWidget()
        lowerSection.setFixedHeight(int(0.58 * 800))  # 60% of the height
        lowerSection.setStyleSheet("""
            background-color: #000;
            border-radius: 5px;
        """)
        background_layout.addWidget(lowerSection)

        # Make sure both sections stretch to fill the available width
        upperSection.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        lowerSection.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)



        # layout for the upper section to contain 3 rows
        upperLayout = QVBoxLayout()
        upperLayout.setContentsMargins(0,0,0,0)
        upperLayout.setSpacing(0)
        upperSection.setLayout(upperLayout)

        #Uppersection have 3 rows, header, screen and primary row
        # Add three equally sized rows to the upper section
        # Define percentage heights for each row

        # Row 1: Two columns with percentage-based width
        row1 = QWidget()
        row1Layout = QHBoxLayout()
        row1Layout.setContentsMargins(0, 0, 0, 0)
        row1Layout.setSpacing(0)
        row1.setLayout(row1Layout)

        



        col1 = QLabel('''<div style="text-align: left;">
                            <span style="font-family: 'Copperplate Gothic Bold'; font-size: 25px; font-weight: bold; color: #fff;">LiteSci-Cal</span><br>
                            <span style="font-family: 'Aptos Narrow'; font-size: 12px; font-style: italic; color: #fff;">by CipherCalcLeak</span>
                        </div>''')
        row1Layout.addWidget(col1)

        #col1.setStyleSheet("background-color: #A9A9A9;")  # Column 1 in gray
        col2 = QLabel('''<div style="text-align: right;">
                            <span style="font-family: 'Copperplate Gothic Bold'; font-size: 20px; color: #fff;">Ver. 1</span><br>
                            <span style="font-family: 'Aptos Narrow'; font-size: 12px; font-style: italic; color: #fff;">BETA</span>
                        </div>''')
        row1Layout.addWidget(col2)
        #col2.setStyleSheet("background-color: #808080;")  # Column 2 in darker gray

        row1Layout.addWidget(col1)
        row1Layout.setStretch(0, 50)  # 50% width for Column 1
        row1Layout.addWidget(col2)
        row1Layout.setStretch(1, 50)  # 50% width for Column 2


        upperLayout.addWidget(row1)
        upperLayout.setStretch(0, 15)  # 15% of the upper section height for Row 1







        # Row 2: Two rows with percentage-based height
        row2 = QWidget()
        row2Layout = QVBoxLayout()
        row2Layout.setContentsMargins(0, 20, 0, 20)  # Setting margins directly without converting to int
        row2Layout.setSpacing(0)
        row2.setStyleSheet("border-radius: 15px; background-color: #DCEAF7;")
        row2.setLayout(row2Layout)

        # Sub Row 1: Typing show text field
        self.input_field = CustomLineEdit()  # Create a QLineEdit for user input
        self.input_field.setStyleSheet("""
            border-radius: 0px;
            font-size: 25px;
            font-weight: bold;  /* Make text bold */
            color: #000;        /* Black text color */
        """)
        self.input_field.setPlaceholderText("")  # Placeholder text
        self.input_field.setFixedHeight(50)  # Fixed height for the input field

        # Add QLineEdit to the layout
        row2Layout.addWidget(self.input_field)
        row2Layout.setStretch(0, 60)  # 60% of Row 2 height for Sub Row 1




        # Sub Row 2: Answer section
        subRow2 = QLabel("")  # Create a QLabel for displaying the answer
        subRow2.setStyleSheet("""
            border-radius: 0px;
            font-size: 20px;
            font-weight: bold;  /* Make text bold */
            color: #000;        /* Black text color */
        """)
        subRow2.setFixedHeight(50)  # Fixed height for the answer display

        # Add answer display to the layout
        row2Layout.addWidget(subRow2)
        row2Layout.setStretch(1, 40)  # 40% of Row 2 height for Sub Row 2

        # Add the row2 widget to the upper layout
        upperLayout.addWidget(row2)
        upperLayout.setStretch(1, 40)  # 40% of the upper section height for Row 2









        # Row 3: Grid layout (6 columns, 3 rows) with merged cells
        row3 = QWidget()
        gridLayout = QGridLayout()
        row3.setLayout(gridLayout)




        # Add widgets to the grid (6x3)
        for i in range(18):  # 6 columns * 3 rows = 18 cells
            cell = QLabel()
            cell.setAlignment(Qt.AlignCenter)  # Corrected alignment with Qt.AlignCenter
            gridLayout.addWidget(cell, i // 6, i % 6)

        # Merge cells 3 and 4 (first row, columns 3 and 4)
        gridLayout.addWidget(QLabel(), 0, 2, 1, 2)
        gridLayout.addWidget(QLabel(), 2, 2, 1, 2)

        # Add buttons to the grid layout
        gridLayout.addWidget(self.shift_button, 0, 0)  # Cell 1
        gridLayout.addWidget(self.info_button, 0, 1)  # Cell 2
        gridLayout.addWidget(self.up_button, 0, 2, 1, 2)  # Merged cell 3 and 4
        gridLayout.addWidget(self.off_button, 0, 4)  # Cell 5
        gridLayout.addWidget(self.on_button, 0, 5)  # Cell 6
        gridLayout.addWidget(self.left_button, 1, 2)  # Cell 9
        gridLayout.addWidget(self.right_button, 1, 3)  # Cell 10
        gridLayout.addWidget(self.down_button, 2, 2, 1, 2)  # Merged cell 15 and 16

        # Create placeholders (spacers) for the empty cells
        gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0) 
        gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 1)  
        gridLayout.addItem(QSpacerItem(50, 30, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 3) 
        gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 4)  
        gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0)
        gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 1)
        gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 3)  
        gridLayout.addItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 4)

        upperLayout.addWidget(row3)
        upperLayout.setStretch(2, 40)  # 35% of the upper section height for Row 3

    def create_global_buttons(self):
        # Button attribute function (global styles for all buttons)
        def set_button_attributes(button):
            button.setStyleSheet("""
                QPushButton {
                    background-color: #DCEAF7;
                    border-radius: 5px;
                    font-family: 'Aptos Narrow';
                    font-size: 14px;
                    color: #000;
                }
                QPushButton:hover {
                    background-color: #A4D7F1;
                }
                QPushButton:pressed {
                    background-color: #4DB8E6;
                }
            """)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Set button size policy

        # Create buttons
        self.shift_button = QPushButton('Shift')
        set_button_attributes(self.shift_button)

        self.info_button = QPushButton('ⓘInfo')
        set_button_attributes(self.info_button)

        self.up_button = QPushButton('↑')
        set_button_attributes(self.up_button)

        self.off_button = QPushButton('Off')
        set_button_attributes(self.off_button)

        self.on_button = QPushButton('On')
        set_button_attributes(self.on_button)

        self.left_button = QPushButton('←')
        set_button_attributes(self.left_button)

        self.right_button = QPushButton('→')
        set_button_attributes(self.right_button)

        self.down_button = QPushButton('↓')
        set_button_attributes(self.down_button)



        # Connect buttons to their respective functions
        self.up_button.clicked.connect(self.move_cursor_up)
        self.down_button.clicked.connect(self.move_cursor_down)
        self.left_button.clicked.connect(self.move_cursor_left)
        self.right_button.clicked.connect(self.move_cursor_right)


    def move_cursor_up(self):
        print("Moving cursor up")  # Placeholder action

    def move_cursor_down(self):
        print("Moving cursor down")  # Placeholder action



    def move_cursor_left(self):
        cursor_pos = self.input_field.cursorPosition()
        print(f"Current cursor position before left: {cursor_pos}")
        if cursor_pos > 0:
            self.input_field.setCursorPosition(cursor_pos - 1)
            print(f"Cursor moved left to position: {self.input_field.cursorPosition()}")
        else:
            print("Cursor already at the start")

    def move_cursor_right(self):
        cursor_pos = self.input_field.cursorPosition()
        print(f"Current cursor position before right: {cursor_pos}")
        if cursor_pos < len(self.input_field.text()):
            self.input_field.setCursorPosition(cursor_pos + 1)
            print(f"Cursor moved right to position: {self.input_field.cursorPosition()}")
        else:
            print("Cursor already at the end")


    def move_cursor_left(self):
            self.input_field.move_cursor_left()  # Move the cursor left
            self.input_field.setFocus()  # Set focus back to input field

    def move_cursor_right(self):
            self.input_field.move_cursor_right()  # Move the cursor right
            self.input_field.setFocus()  # Set focus back to input field