from decimal import Decimal
from django.conf import settings
from productos.models import Producto

class Compra(object):

    def __init__(self, request):
        self.session = request.session
        compra = self.session.get(settings.CART_SESSION_ID)
        if not compra:
            compra = self.session[settings.CART_SESSION_ID] = {}
        self.compra = compra

    def add(self, producto, costo, cantidad = 1):
        product_id = str(producto.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'cantidad': cantidad, 'costo': str(costo)}

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.compra
        

    def remove(self, producto):
        product_id = str(producto.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.compra.keys()
        products = Producto.objects.filter(id__in=product_ids)
        for product in products:
            self.compra[str(product.id)]['product'] = product

        for item in self.compra.values():
            item['costo'] = Decimal(item['costo'])
            item['totalcosto'] = item['costo'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.compra.values())

    def get_total_price(self):
        return sum(Decimal(item['costo']) * item['cantidad'] for item in self.compra.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
