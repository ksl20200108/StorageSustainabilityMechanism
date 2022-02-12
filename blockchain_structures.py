"""
tbc: to be continued
tbt: to be tested
    Block.serialize
    Block.deserialize
    Blockchain.serialize
    Blockchain.deserialize
tbd: to be deleted
tbm: to be modified
"""


import time
import hashlib
import threading
import logging    # for logging info in tests


MAX_DIFF = 256
DIFF_INCREASE = 1


"""
Use logging to help debugging
"""
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)


class Block:

    def __init__(self, index, pre_block_hash, txs):    # tbc
        """
        Block Header
        self.index: the index of the block in Blockchain
        self.pre_block_hash: the hash of the previous block
        """
        # version: irrelevant to the experiment, omitted here
        self.index = index
        self.time_stamp = time.time()
        self.pre_block_hash = pre_block_hash
        """
        Given that there is no dishonest nodes in the experiment setting network,
        and calculating merkle root of hundreds of transactions takes much time,
        we omitted merkle root calculation.
        You can add calculation back by changing the following code into:
            self.merkle_root = cal_merkle_root(txs)
        """
        self.merkle_root = '0'
        self.difficulty_target = 1 << (MAX_DIFF - DIFF_INCREASE)
        self.nounce = 0
        """
        Others
        self.transactions: the transactions in this block
        """
        # self.block_size: irrelevant to the experiment, omitted here
        # self.transaction_counter: irrelevant to the experiment, omitted here
        """
        Transactions in blocks are simplified as float numbers in lists since wallet 
        and account balance are irrelevant to the experiment. 
        """
        self.transactions = txs

    def make_string(self):
        """
        Prepare the block's string for Proof of Work
        :return: the string of the block
        """
        return str(self.index) + str(self.time_stamp) + str(self.pre_block_hash) + \
               str(self.merkle_root) + str(self.difficulty_target) + str(self.nounce)

    def get_block_hash(self):
        """
        :return: the hash of current block
        """
        m = hashlib.sha3_256()
        m.update(self.make_string().encode())
        return m.hexdigest()

    def verify_hash(self):
        """
        Verify whether Proof of Work is satisfied
        :return: satisfied (True) or not (False)
        """
        hash_val = int(self.get_block_hash(), 16)
        return hash_val < self.difficulty_target

    def serialize(self):
        return {
            "index": self.index,
            "time_stamp": self.time_stamp,
            "pre_block_hash": self.pre_block_hash,
            "merkle_root": self.merkle_root,
            "difficulty_target": self.difficulty_target,
            "nounce": self.nounce,
            "transactions": self.transactions
        }

    def show(self):
        return {
            "index": self.index,
            "time_stamp": self.time_stamp,
            "pre_block_hash": self.pre_block_hash,
            "merkle_root": self.merkle_root,
            "difficulty_target": self.difficulty_target,
            "nounce": self.nounce,
            "transaction_num": len(self.transactions)
        }

    @classmethod
    def deserialize(cls, data):
        b = cls(data["index"], data["pre_block_hash"], data["transactions"])
        b.time_stamp = data["time_stamp"]
        b.merkle_root = data["merkle_root"]
        b.difficulty_target = data["difficulty_target"]
        b.nounce = data["nounce"]
        # log.info("deserialized block index: " + str(b.index))
        return b


class Blockchain:

    def __init__(self, fees1, fees2, mode, propose):
        # print("The current Mode and Propose are % s and %s" % (mode, propose))
        """
        :param fees1: storing fees for simultaneous proposing and early half fees for Non-simultaneous proposing
        :param fees2: storing fees for late half half fees for Non-simultaneous proposing
        """
        """
        The reward in the genesis block is omitted since it is irrelevant to the experiment
        """
        if propose == "SIM":
            fees2 = []
        """Create Genesis Block"""
        self.blocks = [Block(0, hashes256("Genesis".encode()), [])]
        self.blocks[0].time_stamp = 0
        """Other stuffs"""
        self.current_social_welfare = 0
        self.transaction_number = len(fees1) + len(fees2)
        self.transaction_pool1 = fee_sort(fees1)
        self.transaction_pool2 = fees2
        """the MODE can be FTET or CURRENT"""
        self.MODE = mode
        """the PROPOSE can be SIM or NSIM"""
        self.PROPOSE = propose

    def add_block_by_mining(self, lock):
        index = self.blocks[-1].index + 1
        previous_hash = self.blocks[-1].get_block_hash()
        if self.PROPOSE == "NSIM" and index == 6:
            self.transaction_pool1 = fee_sort(self.transaction_pool1 + self.transaction_pool2)
            self.transaction_pool2 = []    # de-reference to start garbage collection, to safe memory
        """
        check the experiment requirement
        """
        if self.MODE == "FTET":
            """
            Since there is a Genesis Block
            """
            if len(self.transaction_pool1) >= 200 and len(self.blocks) < 14:
                txs = self.transaction_pool1[:200]
                self.transaction_pool1 = self.transaction_pool1[200:]
            elif len(self.blocks) < 14:
                txs = self.transaction_pool1
                self.transaction_pool1 = []
            else:
                txs = []
        elif self.MODE == "CURRENT":
            if len(self.transaction_pool1) >= 200 and len(self.blocks):
                txs = self.transaction_pool1[:200]
                self.transaction_pool1 = self.transaction_pool1[200:]
            elif len(self.blocks):
                txs = self.transaction_pool1
                self.transaction_pool1 = []
            else:
                txs = []
        """
        construct the block
        """
        b = Block(index, previous_hash, txs)
        """
        start mining
        """
        while not b.verify_hash():
            b.nounce += 1
        # print('mining succeeded')    # tbd
        """
        success
        """
        lock.acquire()
        self.blocks.append(b)
        lock.release()
        # self.update_total_welfare()
        # return b

    def update_total_welfare(self):
        transactions_included = 0
        self.current_social_welfare = 0
        for b in range(1, len(self.blocks)):
            self.current_social_welfare += \
                (70 - 8 * b) \
                * sum(1 for i in self.blocks[b].transactions if i > 0)    # len(self.blocks[b].transactions)
            self.current_social_welfare += \
                (70 - 8 * (b - 5)) \
                * sum(1 for i in self.blocks[b].transactions if i < 0)  # len(self.blocks[b].transactions)
            transactions_included += len(self.blocks[b].transactions)
        self.current_social_welfare -= 40 * (self.transaction_number - transactions_included)
        # print("The current total social welfare is %d." % self.current_social_welfare)

    def serialize(self):
        return {
            "blocks": [i.serialize() for i in self.blocks],
            "transaction_number": self.transaction_number,
            "transaction_pool1": self.transaction_pool1,
            "transaction_pool2": self.transaction_pool2,
            "MODE": self.MODE,
            "PROPOSE": self.PROPOSE
        }

    @classmethod
    def deserialize(cls, data):
        bc = cls([0], [0], data["MODE"], data["PROPOSE"])
        bc.blocks = [Block.deserialize(i) for i in data["blocks"]]
        bc.transaction_number = data["transaction_number"]
        bc.transaction_pool1 = data["transaction_pool1"]
        bc.transaction_pool2 = data["transaction_pool2"]
        return bc


def fee_sort(fees):
    """
    Need to sort by absolute value here
    since we use minus number to denote
    transaction fees generated in late
    half in non-simultaneous proposing
    """
    fees = sorted(fees, key=abs)
    fees.reverse()
    return fees


def hashes256(stuff):
    m = hashlib.sha256()
    m.update(str(stuff).encode())
    return m.hexdigest()


def cal_merkle_root(txs):
    current_txs = []
    for i in range(0, len(txs)):
        txs[i] = hashes256(str(txs[i]).encode())
    while len(txs) != 1:
        current_txs = []
        while len(txs) > 0:
            if len(txs) > 1:
                current_txs.append(hashes256(txs[0] + txs[1]))
                txs = txs[2:]
            else:
                current_txs.append(hashes256(txs[0] + txs[0]))
                txs = []
        txs = current_txs
    return txs[0]
