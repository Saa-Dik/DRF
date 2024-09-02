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
    def create(self,validated_data):
        return Student.object.create(**validated_data)

