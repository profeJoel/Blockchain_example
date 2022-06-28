'''
NeuralCoin (NC)

t1: Anna sends Bob 2 NC
t2: Bob sends Daniel 4.3 NC
t3: Marck sends Charlie 3.2 NC

B1 ("AAA", t1, t2, t3) -> 76fd89 (ejemplo), B2 ("76bf89", t4, t5, t6) -> 8923ff, B3 (8923ff, t7, t8, t9)

NeuralHash()


'''

import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.trasaction_list = transaction_list
        
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        

t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.3 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 0.3 NC to Anna"
t5 = "Mike sends 1 NC to Charlie"
t6 = "Mike sends 5.4 NC to Daniel"

initial_block = NeuralCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)