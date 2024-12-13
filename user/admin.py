from django.contrib import admin

from .models import User, MatrixRequest, Master, Session, ReferralLink

admin.site.register((User, MatrixRequest, Master, Session, ReferralLink))