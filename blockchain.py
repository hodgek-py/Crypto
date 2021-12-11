import hashlib
import time




class Block:

    def __init__(self,index,proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()



    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no, self.prev_hash,
        self.data, self.timestamp)

        return hashlib.sha256(block_of_string.encode()).hexdigest()
    #calculates the cryptographic hash of every block

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no, self.prev_hash,
        self.data, self.timestamp)


class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()
     # constructor method

    def construct_genesis(self):
        # constructs the initial block
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash):
        # constructs a new block and adds it to the chain
        block = Block(index=len(self.chain), proof_no=proof_no, prev_hash=prev_hash,
        data=self.current_data)
        self.current_data = []

        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block,prev_block):
        # checks whether the blockchain is valid
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash != block.prev_hash:
            return False

        elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

    def new_data(self, sender, recipient, quantity):
        # adds a new transaction to the data of the transactions
        pass

    @staticmethod
    def construct_proof_of_work(prev_proof):
        # protects the blockchain from attack
        pass

    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]
