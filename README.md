## Project : AlphaMelee, Automatic Position Evaluation in Super Smash Bros. Melee

AlphaMelee is an applied machine learning research project that aims to develop a neural network capable of evaluating the quality of a given position in Super Smash Bros. Melee, in a manner comparable to how engines like AlphaZero assess positions in chess.

The evaluation is performed frame by frame, based on in-game data extracted from Slippi replay files (.slp), allowing the model to assign a quantitative score to each situation. This score reflects the strategic advantage of a player at a specific moment during the match.

### **Core Components**:

- Data Extraction & Preprocessing: Parsing Slippi .slp files using the py-slippi Python library.

- Feature Engineering: Building input representations that capture both mechanical and strategic elements of gameplay.

- Evaluation Framework: Tools for model performance analysis and testing on real-world competitive match data.


### **Project Goals**:
Deliver a numerical assessment of in-game situations, supporting player training and post-match review.

Adapt position evaluation techniques inspired by game-playing AIs (e.g., chess engines) to the fast-paced, real-time nature of Super Smash Bros. Melee.

Build the foundation for advanced systems such as a delayed input recommendation engine, capable of suggesting optimal actions based on future frames.