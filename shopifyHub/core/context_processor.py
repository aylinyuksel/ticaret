from core.models import Product, Category, Vendor, ProductImages, ProductReview,  CartOrder, CartOrderItems, wishlist_model, Address
from django.db.models import Min, Max
from django.contrib import messages


def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))

    try:
        wishlist = wishlist_model.objects.filter(user=request.user)
    except:
        messages.warning(request,"You need to login before accessing your wishlist.")
        wishlist = 0

    # address = Address.objects.get(user=request.user)
    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return { 
        'categories':categories,
        'wishlist':wishlist,
        'address':address,
        'vendors':vendors,
        'min_max_price':min_max_price,

    }