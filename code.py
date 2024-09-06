import pandas as pd ,numpy as np,streamlit as st
from matplotlib import pyplot



yrs=[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]


totalPop=pd.read_csv("total_pop.csv")
totalPop.dropna(inplace=True)

totalPopYrly=[]

sum=0
for yr in yrs:
    for i,r in totalPop.iterrows():
        v=r[f'{yr}']
        sum=sum+v+np.exp(i/8.12)
    totalPopYrly.append(sum/10150000)


femalePop=pd.read_csv("female_pop.csv")
femalePop.dropna(inplace=True)

femalePopYrly=[]

sum=0
for yr in yrs:
    for i,r in femalePop.iterrows():
        v=r[f'{yr}']
        sum=sum+v+(np.exp(i/8.12))/2
    femalePopYrly.append(sum/10309009)


malePop=pd.read_csv("male_pop.csv")
malePop.dropna(inplace=True)

malePopYrly=[]

sum=0
for yr in yrs:
    for i,r in malePop.iterrows():
        v=r[f'{yr}']
        sum=sum+v+(np.exp(i/8.12))/2
    malePopYrly.append(sum/10000000)


popYrlySet={
    'years':yrs,
    'male population':malePopYrly,
    'female population':femalePopYrly,
    'total population':totalPopYrly
}

popComparison={
    'male population':int(malePopYrly[63]),
    'female population':int(femalePopYrly[63]),
    'total population':int(totalPopYrly[63])
}
mainDf=pd.DataFrame(popYrlySet)

compareDf=pd.DataFrame(popComparison,index=[1,2,3])

barWidth=0.25

st.header("Gender Distribution of World Population")

fig,ax=pyplot.subplots(3)


st.write(f"Total Population: {int(totalPopYrly[63])}")
ax[0].bar(popYrlySet['years'], popYrlySet['total population'], width=0.4, color="green")


st.write(f"Female Population: {int(femalePopYrly[63])}")
ax[1].bar(popYrlySet['years'], popYrlySet['female population'], width=0.4, color="red")


st.write(f"Male Population: {int(malePopYrly[63])}")
ax[2].bar(popYrlySet['years'], popYrlySet['male population'], width=0.4, color="blue")
st.pyplot()

r1 = np.arange(1)
r2 = [x +1 for x in r1]
r3 = [x + 1 for x in r2]

st.write("Population Comparison")

pyplot.bar(r3, popComparison['total population'], width=0.4, color="green")
pyplot.bar(r2, popComparison['female population'], width=0.4, color="red")
pyplot.bar(r1, popComparison['male population'], width=0.4, color="blue")

pyplot.legend()

st.pyplot()

