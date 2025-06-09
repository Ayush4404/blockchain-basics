import hashlib  # For SHA-256 hashing
import time     # For timestamps
import sys

sys.stdout.reconfigure(encoding='utf-8')
# Define a Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()  # Calculate hash on creation

    def calculate_hash(self):
        # Concatenate all block information
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        # Convert to bytes and compute SHA-256 hash
        return hashlib.sha256(block_string.encode()).hexdigest()

# ----------------------------
# Step 1: Create Genesis Block
# ----------------------------
genesis_block = Block(
    index=0,
    timestamp=time.time(),
    data="Genesis Block",
    previous_hash="0"
)

# ----------------------------
# Step 2: Add More Blocks
# ----------------------------
block_1 = Block(
    index=1,
    timestamp=time.time(),
    data="Transaction A: Alice pays Bob $10",
    previous_hash=genesis_block.hash
)

block_2 = Block(
    index=2,
    timestamp=time.time(),
    data="Transaction B: Bob pays Charlie $5",
    previous_hash=block_1.hash
)

# ----------------------------
# Step 3: Print the Blockchain
# ----------------------------
print("🔗 ----- Original Blockchain -----\n")
for block in [genesis_block, block_1, block_2]:
    print(f"📦 Block {block.index}")
    print(f"   Data           : {block.data}")
    print(f"   Prev. Hash     : {block.previous_hash[:10]}...")
    print(f"   Block Hash     : {block.hash[:10]}...\n")

# ----------------------------
# Step 4: Tamper with Block 1
# ----------------------------
print("🚨 ----- After Tampering Block 1 -----\n")

# Change the data in Block 1
block_1.data = "TRANSACTION TAMPERED: Alice pays Eve $1000"
block_1.hash = block_1.calculate_hash()  # Recalculate hash to hide the tampering

# Output tampered block info
print(f"⚠️  Block 1 New Data  : {block_1.data}")
print(f"🔄 Block 1 New Hash  : {block_1.hash[:10]}...")
print(f"🔗 Block 2's Prev Hash: {block_2.previous_hash[:10]}...\n")

# ----------------------------
# Step 5: Detect Integrity Issue
# ----------------------------
if block_2.previous_hash != block_1.hash:
    print("❌ Result: Block 2's previous hash does NOT match Block 1's new hash ➜ 🔓 BLOCKCHAIN BROKEN!")
else:
    print("✅ Blockchain intact.")


#A blockchain's integrity relies on each block's hash.
#If you tamper with data, even if you recalculate the hash,
# the chain is broken unless you recompute hashes for all following blocks — 
# which is the core defense mechanism of blockchain