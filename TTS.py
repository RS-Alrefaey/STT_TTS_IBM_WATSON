#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ibm_watson')


# In[2]:


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[3]:


apikey = '5Og-v5BGuftslkfEhPtGtST8MVYf1TDifMDOr-27jG1J'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/eb5df609-8aa9-4e9e-a97d-e4577ddec989'


# In[4]:


authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


# In[7]:


with open('C:\\Users\\razan\\Desktop\\python39\\TTS\\hello.txt.TXT', 'r') as myFile:
    text = myFile.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)

with open('./winston.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)


# In[ ]:




