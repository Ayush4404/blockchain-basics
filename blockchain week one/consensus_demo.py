import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

# -----------------------------
# Create mock data for demo
# -----------------------------

# Miners for Proof-of-Work (PoW)
miners = [
    {"id": "Miner A", "power": random.randint(1, 100)},
    {"id": "Miner B", "power": random.randint(1, 100)},
    {"id": "Miner C", "power": random.randint(1, 100)}
]

# Stakers for Proof-of-Stake (PoS)
stakers = [
    {"id": "Staker X", "stake": random.randint(100, 1000)},
    {"id": "Staker Y", "stake": random.randint(100, 1000)},
    {"id": "Staker Z", "stake": random.randint(100, 1000)}
]

# Voters and delegates for Delegated Proof-of-Stake (DPoS)
voters = [
    {"id": "Voter 1", "tokens": random.randint(10, 50), "vote": None},
    {"id": "Voter 2", "tokens": random.randint(10, 50), "vote": None},
    {"id": "Voter 3", "tokens": random.randint(10, 50), "vote": None}
]
delegates = ["Delegate Alpha", "Delegate Beta", "Delegate Gamma"]

# -----------------------------
# Proof-of-Work Simulation
# -----------------------------
def simulate_pow():
    print("\n=== ⛏️ Proof-of-Work (PoW) ===")
    print("🔎 Logic: The miner with the highest computational power gets to validate the block.\n")
    
    # Display all miner powers
    print("🧱 Miner Powers:")
    for miner in miners:
        print(f"  - {miner['id']}: {miner['power']} TH/s")
    
    # Select miner with highest power
    selected = max(miners, key=lambda x: x["power"])
    
    print(f"\n✅ Selected Miner: {selected['id']} ({selected['power']} TH/s)")
    print("📘 Why: They have the highest computing power, so they are most likely to solve the cryptographic puzzle first.")

# -----------------------------
# Proof-of-Stake Simulation
# -----------------------------
def simulate_pos():
    print("\n=== 🪙 Proof-of-Stake (PoS) ===")
    print("🔎 Logic: The staker with the largest stake has the highest chance of being selected.\n")
    
    # Display staker stakes
    print("💰 Staker Stakes:")
    for staker in stakers:
        print(f"  - {staker['id']}: ${staker['stake']}")
    
    # Select staker with highest stake
    selected = max(stakers, key=lambda x: x["stake"])
    
    print(f"\n✅ Selected Validator: {selected['id']} (${selected['stake']})")
    print("📘 Why: Higher stake means more investment in the network, so more trustworthy to validate blocks.")

# -----------------------------
# Delegated Proof-of-Stake Simulation
# -----------------------------
def simulate_dpos():
    print("\n=== 🗳️ Delegated Proof-of-Stake (DPoS) ===")
    print("🔎 Logic: Token holders vote for delegates; the one with the most weighted votes is elected.\n")
    
    # Simulate voting
    for voter in voters:
        voter["vote"] = random.choice(delegates)
    
    # Tally weighted votes
    vote_counts = {delegate: 0 for delegate in delegates}
    for voter in voters:
        vote_counts[voter["vote"]] += voter["tokens"]
    
    # Display vote weights
    print("📊 Vote Totals (weighted by tokens):")
    for delegate in delegates:
        print(f"  - {delegate}: {vote_counts[delegate]} tokens")
    
    print("\n🧑‍⚖️ Voter Choices:")
    for voter in voters:
        print(f"  - {voter['id']} ({voter['tokens']} tokens) ➜ {voter['vote']}")
    
    # Select delegate with highest votes
    winner = max(vote_counts, key=vote_counts.get)
    
    print(f"\n✅ Elected Delegate: {winner} ({vote_counts[winner]} votes)")
    print("📘 Why: This delegate received the most total votes (weighted by token ownership).")

# -----------------------------
# Run All Simulations
# -----------------------------
simulate_pow()
simulate_pos()
simulate_dpos()


#PoW: Chooses miner with the most computational power.

#PoS: Chooses validator with the most stake.

#DPoS: Simulates voting process and picks delegate with highest token-weighted votes.