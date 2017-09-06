import numpy,csv,json
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
    print next(reader, None)
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
result_ttr = []
for attr in result:
    attr_array = []
    for attr2 in result:
        attr_array.append( numpy.corrcoef(attr,attr2)[0][1])
    result_ttr.append(attr_array)


for attr in result_ttr:
    print index[result_ttr.index(attr)]
    print attr
    result  = 0
    for attr2 in attr:
        result += attr2
    print result
# print '[{'
# print '"nodes":['
# for name in names:
#     print '{'
#     print '"name":"'+name+'"'
#     print '},'
# print ']'
#
# print '}]'
#
# print '"links":['
# for attr in result_ttr:
#     for attr2 in attr:
#         print'{'
#         print '"source":'+str(result_ttr.index(attr))+','
#         print '"target":'+str(attr.index(attr2))+','
#         print '"value":'+str(attr2)
#         print '},'
# print "]"

