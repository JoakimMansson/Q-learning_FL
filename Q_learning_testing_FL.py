import random
import time
import numpy as np
import pickle

from frozen_lake import FrozenLake


env = FrozenLake()

max_steps = 99                # Max steps per episode
with open("Q_learning_FL/Q_table_FL.pkl", "rb") as f:
    qtable = pickle.load(f)


# Testing the agent
for episode in range(5):
    env.reset_board()
    state = env.get_current_state()

    step = 0
    done = False
    print("****************************************************")
    print("EPISODE ", episode)

    for step in range(max_steps):
        
        action = np.argmax(qtable[state,:])
        
        new_state, reward = env.make_move_index(action)
        
        if reward == 1:
            
            print("Number of steps", step)
            break
        
        state = new_state