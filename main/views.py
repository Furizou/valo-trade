from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Valorant Trade',
        'name': 'Kukuh Cikal Yuntama',
        'class': 'PBP F',
        'username': 'Furizou#9999',
    }

    return render(request, "main.html", context)