from rest_framework import serializers


class CartSerializer(serializers.Serializer):
    """
    Serializer for:
    * returning serialized/deserialized data
    * validate data
    * Act as Encapsulation for session's Cart class:
        - set:
            Prevent access session's methods directly with data,
            First it makes sure data is Valid using fields and it's validators,
            also we can make restriction as much as we need.
        - get:
            Perform Type Conversion on methods returns str => int,
            attach additional info for each product.
    """

    def __init__(self, instance=None, data=None, cart=None, request=None, **kwargs):
        super().__init__(instance, data, **kwargs)
        self.cart = cart
        self.request = request

    product_crafted_id = serializers.CharField(max_length=100, required=False)
    product_id = serializers.CharField(max_length=80, required=True)
    price = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1)
    color = serializers.CharField(max_length=50, required=True)
    size = serializers.CharField(max_length=10, required=True)
    commission = serializers.IntegerField(min_value=1)
    total_products_price = serializers.SerializerMethodField()
    total_commission_price = serializers.SerializerMethodField()
    total_cart_price = serializers.SerializerMethodField()

    def add_product(self):
        # if self.is_valid(raise_exception=True):
        # validation goes here
        data = self.request.data
        self.cart.add(data)

    def update_product(self):
        # if self.is_valid(raise_exception=True):
        # validation goes here
        data = self.request.data
        self.cart.update(data)

    def remove_product(self):
        # if self.is_valid(raise_exception=True):
        # validation goes here
        data = self.request.data
        self.cart.remove(data)

    def get_total_products_price(self, obj):
        value = int(self.cart.get_total_products_price())
        return value

    def get_total_commission_price(self, obj):
        # convert the result to int
        value = int(self.cart.get_total_commissions())
        return value

    def get_total_cart_price(self, obj):
        # convert the result to int
        value = int(self.cart.get_total_cart_price())
        return value

    # def validate_product_id(self, value):
    #     pass

    # def validate_price(self, value):
    #     pass

    # def validate_quantity(self, vlaue):
    #     pass

    # def validate_color(self, value):
    #     pass

    # def validate_size(self, value):
    #     pass

    # def validate_commission(self, value):
    #     pass

    # def validate_product_crafted_id(self, value):
    #     expected_id = self.product_id + self.color + self.size
    #     if value != expected_id:
    #         raise serializers.ValidationError(
    #             "Unexcpected value for prduct_crafted_id !"
    #         )

    #     return value
