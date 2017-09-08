## this file includes a set of function to create embeddings of time series..

import pandas as pd

def embed_ts(inseries,dimension,colnames=None):

    ## apply 0 index correction
    dimension+=1
    
    ## take a time series and craete a new pandas dataframe
    ## up to n dimensions    
    if colnames == None:
        colnames = ["embedding_"+str(step) for step in range(0,dimension)]
    finalFrame = pd.DataFrame(columns=colnames)
    tmpFrame = inseries.iloc[dimension:]

    for j in tmpFrame.index.tolist():
        embedding = []
        for tau in range(0,dimension):
            embedding.append(inseries.iloc[j-tau])
        data = dict(zip(colnames,embedding))
        finalFrame = finalFrame.append(data,ignore_index=True)
    
    return finalFrame



if __name__ == '__main__':

    import random

    series = random.sample(range(1, 10000), 1000)
    timeSeries = pd.Series(series)
    dimension = 10    

    ## embed
    embedded_ts = embed_ts(timeSeries,dimension)
    
    print(embedded_ts.head())
