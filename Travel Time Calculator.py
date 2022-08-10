#Simple project about calculate your travel time

#Leave time
jb = int(input('Departing hours : '))
mb = int(input('Departing minutes : '))
db = int(input('Departing seconds : '))
print('You will leave at', jb,':', mb,':', db)

print('----------------------------------')

#Travel time
jp = int(input('Travel hours : '))
mp = int(input('Travel minutes : '))
dp = int(input('Travel seconds : '))
print('You will travel for', jp,':', mp,':', dp)

print('----------------------------------')

#Travel time
js = (jb + jp)
if (js > 24):
    js = int(js) - int(24)
elif (js == 24):
    js = 0
    
ms = (mb + mp)
if (ms > 60):
    ms = int(ms) - int(60)
    js = js + 1
elif (ms == 60):
    ms = 0
    js = js + 1

ds = (db + dp)
if (ds > 60):
    ds = int(ds) - int(60)
    ms = ms + 1
elif (ds == 60):
    ds = 0
    ms = ms + 1

#Result
print('So your travel time is', js,':', ms,':', ds)


