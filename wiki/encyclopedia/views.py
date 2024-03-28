from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def search(request):
    if request.method == "POST":
        q = request.POST.get('q')
        content = util.get_entry(q)
        if content != None:
            return render(request, "encyclopedia/entry.html", {
                "title": q,
                "content": content
            })
        else:
            entries = util.list_entries()
            recommend = []
            for entry in entries:
                if q.lower() in entry.lower():
                    recommend.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommend": recommend, "q": q
            })
        