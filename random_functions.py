"""
Experiment on users of number 1600 and 4800
"""


import numpy as np


def FTET_Sim(num_of_users, given_seed=0):
    # FTET mechanism and simultaneous proposing
    """
    :return: Blockchain.transaction_pool1
    """

    """new"""
    np.random.seed(given_seed)

    if num_of_users == 1600:
        return np.random.uniform(low=50, high=106 + 1, size=(num_of_users,))
    elif num_of_users == 2400:
        distribution = np.random.rand(num_of_users)
        return np.random.uniform(low=50, high=115.02 + 1, size=(np.count_nonzero(distribution <= 0.673),))
    elif num_of_users == 3200:
        distribution = np.random.rand(num_of_users)
        return np.random.uniform(low=50, high=114.90 + 1, size=(np.count_nonzero(distribution <= 0.506),))
    elif num_of_users == 4000:
        distribution = np.random.rand(num_of_users)
        return np.random.uniform(low=50, high=114.84 + 1, size=(np.count_nonzero(distribution <= 0.405),))
    elif num_of_users == 4800:
        distribution = np.random.rand(num_of_users)
        return np.random.uniform(low=50, high=114.80 + 1, size=(np.count_nonzero(distribution <= 0.338),))


def FTET_Nonsim(num_of_users, given_seed=0):
    # FTET mechanism and non-simultaneous proposing
    """
    :return: Blockchain.transaction_pool1, Blockchain.transaction_pool2
    """

    """new"""
    np.random.seed(given_seed)

    if num_of_users == 1600:
        return \
            np.random.uniform(low=50, high=74, size=(int(num_of_users / 2),)), \
            -1 * np.random.uniform(low=50, high=74, size=(int(num_of_users / 2),))
    else:
        distribution = np.random.rand(int(num_of_users / 2))
        if num_of_users == 2400:
            return \
                np.random.uniform(low=50, high=136.20, size=(np.count_nonzero(distribution <= 0.835),)), \
                -1 * np.random.uniform(low=50, high=90, size=(int(num_of_users / 2),))

        elif num_of_users == 3200:
            return \
                np.random.uniform(low=50, high=136.37, size=(np.count_nonzero(distribution <= 0.623),)), \
                -1 * np.random.uniform(low=50, high=106, size=(int(num_of_users / 2),))
        elif num_of_users == 4000:
            return \
                np.random.uniform(low=50, high=136.32, size=(np.count_nonzero(distribution <= 0.498),)), \
                -1 * np.random.uniform(low=50, high=115.14, size=(np.count_nonzero(distribution <= 0.806),))
        elif num_of_users == 4800:
            return \
                np.random.uniform(low=50, high=136.28, size=(np.count_nonzero(distribution <= 0.415),)), \
                -1 * np.random.uniform(low=50, high=115.01, size=(np.count_nonzero(distribution <= 0.673),))


def Current_Sim(num_of_users, given_seed=0):
    # Current blockchain mechanism and simultaneous proposing
    """
    :return: Blockchain.transaction_pool1
    """

    """new"""
    np.random.seed(given_seed)

    if num_of_users == 1600:
        return np.random.uniform(low=1, high=55, size=(num_of_users,))
    elif num_of_users == 2400:
        return np.random.uniform(low=1, high=87, size=(num_of_users,))
    else:
        distribution = np.random.rand(num_of_users)
        if num_of_users == 3200:
            return np.random.uniform(low=1, high=113.30, size=(np.count_nonzero(distribution <= 0.896),))
        elif num_of_users == 4000:
            return np.random.uniform(low=1, high=111.97, size=(np.count_nonzero(distribution <= 0.725),))
        elif num_of_users == 4800:
            return np.random.uniform(low=1, high=111.93, size=(np.count_nonzero(distribution <= 0.604),))


def Current_Nonsim(num_of_users, given_seed=0):
    # Current blockchain mechanism and non-simultaneous proposing
    """
    :return: Blockchain.transaction_pool1, Blockchain.transaction_pool2
    """

    """new"""
    np.random.seed(given_seed)

    if num_of_users == 1600:
        return \
            np.random.uniform(low=1, high=23, size=(int(num_of_users / 2),)), \
            -1 * np.random.uniform(low=1, high=23, size=(int(num_of_users / 2),))
    elif num_of_users == 2400:
        return \
            np.random.uniform(low=1, high=112.31, size=(int(num_of_users / 2),)), \
            -1 * np.random.uniform(low=1, high=39, size=(int(num_of_users / 2),))
    else:
        distribution = np.random.rand(int(num_of_users / 2))
        if num_of_users == 3200:
            return \
                np.random.uniform(low=1, high=143.32, size=(np.count_nonzero(distribution <= 0.789),)), \
                -1 * np.random.uniform(low=1, high=55, size=(int(num_of_users / 2),))
        elif num_of_users == 4000:
            return \
                np.random.uniform(low=1, high=174.33, size=(np.count_nonzero(distribution <= 0.515),)), \
                -1 * np.random.uniform(low=1, high=71, size=(int(num_of_users / 2),))
        elif num_of_users == 4800:
            return \
                np.random.uniform(low=1, high=175.80, size=(np.count_nonzero(distribution <= 0.424),)), \
                -1 * np.random.uniform(low=1, high=87, size=(int(num_of_users / 2),))

# array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
