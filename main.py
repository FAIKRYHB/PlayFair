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
                    if len(outstr)!=0:
                        if outstr[-1]=="M":
                            outstr+="X"
                    outstr+="MEZERA"
                else:
                    if instr[i]==chr(ord(self.lang)+32):
                        if self.lang=="W":
                            if len(outstr)!=0:
                                if outstr[-1]=="V":
                                    outstr+="X"
                            outstr+="V"
                        if self.lang=="J":
                            if len(outstr)!=0:
                                if outstr[-1]=="I":
                                    outstr+="X"
                            outstr+="I"
                    else:
                        for j in range(0, len(reple)):
                            if instr[i] in reple[j]:
                                if len(outstr)!=0:
                                    if outstr[-1]==forThing[j]:
                                        outstr+="X"
                                outstr+=forThing[j]
            else:
                if instr[i]==self.lang:
                    if self.lang=="W":
                        if len(outstr)!=0:
                                if outstr[-1]=="V":
                                    outstr+="X"
                        outstr+="V"
                    if self.lang=="J":
                        if len(outstr)!=0:
                                if outstr[-1]=="I":
                                    outstr+="X"
                        outstr+="I"
                else:
                    if len(outstr)!=0:
                                if outstr[-1]==instr[i]:
                                    outstr+="X"
                    outstr+=instr[i]
        if (len(outstr)%2)==1:
            if outstr[-1]=="X":
                outstr+="W"
            else:
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
        instr = self.input.toPlainText()
        instr = self.Fry(instr)
        print(instr)
        # Načtená tabulka s aktuálním klíčem
        table = self.GenTable(self.key.text())
        # Obsah této proměné se zobrazí
        outstr = ""
        
        ## Sem příjde dané šifrování
        prvni=0
        druhe=0
        for i in range(0,len(instr),2):
            for j in range(0,25):
                if instr[i+1]==table[j]:
                    print(table[j])
                    druhe=j
                    break
            x=druhe%5
            for j in range(0,25):
                if instr[i]==table[j]:
                    print(table[j])
                    prvni=j
                    break
            if (int(prvni/5))==(int(druhe/5)):
                if (int(prvni/5))==(int((prvni+1)/5)):
                    outstr+=table[prvni+1]
                else:
                    outstr+=table[prvni-4]
                if (int(druhe/5))==(int((druhe+1)/5)):
                    outstr+=table[druhe+1]
                else:
                    outstr+=table[druhe-4]
            else:
                if prvni%5==druhe%5:
                    if prvni+5>24:
                        outstr+=table[prvni%5]
                    else:
                        outstr+=table[prvni+5]
                    if druhe+5>24:
                        outstr+=table[druhe%5]
                    else:
                        outstr+=table[druhe+5]
                else:
                    y=(int(prvni/5))*5
                    outstr+=table[x+y]
                    print(table[x+y])
                    
                    for j in range(0,25):
                        if instr[i]==table[j]:
                            prvni=j
                            break
                    x=prvni%5
                    for j in range(0,25):
                        if instr[i+1]==table[j]:
                            druhe=j
                            break
                    y=(int(druhe/5))*5
                    outstr+=table[x+y]
                    print(table[x+y])

        self.output.setText(outstr)

    def desifrovat(self):
        # Načtená vstupní data
        instr = self.input.toPlainText()
        # Načtená tabulka s aktuálním klíčem
        table = self.GenTable(self.key.text())
        # Obsah této proměné se zobrazí
        outstr = ""
        
        ## Sem příjde dané dešifrování
        prvni=0
        druhe=0
        for i in range(0,len(instr),2):
            for j in range(0,25):
                if instr[i+1]==table[j]:
                    print(table[j])
                    druhe=j
                    break
            x=druhe%5
            for j in range(0,25):
                if instr[i]==table[j]:
                    print(table[j])
                    prvni=j
                    break
            if (int(prvni/5))==(int(druhe/5)):
                if (int(prvni/5))==(int((prvni-1)/5)):
                    outstr+=table[prvni-1]
                else:
                    outstr+=table[prvni+4]
                if (int(druhe/5))==(int((druhe-1)/5)):
                    outstr+=table[druhe-1]
                else:
                    outstr+=table[druhe+4]
            else:
                if prvni%5==druhe%5:
                    if prvni-5<0:
                        outstr+=table[24-prvni-5]
                    else:
                        outstr+=table[prvni-5]
                    if druhe-5<0:
                        outstr+=table[24-druhe-5]
                    else:
                        outstr+=table[druhe-5]
                else:
                    y=(int(prvni/5))*5
                    outstr+=table[x+y]
                    print(table[x+y])
                    
                    for j in range(0,25):
                        if instr[i]==table[j]:
                            prvni=j
                            break
                    x=prvni%5
                    for j in range(0,25):
                        if instr[i+1]==table[j]:
                            druhe=j
                            break
                    y=(int(druhe/5))*5
                    outstr+=table[x+y]
                    print(table[x+y])
            
        self.output.setText(outstr)
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