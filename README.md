# Q-learning_FL
Implementation of the reinforcement learning algorithm Q-learning. Solving the game Frozen Lake.


Frozen Lake is a 2D-game consisting of a game board such as: 
&nbsp; &nbsp; &nbsp; &nbsp; 
["S", "F", "F"],
&nbsp; &nbsp; &nbsp; &nbsp;
["F", "H", "F"],
&nbsp; &nbsp; &nbsp; &nbsp; 
["F", "H", "F"],
&nbsp; &nbsp; &nbsp; &nbsp;
["F", "F", "G"]

The ultimate goal of the game is for player ("S") to reach the goal ("G") walking through frozen areas ("F") without
falling through any of the holes ("H"). 

This task was solved through tabular reinforcement learning (Q-learning). The AI learns during the training stage using
an epsilon greedy strategy to balance exploring and exploitation of the environment. After training the model is is saved and
can be used to win the game. 
