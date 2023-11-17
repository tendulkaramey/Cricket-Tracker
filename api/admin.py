from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(TournamentPlayer)
admin.site.register(TournamentFixture)
admin.site.register(TournamentMatch)