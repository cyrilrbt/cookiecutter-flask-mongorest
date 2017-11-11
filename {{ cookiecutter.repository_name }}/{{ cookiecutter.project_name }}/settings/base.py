import datetime

DEBUG = True
MONGODB_SETTINGS = {
    'HOST': 'localhost',
    'PORT': 27017,
    'DB': '{{ cookiecutter.project_name }}',
    'TZ_AWARE': False,
}
JWT_SECRET = '>vcFu>ab"zJ/?X{ i9n]m[7FEzJ5qO$c:#R:#^T04 .;J9T2)nz!U!v$! ' \
    'EQko4kogFl5q6W"A(XAf-v3iA"uTj,wCU2n|>--&H IZyy}7o-M+1!/P+BbaWi}o'
JWT_EXPIRATION = datetime.timedelta(days=30)
