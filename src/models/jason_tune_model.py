def searchCV(model, params, X, y, kfold=None, random=False):
    """
    Tuning the model by sequently or randomly search the set of supplied
    values to find the best combination of the model's hyperparameters

    Parameters
    ----------
    model: sk.learn model
        Model to fit the training data
    params: Dictionary
        sets of hyperparameters and their values
    X: Numpy Array
        features to train the model 
    y: Numpy Array
        target to train the model 
    kfold:  
        int or cross-validation generator
    random: Boolean
        toggle between Grid Search or Random Search

    Returns
    -------
    """
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
    if random:
	    search = RandomizedSearchCV(model, params, cv=kfold, n_iter=20, scoring='roc_auc', n_jobs=-1, random_state=2)
    else:
	    search = GridSearchCV(model, params, cv=kfold, scoring='roc_auc', n_jobs=-1)	
    search.fit(X, y)
    best_params = search.best_params_
    print("Best params:", best_params)
    best_score = search.best_score_
    print("Training AUC score: {:.3f}".format(best_score))
