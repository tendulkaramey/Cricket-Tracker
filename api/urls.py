from api.views import LiveMatchScore
from django.urls import path

urlpatterns = [
    path('live-score/<int:matchid>', LiveMatchScore.as_view()),

]