# from django.shortcuts import render
# from django.http import HttpResponse
# from . models import Organization
# from . serializers import OrganizationSerializer
# from rest_framework import JSONRenderer
# # Create your views here.

# #queary set :
# def organization_info(request):
#     #complex data
#     info = Organization.objects.all()
#     #python
#     serializer = OrganizationSerializer(info, many =True) # akn a amra  (many =True) aita use korar karon amara (info = Organization.objects.all()) ai line a (Organization) model a onek data ace tai amra many= true use korci nah korle error asbe

#     #converted jason
#     json_data = JSONRenderer().render(serializer.data)

#     # json data to frontend 
#     return HttpResponse(json_data, content_type ='application/json') # akn a (content_type ='application/json') content_type diyeci amra kon type ar data jacce