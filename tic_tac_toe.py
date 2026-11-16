
import random
import pickle

# Tic-Tac-Toe game
class TicTacToe:

    def __init__(self):
        self.board = [' '] * 9

    def display(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("------")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]

        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]

        return None


# Q-Learning Agent
class QLearningAgent:

    def __init__(self):
        self.q = {}
        self.lr = 0.1
        self.discount = 0.9
        self.epsilon = 0.2

    def get_state(self, board):
        return tuple(board)

    def choose_action(self, board):
        state = self.get_state(board)
        moves = [i for i, x in enumerate(board) if x == ' ']

        if random.uniform(0, 1) < self.epsilon:
            return random.choice(moves)

        qvals = [self.q.get((state, a), 0) for a in moves]
        max_q = max(qvals)

        best_moves = [
            a for a, q in zip(moves, qvals) if q == max_q
        ]

        return random.choice(best_moves)

    def update(self, state, action, reward, next_state, done):
        old_q = self.q.get((state, action), 0)

        if done:
            future_q = 0
        else:
            future_q = max(
                [self.q.get((next_state, a), 0)
                 for a in range(9)
                 if next_state[a] == ' '],
                default=0
            )

        self.q[(state, action)] = old_q + self.lr * (
            reward + self.discount * future_q - old_q
        )


# Training function
def train_agent(agent, episodes):

    for ep in range(episodes):

        game = TicTacToe()

        while True:

            # AI plays X
            state = agent.get_state(game.board)
            action = agent.choose_action(game.board)
            game.make_move(action, 'X')

            if game.check_winner() == 'X':
                agent.update(state, action, 1, None, True)
                break

            if not game.available_moves():
                agent.update(state, action, 0, None, True)
                break

            # Random opponent plays O
            opponent_move = random.choice(game.available_moves())
            game.make_move(opponent_move, 'O')

            if game.check_winner() == 'O':
                agent.update(state, action, -1, None, True)
                break

            if not game.available_moves():
                agent.update(state, action, 0, None, True)
                break

            next_state = agent.get_state(game.board)
            agent.update(state, action, 0, next_state, False)

        # Reduce exploration gradually
        agent.epsilon = max(0.05, agent.epsilon * 0.9997)


# Testing function
def test_agent(agent, games=100):

    old_epsilon = agent.epsilon
    agent.epsilon = 0

    wins = 0
    draws = 0
    losses = 0

    for _ in range(games):

        game = TicTacToe()

        while True:

            action = agent.choose_action(game.board)
            game.make_move(action, 'X')

            if game.check_winner() == 'X':
                wins += 1
                break

            if not game.available_moves():
                draws += 1
                break

            opponent_move = random.choice(game.available_moves())
            game.make_move(opponent_move, 'O')

            if game.check_winner() == 'O':
                losses += 1
                break

            if not game.available_moves():
                draws += 1
                break

    agent.epsilon = old_epsilon

    print("\n===== TEST RESULTS =====")
    print("Wins:", wins)
    print("Draws:", draws)
    print("Losses:", losses)


# Main program
agent = QLearningAgent()

print("Training Tic-Tac-Toe Agent...")
train_agent(agent, 20000)

print("Training Completed!")

print("Total Q-values learned:", len(agent.q))

test_agent(agent, 100)

























# 1. Import required libraries
# import randomimport pickle



# - random: Used to select random moves for the AI during exploration and for the opponent.
# - pickle: Used to save and load Python objects such as trained models or Q-tables. Note: It is imported in this code but not actually used.
# 2. Create the Tic-Tac-Toe game class
# class TicTacToe:



# - Defines a class named TicTacToe.
# - A class is used to group related data and functions together.
# - This class manages the game board and its rules.
# Initialize the game board
# def __init__(self):    self.board = [' '] * 9



# - __init__() is a constructor that runs automatically when an object is created.
# - self.board represents the Tic-Tac-Toe board.
# - [' '] * 9 creates a list containing 9 empty spaces.
# - The board has 3 rows and 3 columns.
# In simple words: It creates an empty Tic-Tac-Toe board before the game starts.
# Display the board
# def display(self):    for i in range(0, 9, 3):        print("|".join(self.board[i:i+3]))        if i < 6:            print("------")



# - display() prints the current game board.
# - range(0, 9, 3) selects positions 0, 3 and 6.
# - self.board[i:i+3] selects three positions at a time.
# - "|".join() joins the three positions using vertical lines.
# - The if condition prints horizontal separators between rows.
# Find available moves
# def available_moves(self):    return [i for i, x in enumerate(self.board) if x == ' ']



# - Returns the positions that are still empty.
# - enumerate() provides the index and value of each board position.
# - The condition x == ' ' checks whether a position is empty.
# - Returns a list of available positions.
# Make a move
# def make_move(self, position, player):    if self.board[position] == ' ':        self.board[position] = player        return True    return False



# - Places the player's symbol at the selected position.
# - position represents the board location.
# - player represents either X or O.
# - If the position is empty, the move is made and True is returned.
# - Otherwise, the move is rejected and False is returned.
# Check the winner
# def check_winner(self):    wins = [        (0,1,2), (3,4,5), (6,7,8),        (0,3,6), (1,4,7), (2,5,8),        (0,4,8), (2,4,6)    ]



# - Defines all 8 possible winning combinations.
# - There are 3 horizontal combinations.
# - There are 3 vertical combinations.
# - There are 2 diagonal combinations.
# for a, b, c in wins:    if self.board[a] == self.board[b] == self.board[c] != ' ':        return self.board[a]return None



# - Checks each winning combination.
# - If all three positions contain the same symbol and are not empty, that player wins.
# - Returns X or O depending on the winner.
# - Returns None if nobody has won.
# 3. Create the Q-Learning Agent class
# class QLearningAgent:



# - Defines a class named QLearningAgent.
# - It represents the AI player that learns how to play Tic-Tac-Toe using Q-Learning.
# Initialize the Q-Learning agent
# def __init__(self):    self.q = {}    self.lr = 0.1    self.discount = 0.9    self.epsilon = 0.2



# - self.q = {} creates an empty dictionary to store Q-values.
# - lr = 0.1 represents the learning rate.
# - discount = 0.9 represents the discount factor.
# - epsilon = 0.2 represents the exploration probability.
# In simple words: These parameters control how the AI learns and chooses its moves.
# Convert the board into a state
# def get_state(self, board):    return tuple(board)



# - Converts the board list into a tuple.
# - The tuple represents the current game state.
# - It is used as a key in the Q-value dictionary.
# Choose an action
# def choose_action(self, board):    state = self.get_state(board)    moves = [i for i, x in enumerate(board) if x == ' ']



# - Converts the current board into a state.
# - Finds all available positions where the AI can place X.
# if random.uniform(0, 1) < self.epsilon:    return random.choice(moves)



# - Generates a random number between 0 and 1.
# - If the number is less than epsilon, the AI selects a random available move.
# - This is called exploration.
# qvals = [self.q.get((state, a), 0) for a in moves]max_q = max(qvals)



# - Retrieves the Q-value of every available move.
# - self.q.get((state, a), 0) returns the stored Q-value.
# - If a Q-value does not exist, it returns 0.
# - max(qvals) finds the highest Q-value.
# best_moves = [    a for a, q in zip(moves, qvals) if q == max_q]return random.choice(best_moves)



# - Finds all moves having the highest Q-value.
# - zip() combines available moves with their Q-values.
# - random.choice() selects one of the best moves randomly.
# - This is called exploitation.
# Update the Q-values
# def update(self, state, action, reward, next_state, done):    old_q = self.q.get((state, action), 0)



# - Updates the Q-value after the AI performs an action.
# - state is the previous board state.
# - action is the move performed.
# - reward is the reward received.
# - next_state is the new board state.
# - done indicates whether the game has finished.
# - old_q stores the previous Q-value.
# if done:    future_q = 0



# - If the game is over, there are no future moves.
# - Therefore, the future Q-value is set to zero.
# else:    future_q = max(        [self.q.get((next_state, a), 0)         for a in range(9)         if next_state[a] == ' '],        default=0    )



# - If the game is not over, it calculates the highest possible Q-value from the next state.
# - Checks all 9 board positions.
# - Considers only empty positions.
# - default=0 returns zero if no available move exists.
# self.q[(state, action)] = old_q + self.lr * (    reward + self.discount * future_q - old_q)



# - Updates the Q-value using the Q-Learning formula.
# - The new value depends on the old Q-value, immediate reward and estimated future reward.
# 4. Create the training function
# def train_agent(agent, episodes):



# - Defines a function to train the AI agent.
# - agent represents the Q-Learning agent.
# - episodes represents the number of training games.
# for ep in range(episodes):    game = TicTacToe()



# - Repeats training for the given number of episodes.
# - Creates a new Tic-Tac-Toe game for every episode.
# AI plays as X
# state = agent.get_state(game.board)action = agent.choose_action(game.board)game.make_move(action, 'X')



# - Stores the current board state.
# - AI selects an action using its Q-values and exploration strategy.
# - The selected move is placed on the board as X.
# Check whether AI wins
# if game.check_winner() == 'X':    agent.update(state, action, 1, None, True)    break



# - Checks whether X has won.
# - If the AI wins, it receives a reward of +1.
# - Updates the Q-value.
# - break ends the current game.
# Check for a draw
# if not game.available_moves():    agent.update(state, action, 0, None, True)    break



# - Checks whether the board has any empty positions.
# - If no positions are available, the game is a draw.
# - The AI receives a reward of 0.
# - The current episode ends.
# Random opponent plays as O
# opponent_move = random.choice(game.available_moves())game.make_move(opponent_move, 'O')



# - The opponent selects a random available position.
# - Places O at that position.
# - The opponent does not use Q-Learning.
# Check whether opponent wins
# if game.check_winner() == 'O':    agent.update(state, action, -1, None, True)    break



# - Checks whether O has won.
# - If the opponent wins, the AI receives a penalty of -1.
# - The Q-value is updated and the game ends.
# Check for draw again
# if not game.available_moves():    agent.update(state, action, 0, None, True)    break



# - Checks whether the board is full after the opponent's move.
# - If no moves remain, the game ends in a draw.
# - The AI receives a reward of zero.
# Update the Q-table after a normal move
# next_state = agent.get_state(game.board)agent.update(state, action, 0, next_state, False)



# - Stores the new board state after both players have moved.
# - Updates the Q-value.
# - The reward is zero because the game has not ended.
# - False indicates that the game is still running.
# Reduce exploration
# agent.epsilon = max(0.05, agent.epsilon * 0.9997)



# - Gradually reduces the exploration probability after each episode.
# - 0.9997 slowly decreases epsilon.
# - max(0.05, ...) ensures epsilon never becomes less than 0.05.
# In simple words: Initially, the AI tries many random moves. As it learns, it relies more on its learned Q-values.
# 5. Create the testing function
# def test_agent(agent, games=100):



# - Defines a function to test the trained AI.
# - games=100 means the agent is tested against the random opponent for 100 games by default.
# old_epsilon = agent.epsilonagent.epsilon = 0



# - Stores the original epsilon value.
# - Sets epsilon to zero so the AI does not explore randomly during testing.
# - The AI chooses moves based on its learned Q-values.
# wins = 0draws = 0losses = 0



# - Initializes counters for wins, draws and losses.
# for _ in range(games):    game = TicTacToe()



# - Runs the testing process for 100 games.
# - Creates a new game for each test.
# AI makes a move
# action = agent.choose_action(game.board)game.make_move(action, 'X')



# - AI selects its move using the learned Q-values.
# - Places X on the board.
# Check AI win or draw
# if game.check_winner() == 'X':    wins += 1    break



# - If AI wins, increases the win counter by one.
# - Ends the current game.
# if not game.available_moves():    draws += 1    break



# - If the board is full and nobody has won, increases the draw counter.
# - Ends the game.
# Opponent makes a move
# opponent_move = random.choice(game.available_moves())game.make_move(opponent_move, 'O')



# - The opponent selects a random available position.
# - Places O on the board.
# Check opponent win or draw
# if game.check_winner() == 'O':    losses += 1    break



# - If the opponent wins, increases the loss counter.
# if not game.available_moves():    draws += 1    break



# - If the board is full, increases the draw counter.
# Restore epsilon and display results
# agent.epsilon = old_epsilon



# - Restores the original exploration probability after testing.
# print("\n===== TEST RESULTS =====")print("Wins:", wins)print("Draws:", draws)print("Losses:", losses)



# - Displays the total wins, draws and losses obtained during testing.
# 6. Main program
# agent = QLearningAgent()



# - Creates the Q-Learning agent.
# print("Training Tic-Tac-Toe Agent...")train_agent(agent, 20000)



# - Displays a training message.
# - Trains the AI for 20,000 episodes.
# - During training, the AI learns from wins, losses and draws.
# print("Training Completed!")



# - Displays a message after training is completed.
# print("Total Q-values learned:", len(agent.q))



# - Displays the number of state-action Q-values stored in the dictionary.
# test_agent(agent, 100)



# - Tests the trained AI against a random opponent for 100 games.
# - Displays the final wins, draws and losses.

