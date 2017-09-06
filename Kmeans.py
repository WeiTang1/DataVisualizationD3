
import csv
import numpy
from sklearn import cluster
from matplotlib import pyplot
# open file and read
f= open("data.csv",'rb')
reader = csv.reader(f)
f.readline()
data = list(reader)
data_set = []
# get numerical data
for entry in data:
   new_entry = []
   if entry[6].isdigit() and entry[13].isdigit():

       new_entry.append(int(entry[6][:3]))
       new_entry.append(int(entry[13]))
       data_set.append(new_entry)

data_set = numpy.array(data_set)
print data_set

# k = 5
for k in range(2,6):
    kmeans= cluster.KMeans(n_clusters = k)
    kmeans.fit(data_set)
#get label and center
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
#plot
    for i in range(k):
        # find data with certain label
        cluster_set = data_set[numpy.where(labels==i)]
        #plot data entry
        pyplot.plot(cluster_set[:,0],cluster_set[:,1],'o')
        #plot cluster center
        lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
        pyplot.setp(lines,ms=15.0)
        pyplot.setp(lines,mew=2.0)
    print "K= ", k, "\n labels: \n", labels, "\n centroids: \n", centroids

    pyplot.show()
