from django.shortcuts import render

# Create your views here.


"""
LANDING PAGE
"""
def home(request):
	return render(request, 'home/index.html')

def app(request):
	return render(request, 'app.html', {'noheader': True, 'nofooter': True})


def handler404(request):
	return render(request, '404.html', {'noheader': True, 'nofooter': True}, status=404)


def handler500(request):
	return render(request, '500.html', {'noheader': True, 'nofooter': True}, status=500)