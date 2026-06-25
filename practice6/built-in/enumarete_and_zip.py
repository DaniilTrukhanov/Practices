names = ["name1", "name2", "name3"]

for index, name in enumerate(names, start=1):
    print(index, name)

scores = [90, 95, 80]

for name, score in zip(names, scores):
    print (name, score)