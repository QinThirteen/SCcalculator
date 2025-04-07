import torch
import pandas
from dataset.jsload import *
from dataset.excel import *

def Nature_First_Load():
    NAME = None
    HP = 0
    ATK = 0
    DEF = 0
    SPD = 0
    CR = 0
    CD = 0
    BE = 0
    OHB = 0
    ME = 0
    ERA = 1
    EHA = 0
    ER = 0

def LoadData():
    Light_cones = load_data_for_excel("Light_cones.xlsx") #光锥
    print("光锥导入完成")
    relics = load_data_for_excel("relics.xlsx") #仪器
    print("仪器导入完成")
    characters = load_data_for_excel("characters.xlsx") #角色
    print("角色导入完成")
    return Light_cones,relics,characters