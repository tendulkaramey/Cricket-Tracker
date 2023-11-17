from django.core.management.base import BaseCommand
import random
from datetime import datetime, timedelta
from faker import Faker
from api.models import *

fake = Faker()


class Command(BaseCommand):
    help = 'Custom management command description'

    def handle(self, *args, **options):
        TournamentMatch.objects.all().delete()
        TournamentFixture.objects.all().delete()
        TournamentPlayer.objects.all().delete()
        Tournament.objects.all().delete()
        Player.objects.all().delete()
        Team.objects.all().delete()

        team_bulk = []
        for i in range(10):
            team = Team(name=fake.company(),country=fake.country(),league=fake.word())
            team_bulk.append(team)
        
        Team.objects.bulk_create(team_bulk)
        teams = Team.objects.all()
        for team in teams:
            #players addition
            players_bulk = []
            for j in range(11):
                player = Player(first_name=fake.first_name(), last_name=fake.last_name(), age=random.randint(18, 40), team=team)
                players_bulk.append(player)
            Player.objects.bulk_create(players_bulk)
        
        tournament = Tournament(name='World Cup', league='International')
        tournament.save()

        tournament = Tournament.objects.get(name='World Cup')
        players = Player.objects.all()
        tpbulk = []
        for player in players:
            tplayer = TournamentPlayer(team=player.team, player=player, tournament=tournament)
            tpbulk.append(tplayer)
        TournamentPlayer.objects.bulk_create(tpbulk)

        self.stdout.write(self.style.SUCCESS('Successfully populated database.'))

