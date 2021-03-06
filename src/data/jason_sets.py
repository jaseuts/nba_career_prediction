def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, path='../data/processed/'):
    """Save the different sets locally

    Parameters
    ----------
    X_train: Numpy Array
        Features for the training set
    y_train: Numpy Array
        Target for the training set
    X_val: Numpy Array
        Features for the validation set
    y_val: Numpy Array
        Target for the validation set
    X_test: Numpy Array
        Features for the testing set
    y_test: Numpy Array
        Target for the testing set
    test_id: Numpy Array
        The ID of instances in the testing set
    path : str
        Path to the folder where the sets will be saved (default: '../data/processed/')

    Returns
    -------
    """
    import numpy as np

    if X_train is not None:
      np.save(f'{path}train_scaled', X_train)
    if X_val is not None:
      np.save(f'{path}val_scaled',   X_val)
    if X_test is not None:
      np.save(f'{path}test_scaled',  X_test)
    if y_train is not None:
      np.save(f'{path}train_target', y_train)
    if y_val is not None:
      np.save(f'{path}val_target',   y_val)
    if y_test is not None:
      np.save(f'{path}test_target',  y_test)
    if test_id is not None:
      np.save(f'{path}test_id',  test_id)
      
        
def load_sets(path='../data/processed/', val=False):
    """Load the different locally save sets

    Parameters
    ----------
    path : str
        Path to the folder where the sets are saved (default: '../data/processed/')

    Returns
    -------
    Numpy Array
        Features for the training set
    Numpy Array
        Target for the training set
    Numpy Array
        Features for the validation set
    Numpy Array
        Target for the validation set
    Numpy Array
        Features for the testing set
    Numpy Array
        Target for the testing set
    Numpy Array
        Row Id for the testing set      
    """
    import numpy as np
    import os.path

    X_train = np.load(f'{path}train_scaled.npy') if os.path.isfile(f'{path}train_scaled.npy') else None
    X_val   = np.load(f'{path}val_scaled.npy'  ) if os.path.isfile(f'{path}val_scaled.npy')   else None
    X_test  = np.load(f'{path}test_scaled.npy' ) if os.path.isfile(f'{path}test_scaled.npy')  else None
    y_train = np.load(f'{path}train_target.npy') if os.path.isfile(f'{path}train_target.npy') else None
    y_val   = np.load(f'{path}val_target.npy'  ) if os.path.isfile(f'{path}val_target.npy')   else None
    y_test  = np.load(f'{path}test_target.npy' ) if os.path.isfile(f'{path}test_target.npy')  else None
    test_id = np.load(f'{path}test_id.npy') if os.path.isfile(f'{path}test_id.npy') else None
    
    return X_train, y_train, X_val, y_val, X_test, y_test, test_id

