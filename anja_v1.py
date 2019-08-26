#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:41:17 2019

@author: anjastene
"""

#==============================================================================
# Import modules
#==============================================================================
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import pandas as pd
import seaborn as sns

#==============================================================================
# Prepro. data
#==============================================================================

#import dataset into pandas dataframe, handle encoding problem
data = pd.read_csv("crime.csv", encoding = "ISO-8859-1", low_memory=False)


colnames=data.columns
nullvalues=data.isnull().sum()

print(data['STREET'].unique())

#Highest number of incidents for a particular crime occured in each year
topnum=data.groupby(['OFFENSE_CODE_GROUP','YEAR']).size().reset_index(name='count').sort_values(by=['count'], ascending=False)


#-------
mydata=data[:100][:100]
#values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
hmydata=mydata.fillna(0)

import numpy as np
import matplotlib.cm as cm
from matplotlib.pyplot import figure, show, rc


whatsthis=np.arange(0.0, 2*np.pi, 2*np.pi/20)
plotdis= data.groupby('OFFENSE_CODE_GROUP')['INCIDENT_NUMBER'].count()
#toplot=plotdis:[1]
#==============================================================================
# Data Visualization
#==============================================================================

# District wise crimes
plt.figure(figsize=(16,8))
data['DISTRICT'].value_counts().plot.bar()
plt.title('BOSTON: District wise Crimes')
plt.ylabel('Number of Crimes')
plt.xlabel('Police District')
plt.show()
# Maxium number of Crimes observed in Police District B2 in Boston.


# District wise crimes For individual years: 2018
plt.figure(figsize=(16,8))
data['DISTRICT'].loc[data['YEAR']==2018].value_counts().plot.bar()
plt.title('BOSTON: Police District Wise Crimes in 2018')
plt.show()
# Maxium number of Crimes observed in Police District B2 in Boston.

#  Offence Code Group (All offences)
plt.figure(figsize=(16,8))
data['OFFENSE_CODE_GROUP'].value_counts().plot.bar()
plt.title('BOSTON: Crime Offence Code Groups')
plt.show()
# Motor Vehicle Accident Response tops in the list.

# Number of Crimes reported in Boston Each Year
plt.figure(figsize=(16,8))
sns.countplot(x='YEAR', data = data)
plt.ylabel('Number of Crimes')
plt.title('BOSTON: Year wise # of Crimes Reported')
plt.show()
# Maxium number of Crimes is observed in 2017


# Top 10

# Top 10 Crime District Locations
plt.figure(figsize=(16,8))
top10cloc = data.groupby('DISTRICT')['INCIDENT_NUMBER'].count().sort_values(ascending=False)
top10cloc = top10cloc [:10]
top10cloc.plot(kind='bar', color='green')
plt.ylabel('Number of Crimes')
plt.xlabel("POLICE DISTRICTS")
plt.title('BOSTON: Top 10 Crime District Locatins')
plt.show()
# Maxium number of Crimes observed in Police District B2 in Boston.


# Top 10 Types of Crime
plt.figure(figsize=(16,8))
top10ctype = data.groupby('OFFENSE_CODE_GROUP')['INCIDENT_NUMBER'].count().sort_values(ascending=False)
top10ctype = top10ctype [:10]
top10ctype.plot(kind='bar', color='blue')
plt.ylabel('Number of Crimes')
plt.title('BOSTON: Top 10 Types of Crime')
plt.show()
# Motor Vehicle Accident Response tops in the list.



# When do serious crimes occur?
#We can consider patterns across several different time scales: hours of the day, days of the week, and months of the year.

# Number of Crimes reported at Hour during the Day
plt.figure(figsize=(16,8))
sns.countplot(x='HOUR', data = data)
plt.ylabel('Number of Crimes')
plt.title('BOSTON: Hour wise # of Crimes Reported')
#plt.savefig("C:\\Users\\bk42969\\Desktop\\BigData\\CrimeHourDuringTheDay.png")
plt.show()
# Crimes are observed Least in the Early Hours of the Morning. 


# Comparing crimes during months.
plt.figure(figsize=(16,8))
data.groupby(['MONTH'])['INCIDENT_NUMBER'].count().plot(kind = 'bar')
plt.ylabel('Number of Crimes')
plt.title('BOSTON: Month wise Crimes')
#plt.savefig("C:\\Users\\bk42969\\Desktop\\BigData\\CrimeDuringTheMonth.png")
plt.show()
# Maximum number of Crimes observed in July, Aug & Sep Months.


# Top 10 locations of Crime (streetwise)
plt.figure(figsize=(16,8))
top10loc = data.groupby('STREET')['INCIDENT_NUMBER'].count().sort_values(ascending=False)
top10loc = top10loc [:10]
top10loc.plot(kind='bar', color='blue')
plt.ylabel('Number of Crimes')
plt.title('BOSTON: Top 10 locations of Crime')
plt.show()

##Can delete this
##for testing only (seaborn)
#plt.figure(figsize=(16,8))
#sns.countplot(x='index', data = top10loc)
#plt.ylabel('Number of Crimes')
#plt.title('snstest')
##plt.savefig("C://Users/anjastene/gitrepos//CrimeHourDuringTheDay.png")
#plt.show()




