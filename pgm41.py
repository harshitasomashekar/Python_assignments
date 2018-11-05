

file = open("pgm41.csv","r")
for line in file:
        for word in line.split(','):
       		if word.endswith('n'):
          		print(word)

