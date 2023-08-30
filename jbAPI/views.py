from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view
from dashboard.models import DashboardModel
from dashboard.serializers import DashboardModelSerializer

@api_view(['GET'])
def dashboard_model_list(request):
    queryset = DashboardModel.objects.all()
#    serializer = DashboardModelSerializer(queryset, many=True)
    serializer = DashboardModelSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)
    
