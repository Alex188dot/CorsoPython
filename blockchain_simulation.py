import hashlib
import json
import time
import random


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Added nonce attribute
        self.difficulty = 4  # Added difficulty attribute
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = json.dumps(self.data, sort_keys=True).encode()
        # Added nonce to hash calculation
        return hashlib.sha256(str(self.index).encode() + str(self.timestamp).encode() + data_string + str(
            self.previous_hash).encode() + str(self.nonce).encode()).hexdigest()

    def mine_block(self):
        # Loop until a valid hash is found
        while True:
            # Calculate a new hash
            self.hash = self.calculate_hash()
            # Check if the hash meets the difficulty criteria
            if self.hash.startswith("0" * self.difficulty):
                # Return the hash and stop the loop
                return self.hash
            else:
                # Increment the nonce and continue the loop
                self.nonce += 1


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        # Call mine_block on new_block before appending it to the chain
        new_block.mine_block()
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

    def generate_random_data(self):
        # Define some possible values for each field of the data
        names = ["Parmigiano", "Brie", "Gouda", "Emmental", "Cheddar"]
        origins = ["Italy", "France", "Netherlands", "Switzerland", "USA"]
        producers = ["Parmesan Co.", "Brie LLC", "Gouda Corp.", "Emmy Gmbh", "Cheddy Ltd."]
        locations = ["Warehouse A", "Warehouse B", "Distribution Center", "Retail Store", "Customer"]

        # Get the latest block's data
        latest_data = self.get_latest_block().data

        # Generate a random index for each field of the data except for name, origin and producer
        location_index = random.randint(0, len(locations) - 1)

        # Create a new data dictionary with random values based on the previous blocks and the interconnection between name, origin and producer
        new_data = {}

        # If the latest block's data is the genesis block, use random values for all fields
        if latest_data == "Genesis Block":
            # Generate a random index for name, origin and producer that are interconnected
            name_origin_producer_index = random.randint(0, len(names) - 1)
            new_data["name"] = names[name_origin_producer_index]
            new_data["origin"] = origins[name_origin_producer_index]
            new_data["producer"] = producers[name_origin_producer_index]
            new_data["production_date"] = time.strftime("%Y-%m-%d")
            new_data["location"] = locations[location_index]
            new_data["date"] = time.strftime("%Y-%m-%d")

        # Otherwise, use the next values from the lists for name, origin and producer and some random values for the rest of the fields
        else:
            # Get the index of the latest block's name in the names list
            latest_name_index = names.index(latest_data["name"])
            # Get the next index by adding one and using modulo to wrap around if needed
            next_name_index = (latest_name_index + 1) % len(names)
            # Use the next index to get the next values for name, origin and producer from the lists
            new_data["name"] = names[next_name_index]
            new_data["origin"] = origins[next_name_index]
            new_data["producer"] = producers[next_name_index]
            new_data["production_date"] = latest_data["production_date"]
            new_data["location"] = locations[location_index]
            new_data["date"] = time.strftime("%Y-%m-%d")

        # Return the new data dictionary
        return new_data


# Example of usage

# Create the blockchain
blockchain = Blockchain()

# Create and add the first block with random data
first_block = Block(1, time.time(), blockchain.generate_random_data(), "")
blockchain.add_block(first_block)

# Print the first block of the blockchain
print("Block Index:", first_block.index)
print("Timestamp:", first_block.timestamp)
print("Data:", first_block.data)
print("Hash:", first_block.hash)
print("Previous Hash:", first_block.previous_hash)
print("--------------------")

# Loop indefinitely to generate and print a new block every second
while True:
    # Get the latest block's index
    latest_index = blockchain.get_latest_block().index
    # Create a new block with random data and the next index
    new_block = Block(latest_index + 1, time.time(), blockchain.generate_random_data(), "")
    # Add the new block to the blockchain
    blockchain.add_block(new_block)
    # Print the new block
    print("Block Index:", new_block.index)
    print("Timestamp:", new_block.timestamp)
    print("Data:", new_block.data)
    print("Hash:", new_block.hash)
    print("Previous Hash:", new_block.previous_hash)
    print("--------------------")
    # Wait for one second before repeating the loop
    time.sleep(1)
