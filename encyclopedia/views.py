from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def addpage(request):
    return render(request, "encyclopedia/addpage.html")

def converting_to_html(title):
    page = util.get_entry(title)
    html = markdown(page)
    return html

def entry(request, title):
    html_page = converting_to_html(title)
    return render(request, "encyclopedia/wiki.html", {
        "page": html_page
    })
