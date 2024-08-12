import intro
print (intro.sum (2,4))

import calendar as cl
print(cl.firstweekday())
print(cl.isleap(2020))
print(cl.weekday(2024,8, 20))
print(cl.month(2024,8))
print(cl.calendar(2024,3,1,9))


import math as m

print(m.ceil(5.7))
print(m.ceil(6.8))
print(m.floor(3.4))
print(m.factorial(5))
print(m.log(8,5))


import re
line = 'python is a programming language'
x = re.match('python',line)

print(x)
y = re.search('programming ',line)
print(y)
if y :
    print ('match found')
else:
    print('no match')

s = re.sub('programming','high level programming lang',line)

print(s)

line1 = 'python is a programming language python is a high level programming language '
s = re.sub('python', 'java', line1,1)
print(s)

line2 = '4321567890 00987654 pyhon is 123456789 prigramming language python is good'
x = re.sub('\d', 'a',line2)
print(x)

#\d numerics
#\D exclude
#\S,exclude
#\s exc space

line3 = 'python is 1234 !@#$$ simple humble 5678 *&8%$$****'
x = re.sub('[^a-z,A-Z,0-9]', ' ',line3)
print(x)

line4 = 'python is a high level language'
x = re.split('\s', line4)
print(x)

line5 = 'python is simple language'
x = re.split('\s',line5,2)
print(x)

line6 ='python 12345 pyt6789 simple humble 987654321 language 2468'
x = re.findall('\d',line6)
print(x)
line7 = 'python987654321 simple easy 2345678 lala yy 22uu34ed5'
x = re.findall('\d+',line7)
print(x)

x = re.findall('[0-9]+',line7)
print(x)

line8 ='python 123456789 simple +98425065 is simple like +2245'\

x = re.findall('[+][0-9]+',line8)

print(x)
x = re.findall('[+][\d]+',line8)
print(x)
