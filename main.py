rawinstring="ab.Cč d Eěf#GiÍJ  KL:&mnňoó pQrŘsšTťUúův wxYzž"
friedinstring=""
reple = [["a","á","ä","Á","Ä"],["b"],["č","ć","c","Č","Ć"],["d","ď","Ď"],["ě","é","e","ë","Ě","É","Ë"],["f"],["g"],["h"],["i","í","ï","Í","Ï"],["j"],["k"],["l","ĺ","Ĺ"],["m"],["n","ň","ń","Ň","Ń"],["o","ó","ö","Ó","Ö"],["p"],["q"],["r","ř","ŕ","Ř","Ŕ"],["š","ś","s","Š","Ś"],["t","ť","Ť"],["u","ú","ů","Ů","Ú"],["v"],["w"],["x"],["y","ý","ÿ","Ý","Ÿ"],["z","ž","ź","Ž","Ź"]]
forThing = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lang="W"

for i in range(0,len(rawinstring)):
    if rawinstring[i]<"A" or rawinstring[i]>"Z":
        if rawinstring[i]==" ":
            friedinstring+="MEZERA"
        else:
            if rawinstring[i]==chr(ord(lang)+32):
                if lang=="w":
                    friedinstring+="V"
                if lang=="j":
                    friedinstring+="I"
            else:
                for j in range(0, len(reple)):
                    if rawinstring[i] in reple[j]:
                        #print(forThing[j])
                        friedinstring+=forThing[j]
    else:
        if rawinstring[i]==lang:
            if lang=="W":
                friedinstring+="V"
            if lang=="J":
                friedinstring+="I"
        else:
            friedinstring+=rawinstring[i]
        
key="BANANOVNIK" #banovik
table=""
            
for i in range(0,len(key)):
    if not(key[i] in table):
        table+=key[i]

for j in range(0,26):
    if (not(chr(65+j) in table)) and 65+j!=ord(lang):
        table+=chr(65+j)