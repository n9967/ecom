from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get current sess
        cart = self.session.get('session_key')

        #if user is new, no sess
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

#make sure cart is avilable on all pages
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #Get ids from cart
        product_ids = self.cart.keys()
        #Use ids to lookup products in databasemodel
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        #get cart
        ourcart = self.cart
        #update
        ourcart[product_id] = product_qty

        self.session.modified = True
        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        #delete
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def cart_total(self):
        quantities = self.cart
        #get ids
        product_ids = self.cart.keys()
        #lookup
        products = Product.objects.filter(id__in=product_ids)
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total


        
