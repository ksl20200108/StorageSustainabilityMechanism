import blockchain_structures
from random_functions import *


def test_blockchain(mode, propose, sample_fees1, sample_fees2):
    # print("Generate random fees.\n")
    bc = blockchain_structures.Blockchain(sample_fees1, sample_fees2, mode, propose)
    print("At the start,")
    print("transaction pool1 has %d transactions, transaction pool2 has %d transactions"
          % (len(bc.transaction_pool1), len(bc.transaction_pool2)))
    if mode == "FTET":
        round = 13
    else:
        round = 24
    for i in range(0, round + 1):
        bc.add_block_by_mining()
        # print("After adding %d block," % i)
        # print("transaction pool1 has %d transactions, transaction pool2 has %d transactions"
        #       % (len(bc.transaction_pool1), len(bc.transaction_pool2)))
    bc.update_total_welfare()
    print("The social welfare is % d." % bc.current_social_welfare)


def multiple_blockchain_tests(num_of_users):
    # FTET mechanism and simultaneous proposing
    # print("FTET mechanism and simultaneous proposing")
    sample_fees1 = FTET_Sim(num_of_users)
    test_blockchain("FTET", "SIM", sample_fees1, [])
    # FTET mechanism and non-simultaneous proposing
    # print("\nFTET mechanism and non-simultaneous proposing")
    sample_fees1, sample_fees2 = FTET_Nonsim(num_of_users)
    test_blockchain("FTET", "NSIM", sample_fees1, sample_fees2)
    # Current blockchain mechanism and simultaneous proposing
    # print("\nCurrent blockchain mechanism and simultaneous proposing")
    sample_fees1 = Current_Sim(num_of_users)
    test_blockchain("CURRENT", "SIM", sample_fees1, [])
    # Current blockchain mechanism and non-simultaneous proposing
    # print("\nCurrent blockchain mechanism and non-simultaneous proposing")
    sample_fees1, sample_fees2 = Current_Nonsim(num_of_users)
    test_blockchain("CURRENT", "NSIM", sample_fees1, sample_fees2)


def one_node_test():
    for i in [1600, 2400, 3200, 4000, 4800]:
        print("Test for %i users\n\n" % i)
        multiple_blockchain_tests(i)
        print("\n\n")
