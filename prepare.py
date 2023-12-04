import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def prep_iris(df):
    """
    This functions will clean up the df by dropping unnecessary columns
    """
    df = df.drop(columns=['species_id','measurement_id'])
    df = df.rename(columns={"species_name":'species'})
    
    return df

def clean_titanic(df): 
    """
    This function will  drop unnecessary columns and assign the pclass column as an object 
    rather than an INT because we want it to be a categorical value
    """
    
    df = df.drop(columns=['embarked', 'deck', 'class'])
    
    df = df.dropna()

    #changing it into a string so its categorical
    df.pclass = df.pclass.astype(object)
    
    #filled all nas with the mode 
    df.embark_town = df.embark_town.fillna('Southampton')
    
    return df

def split_titanic(df):
    '''
    Does the process of splitting the titanic dataframe, setting the train
    size and stratifying it. Does this twice 'first split' and 'second split'.
    '''
    #first split
    train, validate_test = train_test_split(df, #send in intitial df
                train_size=0.60, 
                random_state = 123, 
                stratify=df.survived 
                )
    
    #second split
    validate, test = train_test_split(validate_test, 
                test_size=0.50, 
                random_state=123, 
                stratify=validate_test.survived 
                )
    return train, validate, test


def clean_and_split_titanic_data(df):
    '''
    this will clean and split the titanic df
    '''
    
    
    df = clean_titanic(df)
    
    
    train, validate, test = split_titanic(df)
    
    return train, validate, test

def prep_telco(df):
    '''
    Drops columns and will also replace empty space values with 0.0 
    so it can have a value
    '''
    df = df.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    
    
    return df

def splitting_data(df, col, seed=123):
    '''
    Splits a DataFrame into training, validation, and test sets using a two-step process.
    '''

    #first split
    train, validate_test = train_test_split(df,
                     train_size=0.6,
                     random_state=seed,
                     stratify=df[col]
                    )
    
    #second split
    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=seed,
                                      stratify=validate_test[col]
                        
                                     )
    return train, validate, test