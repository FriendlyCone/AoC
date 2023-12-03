# Challenge input
inputfile = open("input.txt", "r")

### PART 1 ###
batch = []
amount = 0
for line in inputfile:
    if line.strip():
        amount = amount + int(line)
        print(f"Counting... {amount}")
    else:
        print(f"Batch total: {amount}")
        batch.append(amount)
        amount = 0
print(f"Batch total: {amount}")
batch.append(amount)
highestbatch = max(batch)
print(f"The highest batch is {highestbatch}")

### PART 2 ###
print("Highest 3 batches:")
print(sorted(batch)[-1])
print(sorted(batch)[-2])
print(sorted(batch)[-3])
sumbatch = sorted(batch)[-1] + sorted(batch)[-2] + sorted(batch)[-3]
print(f"Combined these amount to: {sumbatch}")