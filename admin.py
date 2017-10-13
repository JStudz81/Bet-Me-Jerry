from django.contrib import admin

from .models import Bet
from .models import User

admin.site.register(Bet)
admin.site.register(User)