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








'''

The above is a much, much better way of handling this data - created a function called 'cleanData' that outputs what I'm interested in. 
This saves me having to create all these names for all these files, instead I can just write a few lines :)
I started out by doing this manually because I was learning as I went and wanted to carefully investigate the data


# English Premier League DATA for 2018-19 season, where VAR was not yet introduced.

dataEPL = pd.read_csv("epl_season-1819.csv")

FTR_EPL = dataEPL['FTR']

homeWinsEPL=0
awayWinsEPL=0
drawsEPL=0


for i in range(0, len(FTR_EPL.to_numpy())-1):
    
    if (FTR_EPL.to_numpy()[i] == 'H'):
        homeWinsEPL += 1
        #print(j)
    elif (FTR_EPL.to_numpy()[i] == 'A'):
        awayWinsEPL += 1
    else:
        drawsEPL +=1
    

# EPL Stats printed to console/terminal

print('')
print('English Premier League 2018-19 Season (Without VAR)')
print('')
print('        ', 'Home Wins:', homeWinsEPL, '; ', 'Away Wins:', awayWinsEPL, ';', 'Draws:', drawsEPL)




                                            # Serie A DATA for Season 15/16 two years before VAR was first introduced

dataSerieA15_16 = pd.read_csv("serieA_season-1516.csv")

FTR_SerieA15_16 = dataSerieA15_16['FTR']

homeWinsSerieA15_16=0
awayWinsSerieA15_16=0
drawsSerieA15_16=0


for i in range(0, len(FTR_SerieA15_16.to_numpy())-1):
    
    if (FTR_SerieA15_16.to_numpy()[i] == 'H'):
        homeWinsSerieA15_16 += 1
        #print(j)
    elif (FTR_SerieA15_16.to_numpy()[i] == 'A'):
        awayWinsSerieA15_16 += 1
    else:
        drawsSerieA15_16 +=1
    


# Serie A Stats printed to console/terminal
print('')
print('Serie A 2015-16 Season (without VAR)')
print('')
print('        ', 'Home Wins:', homeWinsSerieA15_16, '; ', 'Away Wins:', awayWinsSerieA15_16, ';', 'Draws:', drawsSerieA15_16)




                                            # SERIE A DATA for 2016-17 season, where VAR was not yet introduced.


dataSerieA16_17 = pd.read_csv("serieA_season-1617.csv")

FTR_SerieA16_17 = dataSerieA16_17['FTR']

homeWinsSerieA16_17=0
awayWinsSerieA16_17=0
drawsSerieA16_17=0


for i in range(0, len(FTR_SerieA16_17.to_numpy())-1):
    
    if (FTR_SerieA16_17.to_numpy()[i] == 'H'):
        homeWinsSerieA16_17 += 1
        #print(j)
    elif (FTR_SerieA16_17.to_numpy()[i] == 'A'):
        awayWinsSerieA16_17 += 1
    else:
        drawsSerieA16_17 +=1
    


# Serie A Stats printed to console/terminal
print('')
print('Serie A 2016-17 Season (without VAR)')
print('')
print('        ', 'Home Wins:', homeWinsSerieA16_17, '; ', 'Away Wins:', awayWinsSerieA16_17, ';', 'Draws:', drawsSerieA16_17)


                                            # Serie A DATA for Season 17/18 when VAR was first introduced

dataSerieA17_18 = pd.read_csv("serieA_season-1718.csv")

FTR_SerieA17_18 = dataSerieA17_18['FTR']

homeWinsSerieA17_18=0
awayWinsSerieA17_18=0
drawsSerieA17_18=0


for i in range(0, len(FTR_SerieA17_18.to_numpy())-1):
    
    if (FTR_SerieA17_18.to_numpy()[i] == 'H'):
        homeWinsSerieA17_18 += 1
        #print(j)
    elif (FTR_SerieA17_18.to_numpy()[i] == 'A'):
        awayWinsSerieA17_18 += 1
    else:
        drawsSerieA17_18 +=1
    


# Serie A Stats printed to console/terminal
print('')
print('Serie A 2017-18 Season (without VAR)')
print('')
print('        ', 'Home Wins:', homeWinsSerieA17_18, '; ', 'Away Wins:', awayWinsSerieA17_18, ';', 'Draws:', drawsSerieA17_18)



                                            # SERIE A DATA for 2018-19 season, where VAR was introduced.


dataSerieA = pd.read_csv("serieA_season-1819.csv")

FTR_SerieA = dataSerieA['FTR']

homeWinsSerieA=0
awayWinsSerieA=0
drawsSerieA=0


for i in range(0, len(FTR_SerieA.to_numpy())-1):
    
    if (FTR_SerieA.to_numpy()[i] == 'H'):
        homeWinsSerieA += 1
        #print(j)
    elif (FTR_SerieA.to_numpy()[i] == 'A'):
        awayWinsSerieA += 1
    else:
        drawsSerieA +=1
    


# Serie A Stats printed to console/terminal
print('')
print('Serie A 2018-19 Season (with VAR)')
print('')
print('        ', 'Home Wins:', homeWinsSerieA, '; ', 'Away Wins:', awayWinsSerieA, ';', 'Draws:', drawsSerieA)


#---------------------------------------------------------------------------------------------------------------------------------------

# Comparing the stats


print('')
print('')
print('EPL season 18/19 Ratio of Home Wins out of total games: ', homeWinsEPL / len(FTR_EPL))
print('SerieA season 15/16 Ratio of Home Wins out of total games: ', homeWinsSerieA15_16 / len(FTR_SerieA15_16))
print('SerieA season 16/17 Ratio of Home Wins out of total games: ', homeWinsSerieA16_17 / len(FTR_SerieA16_17))
print('Serie A season 17/18 Ratio of Home Wins out of total games: ', homeWinsSerieA17_18 / len(FTR_SerieA17_18))
print('SerieA season 18/19 Ratio of Home Wins out of total games: ', homeWinsSerieA / len(FTR_SerieA))

plt.plot(np.array([0, 1, 2, 3]), np.array([homeWinsSerieA15_16 / len(FTR_SerieA15_16), homeWinsSerieA16_17 / len(FTR_SerieA16_17), homeWinsSerieA17_18 / len(FTR_SerieA17_18), homeWinsSerieA / len(FTR_SerieA)]))
plt.show()


# Hmm... these are pretty inconclusive to be honest. Then again, it's tough because VAR has only been around for two seasons. And we're looking at 4 Serie A Seasons



'''



