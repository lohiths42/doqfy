from django.shortcuts import render, redirect, get_object_or_404
from snippets.forms import SnippetForm
from snippets.models import Snippet
from cryptography.fernet import Fernet
import base64

def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.shareable_url = snippet.pk  # Use snippet ID as the shareable URL

            if snippet.secret_key:
                key = Fernet.generate_key()
                snippet.secret_key = base64.urlsafe_b64
                encode(key).decode()
                snippet.encrypt_content()

            snippet.save()
            return redirect('snippet_detail', shareable_url=snippet.shareable_url)
    else:
        form = SnippetForm()
    return render(request, '/Users/lohithsapple/Documents/Django/Doqfy/snippet_ap/snippets/templates/create_snippet.html', {'form': form})


def snippet_detail(request, shareable_url):
    snippet = get_object_or_404(Snippet, shareable_url=shareable_url)

    if snippet.secret_key and snippet.encrypted_content:
        snippet.decrypt_content()

    return render(request, '/Users/lohithsapple/Documents/Django/Doqfy/snippet_ap/snippets/templates/snippet_detail.html', {'snippet': snippet})
