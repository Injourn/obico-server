import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from .authentication import CsrfExemptSessionAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication



class PowerPlugStatusView(APIView):
    authentication_classes = [OAuth2Authentication, CsrfExemptSessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        url = request.data.get('url', '')
        res = requests.get(url + "/cm?cmnd=Power")
        return JsonResponse(res.json(), status=status.HTTP_200_OK)
class PowerPlugView(APIView):
    authentication_classes = [OAuth2Authentication, CsrfExemptSessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        url = request.data.get('url', '')
        res = requests.get(url + "/cm?cmnd=Power%20Toggle")
        return JsonResponse(res.json(), status=status.HTTP_200_OK)