from dotenv import load_dotenv 
import os

load_dotenv() 

USER_AGENT = os.getenv('USER_AGENT')

HEADERS = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en; q=0.5'
}

if not HEADERS['User-Agent']:
    print("⚠️ Warning: USER_AGENT not found in .env file. Using default User-Agent.")
