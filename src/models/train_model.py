def classification_model(model, X, y):
    """
    Fit a classification model using cross validation of stratified data.
    The model's performance is measured by the AUC score

    Parameters
    ----------
    model: sk.learn model
        Model to fit the training data
    X: Numpy Array
        features to train the model
    y: Numpy Array
        target to train the model    

    Returns
    -------
    The average score of the cross validation models
    """
    from sklearn.model_selection import StratifiedKFold
    from sklearn.model_selection import cross_val_score

    kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=2)
    scores = cross_val_score(model, X, y, scoring='roc_auc', cv=kfold)
    return scores.mean()
    
 
