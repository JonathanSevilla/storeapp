from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    BrandSerializer,
    StoresSerializer,
    DealsSerializer,
    SubscriptionSerializer
)
from .models import (
    Brand,
    Stores,
    Deals,
    Subscription    
)

# Create your views here.

@api_view(['GET','POST'])
def post_subscriptions(request):
        
    if request.method == 'GET':
        subscription = Subscription.objects.all()
        queryset = SubscriptionSerializer(subscription, many=True)

        return Response(queryset.data)
    
    if request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST'])
def brands(request):

    if request.method == 'GET':
        brand = Brand.objects.all()
        queryset = BrandSerializer(brand, many=True)

        return Response(queryset.data)

    if request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def store(request):

    if request.method == 'GET':
        store = Stores.objects.all()
        queryset = StoresSerializer(store, many=True)  

        return Response(queryset.data)

    if request.method == 'POST':
        serializer = StoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST'])
def deals(request):

    if request.method == 'GET':
        deals = Deals.objects.all()
        queryset = DealsSerializer(deals, many=True)  

        return Response(queryset.data)

    if request.method == 'POST':
        serializer = DealsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def brand(request):
    if request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListByStoreView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):     
        store_id = self.kwargs['store_id']
        queryset = Subscription.objects.filter(store=store_id)
        return queryset