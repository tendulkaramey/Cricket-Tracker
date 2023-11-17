from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status as api_response_status
from api.models import *
from api.serializers import *
from django.core.cache import cache
import json

class LiveMatchScore(APIView):

    def get(self, request, matchid, format=None):

        try:
            match = TournamentFixture.objects.get(id=matchid)
        except TournamentFixture.DoesNotExist:
            return JsonResponse({
                'success': False,
                'userMessage': 'Not Found',
            }, status = api_response_status.HTTP_404_NOT_FOUND)
        
        #check in cache else db
        score = cache.get('match'+str(matchid))
        if score is not None:
            print('***************'*20)
            print(score)
            score = json.loads(score)
            return JsonResponse({
                'success': True,
                'userMessage': 'from cache!',
                'data': score,
            }, status = api_response_status.HTTP_200_OK)
        

        latest_score = TournamentMatch.objects.filter(match=match).order_by('-id')
        if latest_score.count():
            score = TournamanetMatchSerializer(latest_score[0])
            score = score.data
        else:
            score = []

        return JsonResponse({
            'success': True,
            'userMessage': '',
            'data': score,
        }, status = api_response_status.HTTP_200_OK)

class AddLiveScore(APIView):

    def post(self, request, matchid, format=None):

        data = json.loads(request.body)

        required_fields = {'batting_team', 'bowling_team', 'bowler', 'batsman_at_strike', 'batsman_at_nonstrike', 'inning', 'over', 'ball', 'runs', 'is_extra', 'extra', 'is_wicket', 'stats'}

        if len(required_fields - set(data.keys())):
            return JsonResponse({
                'success': False,
                'userMessage': 'Please fill all the fields',
                'internalMessage': 'All fields not present or some field is blank',
            }, status = api_response_status.HTTP_400_BAD_REQUEST)

        try:
            match = TournamentFixture.objects.get(id=matchid)
        except TournamentFixture.DoesNotExist:
            return JsonResponse({
                'success': False,
                'userMessage': 'Not Found',
            }, status = api_response_status.HTTP_404_NOT_FOUND)
        
        batting_team = data['batting_team']
        bowling_team = data['bowling_team']
        bowler = data['bowler']
        batsman_at_strike = data['batsman_at_strike']
        batsman_at_nonstrike = data['batsman_at_nonstrike']
        inning = data['inning']
        over = data['over']
        ball = data['ball']
        runs = data['runs']
        is_extra = data['is_extra']
        extra = data['extra']
        is_wicket = data['is_wicket']
        stats = data['stats']

        try:
            batting_team = Team.objects.get(id=batting_team)
            bowling_team = Team.objects.get(id=bowling_team)
        except Team.DoesNotExist:
            return JsonResponse({
                'success': False,
                'userMessage': 'Team Not Found',
            }, status = api_response_status.HTTP_404_NOT_FOUND)
        
        try:
            bowler = TournamentPlayer.objects.get(id=bowler)
            batsman_at_strike = TournamentPlayer.objects.get(id=batsman_at_strike)
            batsman_at_nonstrike = TournamentPlayer.objects.get(id=batsman_at_nonstrike)
        except TournamentPlayer.DoesNotExist:
            return JsonResponse({
                'success': False,
                'userMessage': 'Player Not Found',
            }, status = api_response_status.HTTP_404_NOT_FOUND)
        
        score = TournamentMatch(match=match, batting_team=batting_team, bowling_team=bowling_team, bowler=bowler, batsman_at_strike=batsman_at_strike, batsman_at_nonstrike=batsman_at_nonstrike, inning=inning, over=over, ball=ball, runs=runs, is_extra=is_extra, extra=extra, is_wicket=is_wicket, stats=stats)
        score.save()

        #update in cache also here
        latest_score = TournamentMatch.objects.filter(match=match).order_by('-id')
        score = TournamanetMatchSerializer(latest_score[0])
        score = score.data
        score = json.dumps(score)
        cache.set('match2', score, 60)

        

        return JsonResponse({
            'success': True,
            'userMessage': 'score added',
            'data': [],
        }, status = api_response_status.HTTP_200_OK)
            

