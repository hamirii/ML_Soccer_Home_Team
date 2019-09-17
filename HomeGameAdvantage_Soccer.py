import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# General function that creates the necessary files

def cleanData(data, leagueName):
    
    ftr = data['FTR']

    homeWins=0
    awayWins=0
    draws=0
    
    for i in range(0, len(ftr.to_numpy())-1):
    
        if (ftr.to_numpy()[i] == 'H'):
            homeWins += 1
            #print(j)
        elif (ftr.to_numpy()[i] == 'A'):
            awayWins += 1
        else:
            draws +=1

    return leagueName, 'HomeWins: %s' % homeWins, 'Away Wins: %s' % awayWins, 'Draws: %s' % draws

print(cleanData(pd.read_csv("serieA_season-1516.csv"), 'SerieA_15_16'))
print(cleanData(pd.read_csv("serieA_season-1617.csv"), 'SerieA_16_17'))
print(cleanData(pd.read_csv("serieA_season-1819.csv"), 'SerieA_18_19'))
print(cleanData(pd.read_csv("epl_season-1819.csv"), 'EPL_18_19'))





