import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#removing accents (diakretyczne znaki)
import unidecode
#for saving multiple outputs into one PDF
from matplotlib.backends.backend_pdf import PdfPages

class Csv2Frame:
    file = str()
    def ReadCSV(self, file):
        data = pd.read_csv(file)
        return data
    def CreateDF(self, csv):
        df = pd.DataFrame(csv, columns=['WOJ','WOJEWÓDZTWO', 'IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ'])
        woj = df['WOJ'].unique()
        return df, woj

    def ConditionMax(self, df, arg):
        a = arg
        df2 = df.query('WOJ == @a')
        df = df2.head(5)
        return df

    def SetOfDataFrames(self, df, arr):
        dfs = {}
        for i in arr:
            dfs[i] = self.ConditionMax(df, i)
        return  dfs

    def DataFramesMax(self, data):
        df_max = pd.DataFrame(columns=['WOJEWÓDZTWO', 'IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ'])
        for key in data:
            tmpDF = data[key]
            tmpDict = tmpDF[['WOJEWÓDZTWO', 'IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ']].head(1)
            df_max = df_max.append(tmpDict, ignore_index=True)
        #removing rows with NaN value
        df_max = df_max.dropna(subset=['WOJEWÓDZTWO'])
        return df_max

    def MergingData(self, geodata, stats):
        newDict = {}
        amountWoj = [x+1 for x in range(16)]
        #taking max from each data frame of stats
        #decoding and lowercasing for later merging

        geodata['VARNAME_1'] = geodata['VARNAME_1'].apply(unidecode.unidecode)
        geodata['VARNAME_1'] = geodata['VARNAME_1'].str.lower()
        stats['WOJEWÓDZTWO'] = stats['WOJEWÓDZTWO'].apply(unidecode.unidecode)
        stats['WOJEWÓDZTWO'] = stats['WOJEWÓDZTWO'].str.lower()
        merged = geodata.merge(stats, how='left', left_on='VARNAME_1', right_on='WOJEWÓDZTWO')
        """for i in amountWoj:
            tmp = geodata.query('ID_1 == @i')
            if not tmp.empty:
               #st = str(tmp['VARNAME_1'][1])
               print(tmp['VARNAME_1'][1])"""
        #normalized = unidecode.unidecode(stats)
        return merged

    def sumByName(self, df):
        tmp = df.groupby(['IMIĘ_PIERWSZE'], as_index=False).sum()
        tmp2 = tmp[['IMIĘ_PIERWSZE','LICZBA_WYSTĄPIEŃ']].sort_values(by=['LICZBA_WYSTĄPIEŃ'], ascending=False)
        return tmp2

    def percByName(self, df, top):
        dfSum = self.sumByName(df)
        #changing columns names
        tmpDf = dfSum.rename(columns={'IMIĘ_PIERWSZE':'name','LICZBA_WYSTĄPIEŃ':'occurences'})
        #calculating sum of all occurences
        overallSum = tmpDf['occurences'].sum()
        #new blank column, iterrating over each row and assigning
        tmpDf['perc'] = ''
        for index, row in tmpDf.iterrows():
            tmpDf.loc[index, 'perc'] = ((row['occurences'] / overallSum) * 100)
        #creating last row with rest values
        tmpDf = tmpDf.head(top)
        restPerc = 100 - tmpDf['perc'].sum()
        rest = overallSum - tmpDf['occurences'].sum()
        restRow = {'name':'pozostałe imiona', 'occurences': rest, 'perc':restPerc}
        tmpDf = tmpDf.append(restRow, ignore_index=True)
        # changing index column for pie chart
        tmpDf = tmpDf.set_index('name')
        return tmpDf

class saveToPDF:
    def saving(self, *args):
        fileName = input("Podaj nazwe pliku: ")
        fileName = fileName + '.pdf'
        with PdfPages(fileName) as pdf:
            for arg in args:
                pdf.savefig(arg)
                plt.close()



