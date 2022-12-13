#epub to txt
#bere jen p tag

import sys
import ebooklib
from ebooklib import epub
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from bs4 import BeautifulSoup, Doctype

class Konverter(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setFixedHeight(200)
        self.setFixedWidth(500)
        self.soubor=QtWidgets.QLabel("umisteni souboru")
        self.tacitko_konce = QtWidgets.QPushButton('konec')
        self.tacitko_konce.clicked.connect(self.close)
        self.tlacitko_knizka = QtWidgets.QPushButton('otevri')
        self.tlacitko_knizka.clicked.connect(self.otevri)
        self.tlacitko_uknizka = QtWidgets.QPushButton('uloz')
        self.tlacitko_uknizka.clicked.connect(self.uloz)
        p = QtWidgets.QGridLayout()
        p.addWidget(self.soubor, 0,0)
        p.addWidget(self.tlacitko_knizka, 1,0)
        p.addWidget(self.tlacitko_uknizka, 3,0)
        p.addWidget(self.tacitko_konce, 4, 0)
        self.setLayout(p)
        self.show()

    def otevri(self):
        self.a = ""
        otevri=QFileDialog.getOpenFileName(self, "otevri","",'(*.epub)')
        if len(str(otevri))>=9:
            c=str(otevri)[2:-14]    #čistá cesta souboru
            self.soubor.setText(c)
            self.knizka=epub.read_epub(c)
            items = list(self.knizka.get_items_of_type(ebooklib.ITEM_DOCUMENT))
            for i in items:
                soup = BeautifulSoup(i.get_body_content(), 'html.parser')
                for t in soup.find_all('p'):
                    l=t.get_text()+'\n(_,_)'
                    self.a=self.a+str(l)

    def uloz(self):
        uloz=QFileDialog.getSaveFileName(self,"uloz","knizka.txt","(*.txt)")
        print(uloz)
        g=str(self.a)
        s=g.split('(_,_)')
        b=str(uloz)[2:-13]
        if len(self.a)>1:
            f=open(b,"w")
            for i in s:
                try:
                    f.write(str(i))
                except:
                    f.write("něco se tu pokazilo obsah tagu chybí")
            f.close()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = Konverter(windowTitle='konverter')
    sys.exit(app.exec_())