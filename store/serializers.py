from rest_framework import serializers
from .models import Product , Flavor


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = "__all__"
        



class ProductSerializer(serializers.ModelSerializer):
    flavor = FlavorSerializer(read_only=True,many =True)

    class Meta:
        model = Product
        fields = "__all__"
        depth =1
        

