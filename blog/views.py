from django.shortcuts import render
from django.utils.translation import activate, get_language, gettext as _


def translate(language, text):
    cur = get_language()
    try:
        activate(language)
        text = _('Hello in this site')
    finally:
        activate(cur)
    return text


def home(request):
    m = translate(language='fr', text='Hello in this site')
    context = {
        'm': m,
    }
    return render(request, 'index.html', context)
