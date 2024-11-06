import os
from dotenv import load_dotenv
load_dotenv()

if os.getenv('PROJECT_ENV')=='DEV':
    from settings.dev import *
elif os.getenv('PROJECT_ENV')=='PROD':
    from settings.production import *
else:
    from settings.local import *