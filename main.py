rawinstring="ab.Cč d Eěf#GiÍJ  KL:&mnňoó pQrŘsšTťUúův wxYzž"
rawinstring = "ěeš"
friedinstring=""
reple = [["ě","é","e"],["š"],["č"]]
forThing = ["E","S","C"]
for i in range(0,len(rawinstring)):
    if rawinstring[i]<"A" or rawinstring[i]>"Z":
        for j in range(0, len(reple)):
            if rawinstring[i] in reple[j]:
                print(forThing[j])
                print("jap")