import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments!")

counts = {}
with open(sys.argv[1], 'r') as f:
    for line in f:
        words = line.lower().strip().split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1    

for word, count in counts.items():
    print(f"{word}: {count}")