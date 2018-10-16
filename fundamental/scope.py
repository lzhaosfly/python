total = 0


def increment():
    global total
    total += 1
    return total


increment()
print(f"total is {total}")
