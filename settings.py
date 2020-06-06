import os
from dotenv import load_dotenv
load_dotenv()

ZWSID = os.getenv('ZWSID')

print(ZWSID)