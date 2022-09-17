import os

comm = os.popen('docker inspect -f \'{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}\' postgres').read()

ip = str(comm).strip("\n")
new = open(".env","w")
new.write("POSTGRES_USER=postgres")
new.write("\n")
new.write("POSTGRES_PASSWORD=postgres")
new.write("\n")
new.write("POSTGRES_DB=paginas")
new.write("\n")
new.write("POSTGRES_HOST="+ip)
new.write("\n")
new.write("POSTGRES_PORT=5432")
new.write("\n")
new.write("HIDE_EMPTY_PASSWORD=yes")
