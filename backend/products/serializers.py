from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            # 'get_discount' # No need for my_discount and get_my_discount can just use as is instead 
            'my_discount',
        ]

    def get_my_discount(self, obj):
        # print(obj.id)
        # get foreign key stuff
        # obj.user -> obj.username

        if not hasattr(obj, 'id'):
            return None
        
        # Or this has the same effect
        # if not isinstance(obj, Product):
        #     return None
        
        return obj.get_discount()
    

# can have multiple serializers for the same model