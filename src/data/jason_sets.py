<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, path='../data/processed/'):
=======
def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, test_id=None, path='../data/processed/'):
>>>>>>> c97e6a1 (jason resolved problem of pull request and reinstated stashed works)
=======
def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, test_id=None, path='../data/processed/'):
=======
def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, path='../data/processed/'):
>>>>>>> 05a0cfad27e9f7a5e3860a6eb31fb96e94217304
>>>>>>> master
=======
def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, test_id=None, path='../data/processed/'):
=======
def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, path='../data/processed/'):
>>>>>>> 05a0cfad27e9f7a5e3860a6eb31fb96e94217304
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    test_id: Numpy Array
        The ID of instances in the testing set
>>>>>>> c97e6a1 (jason resolved problem of pull request and reinstated stashed works)
=======
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
    test_id: Numpy Array
        The ID of instances in the testing set
=======
>>>>>>> 05a0cfad27e9f7a5e3860a6eb31fb96e94217304
<<<<<<< HEAD
>>>>>>> master
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
    path : str
        Path to the folder where the sets will be saved (default: '../data/processed/')

    Returns
    -------
    """
    import numpy as np

    if X_train is not None:
      np.save(f'{path}X_train', X_train)
    if X_val is not None:
      np.save(f'{path}X_val',   X_val)
    if X_test is not None:
      np.save(f'{path}X_test',  X_test)
    if y_train is not None:
      np.save(f'{path}y_train', y_train)
    if y_val is not None:
      np.save(f'{path}y_val',   y_val)
    if y_test is not None:
      np.save(f'{path}y_test',  y_test)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
    if test_id is not None:
      np.save(f'{path}test_id',  test_id)
      
      
def load_sets(path='../data/processed/', val=False):
    """Load various locally saved sets
=======
<<<<<<< HEAD
>>>>>>> master
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
    
    

def load_sets(path='../data/processed/', val=False):
    """Load the different locally save sets
<<<<<<< HEAD
<<<<<<< HEAD
=======
    if test_id is not None:
      np.save(f'{path}test_id',  test_id)
      
      
def load_sets(path='../data/processed/', val=False):
    """Load various locally saved sets
>>>>>>> c97e6a1 (jason resolved problem of pull request and reinstated stashed works)
=======
>>>>>>> 05a0cfad27e9f7a5e3860a6eb31fb96e94217304
>>>>>>> master
=======
>>>>>>> 05a0cfad27e9f7a5e3860a6eb31fb96e94217304
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    Numpy Array
        Row Id for the testing set      
>>>>>>> c97e6a1 (jason resolved problem of pull request and reinstated stashed works)
=======
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
    Numpy Array
        Row Id for the testing set      
=======
>>>>>>> 05a0cfad27e9f7a5e3860a6eb31fb96e94217304
<<<<<<< HEAD
>>>>>>> master
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
    """
    import numpy as np
    import os.path

    X_train = np.load(f'{path}X_train.npy') if os.path.isfile(f'{path}X_train.npy') else None
    X_val   = np.load(f'{path}X_val.npy'  ) if os.path.isfile(f'{path}X_val.npy')   else None
    X_test  = np.load(f'{path}X_test.npy' ) if os.path.isfile(f'{path}X_test.npy')  else None
    y_train = np.load(f'{path}y_train.npy') if os.path.isfile(f'{path}y_train.npy') else None
    y_val   = np.load(f'{path}y_val.npy'  ) if os.path.isfile(f'{path}y_val.npy')   else None
    y_test  = np.load(f'{path}y_test.npy' ) if os.path.isfile(f'{path}y_test.npy')  else None
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    
    return X_train, y_train, X_val, y_val, X_test, y_test
=======
    test_id = np.load(f'{path}test_id.npy') if os.path.isfile(f'{path}test_id.npy') else None
    
    return X_train, y_train, X_val, y_val, X_test, y_test, test_id

>>>>>>> c97e6a1 (jason resolved problem of pull request and reinstated stashed works)
=======
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
    test_id = np.load(f'{path}test_id.npy') if os.path.isfile(f'{path}test_id.npy') else None
    
    return X_train, y_train, X_val, y_val, X_test, y_test, test_id

=======
    
    return X_train, y_train, X_val, y_val, X_test, y_test
>>>>>>> 05a0cfad27e9f7a5e3860a6eb31fb96e94217304
<<<<<<< HEAD
>>>>>>> master
=======
>>>>>>> b286286b282d5d6595fcdb80ddccf6658227e1f6
