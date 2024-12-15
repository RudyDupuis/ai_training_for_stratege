import os
import random
import tensorflow as tf
import numpy as np

LEARNING_RATE = 0.001
EPSILON = 0.2
GAMMA = 0.95


class Agent:
    def __init__(self, name, player_role, model_path=None):
        self.name = name
        self.player_role = player_role

        if model_path and os.path.exists(model_path):
            self.model = tf.keras.models.load_model(model_path)
            self.model.compile(
                optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
                loss=tf.keras.losses.MeanSquaredError(),
            )
            print(f"Modèle chargé depuis {model_path}")
        else:
            self.model = self.build_model()

    def build_model(self):
        model = tf.keras.models.Sequential(
            [
                tf.keras.layers.Dense(256, activation="relu", input_shape=(270,)),
                tf.keras.layers.Dense(128, activation="relu"),
                tf.keras.layers.Dense(64, activation="relu"),
                tf.keras.layers.Dense(1, activation="linear"),
            ]
        )
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
            loss=tf.keras.losses.MeanSquaredError(),
        )
        return model

    def predict(self, state, actions):
        inputs = np.array([np.concatenate((state, action)) for action in actions])
        q_values = self.model.predict(inputs)
        return q_values.flatten()

    def train(self, state, action, reward, next_state, possible_actions):
        next_q_values = self.predict(next_state, possible_actions)
        max_next_q_value = np.max(next_q_values)
        target = reward + GAMMA * max_next_q_value

        input_data = np.array([np.concatenate((state, action))])
        target_data = np.array([target])

        loss = self.model.train_on_batch(input_data, target_data)
        return loss

    def choose_action(self, state, possible_actions):
        if random.random() < EPSILON:
            return random.choice(possible_actions)

        q_values = self.predict(state, possible_actions)
        best_action_index = np.argmax(q_values)
        return possible_actions[best_action_index]
