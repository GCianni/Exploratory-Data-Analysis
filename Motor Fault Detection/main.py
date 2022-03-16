import time
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()
    df = pd.read_csv('C:\\Git\\Motor Fault Detection\\Teste_Data\\saved_csv\\Feature_DataFrame.csv', index_col=0)
    print(df.var())

#get correlations of each features in dataset
    corrmat = df.corr()
    print(corrmat.loc[abs(corrmat['Target']) < 0.2].index.values)
    print(corrmat.loc[abs(corrmat['Target']) < 0.2])
    newdf = df[corrmat.loc[abs(corrmat['Target']) < 0.2].index.values]
    newdf.to_csv('C:\\Git\\Motor Fault Detection\\Teste_Data\\saved_csv\\Feature_Sel_X.csv')
    df['Target'].to_csv('C:\\Git\\Motor Fault Detection\\Teste_Data\\saved_csv\\Feature_Sel_Y.csv')



    #print(corrmat['Target'][corrmat['Target']<0.2)
    #print(top_corr_features)
    #figure(figsize=(20,20))
    #plt.plot(df['Kurtosis Acc_Outer_Y'])
    #plt.plot(df['Kurtosis Acc_Outer_Z'])
    #plt.plot(df['Kurtosis Acc_Outer_X'])

    #plot heat map

    #g=sns.heatmap(df[top_corr_features].corr(), annot=False, cmap="RdYlGn")

   # plt.show()
