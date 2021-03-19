#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Vaja 2 VZORCENJE ROK ROZMAN
import numpy as np
import matplotlib.pyplot as plt
#import sounddevice as sd


# In[19]:


def generiraj_ton_mono(cas, vzorcevalna_frekvenca, bitna_locljivost, frekvenca_tona):
    max_element = (pow(2,bitna_locljivost)/2-1)
    #preverimo v katero spada
    #int8 do 127
    #int16 do 32767
    #int32 do 2147483647
    #int64 do 9223372036854775807
    if max_element < 128:
        res="int8"
    elif max_element<32768:
        res="int16"
    elif max_element <2147483648:
        res="int32"
    else:
        res="int64"
    
    t = np.arange(0, cas * vzorcevalna_frekvenca, 1, dtype=res) / vzorcevalna_frekvenca
    #f = 5 # frekvenca sinusoide
    #A = 1 # amplituda sinusoide
    #nchans = 1 # 1 (mono), 2 (stereo)
    s = (pow(2,bitna_locljivost)/2-1)*np.sin(2*np.pi*frekvenca_tona*t)

    temp = np.random.rand(len(s), 1)
    i = 0
    while i < len(s):
        temp[i] = s[i]
        i = i + 1
    return temp


# In[20]:


#generiraj_ton_mono(1, 10, 8, 5)


# In[21]:


if __name__ == '__main__':
    test=generiraj_ton_mono(1, 10, 8, 5)
    plt.plot(test)


# In[ ]:




