from django.shortcuts import render

def cart_summary(request):
    content = {}
    return render(request, "cart_summary.html", content )

def cart_add(request):
    content = {}
    return render(request, "cart_add.html", content )

def cart_delete(request):
    content = {}
    return render(request, "cart_delete.html", content )

def cart_update(request):
    content = {}
    return render(request, "cart_update.html", content )
  
