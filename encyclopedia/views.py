from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseNotFound
import markdown2
import random

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(label="Content (Markdown)", widget=forms.Textarea)

class EditEntryForm(forms.Form):
    content = forms.CharField(label="Content (Markdown)", widget=forms.Textarea)

def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry_page(request, title):
    content_md = util.get_entry(title)
    if content_md is None:
        return render(request, "encyclopedia/notfound.html", {"title": title})
    content_html = markdown2.markdown(content_md)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content_html": content_html
    })

def search(request):
    query = request.GET.get("q", "") or request.POST.get("q", "")
    if not query:
        return redirect("encyclopedia:index")

    # exact match -> redirect to entry
    entries = util.list_entries()
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("encyclopedia:entry", title=entry)

    # partial matches -> show results
    results = [e for e in entries if query.lower() in e.lower()]
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })


def new_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].strip()
            content = form.cleaned_data["content"]
            # If entry exists -> show error
            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/new.html", {
                    "form": form,
                    "error": "An entry with that title already exists."
                })
            util.save_entry(title, content)
            return redirect("encyclopedia:entry", title=title)
    else:
        form = NewEntryForm()
    return render(request, "encyclopedia/new.html", {"form": form})

def edit_page(request, title):
    current = util.get_entry(title)
    if current is None:
        return HttpResponseNotFound("Page not found.")
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect("encyclopedia:entry", title=title)
    else:
        form = EditEntryForm(initial={"content": current})
    return render(request, "encyclopedia/edit.html", {"title": title, "form": form})

def random_page(request):
    entries = util.list_entries()
    if not entries:
        return redirect("encyclopedia:index")
    title = random.choice(entries)
    return redirect("encyclopedia:entry", title=title)