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
