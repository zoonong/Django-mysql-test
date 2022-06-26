# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 데이터베이스 이름,
        'USER': sql 유저명,
        'PASSWORD': sql 비번,
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
SECRET_KEY = 장고 시크릿키