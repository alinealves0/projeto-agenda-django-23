from django.contrib import messages
from django.shortcuts import render

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    messages.info(request, 'Um texto qualquer')
    messages.success(request, 'Um texto qualquer')
    messages.warning(request, 'Um texto qualquer')
    messages.error(request, 'Um texto qualquer')
    

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
    

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )