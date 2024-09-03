# study mart:
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#  # Create your views here.

#queary set :
# def organization_info(request):
#     #complex data
#     info = Organization.objects.all()
#     #python
#     serializer = OrganizationSerializer(info, many =True) # akn a amra  (many =True) aita use korar karon amara (info = Organization.objects.all()) ai line a (Organization) model a onek data ace tai amra many= true use korci nah korle error asbe

#     #converted jason
#     json_data = JSONRenderer().render(serializer.data)

#     # json data to frontend 
#     return HttpResponse(json_data, content_type ='application/json') # akn a (content_type ='application/json') content_type diyeci amra kon type ar data jacce

#geekey:

def student_information(request, pk):
    #complex data to python data
    info = Student.objects.get(id = pk) #(amra first a id = 1) ID দ্বারা ফিল্টারিং: কোডের get(id = 1) অংশটি স্টুডেন্ট মডেলের ক্যোয়ারীসেটকে ফিল্টার করে সেই ছাত্রকে খুঁজে বের করার জন্য যার আইডি 1 এর সমান। এটি নিশ্চিত করে যে আপনি যে শিক্ষার্থীর প্রতি আগ্রহী সেই সঠিক ছাত্রটিকে পুনরুদ্ধার করতে পারেন। এটি আপনার স্টুডেন্ট মডেলে সংরক্ষিত ডেটার সাথে ইন্টারঅ্যাক্ট এবং অনুসন্ধান করার একটি উপায় প্রদান করে। get(id = 1): এই পদ্ধতিটিকে একটি একক স্টুডেন্ট অবজেক্টে ফিল্টার করার জন্য কোয়েরিসেটে বলা হয়। আইডি যুক্তিটি নির্দিষ্ট করে যে আপনি 1 এর আইডি সহ শিক্ষার্থীকে খুঁজে পেতে চান।
    #id = 1 ke change kore amra akn a id = pk dilam [akn a pk = primary key amra backend a datagula imnput dile amder data gula te id/ primary key hisabe takbe. ar akn pk use korle amar sokol data gula amara url a 1,2,3.. dile sei id hisabe amake data gula dekabe ]

    serializer = StudentSerializer(info)

    
    # python data to json renderer
    json_data = JSONRenderer().render(serializer.data)
    # json data to frontend 
    return HttpResponse(json_data, content_type='application/json')

    #return JsonResponse(serializer.data) #akn return JsonResponse use korle 33 & 35 line likhar drk nai karon ai 2 line ar kaj JsonResponse kore take. 

#queary set:
def student_list(request):
    #complex data to python data
    info = Student.objects.all()# akn a amra (many =True) aita use korar karon amara (info = Student.objects.all() ai line a (Student) model a onek data ace tai amra many= true use korci nah korle error asbe

    serializer = StudentSerializer(info, many =True)

    
    # python data to json renderer
    json_data = JSONRenderer().render(serializer.data)

    # json data to frontend 
    return HttpResponse(json_data, content_type='application/json')

#amara serialization ar jnno view create korbo ja amader deserialization ar kaje lagbe:
@csrf_exempt
def student_create(request):  
    if request.method == 'POST':
        json_data = request.body
        # json_data to stame:
        stream = io.BytesIO(json_data)
        # strame to python data:
        python_data = JSONParser().parse(stream)
        # python to complex_data/serializer
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(response_msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type= 'application/json')
    return HttpResponse(status=405)  # Method Not Allowed if not POST