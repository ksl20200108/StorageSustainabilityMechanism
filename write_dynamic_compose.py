def write_yaml(main_num):

    fee1 = ["", "FTETSIMfee11600", "FTETSIMfee14800", "FTETNSIMfee11600", "FTETNSIMfee14800",
            "CURRENTSIMfee11600", "CURRENTSIMfee14800", "CURRENTNSIMfee11600", "CURRENTNSIMfee14800"]
    fee2 = ["", "FTETSIMfee21600", "FTETSIMfee24800", "FTETNSIMfee21600", "FTETNSIMfee24800",
            "CURRENTSIMfee21600", "CURRENTSIMfee24800", "CURRENTNSIMfee21600", "CURRENTNSIMfee24800"]

    """new"""
    f = open(str(main_num) + "dynamic.yaml", "w")

    f.write("version: '3'\n")
    f.write("\n")
    f.write('services:\n')
    f.write("\n")

    for i in range(2, 10001):    # 10000 users
        f.write("  node" + str(i) + ":\n")
        f.write("    image: test \n")

        """new"""
        f.write("    deploy: \n")
        f.write("      restart_policy: \n")
        f.write('        condition: none \n')

        """old"""
        # f.write("    depends_on:\n")
        # f.write("      - experimenter\n")
        # f.write("      - peerhandler\n")

        # f.write("    container_name: node" + str(i) + "\n")
        f.write("    ports:\n")
        f.write("      - " + str(5679 + i - 1) + ":5678\n")

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
        f.write("    command: >\n")
        f.write('        bash -c "python3 main.py"\n')
        f.write("    networks:\n")
        f.write("      - test\n")
        # f.write("        ipv4_address: 192.168.1." + str(i) + "\n")
        f.write("\n")
        f.write("\n")

    """new"""
    f.write("networks: \n")
    f.write("  test:\n")
    f.write("    external: true\n")
    # f.write("  name: test\n")

    f.write("\n # docker-compose -f emm.yaml up -d\n")

    f.close()


for i in range(1, 9):
    for j in range(1, 11):
        write_yaml(int(str(i) + str(j)))
