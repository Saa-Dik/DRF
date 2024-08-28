# study mart:
from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
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

