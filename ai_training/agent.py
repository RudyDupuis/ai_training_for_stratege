import tensorflow as tf
import numpy as np
import random

LEARNING_RATE = 0.001

class Agent:
    def __init__(self, name, player_role, model=None):
        self.name = name
        self.player_role = player_role
        self.model = model if model else self.build_model()
        self.epsilon = 0.2  # Probabilité d'explorer (action aléatoire)
        self.gamma = 0.9  # Discount factor (valeur future)

    def build_model(self):
        # Modèle avec état (176) et action (14) combinés
        model = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(128, activation="relu", input_shape=(270,)),
                tf.keras.layers.Dense(64, activation="relu"),
                tf.keras.layers.Dense(1, activation="linear"),  # Prédit une Q-value unique
            ]
        )
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
            loss="mse",
        )
        return model

    def predict(self, state, actions):
        # Combiner l'état avec chaque action possible
        inputs = np.array([np.concatenate((state, action)) for action in actions])
        q_values = self.model.predict(inputs)
        return q_values.flatten()  # Retourne les Q-values comme un tableau

    def train(self, state, action, reward, next_state, possible_actions):
        # Calculer la cible (Q-value cible) pour l'entraînement
        next_q_values = self.predict(next_state, possible_actions)
        max_next_q_value = np.max(next_q_values)
        target = reward + self.gamma * max_next_q_value

        # Combiner l'état et l'action courante pour l'entraînement
        input_data = np.array([np.concatenate((state, action))])
        target_data = np.array([target])

        # Entraîner le modèle sur une seule entrée
        loss = self.model.train_on_batch(input_data, target_data)
        return loss

    def choose_action(self, state, possible_actions):
        # Exploration vs exploitation
        if random.random() < self.epsilon:
            return random.choice(possible_actions)  # Exploration (action aléatoire)
        else:
            # Exploitation : Prédire les Q-values et choisir la meilleure action
            q_values = self.predict(state, possible_actions)
            best_action_index = np.argmax(q_values)
            return possible_actions[best_action_index]
