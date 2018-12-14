'''

    Testowy skrypt sprawdzający czy wszystkie wymagane biblioteki poprawnie działają.

'''

# Importowanie potrzebnych bibliotek
import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory


# Definicja zmiennych
ENV_NAME = 'CartPole-v0'
# Get the environment and extract the number of actions available in the Cartpole problem
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n


# Tworzenie modelu z jedną wartwą ukrytą 
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())

# Tworzenie i konfiguracja agenta.
# Polityka Epsilon Greedy
# Pamięć sekwencyjna do przechowywania wyników działań i nagrody

policy = EpsGreedyQPolicy()
memory = SequentialMemory(limit=50000, window_length=1)
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=5,
target_model_update=1e-2, policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

# Odpalamy agenta i zaczynamu jego nauke
dqn.fit(env, nb_steps=50000, visualize=True, verbose=2)

# Na koniec odpalamy naszego agenta i go testujemy
dqn.test(env, nb_episodes=5, visualize=True)
