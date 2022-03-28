import random 

extensions = ["png", "pdf", "txt", "jpg"]
counter = 1

for x in range(3000):
    fp = open(f"file{counter}.{random.choice(extensions)}", "x")
    fp.close()

    counter += 1
