import requests


class Cart:
    def __init__(self,request):
        self.session=request.session
        self.cart=self.session.get('CART_SESSION_ID')

        if not self.cart:
            self.cart=self.session["CART_SESSION_ID"]={}

    def unique_id_generator(self,id,name):
        result=f'{name}-{id}'
        return  result

    def add(self, product, quantity, color="none", size="none"):
        unique = self.unique_id_generator(product.id,product.title_en)

        if unique not in self.cart:
            self.cart[unique] = {
                'quantity': int(quantity),  # تبدیل به عدد صحیح در زمان ایجاد
                'price': str(product.price),
                'color': color,
                'size': size,
                'id': product.id
            }
        else:
            self.cart[unique]["quantity"] += int(quantity)  # اطمینان از اینکه مقدار فعلی نیز عدد صحیح است

        self.session.modified = True

    def delete(self, product_id, product_name):
        # Generate the unique key for the product to be deleted
        unique = self.unique_id_generator(product_id, product_name)

        # Remove the product from the cart if it exists
        if unique in self.cart:
            del self.cart[unique]
            self.session.modified = True

    def total(self):
        return sum(int(item['quantity']) * float(item['price']) for item in self.cart.values())











