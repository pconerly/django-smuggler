
# DEBUG = True


# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'console':{
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#         # 'chrome-console': {
#         #     'level': 'DEBUG',
#         #     'class': 'test_app.ChromeLoggerLogHandler',
#         # },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers':['console'],
#             'propagate': True,
#             'level':'DEBUG',
#             },
#         },
#     }

# # l = logging.getLogger('django.db.backends')
# # l.setLevel(logging.INFO)
# # l.addHandler(logging.StreamHandler())


# Haystack settings for running tests.
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'smuggler.db'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'smuggler.db'
    }
}

SECRET_KEY = 'mAtTzVPOV9JY4eJQfqgW8eAS9DWKnt3MkvvpQI2MzkhAz7z3'

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.flatpages',
    'smuggler',
    'test_app',
]
