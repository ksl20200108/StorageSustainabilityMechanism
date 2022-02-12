def write_yaml(main_num):

    fee1 = ["", "FTETSIMfee11600", "FTETSIMfee14800", "FTETNSIMfee11600", "FTETNSIMfee14800",
            "CURRENTSIMfee11600", "CURRENTSIMfee14800", "CURRENTNSIMfee11600", "CURRENTNSIMfee14800"]
    fee2 = ["", "FTETSIMfee21600", "FTETSIMfee24800", "FTETNSIMfee21600", "FTETNSIMfee24800",
            "CURRENTSIMfee21600", "CURRENTSIMfee24800", "CURRENTNSIMfee21600", "CURRENTNSIMfee24800"]

    """new"""
    f = open(str(main_num) + "static.yaml", "w")

    f.write("version: '3'\n")
    f.write("\n")
    f.write('services:\n')
    f.write("\n")

    f.write("  experimenter" + ":\n")
    f.write("    image: test1 \n")

    """new"""
    f.write("    deploy: \n")
    f.write("      restart_policy: \n")
    f.write('        condition: none \n')


    f.write("    environment:\n")

    """new"""
    f.write("      - STATIC_IP=192.168.1.0" + "\n")
    f.write("    cap_add:\n")
    f.write("      - NET_ADMIN\n")

    f.write("    ports:\n")
    f.write("      - " + str(5679 + 0 - 1) + ":5678\n")

    """old"""
    # f.write("    privileged: true\n")

    f.write("    volumes:\n")
    f.write("      - ./main" + str(main_num)  + ".py:/run/main.py\n")
    f.write("      - ./network.py:/run/network.py\n")
    f.write("      - ./blockchain_structures.py:/run/blockchain_structures.py\n")
    f.write("      - ./random_functions.py:/run/random_functions.py\n")
    f.write("      - ./tests.py:/run/tests.py\n")
    f.write("      - ./data/" + str(main_num)[1:] + fee1[int(str(main_num)[0])] + ".npy" + ":/run/data/"
        + str(main_num)[1:] + fee1[int(str(main_num)[0])] + ".npy" + "\n")
    f.write("      - ./data/" + str(main_num)[1:] + fee2[int(str(main_num)[0])] + ".npy" + ":/run/data/"
        + str(main_num)[1:] + fee2[int(str(main_num)[0])] + ".npy" + "\n")
    f.write("      - ./peers:/run/peers\n")
    f.write("      - ./experimenter.py:/run/experimenter.py\n")
    f.write("    command: >\n")
    f.write('        bash -c "python3 experimenter.py"\n')

    """new"""
    f.write("    networks:\n")
    f.write("      - test\n")
    f.write("    cap_add:\n")
    f.write("      - NET_ADMIN\n")

    f.write("\n")
    f.write("\n")

    """new"""
    f.write("  peerhandler" + ":\n")
    f.write("    image: test2 \n")

    """new"""
    f.write("    deploy: \n")
    f.write("      restart_policy: \n")
    f.write('        condition: none \n')

    f.write("    environment:\n")

    """new"""
    f.write("      - STATIC_IP=192.168.1.1" + "\n")
    f.write("    cap_add:\n")
    f.write("      - NET_ADMIN\n")

    f.write("    ports:\n")
    f.write("      - " + str(5679 + 1 - 1) + ":5678\n")

    """old"""
    # f.write("    privileged: true\n")

    f.write("    volumes:\n")
    f.write("      - ./main" + str(main_num) + ".py:/run/main.py\n")
    f.write("      - ./network.py:/run/network.py\n")
    f.write("      - ./blockchain_structures.py:/run/blockchain_structures.py\n")
    f.write("      - ./random_functions.py:/run/random_functions.py\n")
    f.write("      - ./tests.py:/run/tests.py\n")
    f.write("      - ./data/" + str(main_num)[1:] + fee1[int(str(main_num)[0])] + ".npy" + ":/run/data/"
            + str(main_num)[1:] + fee1[int(str(main_num)[0])] + ".npy" + "\n")
    f.write("      - ./data/" + str(main_num)[1:] + fee2[int(str(main_num)[0])] + ".npy" + ":/run/data/"
            + str(main_num)[1:] + fee2[int(str(main_num)[0])] + ".npy" + "\n")
    f.write("      - ./peers:/run/peers\n")
    f.write("      - ./experimenter.py:/run/experimenter.py\n")
    f.write("      - ./peer_handler.py:/run/peer_handler.py\n")
    f.write("    command: >\n")
    f.write('        bash -c "python3 peer_handler.py"\n')

    """old"""
    f.write("    networks:\n")
    f.write("      - test\n")
    f.write("    cap_add:\n")
    f.write("      - NET_ADMIN\n")

    f.write("\n")
    f.write("\n")

    """new"""
    f.write("networks: \n")
    f.write("  test:\n")
    f.write("    external: true\n")
    # f.write("    name: test\n")

    f.close()


for i in range(1, 9):
    for j in range(1, 11):
        write_yaml(int(str(i) + str(j)))
