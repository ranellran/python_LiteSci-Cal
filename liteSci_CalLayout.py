from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QGridLayout, QLabel, QPushButton, QSpacerItem
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QColor
from customEditLine import CustomLineEdit  # This is custom line edit
from PyQt5 import *

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
        self.setFixedSize(500, 900)

        # Create the main layout
        mainLayout = QVBoxLayout()  # Using QVBoxLayout for simplicity
        mainLayout.setContentsMargins(0, 10, 0, 0)  # Set top margin to 10
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
        background_layout.setContentsMargins(15, 15, 15, 25)  # Adjust margins, including the bottom
        background_layout.setSpacing(0)  # Remove spacing

        # Set size policy to expand with the window size dynamically
        background_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        background_widget.setLayout(background_layout)

        # Add background widget to the main layout
        mainLayout.addWidget(background_widget)

        # Upper section
        upperSection = QWidget()
        upperSection.setStyleSheet("""
            border-radius: 0px;
            
        """)
        background_layout.addWidget(upperSection)

        # Lower section
        lowerSection = QWidget()
        lowerSection.setStyleSheet("""
            
            border-radius: 0px;
        """)
        background_layout.addWidget(lowerSection)

        # Distribute space between upper and lower sections dynamically
        background_layout.setStretch(0, 40)  # 40% height for upper section
        background_layout.setStretch(1, 60)  # 60% height for lower section

        # Ensure both sections stretch to fill the available width and height
        upperSection.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lowerSection.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)



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











   




        # Assuming lowerSection is already defined as a QWidget somewhere in your code
        lowerLayout = QVBoxLayout()
        lowerLayout.setContentsMargins(0, 0, 0, 0)
        lowerLayout.setSpacing(0)
        lowerSection.setLayout(lowerLayout)


        # Row 1: Contains 3 sub-rows with equally distributed height
        lowerRow1 = QWidget()
        lowerLayoutRow1 = QVBoxLayout()  # Use QVBoxLayout for sub-rows
        lowerLayoutRow1.setContentsMargins(0, 0, 0, 0)
        lowerLayoutRow1.setSpacing(0)






        # Create 3 sub-rows for Row 1
        for row_index in range(3):
            sub_row = QWidget()
            sub_row_layout = QGridLayout()  # Use QGridLayout to arrange columns inside the row
            sub_row_layout.setContentsMargins(int(18), 0, int(18), 0)  # Remove margins
            sub_row_layout.setSpacing(5)  # Set spacing between buttons

            # Add buttons to each row (adjust buttons for each row index)
            if row_index == 0:
                # Row 1 Buttons
                buttons = [
                    self.frac_button, self.cubed_button, self.squared_button, 
                    self.exponent_button, self.factorial_button, self.root_button
                ]
            elif row_index == 1:
                # Row 2 Buttons
                buttons = [
                    self.mfrac_button, self.cubed_root_button, self.sqrt_button, 
                    self.sin_button, self.cos_button, self.tan_button
                ]
            elif row_index == 2:
                # Row 3 Buttons
                buttons = [
                    self.percent_button, self.left_paren_button, self.right_paren_button,
                    self.arcsin_button, self.arccos_button, self.arctan_button
                ]

            # Set button attributes for fixed height
            def set_fixed_button_height(button):
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Width expands, height fixed
                button.setFixedHeight(35)  # Set a fixed height for the button

            # Create 6 equally distributed columns for each row
            for col_index, button in enumerate(buttons):
                set_fixed_button_height(button)
                sub_row_layout.addWidget(button, 0, col_index)  # Add button to the grid

            # Set column stretch so that they are equally distributed in width
            for col_index in range(len(buttons)):
                sub_row_layout.setColumnStretch(col_index, 1)

            sub_row.setLayout(sub_row_layout)
            lowerLayoutRow1.addWidget(sub_row)
            lowerLayoutRow1.setStretch(lowerLayoutRow1.count() - 1, 1)  # Equal height for rows

        # Add Row 1 to the layout and set its height proportion
        lowerRow1.setLayout(lowerLayoutRow1)
        lowerLayout.addWidget(lowerRow1)
        lowerLayout.setStretch(0, 30)  # 30% of the upper section height for Row 1























        # Row 2: Contains 3 columns with adjustable width
        lowerRow2 = QWidget()
        lowerLayoutRow2 = QHBoxLayout()
        lowerLayoutRow2.setContentsMargins(int(18), 0, int(18), 0)
        lowerLayoutRow2.setSpacing(0)



        # Create 3 columns for Row 2
        for i in range(3):
            column = QWidget()
            column.setStyleSheet("background-color: #000; border-radius: 0px; border: 1px solid #000;")
            
            columnLayout = QVBoxLayout()  # Use QVBoxLayout for rows inside the column
            columnLayout.setContentsMargins(0, 0, 0, 0)  # Set all margins to 0
            
            # Column 1: 4 rows with adjustable height
            if i == 0:
                for _ in range(4):
                    row = QWidget()
                    row.setStyleSheet("background-color: #FFF; border-radius: 0px;")
                    columnLayout.addWidget(row)
                    columnLayout.setStretch(columnLayout.count() - 1, 1)  # Equal height for rows

            # Column 3: 4 rows with adjustable height
            elif i == 2:
                for _ in range(4):
                    row = QWidget()
                    row.setStyleSheet("background-color: #FFF; border-radius: 0px;")
                    columnLayout.addWidget(row)
                    columnLayout.setStretch(columnLayout.count() - 1, 1)  # Equal height for rows

            # Add layout to the column
            column.setLayout(columnLayout)
            lowerLayoutRow2.addWidget(column)

        # Set adjustable column widths (percentages)
        lowerLayoutRow2.setStretch(0, 64)  # Column 1: 65% of the width
        lowerLayoutRow2.setStretch(1, 3)  # Column 2: 10% of the width
        lowerLayoutRow2.setStretch(2, 33)  # Column 3: 30% of the width

        # Add Row 2 to the layout and set its height proportion
        lowerRow2.setLayout(lowerLayoutRow2)
        lowerLayout.addWidget(lowerRow2)
        lowerLayout.setStretch(1, 70)  # 60% height for Row 2







































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

        #SciCal Button
        #Row1 Button
        self.frac_button = QPushButton('x/y')
        set_button_attributes(self.frac_button)

        self.cubed_button = QPushButton('x^3')
        set_button_attributes(self.cubed_button)

        self.squared_button = QPushButton('x^2')
        set_button_attributes(self.squared_button)

        self.exponent_button = QPushButton('x^y')
        set_button_attributes(self.exponent_button)

        self.factorial_button = QPushButton('x!')
        set_button_attributes(self.factorial_button)

        self.root_button = QPushButton('n√x')
        set_button_attributes(self.root_button)
           
        #Row2 Button
        self.mfrac_button = QPushButton('z[x/y]')
        set_button_attributes(self.mfrac_button)

        self.cubed_root_button = QPushButton('3√x')
        set_button_attributes(self.cubed_root_button)

        self.sqrt_button = QPushButton('√x')
        set_button_attributes(self.sqrt_button)

        self.sin_button = QPushButton('Sin')
        set_button_attributes(self.sin_button)

        self.cos_button = QPushButton('Cos')
        set_button_attributes(self.cos_button)

        self.tan_button = QPushButton('Tan')
        set_button_attributes(self.tan_button)

        #Row3 Button
        self.percent_button = QPushButton('%')
        set_button_attributes(self.percent_button)

        self.left_paren_button = QPushButton('(')
        set_button_attributes(self.left_paren_button)

        self.right_paren_button = QPushButton(')')
        set_button_attributes(self.right_paren_button)

        self.arcsin_button = QPushButton('Sin^-1')
        set_button_attributes(self.arcsin_button)

        self.arccos_button = QPushButton('Cos^-2')
        set_button_attributes(self.arccos_button) 

        self.arctan_button = QPushButton('Tan^-3')
        set_button_attributes(self.arctan_button)



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