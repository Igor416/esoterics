from django.contrib import admin

from .models import User, MatrixRequest, Master, Session

admin.site.register((User, MatrixRequest, Master, Session))