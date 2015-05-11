__author__ = 'blade'
import re
asta = '   The Dog  '
print asta
print asta.strip(' ')
print asta.split()

rasta = re.findall(r'\w+', asta)
print rasta, '\n'
print rasta.__sizeof__()
#jasta =''
#print rasta
#jasta = sorted(jasta)
#sasta = ''
#sasta = sasta.join(jasta)
#print jasta, sasta
strin = 'something 701-200-7534 etc123 9832-234-1222'

br = re.findall(r'([0-9]+-[0-9]+-[0-9]+)',strin)
for x in br:
    y = x.split('-')
    if y[0].__len__()<=3:
        print x
print br
a = {'a':1, 'b':2}
b = {'a':1, 'b':2}

if a == b:
    print 'a = b'
else:
    print 'a not equal to b'

deta = 'This,%^& is a sentence!'
deta_sp = re.findall(r'[\W]+',deta)
deta_words = re.findall(r'[\w]+', deta)
print deta_words
print deta_sp
y = 0
for x in range(len(deta_words)-1, -1, -1):
    print deta_words[x] + deta_sp[y],
    y+=1

usr = raw_input()
print 'hello', usr

