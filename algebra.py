#! /usr/bin/python
import random
while (1<2):
  a = random.randint (1,3)
  x = random.randint (1,3)
  y = random.randint (1,3)
  w = ((a + x) * y)
  z = "Find a: (a + %s) * %s = %s | a = " % (x,y,w)
  answer=input (z)
  print "a is equal to..."+str(a)
  if answer==(a):
    print "correct"
  else:
    print "incorrect"
  a = random.randint (1,3)
  x = random.randint (1,3)
  y = random.randint (1,3)
  w = (a * x + y)
  z = "Find a: a * %s + %s = %s | a = " % (x,y,w)
  answer=input (z)
  print "a is equal to..."+str(a)
  if answer==(a):
    print "correct"
  else:
    print "incorrect"
  a = random.randint (1,3)
  x = random.randint (1,3)
  y = random.randint (1,3)
  w = (x - a * y)
  z = "Find a: %s - a * %s = %s | a = " % (x,y,w)
  answer=input (z)
  print "a is equal to..."+str(a)
  if answer==(a):
    print "correct"
  else:
    print "incorrect"
