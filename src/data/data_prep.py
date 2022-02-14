def clean_train(df):
    """
    Method returning a cleaned version of the train data 
    that is split into features and target

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
        
    Returns
    -------
    pd.DataFrame
        Pandas dataframe of features
    pd.Series
        Pandas series of target
	"""
    import pandas as pd
	
    df_cleaned = df.copy()
    df_cleaned.drop('Id', axis=1, inplace=True)
    df_cleaned.columns = df_cleaned.columns.str.replace(' ', '_')
    target = df_cleaned.pop('TARGET_5Yrs')
    return df_cleaned, target
    
     
def clean_test(df): 
    """
    Method returning a cleaned version of the test data
    that is split into features and Id

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
        
    Returns
    -------
    pd.DataFrame
        Pandas dataframe of features
    pd.Series
        Pandas series of target    
    """
    import pandas as pd
	
    df_cleaned = df.copy()
    Id = df_cleaned.pop('Id')
    df_cleaned.columns = df_cleaned.columns.str.replace(' ', '_')
    return df_cleaned, Id
    
