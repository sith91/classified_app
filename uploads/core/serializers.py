from rest_framework import serializers
from uploads.core.models import Deals, Category


class DealSerializer(serializers.ModelSerializer):


    class Meta:
        model = Deals
        fields = ('category','description', 'document','expire_date')


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedRelatedField(many=True, view_name='category-detail', read_only= True)


    class Meta:
        model = Category
        fields = ('mname','mdescription')