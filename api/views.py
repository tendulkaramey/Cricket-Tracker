from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import status as api_response_status
from api.models import *

class LiveMatchScore(APIView):

    def get(self, request, matchid, format=None):

        try:
            match = TournamentMatch.objects.get(id=matchid)
        except TournamentMatch.DoesNotExist:
            return JsonResponse({
                'success': False,
                'userMessage': 'Not Found',
            }, status = api_response_status.HTTP_404_NOT_FOUND)

        return JsonResponse({
            'success': True,
            'userMessage': '',
            'data': [],
        }, status = api_response_status.HTTP_200_OK)

class AddLiveScore(APIView):

    def post(self, request, matchid, format=None):

        data = json.loads(request.body)

        required_fields = {}

        if len(required_fields - set(data.keys())):
            return JsonResponse({
                'success': False,
                'userMessage': 'Please fill all the fields',
                'internalMessage': 'All fields not present or some field is blank',
            }, status = api_response_status.HTTP_400_BAD_REQUEST)