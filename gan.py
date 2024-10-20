import torch
from torch import nn

import math
import matplotlib.pyplot as plt

class Discriminator(nn.Module):
    def __init__(self, size):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(size, 256),
            nn.ReLU(),
            #nn.Dropout(0.3), # avoid overfitting, can be removed if no overfitting is being made
            nn.Linear(256, 128),
            nn.ReLU(),
            #nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            #nn.Dropout(0.3),
            nn.Linear(64, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        output = self.model(x)
        return output
    
class Generator(nn.Module):
    def __init__(self, size):
        super(Generator, self).__init__()
        self.size = size
        self.model = nn.Sequential(
            nn.Linear(self.size, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, self.size),
        )

    def forward(self, x):
        output = self.model(x)
        return output