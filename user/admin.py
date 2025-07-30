from django.contrib import admin

from .models import User, MatrixRequest

admin.site.register((User, MatrixRequest))