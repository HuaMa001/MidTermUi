#!/usr/bin/env python3
"""
PyQt5 application with a 3x3 grid layout displaying a pattern:
OXX
XOX
XXO

Where O represents a button, and X represents an empty space (spacer).
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                              QGridLayout, QPushButton, QSpacerItem, 
                              QSizePolicy)
from PyQt5.QtCore import Qt


class GridLayoutWindow(QMainWindow):
    """Main window with a 3x3 grid layout pattern."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('3x3 Grid Layout Pattern')
        self.setGeometry(100, 100, 400, 400)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create grid layout
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        
        # Define the pattern: O = button (True), X = spacer (False)
        # Row 0: OXX
        # Row 1: XOX
        # Row 2: XXO
        pattern = [
            [True, False, False],  # Row 0: OXX
            [False, True, False],  # Row 1: XOX
            [False, False, True]   # Row 2: XXO
        ]
        
        # Create buttons and spacers according to the pattern
        button_count = 0
        for row in range(3):
            for col in range(3):
                if pattern[row][col]:
                    # Create a button
                    button_count += 1
                    button = QPushButton(f'Button {button_count}')
                    button.setMinimumSize(100, 100)
                    button.setMaximumSize(100, 100)
                    grid_layout.addWidget(button, row, col)
                else:
                    # Create a spacer
                    spacer = QSpacerItem(100, 100, QSizePolicy.Fixed, QSizePolicy.Fixed)
                    grid_layout.addItem(spacer, row, col)
        
        # Set spacing between grid cells
        grid_layout.setSpacing(10)
        
        # Center the grid layout in the window
        grid_layout.setAlignment(Qt.AlignCenter)


def main():
    """Main function to run the application."""
    app = QApplication(sys.argv)
    window = GridLayoutWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
