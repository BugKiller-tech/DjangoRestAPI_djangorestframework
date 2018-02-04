from rest_framework import serializers
from .models import Stock



class StockSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stock
    # fields = ('ticker', 'volume')
    fields = '__all__'  # if want to return all the fields as json. then do this. otherwise above command.
