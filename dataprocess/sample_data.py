import csv
sample_data = {}
with open ('../data/sample1.csv','r') as f1,open('../data/sample2.csv','r') as f2,open('../data/sample3.csv','r') as f3:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    reader3 = csv.reader(f3)
    next(reader1)
    next(reader2)
    next(reader3)
    for row in reader1:
        sample_data[row[1]] = row[0]
    for row in reader2:
        sample_data[row[1]] = row[0]
    for row in reader3:
        sample_data[row[1]] = row[0]
test_data={}
with open ('../rowdata/spam.csv','r') as f1,open('../rowdata/sms_pub1.csv','r') as f2 ,open('../rowdata/sms_pub2.csv','r') as f3:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    reader3 = csv.reader(f3)
    next(reader1)
    next(reader2)
    next(reader3)
    for row in reader1:
        if row[1] not in sample_data.keys():
            test_data[row[1]] = row[0]
    for row in reader2:
        
        if row[1] not in sample_data.keys():
            test_data[row[1]] = row[0]
    for row in reader3:
        
        if row[1] not in sample_data.keys():
            test_data[row[1]] = row[0] 
