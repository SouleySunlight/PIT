t= [(2,1),(3,4),(5,6)]

for i in t:
    print(i[0])
dico={}
dico[1]=[1,2,3]
dico[2]=[1,2]
dico[3]=[1]
dico[4]=[]
print(dico)
for i in dico.values():
    if 2 in i:
        i.remove(2)
print(dico)
