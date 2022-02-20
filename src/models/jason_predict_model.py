def save_prediction(model, X, Id, file_name, path='../references/'):
    """
    Use the fitted model to predict on new data and save the result

    Parameters
    ----------
    model: sk.learn model
        Fitted model to make prediction on new data
    X: Numpy Array
        features to make prediction from
    Id: Numpy Array
        The ID of each prediction in the result  

    Returns
    -------
    """
    import warnings
    import pandas as pd
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        probability = model.predict_proba(X)
    
    prediction = pd.DataFrame({'Id': Id, 
                           'TARGET_5Yrs': probability[:, 1]}) 
    prediction.to_csv(f'{path}{file_name}.csv', index=False)
    
    
