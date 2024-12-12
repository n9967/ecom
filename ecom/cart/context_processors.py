from .cart import Cart

#create context processor so cart can work on every page

def cart(request):
    #return the default data from cart
    return{'cart': Cart(request)}