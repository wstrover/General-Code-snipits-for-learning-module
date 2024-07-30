#!/usr/bin/env python
# coding: utf-8

# In[1]:


import threading 

class CountClass:
    def __init__(self):
        self.counter = 0
        
    def increment(self):
        self.counter = self.counter +1
        
mycounter = CountClass()

def foo():
    for i in range(1000000):
        mycounter.increment()
        
first = threading.Thread(target=foo, args=())
second = threading.Thread(target=foo, args=())

first.start()
first.join()

second.start()


second.join ()

print(mycounter.counter)


# In[ ]:




