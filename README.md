

# Conway's Game of Life

This project implements Conway's Game of Life, a famous cellular automaton devised by mathematician John Conway. The simulation demonstrates how simple rules can lead to complex and emergent behavior in a grid-based system.  

## Features
- Randomly initialized grid
- Dynamic updates following the Game of Life rules
- Visualization of grid evolution using `matplotlib`  

## Installation
1. Clone this repository:  
   ```bash
   git clone <repository-url>
   ```
2. Install the required Python libraries:  
   ```bash
   pip install numpy matplotlib
   ```

## How to Run
1. Open the script `game_of_life.py`.
2. Modify grid size (`rows` and `cols`) and number of steps if needed.
3. Run the script:  
   ```bash
   python game_of_life.py
   ```

## Rules of the Game
1. A cell with fewer than 2 neighbors dies (underpopulation).  
2. A cell with 2 or 3 neighbors survives.  
3. A cell with more than 3 neighbors dies (overpopulation).  
4. A dead cell with exactly 3 neighbors becomes alive (reproduction).  

## Example Output
The grid evolves over time and displays the progression of the simulation in real-time.  

## License
This project is released under the [MIT License](LICENSE).  

