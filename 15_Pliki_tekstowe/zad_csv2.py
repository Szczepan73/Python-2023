import os
print(os.getcwd())

with open('data/foods.csv') as f:
    for l in f:
        dane = l.strip().split(',')
        print ("\t".join(dane))
