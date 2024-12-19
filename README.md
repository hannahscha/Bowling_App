# Bowling Advice App
By: 

Lyric Abdul-Rasheed

Dominique Mahoner

Hannah Schaeffer

# Overview
This project is a bowling performance improvement system that helps users optimize their game by providing advice on how to improve their score. The system takes three input parameters from the user: throw speed, throw angle, and last round score. Based on these inputs, the system predicts the score the user should have achieved, and then suggests adjustments to these parameters (speed and angle) to help the user improve their performance.

# How it Works:
## User Inputs:

The user provides their throw speed (ranging from slow to fast), throw angle (ranging from 30° to 60°), and their last round score.
## Score Prediction:

The model takes the user's input values (throw speed, throw angle) and predicts what their score should have been based on the trained model. This prediction is a reflection of how the current combination of parameters would likely perform.
## Adjustment Process:

The system then varies the input values slightly to explore if small changes in either throw speed or throw angle can lead to a better score from the model. It adjusts the values of speed by small increments (±1) and changes the angle within a small range (±2 degrees).
## Evaluation:

For each adjustment, the model re-predicts the score. The system compares all potential adjustments, and provides the combination of changes that results in the largest improvement to the score with minimized adjustments.
## Output:

The app then advises the best combination of throw speed and throw angle that could improve the user's performance.

# Future Implementations
The model needs to be retrained on a larger dataset to make better predictions and discover more patterns between inputs and outputs.
