#import necessary libraries
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

#returns the gaussian(mean, var) pdf values list of integers in [mini,maxi]
def genGaussian(mean,var,mini,maxi):
    data = list(range(mini,maxi+1))
    return [(np.exp((((x-mean)**2)/var)*(-1/2)))*(1/(2*np.pi*var)**(1/2)) for x in data]

#returns the random data stored at file being pointed by fpointer as a numpy array
def cleanCSVreader(fpointer,data):
    reader = csv.reader(fpointer)
    count = 1
    for row in reader:
        if(count==1):
            count+=1
            continue
        if(row[0]=='\x00'):
            continue
        row[0] = "".join(row[0].split('\x00')[1:-1])
        data = np.append(data,int(row[0]))
    return data

(f_name1,f_name2) = sys.argv[1:]

data1 = np.array([],dtype=int)
data2 = np.array([],dtype=int)

with open(f_name1,"r") as randV:
    data1 = cleanCSVreader(randV,data1)
    randV.close()
with open(f_name2,"r") as randV2:
    data2 = cleanCSVreader(randV2,data2)
    randV2.close()

(n1, n2) = (len(data1), len(data2))
print(f'm{n1}={np.mean(data1)}, var{n1}={np.var(data1)}')
print(f'm{n2}={np.mean(data2)}, var{n2}={np.var(data2)}')

# fig,ax = plt.subplots(1,2)
# ax[0].plot(list(range(np.min(data1),np.max(data1)+1)),[22500*x for x in genGaussian(np.mean(data1), np.var(data1),np.min(data1),np.max(data1))])
# ax[0].hist(data1)
# ax[1].plot(list(range(np.min(data2),np.max(data2)+1)),[100000*x for x in genGaussian(np.mean(data2), np.var(data2),np.min(data2),np.max(data2))])
# ax[1].hist(data2)
fig, ax = plt.subplots(2,2)
ax[0,0].plot(list(range(np.min(data1),np.max(data1)+1)),[22500*x for x in genGaussian(np.mean(data1), np.var(data1),np.min(data1),np.max(data1))])
ax[1,0].hist(data1)
ax[0,1].plot(list(range(np.min(data2),np.max(data2)+1)),[100000*x for x in genGaussian(np.mean(data2), np.var(data2),np.min(data2),np.max(data2))])
ax[1,1].hist(data2)
plt.show()

