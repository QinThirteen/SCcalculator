import torch
import pandas
from dataset.jsload import *
from dataset.excel import *

def LoadData():
    Light_cones = load_data_for_excel("Light_cones.xlsx") #光锥
    print("光锥导入完成")
    relics = load_data_for_excel("relics.xlsx") #仪器
    print("仪器导入完成")
    characters = load_data_for_excel("characters.xlsx") #角色
    print("角色导入完成")
    return Light_cones,relics,characters