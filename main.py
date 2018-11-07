#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QFileDialog
from PyQt5 import QtGui, uic

qtCreatorFile = "dialog.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)



class pFair(QMainWindow, Ui_MainWindow):
    # Lang přístupná pouze v tomto objektů
    lang = "W"
    def Fry(self,instr):
        outstr=""
        reple = [["a","á","ä","Á","Ä"],["b"],["č","ć","c","Č","Ć"],["d","ď","Ď"],["ě","é","e","ë","Ě","É","Ë"],["f"],["g"],["h"],["i","í","ï","Í","Ï"],["j"],["k"],["l","ĺ","Ĺ"],["m"],["n","ň","ń","Ň","Ń"],["o","ó","ö","Ó","Ö"],["p"],["q"],["r","ř","ŕ","Ř","Ŕ"],["š","ś","s","Š","Ś"],["t","ť","Ť"],["u","ú","ů","Ů","Ú"],["v"],["w"],["x"],["y","ý","ÿ","Ý","Ÿ"],["z","ž","ź","Ž","Ź"]]
        forThing = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for i in range(0,len(instr)):
            if instr[i]<"A" or instr[i]>"Z":
                if instr[i]==" ":
                    outstr+="MEZERA"
                else:
                    if instr[i]==chr(ord(self.lang)+32):
                        if self.lang=="W":
                            outstr+="V"
                        if self.lang=="J":
                            outstr+="I"
                    else:
                        for j in range(0, len(reple)):
                            if instr[i] in reple[j]:
                                #print(forThing[j])
                                outstr+=forThing[j]
            else:
                if instr[i]==self.lang:
                    if self.lang=="W":
                        outstr+="V"
                    if self.lang=="J":
                        outstr+="I"
                else:
                    outstr+=instr[i]
        if (len(outstr)%2)==1:
            outstr+="X"
        return outstr

    def GenTable(self,key):
        key=self.Fry(key)
        table=""
        for i in range(0,len(key)):
            if not(key[i] in table):
                table+=key[i]
        
        for j in range(0,26):
            if (not(chr(65+j) in table)) and 65+j!=ord(self.lang):
                table+=chr(65+j)
        return table
    
    def ChangeTable(self):
        table = self.GenTable(self.key.text())
        print(table)
        for i in range(1,6):
            row = ""
            for j in range(0,5):
                row = row + "   " + table[(i-1)*5+j]
            getattr(self,"row"+str(i)).setText(row)
            print(row)
    # Funkce na změnu jazyku zároveň se i přepíše tabulka        
    def switchIt(self):
        if self.lang == "W":
            self.lang = "J"
            self.switchLang.setText("Přepnout do CZ")
            
        else:
            self.lang ="W"
            self.switchLang.setText("Přepnout do EN")
        self.ChangeTable()
        
    # Funkce pro šifrování dat zavolána po kliku na button
    def sifrovat(self):
        # Načtená vstupní data
        vstup = self.input.text()
        # Načtená tabulka s aktuálním klíčem
        table = self.GenTable(self.key.text())
        # Obsah této proměné se zobrazí
        result = ""
        
        ## Sem příjde dané šifrování
        
        self.output.setText(result)
    def desifrovat(self):
        # Načtená vstupní data
        vstup = self.input.text()
        # Načtená tabulka s aktuálním klíčem
        table = self.GenTable(self.key.text())
        # Obsah této proměné se zobrazí
        result = ""
        
        ## Sem příjde dané dešifrování
        
        self.output.setText(result)
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.key.textChanged.connect(self.ChangeTable)
        self.switchLang.clicked.connect(self.switchIt)
        self.code.clicked.connect(self.sifrovat)
        self.decode.clicked.connect(self.desifrovat)
        
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pFair()
    window.show()
    sys.exit(app.exec_())


####
friedstring=pFair.Fry("ab.Cč d Eěf#GiÍJ  KL:&mnňoó pQrŘsšTťUúův wxYzž")
table=pFair.GenTable("BANANOVNIK")
#key="BANANOVNIK" #banovik
