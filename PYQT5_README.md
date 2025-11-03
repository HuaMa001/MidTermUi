# PyQt5 Grid Layout Application

This application demonstrates a PyQt5 interface with a 3x3 grid layout pattern.

## Pattern

The grid layout displays buttons in a diagonal pattern:
```
O X X
X O X
X X O
```

Where:
- `O` represents a button
- `X` represents an empty space (spacer)

## Features

- 3x3 grid layout with centered alignment
- Three buttons of equal size (100x100 pixels)
- Spacers maintain the grid structure at empty positions
- Window is centered and properly sized (400x400 pixels)

## Requirements

- Python 3.x
- PyQt5 5.15.11 or later

## Installation

Install the required dependencies:

```bash
pip install PyQt5==5.15.11
```

## Usage

Run the application:

```bash
python3 grid_layout_app.py
```

Or make it executable and run directly:

```bash
chmod +x grid_layout_app.py
./grid_layout_app.py
```

## Implementation Details

The application creates a `QMainWindow` with a central widget containing a `QGridLayout`. The layout places:
- **Button 1** at position (0, 0) - top-left
- **Button 2** at position (1, 1) - center
- **Button 3** at position (2, 2) - bottom-right

Spacers are placed at all other positions to maintain the grid structure and keep the layout centered.
