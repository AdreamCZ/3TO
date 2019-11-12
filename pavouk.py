#from TKinter import *
from random import *


class Hrac():
    jmeno = ""
    vyher = 0
    proher = 0
    hraje = False
    def Hrac(_jmeno):
        jmeno = _jmeno



class Zapas():
    hrac1 = None
    hrac2 = None
    stul = 0
    hraje = False
    def Zapas(_hrac1,_hrac2):
        hrac1 = _hrac1
        hrac2 = _hrac2

def Hraci():
    vstup = input() # -> GUI
    hraci = []
    hracijm = vstup.split(',')
    for h in hracijm:
        hraci.append( Hrac(h))
    Pavouk(hraci)


def Pavouk(hraci):
    zapasy = []

    if(len(hraci)%2!= 0):
        hracnavic = hraci.pop(randint(len(hraci)-1))

    for i in range(hraci.count()/2):
        zapasy.append( Zapas(hraci[i],hraci[-(i+1)]))
        print(zapasy)

        
Hraci()
