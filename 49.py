def pythagorean_triplets(range_start, range_end):
    triplets = []
    for c in range(range_start, range_end+1):
        for b in range(range_start, c):
            for a in range(range_start, b):
                if (a**2 + b**2 == c**2):
                    triplets.append((a, b, c))
    return triplets

triplets = pythagorean_triplets(1, 100)
print("Pythagorean Triplets:", triplets)
