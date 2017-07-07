import time as t
a = 1
b = 1
c = 2
print(1)
t.sleep(0.5)
print(1)
t.sleep(0.5)
while True:
  c=a+b
  print(c)
  a=b
  b=c
  t.sleep(0.5)
