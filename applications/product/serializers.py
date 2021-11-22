from rest_framework import serializers

from applications.product.models import Product, ProductImage
from applications.review.serializers import ReviewSerializer


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            # print(url)
            requests = self.context.get('request')
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
             representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = ProductImageSerializer(ProductImage.objects.filter(product=instance.id),
                                                          many=True, context=self.context).data
        representation['reviews'] = ReviewSerializer(instance.review.filter(product=instance.id, many=True)).data
        return representation


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = ProductImageSerializer(ProductImage.objects.filter(product=instance.id),
                                                          many=True, context=self.context).data
        representation['reviews'] = ReviewSerializer(instance.review.filter(product=instance.id), many=True).data
        return representation
