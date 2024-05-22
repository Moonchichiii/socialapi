from rest_framework import serializers
from .models import DinnerClub, ALLERGY_CHOICES
from profiles.models import Profile

class AllergyListField(serializers.ListField):
    def to_representation(self, value):
        return value.split(',')

    def to_internal_value(self, data):
        if not isinstance(data, list):
            raise serializers.ValidationError('Expected a list of data.')
        return ','.join(data)

class DinnerClubSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.user.username')
    invited_profiles = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    participants = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    allergies = AllergyListField()

    class Meta:
        model = DinnerClub
        fields = ['id', 'host', 'title', 'description', 'location', 'date_time', 'theme_dinner', 'allergies', 'type_of_dinner', 'invited_profiles', 'participants']
        read_only_fields = ['host', 'participants']
