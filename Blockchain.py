import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index).encode('utf-8') +
               str(self.timestamp).encode('utf-8') + 
               str(self.data).encode('utf-8') + 
               str(self.previous_hash).encode('utf-8'))
    return sha.hexdigest()

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hello world! I'm block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 15

file = open("C:\\Users\\LeTienHoc\\OneDrive\\Desktop\\a.txt","w")

for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  
  file.write("{}".format(block_to_add.data))
  file.write("Block {} da duoc them vao blockchain".format(block_to_add.index))
  file.write("Previous_Hash:{}".format(block_to_add.previous_hash))
  file.write("Hash: {}\n".format(block_to_add.hash))

file.close()
  
