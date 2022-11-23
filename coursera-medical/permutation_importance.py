# UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
def permutation_importance(X, y, model, metric, num_samples = 100):
    """
    Compute permutation importance for each feature.

    Args:
        X (dataframe): Dataframe for test data, shape (num subject, num features)
        y (np.array): Labels for each row of X, shape (num subjects,)
        model (object): Model to compute importances for, guaranteed to have
                        a 'predict_proba' method to compute probabilistic 
                        predictions given input
        metric (function): Metric to be used for feature importance. Takes in ground
                           truth and predictions as the only two arguments
        num_samples (int): Number of samples to average over when computing change in
                           performance for each feature
    Returns:
        importances (dataframe): Dataframe containing feature importance for each
                                 column of df with shape (1, num_features)
    """

    importances = pd.DataFrame(index = ['importance'], columns = X.columns)
    
    # Get baseline performance (note, you'll use this metric function again later)
    baseline_performance = metric(y, model.predict_proba(X)[:, 1])

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    num_subject = X.shape[0]
    num_feature = X.shape[1]
    #print("X.shape() ",num_subject, ", ",num_feature)
    # Iterate over features (the columns in the importances dataframe)
    #for feature in None: # complete this line
    #for feature in range(X.shape[1]): # complete this line
    for feature in importances.columns: # complete this line
        
        # Compute 'num_sample' performances by permutating that feature
        
        # You'll see how the model performs when the feature is permuted
        # You'll do this num_samples number of times, and save the performance each time
        # To store the feature performance,
        # create a numpy array of size num_samples, initialized to all zeros
        #feature_performance_arr = None
        feature_performance_arr = [0] * num_samples
        
        # Loop through each sample
        #for i in None: # complete this line
        for i in range(num_samples): # complete this line
            
            # permute the column of dataframe X
            #perm_X = None
            perm_X = permute_feature(X, feature)
            # calculate the performance with the permuted data
            # Use the same metric function that was used earlier
            #feature_performance_arr[i] = None
            feature_performance_arr[i] = metric(y, model.predict_proba(perm_X)[:, 1])
    
    
        # Compute importance: absolute difference between 
        # the baseline performance and the average across the feature performance
        #importances[feature]['importance'] = None
        importances[feature]['importance'] = np.abs(baseline_performance - np.mean(feature_performance_arr))
        
    ### END CODE HERE ###

    return importances