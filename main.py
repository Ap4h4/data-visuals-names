from csv2df import Csv2Frame, saveToPDF
from plots import Plots, Map


"""Creating BAR PLOTS"""
#reading CSV file to panda DataFrames
c = Csv2Frame() #DataFrame create object

#Two files available: male and female names, only one can be active at once
#df = c.ReadCSV('imiona_żeńskie.csv')
df = c.ReadCSV('imiona_meskie.csv')

df, woj = c.CreateDF(df)
dfs = c.SetOfDataFrames(df, woj)
plot = Plots() #BarPlots object
plotBar = plot.bars(dfs)

"""Creating polish provinces map with top 1 name"""
#Reading JSON with polish provinces boundaries
pol_url = "https://raw.githubusercontent.com/deldersveld/topojson/master/countries/poland/poland-provinces.json"
#map instance
map = Map()
m = map.readMap(pol_url)
stats = c.DataFramesMax(dfs)
m_stats= c.MergingData(m, stats)
mapWithLabels = map.mapLabels(m_stats)

"""creating WORD CLOUD with names"""
#sorting and summing occurences of each name
dfSum = c.sumByName(df)
#creating word cloud for top 35 names
wc = plot.wc(dfSum.head(35))

"""creating PIE CHART with a percentage distribution"""
dfPie = c.percByName(df, 15)
pie = plot.pie(dfPie)

"""creating PDF RAPORT"""
s = saveToPDF()
s.saving(plotBar, wc, pie, mapWithLabels)



