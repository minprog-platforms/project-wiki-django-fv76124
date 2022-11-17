from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from markdown2 import markdown

from . import util
from .forms import NewPageForm
from .forms import EditPageForm

def converting_to_html(title):
    content = util.get_entry(title)
    if content == None:
        return None
    else:
        html = markdown(content)
        return html

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def addpage(request):
    form = NewPageForm()
    return render(request, "encyclopedia/addpage.html", {"form": form})

def save_page(request):
    title = request.POST.get("form_title")
    content = request.POST.get("form_content")
    totalentries = util.list_entries()
    for entry in totalentries:
        if title.lower() == entry.lower():
            return render(request, "encyclopedia/error.html", {
                "error": "This page already exists"
            })
    else:
        content = "#" + title + "\n" + content
        util.save_entry(title, content)
        return redirect("/wiki/" + title)

def search_bar(request):
    if request.method == "POST":
        q = request.POST['q']
        html_content = converting_to_html(q)
        if html_content is not None:
            return render(request, "encyclopedia/wiki.html", {
                "title": q,
                "content": html_content
            })
        else:
            totalentries = util.list_entries()
            results = []
            q = request.POST['q']
            for entry in totalentries:
                if q.lower() in entry.lower():
                    results.append(entry)
            else:
                return render(request, "encyclopedia/results.html",{
                    "results": results
            })    
    
def entry(request, title):
    html_content = converting_to_html(title)
    if html_content == None:
        if title == 'edit':
            form = EditPageForm()
            return render(request, "encyclopedia/edit.html", {
                "form": form
            })
        elif title == 'save-edit':
            return save_edit(request)
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "This page does not exist"
        })
    if html_content is not None:
        return render(request, "encyclopedia/wiki.html", {
            "title": title,
            "content": html_content
    }) 
        

def save_edit(request):
        title = request.POST.get("form_title_edit")
        content = request.POST.get("form_content_edit")
        content = "#" + title + "\n" + content
        util.save_entry(title, content)
        return redirect("/wiki/" + title)
    
    
    

