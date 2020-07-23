import gym
from gym import spaces
from scipy.ndimage.interpolation import shift
import numpy as np


class CardGameEnv(gym.Env):
    """Recurrent Environment that follows the gym interface and allow for a sequence representation of card games"""
    metadata = {'render.modes': ['human']}

    def __init__(self, card_game, n_agents=3, n_steps=5, n_context=252):
        super(CardGameEnv, self).__init__()

        # Initialize game
        self.card_game, n_tokens = card_game.initialize(n_agents)

        # Sets up action space and observation space
        self.action_space = spaces.Discrete(n_tokens)
        self.observation_space = spaces.Box(
            low=0, high=n_tokens, shape=(n_context, 1), dtype=np.uint8)

        # Sets up vars
        self.obs_hist = np.zeros((n_context, 1))
        self.n_context = n_context
        self.n_tokens = n_tokens
        self.n_agents = n_agents
        self.n_hands_max = n_steps
        self.n_hands_played = 0

    def _step_agent(self, action, agent):
        new_tokens, reward, done = self.card_game.play(action, agent)
        self.obs_hist = shift(self.obs_hist, len(new_tokens), cval=np.NaN)

        return np.copy(self.obs_hist), reward, done

    def step(self, action_n):
        obs_n = list()
        reward_n = list()
        done_n = list()

        for i in range(self.n_agents):
            obs, reward, done = self._step_agent(action_n[i])
            obs_n.append(obs)
            reward_n.append(reward)
            done_n.append(done)

        return obs_n, reward_n, done_n, {}

    def reset(self):
        self.card_game.reset()
        self.n_hands_played += 1
        self.obs_hist = np.zeros((self.n_context, 1))
        return self.obs_hist

    def render(self, mode='human', close=False):
        print(f'Observations: {self.obs_hist}')