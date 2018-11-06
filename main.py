rawinstring="ab.Cč d Eěf#GiÍJ  KL:&mnňoó pQrŘsšTťUúův wxYzž"
rawinstring = "ěeš"
friedinstring=""
reple = [["a","á","ä","Á","Ä"],["b"],["č","ć","c","Č","Ć"],["d","ď","Ď"],["ě","é","e","ë","Ě","É","Ë"],["f"],["g"],["h"],["i","í","ï","Í","Ï"],["j"],["k"],["l","ĺ","Ĺ"],["m"],["n","ň","ń","Ň","Ń"],["o","ó","ö","Ó","Ö"],["p"],["q"],["r","ř","ŕ","Ř","Ŕ"],["š","ś","s","Š","Ś"],["t","ť","Ť"],["u","ú","ů","Ů","Ú"],["v"],["w"],["x"],["y","ý","ÿ","Ý","Ÿ"],["z","ž","ź","Ž","Ź"]]
forThing = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(0,len(rawinstring)):
    if rawinstring[i]<"A" or rawinstring[i]>"Z":
        for j in range(0, len(reple)):
            if rawinstring[i] in reple[j]:
                print(forThing[j])
                
