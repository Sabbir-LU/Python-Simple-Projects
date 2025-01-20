# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:19:11 2024

@author: ahmed
"""

import tensorflow as tf
import numpy as np
import logging
import matplotlib.pyplot as plt


logger = tf.get_logger()
logger.setLevel(logging.ERROR)

celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

for index,element in enumerate(celsius_q):
    print('{} degree celsius = {} degree farenhite'.format(element, fahrenheit_a[index]))
    
l0 = tf.keras.layers.Dense(units=1, input_shape=[1])
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=1)

model = tf.keras.Sequential([l0,l1,l2])
model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q, fahrenheit_a, epochs= 500, verbose=False)
print('Finished model training')

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss Magnitude')
plt.grid(True)
print(model.predict([100]))

print("These are the l1 variables: {}".format(l1.get_weights()))
print("These are the l2 variables: {}".format(l2.get_weights()))