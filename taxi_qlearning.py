import gym
import numpy as np
import matplotlib.pyplot as plt

# Create environment
env = gym.make("Taxi-v3")

# Initialize Q-table
actions = env.action_space.n
states = env.observation_space.n

Q = np.zeros((states, actions))

# Hyperparameters
episodes = 1000
learning_rate = 0.7
discount = 0.618
epsilon = 1.0
epsilon_decay = 0.01

rewards = []

# Q-learning
for ep in range(episodes):

    state, info = env.reset()
    done = False
    total_reward = 0

    while not done:

        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])

        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        old_value = Q[state, action]
        next_max = np.max(Q[next_state])

        Q[state, action] = old_value + learning_rate * (
            reward + discount * next_max - old_value
        )

        state = next_state
        total_reward += reward

    epsilon = max(0.01, epsilon - epsilon_decay)
    rewards.append(total_reward)

# Plot rewards
plt.plot(rewards)
plt.title("Episode Rewards Over Time")
plt.xlabel("Episodes")
plt.ylabel("Rewards")
plt.grid()
plt.show()

env.close()

























# 1. Import required libraries
# import gymimport numpy as npimport matplotlib.pyplot as plt



# - gym: Provides the Taxi-v3 environment for reinforcement learning.
# - numpy: Used for numerical calculations and creating the Q-table.
# - matplotlib.pyplot: Used to plot the rewards obtained during training.
# 2. Create the environment
# env = gym.make("Taxi-v3")



# - Creates the Taxi-v3 environment using Gym.
# - In this environment, a taxi must pick up a passenger and drop them at the correct destination.
# - The agent learns how to complete this task by interacting with the environment.
# In simple words: We create a virtual taxi game where the computer learns how to pick up and drop off passengers correctly.








# hackernoon.com


# 3. Initialize the Q-table
# actions = env.action_space.nstates = env.observation_space.nQ = np.zeros((states, actions))



# - env.action_space.n returns the total number of possible actions.
# - Taxi-v3 has 6 actions:
#   1. Move south
#   2. Move north
#   3. Move east
#   4. Move west
#   5. Pick up passenger
#   6. Drop off passenger
# - env.observation_space.n returns the total number of possible states.
# - Taxi-v3 has 500 possible states.
# - np.zeros((states, actions)) creates a Q-table containing 500 rows and 6 columns.
# - Initially, all Q-values are set to zero.
# What is a Q-table?

# A Q-table stores the expected value of taking a particular action in a particular state. It helps the agent decide which action is better.
# 4. Define hyperparameters
# episodes = 1000learning_rate = 0.7discount = 0.618epsilon = 1.0epsilon_decay = 0.01



# These values control how the agent learns.
# - episodes = 1000: The agent plays the environment 1000 times.
# - learning_rate = 0.7: Controls how much new information affects the old Q-value.
# - discount = 0.618: Determines the importance of future rewards.
# - epsilon = 1.0: Initially, the agent explores by choosing random actions.
# - epsilon_decay = 0.01: Reduces exploration after every episode.
# Important terms:
# - Learning rate: How quickly the agent learns.
# - Discount factor: How much importance is given to future rewards.
# - Epsilon: Controls exploration versus exploitation.
# 5. Initialize the rewards list
# rewards = []



# - Creates an empty list to store the total reward obtained in each episode.
# - These rewards are later used to plot the learning progress.
# 6. Start Q-Learning training
# for ep in range(episodes):



# - Starts the training loop.
# - range(episodes) repeats the process 1000 times.
# - Each repetition is called an episode.
# Reset the environment
# state, info = env.reset()done = Falsetotal_reward = 0



# - env.reset() resets the environment to its initial state.
# - state stores the current state of the taxi.
# - info contains additional environment information.
# - done = False indicates that the episode is not finished.
# - total_reward = 0 initializes the reward counter.
# 7. Choose an action using Epsilon-Greedy strategy
# while not done:    if np.random.uniform(0, 1) < epsilon:        action = env.action_space.sample()    else:        action = np.argmax(Q[state])



# - while not done continues the episode until it finishes.
# - np.random.uniform(0, 1) generates a random number between 0 and 1.
# - If the random number is less than epsilon, the agent chooses a random action.
# - Otherwise, the agent chooses the action with the highest Q-value.
# - env.action_space.sample() selects a random action.
# - np.argmax(Q[state]) selects the action with the highest Q-value for the current state.
# In simple words: Sometimes the taxi tries a random action to explore. Otherwise, it chooses the action it has learned is best.
# 8. Perform the action
# next_state, reward, terminated, truncated, info = env.step(action)done = terminated or truncated



# - env.step(action) performs the selected action in the environment.
# - next_state stores the new state after performing the action.
# - reward stores the reward or penalty received.
# - terminated indicates whether the task has reached a terminal state.
# - truncated indicates whether the episode ended because of a time or step limit.
# - info contains additional information.
# - done becomes True if either termination condition occurs.
# Taxi-v3 rewards:
# Action or event	Reward
# Successful passenger drop-off	+20
# Illegal pickup or drop-off	-10
# Each normal movement step	-1

# 9. Update the Q-table
# old_value = Q[state, action]next_max = np.max(Q[next_state])



# - old_value stores the previous Q-value of the current state-action pair.
# - next_max finds the highest Q-value available in the next state.
# - This helps the agent estimate the future reward.
# Q[state, action] = old_value + learning_rate * (    reward + discount * next_max - old_value)



# - Updates the Q-value using the Q-Learning formula.
# - It considers the immediate reward and the best possible future Q-value.
# - The learning rate controls how much the new information changes the old value.
# The Q-Learning formula is:
# \[
# Q(s,a) \leftarrow Q(s,a)+
# \alpha[r+\gamma\max Q(s',a')-Q(s,a)]
# \]

# Where:
# - \(Q(s,a)\): Old Q-value.
# - \(\alpha\): Learning rate.
# - \(r\): Immediate reward.
# - \(\gamma\): Discount factor.
# - \(\max Q(s',a')\): Best future Q-value.
# 10. Move to the next state and calculate rewards
# state = next_statetotal_reward += reward



# - Updates the current state to the next state.
# - Adds the received reward to the total reward of the episode.
# - This process continues until the episode ends.
# 11. Reduce exploration and store rewards
# epsilon = max(0.01, epsilon - epsilon_decay)rewards.append(total_reward)



# - Reduces epsilon after every episode.
# - epsilon - epsilon_decay gradually reduces random exploration.
# - max(0.01, ...) ensures epsilon never goes below 0.01.
# - rewards.append(total_reward) stores the total reward obtained in the episode.
# In simple words: As the taxi learns, it explores less and starts using the actions it has learned are better.
# 12. Plot episode rewards
# plt.plot(rewards)plt.title("Episode Rewards Over Time")plt.xlabel("Episodes")plt.ylabel("Rewards")plt.grid()plt.show()



# - plt.plot(rewards) plots the rewards obtained in each episode.
# - plt.title() adds the graph title.
# - plt.xlabel() labels the X-axis.
# - plt.ylabel() labels the Y-axis.
# - plt.grid() displays grid lines.
# - plt.show() displays the graph.
# Graph interpretation: As the agent learns, its rewards should generally improve. Individual episodes can still have different rewards.
# 13. Close the environment
# env.close()



# - Closes the Taxi-v3 environment after training.
# - Releases the resources used by the environment.