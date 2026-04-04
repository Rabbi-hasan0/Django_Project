from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ecomapp.common_func import checkUserPermission
from ecomapp.models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# ------------Function-------------
@login_required
def paginate_data(request, page_num, data_list):
    items_per_page, max_pages = 2, 10
    paginator = Paginator(data_list, items_per_page)
    last_page_number = paginator.num_pages

    try:
        data_list = paginator.page(page_num)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)

    current_page = data_list.number
    start_page = max(current_page - int(max_pages / 2), 1)
    end_page = start_page + max_pages

    if end_page > last_page_number:
        end_page = last_page_number + 1
        start_page = max(end_page - max_pages, 1)

    paginator_list = range(start_page, end_page)

    return data_list, paginator_list, last_page_number




#------------view function-------------
def dashboard_view(request):
    return render(request, 'home/home.html')

@login_required
def setting_view(request):
    get_setting_menu=MenuList.objects.filter(module_name='setting', is_active=True)
    contex = {
        'get_setting_menu': get_setting_menu,
    }
    return render(request, 'home/setting_dashboard.html', contex)

@login_required
def product_main_category_view(request):
    if not checkUserPermission(request, "can_view", "backend/product-main-category-list/"):
        return render(request,"403.html")

    product_main_categories = ProductMainCategory.objects.filter(is_active=True).order_by('-id')
    page_number = request.GET.get('page', 1)
    product_main_categories, paginator_list, last_page_number = paginate_data(request, page_number, product_main_categories)

    context = {
        'paginator_list': paginator_list,
        'last_page_number': last_page_number,
        'products': product_main_categories,
    }
    return render(request, "product/main_category_list.html", context)  

@login_required
def add_product_main_category(request):
    if not checkUserPermission(request, "can_add", "backend/product-main-category-list/"):
        return render(request,"403.html")
    
    if request.method == "POST":
        main_cat_name = request.POST.get('main_cat_name')
        cat_slug = request.POST.get('cat_slug')
        description = request.POST.get('description')
        cat_image = request.FILES.get('cat_image')

        product_main_category = ProductMainCategory(
            main_cat_name=main_cat_name,
            cat_slug=cat_slug,
            description=description,
            cat_image = cat_image,
            created_by=request.user
        )

        product_main_category.save()
        messages.success(request, 'Product Main Category added successfully.')
        return redirect('product_main_category_list')

    return render(request, "product/add_product_main_category.html")
    

def login(request):
    pass
def logout(request):
    pass

