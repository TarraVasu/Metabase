from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from genericresponse import GenericResponse
from django.http import JsonResponse
from .serializers import metaSerializer
from django.http import HttpResponse
from .models import metamodels
import jwt
import time



class metapost(generics.GenericAPIView):
    serializer_class = metaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        s = metaSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        f = s.save()
        return Response(metaSerializer(f).data)




class metaget(generics.GenericAPIView):
    serializer_class = metaSerializer
    permission_classes = (IsAuthenticated,)


    def get(self,request,UserId):
        m = metamodels.objects.filter(UserId=UserId)
        g = metaSerializer(m,many=True)
        return Response({'Result':g.data})








METABASE_SITE_URL = "https://metabase.vivifyhealthcare.com"
METABASE_SECRET_KEY = "c4c44d537a9de8a3163a94f860156b4b2d7bd2916c58b235a6192eb7103af863"

# question_list = [26, 27, 28, 29, 33, 34, 35, 38, 43, 40, 41, 42, 45, 46, 47]

class metabaseclass(generics.GenericAPIView):
    # serializer_class = getSerializer
    permission_classes = (IsAuthenticated,)
#

    def get(self, request,userId,questionids):

        try:
            # Apicall(26)
            questionid = questionids
            print(questionid)
            print(type(questionid))
            # num = int(questionid)
            # print(num)
            h = questionid.split(",")
            print(h)
          
            url = []
            
            for i in h:
                print(i)
                iframeUrl = Apicall(int(i))
                print(iframeUrl)
                url.append(iframeUrl)

            list1 = url

            list2 = ["total_voters", "village_voters", "madugula_voters_by_lastname", "village_voters_by_lastname", "Weekly_Campaign_Data_Update", "Caste_Bifurcation",
                      "Party_Inclination", "Total_Mandals_in_madugula", "Cheedikada_Mandal", "Devarapalli_Mandal",
                      "K.kotapadu_Mandal","Madugula_Mandal","Dissidents_Party_Wise","Non_Local-Resident","Local_Resident"]

            result_dict = {list2[i]: list1[i] for i in range(min(len(list1), len(list2)))}


            # dic = {
            #     'total_voters': url[0],
            #     'village_voters': url[1],
                # 'madugula_voters_by_lastname': url[2],
                # 'village_voters_by_lastname': url[3],
                # 'Weekly_Campaign_Data_Update': url[4],
                # 'Caste_Bifurcation': url[5],
                # 'Party_Inclination': url[6],
                # 'Total_Mandals_in_madugula': url[7],
                # 'Cheedikada_Mandal': url[8],
                # 'Devarapalli_Mandal': url[9],
                # 'K.kotapadu_Mandal': url[10],
                # 'Madugula_Mandal': url[11],
                # 'Dissidents_Party_Wise': url[12],
                # 'Non_Local-Resident': url[13],
                # 'Local_Resident': url[14],

            # }
            
            return Response({'Message': 'Successful',
                             'Result': result_dict,
                             'HasError': False,
                             'Status': 200})
        except:
            return Response({'Message': 'fail',
                             'Result': "fail",
                             'HasError': True,
                             'Status': 400})
print(list)

def Apicall(question_number):
    payload = {
        "resource": {"question": question_number},
        "params": {},
        # "exp": round(time.time()) + (60 * 20)  # 10 minute expiration
    }

    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframeUrl = METABASE_SITE_URL + "/embed/question/" + token + "#bordered=true&titled=true"

    # iframeUrl = METABASE_SITE_URL + "/embed/question/" + token.decode() + "#bordered=true&titled=true"

    return iframeUrl




