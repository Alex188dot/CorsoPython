# Blockchain simulator 

This program creates a blockchain, with each block representing the development of a product from its creation to its distribution. The product in question is cheese and the blockchain tracks the following types: Parmigiano, Brie, Gouda, Emmental, Cheddar. Because each cheese is local they can only be produced by specific companies (Parmesan Co., Brie LLC, Gouda Corp., Emmy Gmbh, Cheddy Ltd.) and in specific locations (Italy, France, Netherlands, Switzerland, USA). The assumption is that this is a private logistics blockchain and that all the companies belong to the same group called Cheese Corp.
        
The code uses the following classes:

Block represents a single block in the blockchain. It has the following attributes:
- index is the index of the block in the chain.
- timestamp is the timestamp of the block.
- data is the data of the block.
- previous_hash is the hash of the previous block in the chain.
- nonce is a random number used to mine the block.
- difficulty is the difficulty of mining the block.
- hash is the hash of the block.
  
Blockchain represents the entire blockchain. It has the following methods:
- create_genesis_block() creates the genesis block, which is the first block in the blockchain.
- get_latest_block() gets the latest block in the blockchain.
- add_block() adds a new block to the blockchain.
- is_chain_valid() checks if the blockchain is valid.
- generate_random_data() generates random data for a block.


This code demonstrates how to create a basic blockchain. It starts by initializing a blockchain object and adding the genesis block, which contains arbitrary data. Then, it enters an infinite loop that creates and displays a new block every second (see below). 


https://github.com/Alex188dot/CorsoPython/assets/117444853/00c81dc5-ecc9-4ab2-ae3a-97c69d20eb68


Each new block contains random data and the next sequential index in the chain. The code also verifies the validity of the blockchain and shows the new block's details. 

This program uses the hashlib module to compute the hash of each block. The hash serves as a unique fingerprint for the block. It is derived from the block's index, timestamp, data, previous hash, and nonce. The nonce is a random number that is used to solve a cryptographic puzzle, known as mining. The difficulty of mining determines how hard it is to find a nonce that produces a hash that begins with a certain number of zeros, in this case 4.

The code uses the time module to obtain the current timestamp which indicates when the block was created. The random module generates random data and random numbers for the nonce. 
