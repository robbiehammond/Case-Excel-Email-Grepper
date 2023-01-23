import csv 

fname = 'grades.csv'
emails = []
file = open(fname)

r = csv.DictReader(file)
for row in r:
    id = row['SIS Login ID']
    if ((len(id)) == 0) or row['Student'] == 'Student, Test':
        continue
    emails.append(id + '@case.edu')


#print(emails)
print(("{0}".format(', '.join(map(str, emails)))))
