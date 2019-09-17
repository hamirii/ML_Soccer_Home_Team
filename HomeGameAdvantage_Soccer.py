import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import classification_report



# General function that isolates the full time result to see record of wins/losses/draws

def winRecords(data, leagueName):
    
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

print(winRecords(pd.read_csv("serieA_season-1516.csv"), 'SerieA_15_16'))
print(winRecords(pd.read_csv("serieA_season-1617.csv"), 'SerieA_16_17'))
print(winRecords(pd.read_csv("serieA_season-1819.csv"), 'SerieA_18_19'))
print(winRecords(pd.read_csv("epl_season-1819.csv"), 'EPL_18_19'))

# Let's start with the training/learning/evaluating/testing Machine Learning Method! Beginning with Serie A 2018/19 dataset

dataSerieA1819 = pd.read_csv("serieA_season-1819.csv")
dataSerieA1819 = dataSerieA1819.drop('Div', axis=1)
dataSerieA1819 = dataSerieA1819.drop('Date', axis=1)

# Change the string for Full Time Result (FTR), AKA the outcome to 0s and 1s. 1 if the Home Team wins, 0 if the Away Team won or if a Draw was achieved

dataSerieA1819['FTR'].unique()

def fix_outcome(outcome):
    if outcome == 'H':
        return 1
    else:
        return 0

dataSerieA1819['FTR'] = dataSerieA1819['FTR'].apply(fix_outcome)

# Train Test Split Data

x_data = dataSerieA1819.drop('FTR', axis=1)
y_labels = dataSerieA1819['FTR']
X_train, X_test, y_train, y_test = train_test_split(x_data, y_labels, test_size=0.3, random_state=101)


# Create tf.feature_columns for Categorical Values

HomeTeam = tf.feature_column.categorical_column_with_hash_bucket('HomeTeam', hash_bucket_size=1000)
AwayTeam = tf.feature_column.categorical_column_with_hash_bucket('AwayTeam', hash_bucket_size=1000)
HTR  = tf.feature_column.sequence_categorical_column_with_hash_bucket('HTR', hash_bucket_size=1000)  # Half Time Result

# Create tf.feature_columns for Numerical/Continuous Values

FTHG = tf.feature_column.numeric_column('FTHG') # Full Time Home Goals Scored
FTAG = tf.feature_column.numeric_column('FTAG') # Full Time Away Goals Scored
#FTR  = tf.feature_column.numeric_column('FTR')  # Full Time Result
HTHG = tf.feature_column.numeric_column('HTHG') # Half Time Home Goals Scored
HTAG = tf.feature_column.numeric_column('HTAG') # Half Time Away Goals Scored
HS   = tf.feature_column.numeric_column('HS')   # Home Shots
AS   = tf.feature_column.numeric_column('AS')   # Away Shots
HST  = tf.feature_column.numeric_column('HST')  # Home Shots on Target
AST  = tf.feature_column.numeric_column('AST')  # Away Shots on Target
HF  = tf.feature_column.numeric_column('HF')    # Home Fouls
AF  = tf.feature_column.numeric_column('AF')    # Away Fouls
HC  = tf.feature_column.numeric_column('HC')    # Home Corners
AC  = tf.feature_column.numeric_column('AC')    # Away Corners
HY  = tf.feature_column.numeric_column('HY')    # Home Yellow Cards
AY  = tf.feature_column.numeric_column('AY')    # Away Yellow Cards
HR  = tf.feature_column.numeric_column('HR')    # Home Red Cards
AR  = tf.feature_column.numeric_column('AR')    # Away Red Cards


# Compile into one features column
#feature_cols = [HomeTeam,AwayTeam,FTHG,FTAG,FTR,HTHG,HTAG,HTR,HS,AS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR]
feature_cols = [HomeTeam,AwayTeam,FTHG,FTAG,HTHG,HTAG,HTR,HS,AS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR]

# Building an input function

input_fnc = tf.estimator.inputs.pandas_input_fn(x=X_train, y=y_train, batch_size=100, num_epochs=None, shuffle=True)

# Using Linear Classifier to create a model with tf.Estimator

model = tf.estimator.LinearClassifier(feature_columns=feature_cols)

model.train(input_fn=input_fnc, steps=5000)

# Now to make 'predictions'

pred_fn = tf.estimator.inputs.pandas_input_fn(x=X_test, batch_size = len(X_test), shuffle=False)
predictions = list(model.predict(input_fn=input_fnc))

print(predictions[0])

final_preds= []
for pred in predictions:
    final_preds.append(pred['class_ids'][0])

print(final_preds[:10])

# Import Classification report from SkLearn-Metrics to evaluate the performance of the test model

print(classification_report(y_test, final_preds))