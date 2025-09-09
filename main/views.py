from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Fadhil Al Afifi Fajar',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
