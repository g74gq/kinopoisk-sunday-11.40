from django.shortcuts import render

def home(request):
    return render(request, 'gn_01/home.html')

def movies_list(request):
    return render(request, 'gn_01/movies_list.html')

def actors_list(request):
    return render(request, 'gn_01/actors_list.html')

def directors_list(request):
    return render(request, 'gn_01/directors_list.html')

def generes_list(request):
    return render(request, 'gn_01/generes_list.html')

def composers_list(request):
    return render(request, 'gn_01/composers_list.html')

def movies_detail(request, movie_id):
    return render(request, 'gn_01/movies_detail.html')

def actors_detail(request, actors_id):
    return render(request, 'gn_01/actors_detail.html')

def directors_detail(request, directors_id):
    return render(request, 'gn_01/directors_detail.html')

def generes_detail(request, generes_id):
    return render(request, 'gn_01/generes_detail.html')

def composers_detail(request, composers_id):
    return render(request, 'gn_01/composers_detail.html')