import os
import pickle
from random_functions import *


"""new"""
def create_data(given_seed=0):
    path = './data'
    for i in range(1, 11):
        for user_num in [1600, 4800]:
            fee1, fee2 = FTET_Sim(user_num), np.array([])
            np.save(os.path.join(path, str(i) + "FTETSIM" + "fee1" + str(user_num) + ".npy"), fee1)
            np.save(os.path.join(path, str(i) + "FTETSIM" + "fee2" + str(user_num) + ".npy"), fee2)

            fee1, fee2 = FTET_Nonsim(user_num)
            np.save(os.path.join(path, str(i) + "FTETNSIM" + "fee1" + str(user_num) + ".npy"), fee1)
            np.save(os.path.join(path, str(i) + "FTETNSIM" + "fee2" + str(user_num) + ".npy"), fee2)

            fee1, fee2 = Current_Sim(user_num), np.array([])
            np.save(os.path.join(path, str(i) + "CURRENTSIM" + "fee1" + str(user_num) + ".npy"), fee1)
            np.save(os.path.join(path, str(i) + "CURRENTSIM" + "fee2" + str(user_num) + ".npy"), fee2)

            fee1, fee2 = Current_Nonsim(user_num)
            np.save(os.path.join(path, str(i) + "CURRENTNSIM" + "fee1" + str(user_num) + ".npy"), fee1)
            np.save(os.path.join(path, str(i) + "CURRENTNSIM" + "fee2" + str(user_num) + ".npy"), fee2)


"""to be modified"""
given_seed = 0

create_data(given_seed)
path = './data'
number = 1
user_num = 1600
type = "FTETSIM"
fee1 = np.load(os.path.join(path, str(number) + type + "fee1" + str(user_num) + ".npy"))
fee2 = np.load(os.path.join(path, str(number) + type + "fee2" + str(user_num) + ".npy"))
print(fee1.tolist())
print(fee2.tolist())
