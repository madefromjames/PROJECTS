from django.shortcuts import render, redirect
from django.urls import reverse
from random import choice
import markdown2

from . import util
from django import forms


class EditForm(forms.Form):
    content = forms.CharField(
        label="Markdown",
        widget=forms.Textarea()
    )

def md_to_html(text):
    return markdown2.markdown(text)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page does not exist"
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": md_to_html(content)
    })

def search(request):
    if request.method == "POST":
        q = request.POST.get('q')
        content = util.get_entry(q.lower())
        if content != None:
            return redirect(reverse("entry", kwargs={"title": q}))
        else:
            entries = util.list_entries()
            recommend = []
            for entry in entries:
                if q.lower() in entry.lower():
                    recommend.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommend": recommend, "q": q
            })
        
    return render(request, "encyclopedia/index.html")

def new_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exist"
            })
        else:
            util.save_entry(title, content)
            return redirect(reverse("entry", kwargs={"title": title}))

    return render(request, "encyclopedia/newpage.html")

def edit(request):
    if request.method == "POST":
        title = request.POST.get("title")
        form = EditForm(request.POST)
        if form.is_valid():
            new_content = form.cleaned_data["content"]
            new_content = '\n'.join(line.strip() for line in new_content.splitlines())
            util.save_entry(title, new_content)
            return redirect(reverse("entry", args=[title]))
   
    title = request.GET.get('title')
    existing_content = util.get_entry(title)
    form = EditForm({'content': existing_content})
    return render(request, "encyclopedia/edit.html", {
        "title": title, "form": form
    })

def random(request):
    any_page = choice(util.list_entries())
    return redirect(reverse("entry", args=[any_page]))
