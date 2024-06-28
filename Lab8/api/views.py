from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category
from django.views.decorators import detail_view, view
from django.views.generic import ListView


def home(request):
    return render(request, 'api/index.html')
# ... (other views)


def api_products(request):
    products = Product.objects.all()
    context = {'products': products}  # Pass products to the template
    return render(request, 'djangoProject\api\front\my-product-app\src\Products\index.html', context)


# Product Detail View
@detail_view(model=Product, pk_field='id')
def api_product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
    }
    return JsonResponse(product_data)

# Category Detail View
@detail_view(model=Category, pk_field='id')
def api_category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    category_data = {
        'id': category.id,
        'name': category.name,
    }
    return JsonResponse(category_data)

# Category Products List View
class CategoryProductsListView(ListView):
    model = Product
    template_name = 'products/category_products.html'  # Adjust as needed

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)

# API Endpoint for Category Products
@view(['GET'])
def api_category_products(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        products = category.products.all()
        product_data = [
            {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'count': product.count,
                'is_active': product.is_active,
            }
            for product in products
        ]
        return JsonResponse(product_data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
# from .models import Product, Category

# def api_products(request):
#     products = Product.objects.all()
#     product_data = [product.serialize() for product in products]
#     return JsonResponse(product_data, safe=False)  # Allow nested serialization

# def api_product_detail(request, product_id):
#     try:
#         product = Product.objects.get(pk=product_id)
#         product_data = product.serialize()
#         return JsonResponse(product_data)
#     except Product.DoesNotExist:
#         return JsonResponse({'error': 'Product not found'}, status=404)

# def api_categories(request):
#     categories = Category.objects.all()
#     category_data = [category.serialize() for category in categories]
#     return JsonResponse(category_data, safe=False)  # Allow nested serialization

# def api_category_detail(request, category_id):
#     try:
#         category = Category.objects.get(pk=category_id)
#         category_data = category.serialize()
#         return JsonResponse(category_data)
#     except Category.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status=404)

# def api_category_products(request, category_id):
#     try:
#         category = Category.objects.get(pk=category_id)
#         products = category.products.all()
#         product_data = [product.serialize() for product in products]
#         return JsonResponse(product_data, safe=False)  # Allow nested serialization
#     except Category.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status=404)

# # Helper method for product serialization
# def serialize_product(self):
#     return {
#         'id': self.id,
#         'name': self.name,
#         'price': self.price,
#         'description': self.description,
#         'count': self.count,
#         'is_active': self.is_active,
#     }

# # Helper method for category serialization (similar to serialize_product)

# # Create your views here.


# def moduls(request):
#     return render(request, 'api/moduls.html')
