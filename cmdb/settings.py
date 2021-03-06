﻿'''
@Description: 
@Author: Henry Sun
@Date: 2019-08-07 14:11:06
@LastEditors: Henry Sun
@LastEditTime: 2019-08-15 21:27:42
'''
"""
Django settings for clone project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
# import configparser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'libs'))
sys.path.insert(0, os.path.join(BASE_DIR, 'configs'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c^#vrcw(kxu(20+j6s3#balhe5bruv42+spb^k*(o2+#pp6t5q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_python3_ldap',
    'clonevm.apps.CloneVmConfig',
    'elementryinfo.apps.ElementryinfoConfig',
    'assets.apps.AssetsConfig',
    'taggit',
    'crispy_forms',
    'xadmin',
    'reversion',
    'django.conf',
    'django_filters',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cmdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cmdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'clone-test1',
        # 'USER': 'postgres',
        # 'PASSWORD': 'mysteel',
        # 'HOST': '192.168.100.227',
        # 'PORT': '5432',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD':'',  
        'HOST': '',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB;'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = [
    'django_python3_ldap.auth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# celery异步配置
# CELERY_BROKER_URL = 'redis://:mysteel123@192.168.100.135:6379/0'
# CELERY_RESULT_BACKEND = 'redis://:mysteel123@192.168.100.135:6379/0'
# # CELERY_TASK_SERIALIZER = 'json'

# #celery内容等消息的格式设置
# CELERY_ACCEPT_CONTENT = ['application/json','json']
# CELERY_TASK_SERIALIZER = 'json'
# # CELERY_RESULT_SERIALIZER = 'json'
 

# CELERY_TIMEZONE = TIME_ZONE



LDAP_AUTH_URL = "ldap://192.168.100.16:389"

#在连接时启动TLS。
LDAP_AUTH_USE_TLS  =  False

#用于查找用户的LDAP搜索库。
LDAP_AUTH_SEARCH_BASE  = "OU=产品研发中心,OU=banksteel,DC=banksteeltech,DC=local"

#表示用户的LDAP类。
LDAP_AUTH_OBJECT_CLASS = "user"

#用户模型字段映射到表示它们的LDAP属性。
LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}
#用于唯一标识用户的django模型字段的元组。
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)


#路径的可调用这需要{model_field_name：值}的字典，
#返回干净的模型数据字典。
#使用此选项可以自定义从LDAP加载的数据如何保存到用户模型。
LDAP_AUTH_CLEAN_USER_DATA  =  "django_python3_ldap.utils.clean_user_data"

#路径一个可调用，需要一个用户模型和一个字典{ldap_field_name：[数值]}， 
#并保存基于所述LDAP数据的任何附加的用户的关系。
#使用此选项可以自定义从LDAP加载的数据如何保存到用户模型关系。
#要自定义不相关的用户模型字段，请使用LDAP_AUTH_CLEAN_USER_DATA。
LDAP_AUTH_SYNC_USER_RELATIONS  =  "django_python3_ldap.utils.sync_user_relations"

#k路径一个可调用该取{ldap_field_name：值}的一个字典，返回的[ldap_search_filter]列表。
#在创建最终搜索过滤器时，搜索过滤器将与AND ＃在一起。
LDAP_AUTH_FORMAT_SEARCH_FILTERS = "django_python3_ldap.utils.format_search_filters"

#路径的可调用这需要{model_field_name：值}的一个字典，并返回用户名的字符串绑定到LDAP服务器。
#用于支持不同类型的LDAP服务器。
LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory_principal"
# LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory"


#设置Active Directory用户的登录域。
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "banksteeltech.local"

#用户的LDAP用户名和密码，用于查询LDAP数据库中的用户
#详细信息。如果没有，则该认证的用户将用于查询和的`ldap_sync_users`命令将执行匿名查询。
# 上面写域名了 这里administrator后面就不要加域名了 详情可看testldap3.py
LDAP_AUTH_CONNECTION_USERNAME  =  "administrator"
LDAP_AUTH_CONNECTION_PASSWORD  =  "!QAZ3edc"

#在底层`ldap3`库上设置连接/接收超时（以秒为单位）。
LDAP_AUTH_CONNECT_TIMEOUT  = None