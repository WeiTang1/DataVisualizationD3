import csv,numpy
from matplotlib import pyplot
from sklearn import cluster
# pre define data entry index
RESTAURANT_ID = 0
RESTAURANT_NAME = 1
BORO = 2
BUILDING_ID =3
STREET = 4
ZIP_CODE=5
PHONE = 6
CUISINE = 7
INSPECT_DATE = 8
ACTION = 9
VIOLATION = 10
VIOLATION_DESCP = 11
CRITICAL = 12
SCORE = 13
GRADE = 14
RECORD_DATA = 15
INSPECT_TYPT = 16
# open and read data
f = open("data.csv",'rb')
# skip the header
header = f.next()
# read and put in to list
data = list(csv.reader(f))
# new_data used to get numeric number of data
new_data = []
for entry in data:
    # new data entry
    new_entry =[]
    # if data entry is missing skip data
    if len(entry[SCORE])==0:
        continue
    if(entry[PHONE].isdigit()):
        new_entry.append(entry[PHONE])
    else:
        continue
    # append data to entry and entry to dataset
    new_entry.append(entry[PHONE])
    new_entry.append(entry[SCORE])
    new_data.append(new_entry)
# get numpy form of data
data = numpy.array(new_data)
kmeans = cluster.KMeans(n_clusters = 10)
kmeans.fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
for i in range(10):
    ds = data[numpy.where(labels==i)]
    pyplot.plot(ds[:,0],ds[:,1],'o')
    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)
pyplot.show()