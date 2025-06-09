import hashlib
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')
# Define the structure of a block
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                      # Block number
        self.timestamp = timestamp              # Time of creation
        self.data = data                        # Transaction or data payload
        self.previous_hash = previous_hash      # Hash of the previous block
        self.nonce = 0                          # Number used for PoW
        self.hash = self.calculate_hash()       # Initial hash without mining

    # Generate SHA-256 hash of the block's contents
    def calculate_hash(self):
        input_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(input_string.encode()).hexdigest()

    # Proof-of-Work mining: find a hash with leading zeros
    def mine_block(self, difficulty):
        target = "0" * difficulty   # E.g., '0000' for difficulty 4
        start_time = time.time()
        attempts = 0

        # Keep trying different nonce values until target match
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        elapsed = time.time() - start_time

        # Log mining summary
        print(f"\n✅ [Mined] Block {self.index} (Difficulty: {difficulty})")
        print(f"   Time Taken : {elapsed:.4f} seconds")
        print(f"   Attempts   : {attempts:,}")
        print(f"   Nonce      : {self.nonce}")
        print(f"   Final Hash : {self.hash}")

# --------------------------
# Simulate the Blockchain
# --------------------------

print("🚀 Starting Blockchain Simulation with Proof-of-Work")

# Mine Genesis Block
print("\n--- Mining Genesis Block ---")
genesis = Block(0, time.time(), "Genesis Block", "0")
genesis.mine_block(difficulty=2)

# Mine Block 1
print("\n--- Mining Block 1 ---")
block1 = Block(1, time.time(), "Alice pays Bob $10", genesis.hash)
block1.mine_block(difficulty=4)

# Mine Block 2
print("\n--- Mining Block 2 ---")
block2 = Block(2, time.time(), "Bob pays Charlie $5", block1.hash)
block2.mine_block(difficulty=5)

# --------------------------
# Display Final Blockchain
# --------------------------
print("\n📦 Final Blockchain Structure")
for block in [genesis, block1, block2]:
    print(f"\n🧱 Block {block.index}")
    print(f"   Nonce      : {block.nonce}")
    print(f"   Hash       : {block.hash[:15]}...")
    print(f"   Prev Hash  : {block.previous_hash[:15]}...")
    print(f"   Data       : {block.data}")

#⛏️ Proof-of-Work involves repeatedly changing a nonce until a hash meets a difficulty condition (starts with N zeros).

#🧱 Each block contains a hash of the previous block, forming a tamper-evident chain.

#🔐 Increasing difficulty = more time & computation = better security.