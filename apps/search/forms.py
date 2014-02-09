__author__ = 'ben'


from django import forms

username_regex = r'^[\w.@+-]+$'

class SearchForm(forms.Form):

    username = forms.RegexField(username_regex, required=False)
    email = forms.EmailField(required=False)
    question = forms.CharField(widget=forms.TextInput(attrs={'size':50,}),required=False)
    class Meta():
        empty_permitted = False
    # luck = forms.CharField()

    #
    # fields = ('user','email','content')

