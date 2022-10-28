from .base import *

print ("PROD")
DEBUG = False
SECRET_KEY = os.getenv("APP_SECRET_KEY", 'djang-inse-cure-*sl%whcx#i*k+gqy+(^2c(b57v22##+ks4*$zyilfxpz^gnny(')
print (SECRET_KEY)
CSRF_TRUSTED_ORIGINS = os.getenv("APP_CSRF_TRUSTED_ORIGINS", 'http://localhost,https://localhost').split(',')
ALLOWED_HOSTS = ['*'] 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATICFILES_STORAGE= 'django.contrib.staticfiles.storage.StaticFilesStorage'
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'
try:
    from .local import *
except ImportError:
    pass
