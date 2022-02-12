def write_py(main_num):
    f = open("main" + str(main_num) + ".py", "w")
    f.write("import os\n")
    f.write("import pickle\n")
    f.write("from network import *\n")
    f.write("from random_functions import *\n")
    f.write("\n")
    f.write("\n")

    f.write("def each_test(number, mode, propose, user_num):\n")
    f.write("    type = mode + propose\n")
    f.write('    if (type != "FTETSIM") and (type != "FTETNSIM") and (type != "CURRENTSIM") and (type != "CURRENTNSIM"):\n')
    f.write('        raise ValueError("Invalid mode or propose")\n')
    f.write("\n")
    f.write("    path = './data'\n")
    f.write('    fee1 = np.load(os.path.join(path, str(number) + type + "fee1" + str(user_num) + ".npy"))\n')
    f.write('    fee2 = np.load(os.path.join(path, str(number) + type + "fee2" + str(user_num) + ".npy"))\n')
    f.write("    fee1 = fee1.tolist()\n")
    f.write("    fee2 = fee2.tolist()\n")
    f.write("\n")

    """old"""
    # f.write("    path = './peers'\n")
    # f.write('    fp = open(os.path.join(path, "peers.txt"), "rb")\n')
    # f.write("    peers = pickle.load(fp)\n")

    f.write("    net = Network(fee1, fee2, mode, propose, user_num)\n")

    """new"""
    f.write("\n")
    f.write("    net.get_ip_and_peers()")
    f.write("\n")

    f.write('    log.info("main function start server")\n')
    f.write('    t1 = threading.Thread(target=net.start_server_loop, args=(10000,))  # only one argument -> not iterable -> add ","\n')
    f.write('    log.info("main function start client")\n')

    """new"""
    f.write("    t2 = threading.Thread(target=net.start_client_loop, args=())\n")

    f.write("    t1.start()\n")
    f.write("    t2.start()\n")
    f.write("    t1.join()\n")
    f.write("    t2.join()\n")
    f.write("\n")
    f.write('    log.info("finally stopped")\n')
    f.write("\n")
    f.write("\n")
    f.write("def main():\n")
    f.write("\n")
    if int(main_num / 10) == 1:
        f.write('    each_test(' + str(main_num % 10) + ', "FTET", "SIM", 1600)\n')
    elif int(main_num / 100) == 1:
        f.write('    each_test(' + str(main_num % 100) + ', "FTET", "SIM", 1600)\n')
    elif int(main_num / 10) == 2:
        f.write('    each_test(' + str(main_num % 10) + ', "FTET", "SIM", 4800)\n')
    elif int(main_num / 100) == 2:
        f.write('    each_test(' + str(main_num % 100) + ', "FTET", "SIM", 4800)\n')
    elif int(main_num / 10) == 3:
        f.write('    each_test(' + str(main_num % 10) + ', "FTET", "NSIM", 1600)\n')
    elif int(main_num / 100) == 3:
        f.write('    each_test(' + str(main_num % 100) + ', "FTET", "NSIM", 1600)\n')
    elif int(main_num / 10) == 4:
        f.write('    each_test(' + str(main_num % 10) + ', "FTET", "NSIM", 4800)\n')
    elif int(main_num / 100) == 4:
        f.write('    each_test(' + str(main_num % 100) + ', "FTET", "NSIM", 4800)\n')
    elif int(main_num / 10) == 5:
        f.write('    each_test(' + str(main_num % 10) + ', "CURRENT", "SIM", 1600)\n')
    elif int(main_num / 100) == 5:
        f.write('    each_test(' + str(main_num % 100) + ', "CURRENT", "SIM", 1600)\n')
    elif int(main_num / 10) == 6:
        f.write('    each_test(' + str(main_num % 10) + ', "CURRENT", "SIM", 4800)\n')
    elif int(main_num / 100) == 6:
        f.write('    each_test(' + str(main_num % 100) + ', "CURRENT", "SIM", 4800)\n')
    elif int(main_num / 10) == 7:
        f.write('    each_test(' + str(main_num % 10) + ', "CURRENT", "NSIM", 1600)\n')
    elif int(main_num / 100) == 7:
        f.write('    each_test(' + str(main_num % 100) + ', "CURRENT", "NSIM", 1600)\n')
    elif int(main_num / 10) == 8:
        f.write('    each_test(' + str(main_num % 10) + ', "CURRENT", "NSIM", 4800)\n')
    elif int(main_num / 100) == 8:
        f.write('    each_test(' + str(main_num % 100) + ', "CURRENT", "NSIM", 4800)\n')
    else:
        raise ValueError("Wrong type")

    f.write("\n")
    f.write("\n")
    f.write("main()\n")
    f.write("\n")

    f.close()


for i in range(1, 9):
    for j in range(1, 11):
        write_py(int(str(i) + str(j)))
