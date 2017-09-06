import numpy,csv,json
from sklearn.preprocessing import Normalizer
CAMIS = []
BORO = []
BUILDING = []
ZIPCODE = []
PHONE = []
VIOLATION_CODE = []
CRITICAL_FLAG = []
SCORE = []
GRADE = []
CUISINE_DESCRIPTION=[]
names = ['CAMIS', 'DBA', 'BORO', 'BUILDING', 'STREET', 'ZIPCODE', 'PHONE', 'CUISINE DESCRIPTION', 'INSPECTION DATE', 'ACTION', 'VIOLATION CODE', 'VIOLATION DESCRIPTION', 'CRITICAL FLAG', 'SCORE', 'GRADE', 'GRADE DATE', 'RECORD DATE', 'INSPECTION TYPE']
index =['CAMIS','BORO',"BUILDING","ZIPCODE",'PHONE','CUISINE DESCRIPTION','VIOLATION CODE','CRITICAL FLAG','SCORE','GRADE']
with open('result.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        CAMIS.append(int(row[0]))
        BORO.append(int(row[2]))
        BUILDING.append(int(row[3]))
        ZIPCODE.append(int(row[5]))
        PHONE.append(int(row[6]))
        CUISINE_DESCRIPTION.append(int(row[7]))
        VIOLATION_CODE.append(int(row[10]))
        CRITICAL_FLAG.append(int(row[12]))
        SCORE.append(int(row[13]))
        GRADE.append(int(row[14]))
result = []
result.append(CAMIS)
result.append(BORO)
result.append(BUILDING)
result.append(ZIPCODE)
result.append(PHONE)
result.append(CUISINE_DESCRIPTION)
result.append(VIOLATION_CODE)
result.append(CRITICAL_FLAG)
result.append(SCORE)
result.append(GRADE)
csvfile.close()

all_samples = numpy.array(result)

all_samples = Normalizer().fit_transform(all_samples)

csv_samples = []

for i in range(0, len(all_samples[0])):
    entry = []
    for s in all_samples:
        entry.append(s[i])
    csv_samples.append(entry)


result = open("result3.csv","wb")
spamwriter = csv.writer(result)
spamwriter.writerow(index)
for i in csv_samples:
    spamwriter.writerow(i)
result.close()

# compute mean;

mean_0 = numpy.mean(all_samples[0,:])
mean_1 = numpy.mean(all_samples[1,:])
mean_2 = numpy.mean(all_samples[2,:])
mean_3 = numpy.mean(all_samples[3,:])
mean_4 = numpy.mean(all_samples[4,:])
mean_5 = numpy.mean(all_samples[5,:])
mean_6 = numpy.mean(all_samples[6,:])
mean_7 = numpy.mean(all_samples[7,:])
mean_8 = numpy.mean(all_samples[8,:])
mean_9= numpy.mean(all_samples[9,:])


mean_vector = numpy.array([ [mean_0], [mean_1], [mean_2], [mean_3], [mean_4], [mean_5], [mean_6], [mean_7], [mean_8], [mean_9] ])

print "mean Vector:\n", mean_vector

# compute covariance matrix:

cov_mat = numpy.cov([all_samples[0,:],all_samples[1,:],all_samples[2,:],all_samples[3,:],all_samples[4,:],all_samples[5,:],all_samples[6,:],all_samples[7,:],all_samples[8,:],all_samples[9,:]])

print "Covariance Matrix:\n", cov_mat


eig_val,eig_vec = numpy.linalg.eig(cov_mat)

for i in range(len(eig_val)):
    eigvec_cov = eig_vec[:,i].reshape(1,10).T
    print "Eigenvector {}:\n{}".format(i,eigvec_cov)
    print "Eigenvalue {}".format(eig_val[i])

for val in eig_val:
    print "%f" %val
eig_pairs = [(numpy.abs(eig_val[i]), eig_vec[:,i]) for i in range(len(eig_val))]
eig_pairs.sort(key=lambda x:x[0],reverse = True)

for i in eig_pairs:
    print (i[0])

print "test", eig_vec[0]
print "test", csv_samples[0]

for i in range(0,10):
    sum = 0.0
    for j in range(0,10):
        sum += numpy.corrcoef(csv_samples[i],eig_vec[j])[0][1]
    print index[i], ' : ', sum


matrix_w = numpy.hstack((eig_pairs[0][1].reshape(10,1), eig_pairs[1][1].reshape(10,1)))
print'Matrix W:\n', matrix_w

transformed= matrix_w.T.dot(all_samples)
print transformed

csv_samples = []

for i in range(0, len(transformed[0])):
    entry = []
    for s in transformed:
        entry.append(s[i])
    csv_samples.append(entry)


result = open("result2.csv","wb")
spamwriter = csv.writer(result)
spamwriter.writerow(['CAMIS','BORO'])
for i in csv_samples:
    spamwriter.writerow(i)
result.close()

