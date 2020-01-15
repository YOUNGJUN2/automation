import csv, re, requests

l = []

f = open('Filename.csv', 'r')
rdr = csv.reader(f)

for line in rdr:  
    p = re.search('Host: (.*.com)',line[5])
    if p != None:
        l.append(p.group(1))
    
for i in l:
    url = 'http://%s' % i
    response = requests.get(url)
    print(url,": ",response)

f.close()
