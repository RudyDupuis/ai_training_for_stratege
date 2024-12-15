from game_logic.displays.test_game_logic import test_game_logic
from ai_training.training import train_agents
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('CPU')
tf.config.set_logical_device_configuration(
    physical_devices[0], [tf.config.LogicalDeviceConfiguration(memory_limit=1024)])

# test_game_logic(800)

train_agents(50000000)
