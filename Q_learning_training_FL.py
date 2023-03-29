import random
import time
import numpy as np
import pickle

from frozen_lake import FrozenLake

env = FrozenLake()


y, x = env.get_dimensions_board()
state_size = y*x
# Up, left, down, right
action_size = 4
qtable = np.zeros((y*x, 4))



total_episodes = 15000        # Total episodes
learning_rate = 0.8           # Learning rate
max_steps = 99                # Max steps per episode
gamma = 0.95                  # Discounting rate

# Exploration parameters
epsilon = 1.0                 # Exploration rate
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.01            # Minimum exploration probability 
decay_rate = 0.005             # Exponential decay rate for exploration prob

rewards = []


# Training the agent
for episode in range(total_episodes):
    env.reset_board()
    state = env.get_current_state()

    step = 0
    done = False
    total_rewards = 0
    

    for step in range(max_steps):
        exp_tradeoff = random.uniform(0,1)

        if exp_tradeoff > epsilon:
            action = np.argmax(qtable[state, :])
        else:
            action = random.randint(0, 3)    

        new_state, reward = env.make_move_index(action)

        qtable[state, action] = qtable[state, action] + learning_rate*(reward + gamma*np.max(qtable[new_state, :]) - qtable[state, action])
        total_rewards += reward

        state = new_state


        if reward == 1:
            break 

    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
    rewards.append(total_rewards)

print ("Score over time: " +  str(sum(rewards)/total_episodes))
print(qtable)
            
with open('Q_learning_FL/Q_table_FL.pkl', 'wb') as f:
    pickle.dump(qtable, f, pickle.HIGHEST_PROTOCOL)

