rawinstring="ab.Cč d Eěf#GiÍJ  KL:&mnňoó pQrŘsšTťUúův wxYzž"
friedinstring=""

for i in range(0,len(rawinstring)):
    if rawinstring[i]<"A" or rawinstring[i]>"Z":
        if rawinstring[i]="á":
            friedstring[i]="A"
        if rawinstring[i]="é" or rawinstring[i]="ě":
            friedstring[i]="E"
        if rawinstring[i]="ď":
            friedstring[i]="D"
        if rawinstring[i]="č":
            friedstring[i]="C"
        if rawinstring[i]="ř":
            friedstring[i]="R"
        if rawinstring[i]="ž":
            friedstring[i]="Z"
        if rawinstring[i]="ý":
            friedstring[i]="Y"
        if rawinstring[i]="í":
            friedstring[i]="I"
        if rawinstring[i]="ĺ":
            friedstring[i]="L"
        if rawinstring[i]="ň":
            friedstring[i]="N"
        if rawinstring[i]="ó":
            friedstring[i]="O"
        if rawinstring[i]="ř":
            friedstring[i]="R"
        if rawinstring[i]="š":
            friedstring[i]="S"
        if rawinstring[i]="ť":
            friedstring[i]="T"
        if rawinstring[i]="ú" or rawinstring[i]="ů":
            friedstring[i]="U"
        if rawinstring[i]="ý":
            friedstring[i]="Y"
        if rawinstring[i]="ž"