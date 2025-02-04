from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HomeContent, HotelInfo
from .serializers import HomeContentSerializer, HotelInfoSerializer

class HomeView(APIView):
    """ View to display home content """
    def get(self, request):
        home_content = HomeContent.objects.first() 
        hotel_info = HotelInfo.objects.first() 
        home_content_serializer = HomeContentSerializer(home_content)
        hotel_info_serializer = HotelInfoSerializer(hotel_info)

        return Response({
            'home_content': home_content_serializer.data,
            'hotel_info': hotel_info_serializer.data
        })
