with open("actors") as f:
    content = f.readlines()

print "["
for line in content:
	print "'"+line.split("\t")[2]+"',"
print "]"
