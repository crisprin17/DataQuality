%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import csv
import random
from collections import Counter
plt.style.use('classic')
%matplotlib inline

with open('/Users/cristiana/Desktop/UpMu_dq/livetimeListNIGHT.txt','r',encoding='utf8') as txtfile:
    subtime = []
    runPlus = []
    runMinus= []
    for row in csv.reader(txtfile, delimiter = ' '):
        subtime.append(int(row[4]))
        if (int(row[4])>185):
            runPlus.append(int(row[0]))
        else:
            runMinus.append(int(row[0]))
 # Plot Distribution of Subrun length           
max_value = max(subtime)
min_value = min(subtime)
ax = plt.axes()
plt.xlabel("time range (s)")
plt.ylabel("Entries")
plt.title("Distribution of Subrun length")
plt.hist(subtime,range(min_value,240))
ax.xaxis.set_major_locator(plt.MaxNLocator())
plt.show()

#Plot Distribution of Run for subrun length > 185 s
max_valueP = max(runPlus)
min_valueP = min(runPlus)
ax = plt.axes()
plt.xlabel("Run")
plt.ylabel("Entries")
plt.title("Distribution of Run for subrun length > 185 s")
plt.hist(runPlus,range(min_valueP,max_valueP))
ax.xaxis.set_major_locator(plt.MaxNLocator())
plt.show()
#Distribution of Run for subrun length < 185 s
max_valueM = max(runMinus)
min_valueM = min(runMinus)
ax = plt.axes()
plt.xlabel("Run")
plt.ylabel("Entries")
plt.title("Distribution of Run for subrun length < 185 s")
plt.hist(runMinus,range(min_valueM,max_valueM))
ax.xaxis.set_major_locator(plt.MaxNLocator())
plt.show()
