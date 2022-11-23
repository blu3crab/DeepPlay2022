def treatment_dataset_split(X_train, y_train, X_val, y_val):
    """
    Separate treated and control individuals in training
    and testing sets. Remember that returned
    datasets should NOT contain the 'TRTMT' column!

    Args:
        X_train (dataframe): dataframe for subject in training set
        y_train (np.array): outcomes for each individual in X_train
        X_val (dataframe): dataframe for subjects in validation set
        y_val (np.array): outcomes for each individual in X_val
    
    Returns:
        X_treat_train (df): training set for treated subjects
        y_treat_train (np.array): labels for X_treat_train
        X_treat_val (df): validation set for treated subjects
        y_treat_val (np.array): labels for X_treat_val
        X_control_train (df): training set for control subjects
        y_control_train (np.array): labels for X_control_train
        X_control_val (np.array): validation set for control subjects
        y_control_val (np.array): labels for X_control_val
    """
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # From the training set, get features of patients who received treatment
    #X_treat_train = None
    X_treat_train = X_train[X_train.TRTMT==True]
    
    # drop the 'TRTMT' column
    #X_treat_train = None
    X_treat_train = X_treat_train.drop(columns='TRTMT')
    
    # From the training set, get the labels of patients who received treatment
    #y_treat_train = None
    y_treat_train = y_train[X_train.TRTMT==True]

    # From the validation set, get the features of patients who received treatment
    #X_treat_val = None
    X_treat_val = X_val[X_val.TRTMT==True]
                        
    # Drop the 'TRTMT' column
    #X_treat_val = None
    X_treat_val = X_treat_val.drop(columns='TRTMT')
                        
    # From the validation set, get the labels of patients who received treatment
    #y_treat_val = None
    y_treat_val = y_val[X_val.TRTMT==True]
                        
# --------------------------------------------------------------------------------------------
                        
    # From the training set, get the features of patients who did not received treatment
    #X_control_train = None
    X_control_train = X_train[X_train.TRTMT==False]
                        
    # Drop the TRTMT column
    #X_control_train = None
    X_control_train = X_control_train.drop(columns='TRTMT')
                        
    # From the training set, get the labels of patients who did not receive treatment
    #y_control_train = None
    y_control_train = y_train[X_train.TRTMT==False]
    
    # From the validation set, get the features of patients who did not receive treatment
    #X_control_val = None
    X_control_val = X_val[X_val.TRTMT==False]
    
    # drop the 'TRTMT' column
    #X_control_val = None
    X_control_val = X_control_val.drop(columns='TRTMT')

    # From the validation set, get teh labels of patients who did not receive treatment
    #y_control_val = None
    y_control_val = y_val[X_val.TRTMT==True]
    
    ### END CODE HERE ###

    return (X_treat_train, y_treat_train,
            X_treat_val, y_treat_val,
            X_control_train, y_control_train,
            X_control_val, y_control_val)