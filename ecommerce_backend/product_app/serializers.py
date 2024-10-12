from rest_framework import serializers
from .models import ProImage, Product

class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProImage
        fields = ["id", "product", "image_url"]

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True)

    class Meta:
        model = Product
        fields = ["id", "title", "description", "num_of_prod_on_stock", "price", "images", "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            new_product_image = ProImage.objects.create(product=product, image=image)
        return product
    
    def update(self, instance, validated_data):
        # Handle image update if provided
        uploaded_images = validated_data.pop("uploaded_images", None)
        if uploaded_images:
            for image in uploaded_images:
                ProImage.objects.create(product=instance, image=image)
        # Update other fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.num_of_prod_on_stock = validated_data.get('num_of_prod_on_stock', instance.num_of_prod_on_stock)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance