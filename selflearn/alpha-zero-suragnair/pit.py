import Arena
from MCTS import MCTS

from connect4.Connect4Game import Connect4Game
from connect4.Connect4Players import *
from connect4.tensorflow.NNet import NNetWrapper as NNet

import numpy as np
from utils import *

human_vs_cpu = True #True
g = Connect4Game(6)
hp = HumanConnect4Player(g).play
n1 = NNet(g)
n1.load_checkpoint('F:/selflearn/alpha-zero-suragnair/temp/','best.pth.tar') #windows
# n1.load_checkpoint('./drive/MyDrive/selflearn/temp/','best.pth.tar') #colab

args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

if human_vs_cpu:
    player2 = hp
else:
    n2 = NNet(g)
    # n2.load_checkpoint('F:/selflearn/alpha-zero-suragnair/temp/','best.pth.tar') #windows
    n2.load_checkpoint('./drive/MyDrive/selflearn/temp/','best.pth.tar (1)') #colab
    args2 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
    mcts2 = MCTS(g, n2, args2)
    n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))
    player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

arena = Arena.Arena(n1p, player2, g, display=Connect4Game.display)
print(arena.playGames(2, verbose=True))
