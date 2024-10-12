from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product_app.serializers import ProductSerializer
from product_app.models import Product


class ProductView(APIView):
#get data
    def get(self, request, *args, **kwargs):
        # single product detail view
        pk = kwargs.get('pk')
        if pk:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data)
        
        qs = Product.objects.all()
        serializer = ProductSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)
#post
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            # will return status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#update
    def put(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete
    def delete(self, request, pk, *args, **kwargs):
        try:
            product = get_object_or_404(Product, pk=pk)
            # Delete associated images
            for image in product.images.all():
                image.image.delete(save=False)
            product.delete()
            return JsonResponse({'message': f'Product with id {pk} deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)