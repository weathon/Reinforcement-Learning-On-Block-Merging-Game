# award = score*20 - steps*0.1 + merge*2, f died, -100
# https://deeplizard.com/learn/video/xVkPh9E9GfE
import numpy as np
import random
import game
import copy

import tensorflow as tf

import os
import tensorflow_datasets as tfds
import numpy as np
import PIL

import matplotlib.pyplot as plt
import matplotlib.patches as patches


model = tf.keras.models.Sequential([
  tf.keras.layers.Input(37),
  tf.keras.layers.Dense(60),
  tf.keras.layers.Dense(120),
  tf.keras.layers.Dense(120),
  tf.keras.layers.Dense(60),
  tf.keras.layers.Dense(30),
  tf.keras.layers.Dense(6),
])
model.summary()


class memoryCell:
    def __init__(self, field, action, num, reward):
        field = field
        # nextState = ns
        action = action
        num = num
        reward = reward

memory = []
epsilon = 1

target = copy.deepcopy(model)
for episode in range(100):
    game.init()
    for step in range(10000000):
        next_number = random.choice(choices)
        if random.random()<=epsilon:
            # random action
            action = random.choice([0,1,2,3,4,5])
        else:
            action = model.predict(game.field, next_number)
        
        old_score = np.max(field)
        old_field = copy.copy(field)
        gameOver = game.push_block(action, next_number)
        if gameOver:
            reward = -100
        else:
            check_merging()
            new_score = np.max(field)
            if not new_score in choices:
                choices.append(int(new_score/2))
            reward = new_score/old_score * 20

        # if len(memory)<10:
        #     memory.append(memoryCell(field, action, num, reward))
        # else:
        #     memory[random.randint(10)] = memoryCell(field, action, num, reward)
        
        result = target.predict(memoryCell(old_field, action, num, reward))
        nextState = field
        loss = result
        model.train(loss)
        # no need for isolation?

        if steps%50 == 0:
            target = copy.deepcopy(model)

        if gameOver:
            break