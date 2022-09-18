import csv
from os import path
from unzip import unziptxt
from waiting import wait

wait(lambda: unziptxt(), timeout_seconds = 30, waiting_for="Descomprimiendo..")


if path.exists("paginas.txt"):
	pass
else:
	new = open("paginas.txt","w")
	with open("user-ct-test-collection-09.txt", 'r') as file:
		rf = csv.reader(file, delimiter='\t')
		for fila in rf:
			if '' in fila:
				continue
			line = '\t'.join(fila)
			new.write(line)
			new.write("\n")
		
