from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review
            
            
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
            
class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField() #custom serializer field
    reviews = ReviewSerializer(many=True,read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"
        #fields = ['name','description','active']
        #exclude = ['name']
        
    #custom serializer field
    def get_len_name(self, object):
        length = len(object.title)
        return length
    
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many = True, read_only = True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie_detail')
    
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
        
    # def validate(self, data):
    #     if data['name'].lower() == data['description'].lower():
    #         raise serializers.ValidationError('Movie name and description cannot be same')
    #     return data

    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is to short')
    #     return value

#commented part is for serializers.Serializer

# commented part is for validators
# def name_length(value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name of movie is to short')
#         return value
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
        
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
      # commented part is for object validation
#     def validate(self, data):
#         if data['name'].lower() == data['description'].lower():
#             raise serializers.ValidationError('Movie name and description cannot be same')
#         return data

      # commented part is for field validation
#     # def validate_name(self,value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError('Name is to short')
#     #     return value    