from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Cart, CartItem

from home.models import Product


# Create your views here.
def view(request):
   try:
       the_id = request.session["cart_id"]
   except:
       the_id = None
   if the_id:
        products = Product.objects.all()
        cart = Cart.objects.get(id = the_id)
        context = {
            "cart": cart,
            "products": products,
        }
   else:
        empty_message = "your cart is empty"
        context  ={
            "empty" :True,
            "empty_message":empty_message,
        }

   return render(request, "cart.html", context)

def remove_cart(request,id):
    cart_item_delete = Cart.objects.get(id=id)
    cart_item_delete.delete()
    return HttpResponseRedirect(reverse("view"))




def update_cart(request, slug):
    request.session.set_expiry(12000)  #the cart items will be removed automatically after 12000s

    try:
        qty = request.GET.get("qty")
        update_qty  =True
        print(qty)
    except:
        qty = None
        update_qty = False


    try:
        the_id = request.session["cart_id"]  #check if there is a cart id else it will create it in the except case
    except:
        new_cart = Cart()
        new_cart.save()
        request.session["cart_id"] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)


    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    
    cart_item ,created  =  CartItem.objects.get_or_create(cart = cart,product = product) # creating a cart item where each cart is unique to each other soo if a cart has a product quantity of 10 that sam equantity will not be followed by anither cart of same product
    if update_qty and qty:
        if int(qty) ==0:
            cart_item.delete()  #to remove the item if the quantity of the product is 0
        else:
            cart_item.quantity  = qty
            cart_item.save()
   
    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total   =  float(item.product.price) * item.quantity   #as in item there will be price of multiple products soo item.product.price will take the price of each product
        new_total = new_total + line_total
    request.session["items_total"] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse("view"))



   
