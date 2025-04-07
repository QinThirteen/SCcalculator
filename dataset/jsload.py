import json
import pandas as pd
def Load_json():
    with open("data.json") as file:
        data = json.load(file)

    light_cones = pd.DataFrame(data["light_cones"])
    relics = pd.DataFrame(data["relics"])
    characters = pd.DataFrame(data["characters"])

    print(light_cones)
    print(relics)
    print(characters)
    
    return(light_cones,relics,characters)