from rest_framework import serializers
from management_discount_cards.models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['series', 'number', 'create_date', 'end_of_activity', 'date_of_use',
                  'total_sum', 'status']
