#study mart
from rest_framework import serializers

# class OrganizationSerializer(serializers.Serializer):
#     teacher_name = serializers.CharField(max_length=100)
#     course_name  = serializers.CharField(max_length=100)
#     course_duration = serializers.IntegerField(max_length=10)
#     seat = serializers.IntegerField()

#geekey
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # class StudentForm (forms.Form):
    #     name = forms.CharField(max_length=100)
    #     roll = forms.IntegerField()
    #     city = forms.CharField(max_length=100)
    """amara akn ceate method use korci karon amader je valided_data ta dibo tar jnno tar jnno amder akti model instance create korbe ar ai model instance ta save korbe """
    # amara serializer a data update korai jnno amra akn a 
    def create(self,validated_data):
        return Student.object.create(**validated_data)
 

#partial update korlam ar ai jnno amara akn a PUT use korlam ar ai code partial ba data update ar jnno

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name) #user jodi data provide kore take tahole akn a
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
         



