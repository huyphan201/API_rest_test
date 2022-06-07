import pandas as pd

def DF(di):

    df = pd.DataFrame(di, columns=['names','urlscates','urlsnews']).drop_duplicates()
    print(df.head(5))

    df.info()


