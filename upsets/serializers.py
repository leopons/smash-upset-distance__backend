from rest_framework import serializers
from upsets.models import UpsetTreeNode, Set, Tournament, Player


class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ['name', 'start_date', 'online']


class LightPlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'tag', 'main_character']


class SetSerializer(serializers.ModelSerializer):

    tournament = TournamentSerializer()
    winner = LightPlayerSerializer()
    winner_characters = serializers.ListField(child=serializers.CharField())
    loser = LightPlayerSerializer()
    loser_characters = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Set
        fields = ['tournament', 'winner', 'loser', 'winner_score',
                  'loser_score', 'round_name', 'best_of', 'winner_characters',
                  'loser_characters']


class UpsetTreeNodeSerializer(serializers.ModelSerializer):

    upset = SetSerializer()

    class Meta:
        model = UpsetTreeNode
        fields = ['node_depth', 'upset']


class PlayerSerializer(serializers.ModelSerializer):

    last_tournament = TournamentSerializer()

    class Meta:
        model = Player
        fields = ['id', 'tag', 'main_character', 'last_tournament']
