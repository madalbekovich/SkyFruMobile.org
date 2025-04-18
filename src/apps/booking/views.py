from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GetOptimalFaresSerializer
from rest_framework.response import Response
from apps.helpers.common.service import ApiClient
from drf_spectacular.utils import extend_schema
from rest_framework import status
import json
from drf_spectacular.utils import extend_schema
from . import models, serializers

class GetOptimalFaresView(APIView):
    @extend_schema(
        parameters=[GetOptimalFaresSerializer], 
        summary="Поиск по Авиабилетам",  
        tags=["Авиабилеты"],
        responses={200: None}
    )
    def get(self, request):
        serializer = GetOptimalFaresSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response({"response": False, "code": "ERROR", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        api = ApiClient(login="api_test_skyfru", password="api_test_skyfru")
        session_token = api.start_session()
        if not session_token:
            return Response({"error": "Session failed"}, status=status.HTTP_400_BAD_REQUEST)

        fares = api.get_optimal_fares(**serializer.validated_data)
        
        if fares:
            return Response(fares, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Idi nahui"}, status=status.HTTP_400_BAD_REQUEST)