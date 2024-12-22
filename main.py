from ai_training.training import train_agents

train_agents(
    num_episodes=1000000,
    start_episode=1800,
    agent1_model_path="h5/1800_agent1.h5",
    agent2_model_path="h5/1800_agent2.h5",
)
