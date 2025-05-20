from django.shortcuts import render

def index(request):
    products = [
        {"Name": "laptop", "Price": 1000},
        {"Name": "phone", "Price": 500},
        {"Name": "tablet", "Price": 300},
    ]
    context = {
        "products": products,
    }
    return render(request, "index.html", context)
