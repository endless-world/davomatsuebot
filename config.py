import os
from environs import Env

env = Env()
if not os.path.exists('.env'):
    print('.env fayli topilmadi!')
    print('.env.example faylidan nusxa ko\'chirib shablonni o\'zizga moslang.')
    exit(1)
env.read_env()



# TELEGRAM BOT ADMINS
ADMINS = env.list('ADMINS')

# TELEGRAM BOT TOKEN
API_TOKEN = env.str('API_TOKEN')

# WEBHOOK
WEB_DOMAIN = env.str('WEB_DOMAIN')

# DJANGO
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG')

# PostgreSQL
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")

# HEMIS APIs
SCHEDULE_URL=env.str("SCHEDULE_URL")
CONTROL_SCHEDULE_URL = env.str("CONTROL_SCHEDULE_URL")

# HEMIS TOKEN
MY_TOKEN=env.str("MY_TOKEN")
