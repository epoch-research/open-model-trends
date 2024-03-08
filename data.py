import pandas as pd


def load_frontier_systems():
    """
    Load the frontier systems from the file

    Returns a list of the frontier systems
    """
    with open('data/frontier_systems.txt', 'r') as f:
        frontier_systems = [line.strip() for line in f]

    return frontier_systems


def load_pcd_df():
    return pd.read_csv('data/All ML Systems - full view.csv')


def load_hardware_df():
    return pd.read_csv('data/Chip dataset-Grid view.csv')


def load_price_df():
    return pd.read_csv('data/Hardware prices.csv')
