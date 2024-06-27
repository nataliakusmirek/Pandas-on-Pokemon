import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemon.csv")
df.head()
df.info()

## How many Pokemons exist with an Attack value greater than 150?
df.loc(df['Attack'] > 150).shape

## Select all pokemons with a Speed of 10 or less.
df.loc(df['Speed'] <= 10)

## How many Pokemons have a Sp. Def value of 25 or less?
df.loc(df['Sp. Def'] <= 25).shape

## Select all Legendary Pokemons
legendary_df = df.loc(df['Legendary'])

## Find the outlier
df.sort_values(by=['Defense'], ascending=True).head() # Using table plus matplotlib to see outliers...

## Advanced Selection

## How many fire-flying Pokemon are there?
(df['Type 1'] == 'Fire' & df['Type 2'] == 'Flying').sum()

## How many 'Poison' pokemon are across both types?

((df['Type 1'] == 'Poison') | (df['Type 2'] == 'Poison')).sum()

## What pokemon of Type 1 Ice has the strongest defense?
df.loc['Defense'].max() # Outputs 184
df.loc(
    (df['Type 1'] == 'Ice') &
    (df['Defense'] == 184)) # Found with max()

# easier way...
df.loc[df['Type 1'] == 'Ice'].sort_values('Defense', ascending=False).head()


## What is the most common type (mean) of Legendary Pokemon?
df.loc[df['Legendary'], 'type 1'].value_counts()

## What is the most powerful pokemon from the first 3 generations of type water?
df.loc[
    (df['Type 1'] == 'Water') &
    (df['Generation'].isin[1,2,3])
].sort_values(by='Total', ascending=False).head()

#NOTE: .isin lets you list the possible value to look at in a column

## What is the most powerful Dragon from the last two generations?
df.loc[
    ((df['Type 1'] == 'Dragon') | (df['Type 2'] == 'Dragon')) &
    (df['Generation'].isin[5,6])
].sort_values(by='Total', ascending=False).head()

df.query(
    "(`Type 1` == 'Dragon' or `Type 2` == 'Dragon') and Generation in [5,6]"
).sort_values(by='Total', ascending=False)


## Select most powerful Fire-Type pokemons.
powerful_fire_df = df.query("Attack > 100 and `Type 1` == 'Fire'")
powerful_fire_df

## Select all Water-type, Flying-type pokemons.
water_flying_df = df.query("`Type 1` == 'Water' and 'Type 2'' == 'Flying'")
water_flying_df

## Select specific columns (Name, Attack, and Generation) of Legendary pokemons of type Fire.
#df.loc [
    #(CONDITIONS FOR INDEX),
    #(COLUMNS)
#]


legendary_df = df.loc[
    (
        df['Type 1'] == 'Fire') & 
        df['Legendary'])
    ),
    ['Name', 'Attack', 'Generation']
]
legendary_df

## Select Slow (bottom 5%) and Fast (top 5%) pokemons.
bottom_5 = [df['Speed'].quantile(.05)
top_5 = [df['Speed'].quantile(.95)
         
slow_fast_df =
    df.loc[
        [df['Speed'] < bottom_5] |
        [df['Speed'] > top_5]
    ]
            
slow_fast_df
            
