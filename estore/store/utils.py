import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False, 'taxes': 0, 'grand_total': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = product.price * cart[i]['quantity']

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'id': product.id,
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'digital': product.digital,
                'get_total': total,
            }
            items.append(item)

            if not product.digital:
                order['shipping'] = True

        except Product.DoesNotExist:
            pass

    # Apply tax calculation based on the total
    total_amount = order['get_cart_total']
    if total_amount < 50:
        order['taxes'] = total_amount * 0.10  # 10% tax if total is less than 50
    elif 50 <= total_amount < 100:
        order['taxes'] = total_amount * 0.05  # 5% tax if total is between 50 and 100
    else:
        order['taxes'] = total_amount * 0.025  # 25% tax if total is above 100

    # Calculate grand total including taxes
    order['grand_total'] = total_amount + order['taxes']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}

	
def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Product.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']), # negative quantity = freebies
		)
	return customer, order

