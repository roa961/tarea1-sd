import csv

new = open("paginas.txt","w")
with open("user-ct-test-collection-09.txt", 'r') as file:
	rf = csv.reader(file, delimiter='\t')
	for fila in rf:
		if '' in fila:
			continue
		line = '\t'.join(fila)
		new.write(line)
		new.write("\n")
		
