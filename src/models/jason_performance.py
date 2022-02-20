def print_class_perf(y_preds, y_actuals, set_name=None, average='macro'):
    """Print the Accuracy and ROC AUC score for the provided data

    Parameters
    ----------
    y_preds : Numpy Array
        Predicted target
    y_actuals : Numpy Array
        Actual target
    set_name : str
        Name of the set to be printed
    average : str
        Parameter  for ROC AUC score averaging
    Returns
    -------
    """
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import roc_auc_score

    print(f"Accuracy {set_name}: {accuracy_score(y_actuals, y_preds)}")
    print(f"ROC AUC {set_name}: {roc_auc_score(y_actuals, y_preds, average=average)}")
