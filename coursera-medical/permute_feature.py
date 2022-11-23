# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
def permute_feature(df, feature):
    """
    Given dataset, returns version with the values of
    the given feature randomly permuted. 

    Args:
        df (dataframe): The dataset, shape (num subjects, num features)
        feature (string): Name of feature to permute
    Returns:
        permuted_df (dataframe): Exactly the same as df except the values
                                of the given feature are randomly permuted.
    """
    permuted_df = df.copy(deep=True) # Make copy so we don't change original df
    
    #print("df.head=",df.head())
    #print("feature=",feature)

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###

    # Permute the values of the column 'feature'
    #permuted_features = None
    #permuted_features =  np.random.permutation(df[:, feature])
    permuted_features =  np.random.permutation(df[feature])
    
    # Set the column 'feature' to its permuted values.
    #permuted_df[feature] = None
    permuted_df[feature] = permuted_features
    
    ### END CODE HERE ###

    return permuted_df