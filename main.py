class pFair():
    def Fry(self,instr,lang):#lang="W" / lang="J"
        outstr=""
        reple = [["a","á","ä","Á","Ä"],["b"],["č","ć","c","Č","Ć"],["d","ď","Ď"],["ě","é","e","ë","Ě","É","Ë"],["f"],["g"],["h"],["i","í","ï","Í","Ï"],["j"],["k"],["l","ĺ","Ĺ"],["m"],["n","ň","ń","Ň","Ń"],["o","ó","ö","Ó","Ö"],["p"],["q"],["r","ř","ŕ","Ř","Ŕ"],["š","ś","s","Š","Ś"],["t","ť","Ť"],["u","ú","ů","Ů","Ú"],["v"],["w"],["x"],["y","ý","ÿ","Ý","Ÿ"],["z","ž","ź","Ž","Ź"]]
        forThing = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for i in range(0,len(instr)):
            if instr[i]<"A" or instr[i]>"Z":
                if instr[i]==" ":
                    outstr+="MEZERA"
                else:
                    if instr[i]==chr(ord(lang)+32):
                        if lang=="W":
                            outstr+="V"
                        if lang=="J":
                            outstr+="I"
                    else:
                        for j in range(0, len(reple)):
                            if instr[i] in reple[j]:
                                #print(forThing[j])
                                outstr+=forThing[j]
            else:
                if instr[i]==lang:
                    if lang=="W":
                        outstr+="V"
                    if lang=="J":
                        outstr+="I"
                else:
                    outstr+=instr[i]
        if (len(outstr)%2)==1:
            outstr+="X"
        return outstr

    def GenTable(self,key,lang):
        key=pFair.Fry(key,lang)
        table=""
        for i in range(0,len(key)):
            if not(key[i] in table):
                table+=key[i]
        
        for j in range(0,26):
            if (not(chr(65+j) in table)) and 65+j!=ord(lang):
                table+=chr(65+j)
        return table



####
friedstring=pFair.Fry("ab.Cč d Eěf#GiÍJ  KL:&mnňoó pQrŘsšTťUúův wxYzž","W")
table=pFair.GenTable("BANANOVNIK","W")
#key="BANANOVNIK" #banovik
