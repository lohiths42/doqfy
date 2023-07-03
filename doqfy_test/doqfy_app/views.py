from django.shortcuts import render,redirect

# Create your views here.
from .forms import URLForm
from .models import URL


def url_shortener(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_object =form.save()
            print(url_object.short_url)
            return render(request, '/Users/lohithsapple/Documents/Django/Doqfy/doqfy_test/templates/success.html',{'short_url': url_object.short_url})
    else:
        form = URLForm()
    return render(request, '/Users/lohithsapple/Documents/Django/Doqfy/doqfy_test/templates/url_form.html', {'form': form})


def redirect_to_original_url(request, short_url):
    try:
        url_object = URL.objects.get(short_url=short_url)
        return redirect(url_object.original_url)
    except URL.DoesNotExist:
        raise Http404("Short URL does not exist.")



# def home(request): # new
#     return render(request, '/Users/lohithsapple/Documents/Django/Doqfy/doqfy_test/templates/index.html')
