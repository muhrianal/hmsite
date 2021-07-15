from django.forms import ModelForm
from .models import Book, Publisher, Author

class BookForm(ModelForm):
    def save(self, author=None, publisher=None, commit=True):

        title = self.cleaned_data.get('title')
        pub_date = self.cleaned_data.get('publication_date')

        book = Book(title=title, publication_date=pub_date, publisher=publisher)
        book.save()
        if commit:
            book.authors.set([author,])
        return book
    class Meta:
        model = Book
        fields = ['title', 'publication_date']

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
