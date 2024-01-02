import json

from apps.product.models import ProductModel
from apps.promotion.models import CouponModel


def cookieCart(request):
    try:
        coupon_d = json.loads(request.COOKIES.get('cupon'))
        coupon_code = coupon_d['cupon_code']
        coupon_exits = CouponModel.objects.filter(coupon_code=coupon_code).count()
        if coupon_exits == 1:
            coupon_object = CouponModel.objects.get(coupon_code=coupon_code)
            coupon = coupon_object.coupon_code
            amount = coupon_object.amount
        else:
            coupon = "None"
            amount = 0
    except:

        coupon = "None"
        amount = 0

    try:
        cart = json.loads(request.COOKIES.get('cart'))

    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False, 'coupon_code': coupon,
             'coupon_amount': amount}
    cartItems = order['get_cart_items']
    cartTotal = order['get_cart_total']

    for i in cart:
        try:
            cartItems += int(cart[i]["quantity"])

            product = ProductModel.objects.get(uuid=i)
            total = float((float(product.price) * int(cart[i]['quantity'])))
            order['get_cart_total'] += total
            order['get_cart_items'] += int(cart[i]['quantity'])
            print(order['get_cart_items'])

            cartTotal = order['get_cart_total']

            if 'color' in cart[i]:
                color = cart[i]['color']
            else:
                color = "undefined"

            if 'size' in cart[i]:
                size = cart[i]['size']
                first_size = size
            else:
                size = "undefined"
                first_size = size

            item = {
                'product': product,
                'quantity': cart[i]["quantity"],
                'get_total': total,
                'color': color,
                'size': size,
                'first_size': first_size
            }
            items.append(item)
            if not product.digital:
                order['shipping'] = True

        except:
            pass

    return {"order": order, "items": items, "cartItems": cartItems, 'cartTotal': cartTotal}


def get_cart(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    cartTotal = cookieData['cartTotal']
    order = cookieData['order']
    items = cookieData['items']

    return {"order": order, "items": items, "cartTotal": cartTotal, 'cartItems':cartItems}
