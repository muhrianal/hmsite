from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, AuthorForm, PublisherForm
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    authors = [[author for author in book.authors.all()] for book in books ]

    # nested loop regular version

    # authors = []
    # for book in books:
    #     author_lst = []
    #     for author in book.authors.all():
    #         author_lst.append(author)
    #     author_lst.append(author_lst)

    books_render = {}
    for i in range(len(books)):
        books_render[books[i]] = authors[i]
    print(books_render)


    context = {
        'page_title' : 'Home',
        'books': books_render,
    }
    return render(request, 'home.html', context)

def add_book_page(request):
    book_form = BookForm()
    author_form = AuthorForm()
    publisher_form = PublisherForm()
    
    if request.method == "POST":
        book_form = BookForm(data=request.POST)
        author_form = AuthorForm(data=request.POST)
        publisher_form = PublisherForm(data=request.POST)
        
        print("masuk ke if method")

        if book_form.is_valid() and publisher_form.is_valid() and author_form.is_valid():
            author = author_form.save()
            publisher = publisher_form.save()
            book = book_form.save(author=author, publisher=publisher)
            return redirect('main:home')
        else:
            print('masuk ke else not valid')
            print(book_form.is_valid())
            print(publisher_form.is_valid())
            print(author_form.is_valid())
            book_form = BookForm()
            author_form = AuthorForm()
            publisher_form = PublisherForm()
    
    context = {
        'page_title': 'Add Book',
        'book_form': book_form,
        'author_form': author_form,
        'publisher_form': publisher_form
    }

    return render(request, 'add-book.html', context)


def detail_book_page(request, id):
    book = Book.objects.get(id=id)
    context = {
        'page_title' : 'Detail Book',
        'book_title' : book.title,
        'book_id' : book.id,
        'book_pub_date' : book.publication_date,
        'book_authors' : [author for author in book.authors.all()],
        'publisher' : book.publisher
    }

    return render(request, 'detail-book.html', context)


def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('main:home')


def update_book_page(request, id):
    book = get_object_or_404(Book, id=id)
    book_form = BookForm(initial={'title': book.title, 'publication_date': book.publication_date})

    if request.method == "POST":
        book_form = BookForm(data=request.POST, instance=book)
        if book_form.is_valid():
            book.title = book_form.cleaned_data.get('title')
            book.publication_date = book_form.cleaned_data.get('publication_date')
            book.save()
            return redirect('main:home')
        else:
            book_form = BookForm(initial={'title': book.title, 'publication_date': book.publication_date})


    context = {
        'page_title': "Update Book's Info",
        'book_form': book_form,
        'book_id': id,
    }

    return render(request, 'update-book.html', context)


def similarity_checker(request):
    context = {
        'page_title': 'Similarity Checker'
    }

    return render(request, 'similarity-checker.html', context)