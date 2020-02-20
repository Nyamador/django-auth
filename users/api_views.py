from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView


class AuthView(APIView):
    authentication_classes = [TokenAuthentication]
    pass