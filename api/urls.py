from api.views import LiveMatchScore, AddLiveScore
from django.urls import path

urlpatterns = [
    path('live-score/<int:matchid>', LiveMatchScore.as_view()),
    path('add-score/<int:matchid>', AddLiveScore.as_view()),

]