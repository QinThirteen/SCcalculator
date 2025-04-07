#from dataset.jsload import *

def Nature_Load(name):
    NAME = None
    HP = 0
    ATK = 0
    DEF = 0
    SPD = 1
    CR = 0
    CD = 0
    BE = 0
    OHB = 0
    ME = 0
    ERA = 1
    EHA = 0
    ER = 0
    return(NAME,HP,ATK,DEF,SPD,CR,CD,BE,OHB,ME,ERA,EHA,ER)

def run_line(name):
    SPD = Nature_Load(name)[4]
    path = 10000
    run_point = path / SPD
    print(run_point)

run_line("1")