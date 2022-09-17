import csv
from os import path


if path.exists("paginas.txt"):
	pass
else:
	new = open("paginas.txt","w")
	with open("user-ct-test-collection-05.txt", 'r') as file:
		rf = csv.reader(file, delimiter='\t')
		for fila in rf:
			if '' in fila:
				continue
			line = '\t'.join(fila)
			new.write(line)
			new.write("\n")
		
