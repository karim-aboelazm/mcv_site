from .serializers import *
from .models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated


# All Cars Retrive Api
class CarListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# Cars details Api
class CarDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# Cars filter search Api
class CarFilterApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(eslf, request, kw, format=None):
        car = Car.objects.filter(Q(car_id__icontains=kw))
        serializer = CarSerializer(car, many=True, context={"request": request})
        return Response({"car_filter": serializer.data})


# All CarDiagnostic Retrive Api
class CarDiagnosticListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car_Diagnostic.objects.all()
    serializer_class = CarDiagnosticSerializer


# CarDiagnostic Detail Api
class CarDiagnosticDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car_Diagnostic.objects.all()
    serializer_class = CarDiagnosticSerializer


# CarDiagnostic Filter search Api
class CarDiagnosticFilterApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(eslf, request, kw, format=None):
        diagnostic = Car_Diagnostic.objects.filter(
            Q(diagnostic_sarial__icontains=kw) | Q(diagnostic_error_type__icontains=kw)
        )
        serializer = CarDiagnosticSerializer(diagnostic, many=True)
        return Response({"diagnostic_filter": serializer.data})


# All Drivers Retrive Api
class DriverListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


# Driver detail Api
class DriverDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


# Driver filter search Api
class DriverFilterApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(eslf, request, kw, format=None):
        driver = Driver.objects.filter(
            
            Q(drive_car__car_id__icontains=kw)
            
        )
        serializer = DriverSerializer(driver, many=True)
        return Response({"driver_filter": serializer.data})
    
class AdminListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MCVUser.objects.all()
    serializer_class = McvUserSerializer
    
# Admin Detail Api
class AdminDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MCVUser.objects.all()
    serializer_class = McvUserSerializer
  
# Admin filter search Api  
class AdminFilterApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,kw,format=None):
        admin = MCVUser.objects.filter(
            Q(full_name__icontains=kw))
        serializer = McvUserSerializer(admin,many=True,context={'request':request})
        return Response({'mcv_user_filter':serializer.data})