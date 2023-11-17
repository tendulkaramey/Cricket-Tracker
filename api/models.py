from django.db import models
from django.utils.timezone import now

def default_json():
    return {}

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    stats = models.JSONField(default=default_json)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return '{0}-{1}'.format(self.first_name, self.team.name)

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

class TournamentPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    stats = models.JSONField(default=default_json)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.player.first_name

class TournamentFixture(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    team_won = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_won', null=True, default=None, blank=True)
    toss_won = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='toss_won', null=True, default=None, blank=True)
    is_draw = models.BooleanField(default=False)
    is_live = models.BooleanField(default=False)
    location = models.JSONField(default=default_json)
    match_time = models.DateTimeField(default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return '{0} VS {1} : Match-ID:{2}'.format(self.team1, self.team2, self.id)

class TournamentMatch(models.Model):
    match = models.ForeignKey(TournamentFixture, on_delete=models.CASCADE)
    batting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='batting_team')
    bowling_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bowling_team')
    bowler = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE, related_name='bowler')
    batsman_at_strike = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE, related_name='batsman_at_strike')
    batsman_at_nonstrike = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE, related_name='batsman_at_nonstrike')
    inning = models.IntegerField(default=1)
    over = models.IntegerField()
    ball = models.IntegerField()
    runs = models.IntegerField(default=0)
    is_extra = models.BooleanField(default=False)
    extra = models.CharField(max_length=20, blank=True)
    is_wicket = models.BooleanField(default=False)
    stats = models.JSONField(default=default_json)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return 'Match ID: {0}'.format(self.match.id)
