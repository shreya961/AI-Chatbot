import cohere
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CO_API_KEY")

co = cohere.Client(api_key)
def get_text_output(input):
    
    output=co.chat(model="command-r-plus-08-2024",
        message=input)
    
    return output.text

#print(co)
#print(output.text)
