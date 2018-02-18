# produce 200 random strings and store them in random.txt
import random
import string
fo = open("random.txt","wb")
for j in range(201):
  seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  sa = []
  for i in range(4):
      sa.append(random.choice(seed))
  sa.append('-')
  for i in range(4):
      sa.append(random.choice(seed))
  sa.append('-')
  for i in range(4):
      sa.append(random.choice(seed))
  salt = ''.join(sa)
  print salt+'\n'
  salt += '\n'
  fo.write(salt+'\r\n')
fo.close()
