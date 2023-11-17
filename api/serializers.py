from rest_framework import serializers
from api.models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TournamanetMatchSerializer(serializers.ModelSerializer):
    bowler = serializers.SerializerMethodField()
    batsman_at_strike = serializers.SerializerMethodField()
    batsman_at_nonstrike = serializers.SerializerMethodField()
    batting_team = serializers.SerializerMethodField()
    bowling_team = serializers.SerializerMethodField()

    def get_bowler(self, match):
        bowler = PlayerSerializer(match.bowler.player)
        return bowler.data

    def get_batsman_at_strike(self, match):
        batsman_at_strike = PlayerSerializer(match.batsman_at_strike.player)
        return batsman_at_strike.data

    def get_batsman_at_nonstrike(self, match):
        batsman_at_nonstrike = PlayerSerializer(match.batsman_at_nonstrike.player)
        return batsman_at_nonstrike.data

    def get_batting_team(self, match):
        batting_team = TeamSerializer(match.batting_team)
        return batting_team.data

    def get_bowling_team(self, match):
        bowling_team = TeamSerializer(match.bowling_team)
        return bowling_team.data

    class Meta:
        model = TournamentMatch
        fields = '__all__'