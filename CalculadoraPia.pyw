from __future__ import division
from msilib.schema import Dialog
import sys 
from PyQt5.QtWidgets import QDialog,QApplication
from numpy import diag
from CalculadoraPia_ui import Ui_CalculadoraDialog

class CalculadoraApplication(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_CalculadoraDialog()
        self.ui.setupUi(self)

        self.ui.btn_sumar.clicked.connect(self.sumar)
        self.ui.btn_restar.clicked.connect(self.restar)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.btn_dividir.clicked.connect(self.dividir) 

        self.show()

    def sumar (self):
        suma=0
        ope1=0
        ope2=0

        if len(self.ui.txt_primer_num.text()) > 0:
            ope1=int(self.ui.txt_primer_num.text())
        
        if len(self.ui.txt_segundo_num.text()) >0:
            ope2=int(self.ui.txt_segundo_num.text())

        suma=ope1+ope2
        
        self.ui.lbl_resultado.setText(str(suma))

    def restar (self):
        resta=0
        ope1=0
        ope2=0

        if len(self.ui.txt_primer_num.text()) > 0:
            ope1=int(self.ui.txt_primer_num.text())
        
        if len(self.ui.txt_segundo_num.text()) >0:
            ope2=int(self.ui.txt_segundo_num.text())

        resta=ope1-ope2
        
        self.ui.lbl_resultado.setText(str(resta))

    def multiplicar (self):
        multi=0
        ope1=0
        ope2=0

        if len(self.ui.txt_primer_num.text()) > 0:
            ope1=int(self.ui.txt_primer_num.text())
        
        if len(self.ui.txt_segundo_num.text()) >0:
            ope2=int(self.ui.txt_segundo_num.text())

        multi=ope1*ope2
        
        self.ui.lbl_resultado.setText(str(multi)) 

    def dividir (self):
        division=0
        ope1=0
        ope2=0

        if len(self.ui.txt_primer_num.text()) > 0:
            ope1=int(self.ui.txt_primer_num.text())
        
        if len(self.ui.txt_segundo_num.text()) >0:
            ope2=int(self.ui.txt_segundo_num.text())

        division=ope1/ope2
        
        self.ui.lbl_resultado.setText(str(division)) 

if __name__ =='__main__':
    app=QApplication(sys.argv)
    dialog=CalculadoraApplication()
    dialog.show()
    
    sys.exit(app.exec_())