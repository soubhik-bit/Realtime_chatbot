import os
from dotenv import load_dotenv,find_dotenv
import google.generativeai as genai



def getAkeyFromGoogle():
    status=load_dotenv(find_dotenv(),override=True)
    key=os.environ.get('GOOGLE_API_KEY')
    return key

