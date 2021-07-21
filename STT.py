#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip install ibm_watson')


# In[3]:


from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[4]:


apikey = 'FFVYXuFNMERRu2hzoHdR06aVjLkOzPSC-daWyOXow_zo'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/fe8c2a6d-21c0-4fdc-8fd3-41c266d41d43'


# In[5]:


authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)


# In[12]:


with open('C:\\Users\\razan\\Desktop\\python39\\when.mp3.mp3', 'rb') as audio_file:
    res = stt.recognize(audio=audio_file, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
    print(res)
    exp= open('C:\\Users\\razan\\Desktop\\python39\\STT.txt.TXT','w')
    
    exp.write(str(res))
    
    exp.close()


# In[ ]:




