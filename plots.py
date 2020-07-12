import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from wordcloud import WordCloud

class Plots:
    #creating subplot for one province
    def subplot(self, df, column3, column1, column2,axes,r,c):
        title = df.iloc[1][column3]
        graph = df[[column1, column2]].plot(kind='bar', x=column1, y=column2, title=title, ax=axes[r,c], figsize=(15,10), legend=False, rot=30)
        graph.set_xlabel("")
    #creating figure with subplots for each province
    def bars(self,dfs):
        fig, axes = plt.subplots(nrows=4, ncols=4)
        fig.suptitle('Top 5 imion nadawanych dzieciom w Polsce w 2019r. wg województw', fontsize=16)
        w=2
        for r in range(0, 4, 1):
            for c in range(0, 4, 1):
                self.subplot(dfs[w], 'WOJEWÓDZTWO', 'IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ', axes, r, c)
                w = w + 2
        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        return fig

    #creating pie chart
    def pie(self,df):
        f, ax = plt.subplots(1,1)
        df.plot.pie(y='perc', figsize=(10, 10), autopct='%1.1f%%', legend=False, ax=ax)
        f.suptitle('Diagram kołowy z udziałem procentowym imion nadawanym dzieciom w 2019r', fontsize=16)
        plt.rcParams['font.size'] = 10
        plt.axis('off')
        return f

    #creating word cloud distribution
    def wc(self, df):
        wc = WordCloud(background_color="white")
        tmpDict = {}
        for name, sum in df.values:
            tmpDict[name] = sum
        wc.generate_from_frequencies(frequencies=tmpDict)
        fig = plt.figure()
        fig.suptitle('Chmura top35 imion nadawanych dzieciom w 2019r.', fontsize=16)
        ax = fig.add_subplot()
        ax.imshow(wc, interpolation="bilinear")
        ax.axis('off')
        return fig

class Map:
    #calling geopandas read_file method
    def readMap(self, data):
        data_read = gpd.read_file(data)
        return data_read
    #creating figure with boundary map with top1 name for each province
    def mapLabels(self, geodata):
        f,ax = plt.subplots(1,1)
        f.suptitle('Najczęściej nadawane imię w województwie w 2019r.', fontsize=16)
        geodata.boundary.plot(ax=ax)
        ax.set_axis_off()
        geodata.apply(lambda x: ax.annotate(s=x['IMIĘ_PIERWSZE'], xy=x.geometry.centroid.coords[0], ha='center'),axis=1)
        return f

