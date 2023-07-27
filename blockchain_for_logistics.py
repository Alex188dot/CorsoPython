import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = json.dumps(self.data, sort_keys=True).encode()
        return hashlib.sha256(str(self.index).encode() + str(self.timestamp).encode() + data_string + str(self.previous_hash).encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Esempio di utilizzo

# Creazione della blockchain
blockchain = Blockchain()

# Dati dell'alimento da tracciare
food_data = {
    "name": "Parmigiano Reggiano",
    "origin": "Italy",
    "producer": "Parmesan Co.",
    "production_date": "2023-07-05"
}

# Creazione e aggiunta del primo blocco
first_block = Block(1, time.time(), food_data, "")
blockchain.add_block(first_block)

# Aggiunta di altri blocchi successivi
second_block_data = {
    "location": "Warehouse A",
    "date": "2023-07-10"
}
second_block = Block(2, time.time(), second_block_data, "")
blockchain.add_block(second_block)

third_block_data = {
    "location": "Distribution Center",
    "date": "2023-07-15"
}
third_block = Block(3, time.time(), third_block_data, "")
blockchain.add_block(third_block)

# Verifica della validità della blockchain
print("Validità della blockchain:", blockchain.is_chain_valid())

# Stampa dei blocchi della blockchain
for block in blockchain.chain:
    print("Block Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("--------------------")