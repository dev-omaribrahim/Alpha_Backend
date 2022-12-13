def build_cart_methods_context(cart):
    return {
        "total_products_price": cart.get_total_products_price(),
        "total_commission_price": cart.get_total_commissions(),
        "total_cart_price": cart.get_total_cart_price(),
    }
