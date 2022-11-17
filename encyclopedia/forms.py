from django import forms


# defines form class with field page_title and page_content
class NewPageForm(forms.Form):
    form_title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Title"}), label='Title', max_length=100)
    form_content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Content in markdown"}), label='Content', max_length=500)
    
class EditPageForm(forms.Form):
    form_title_edit = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label='Title', max_length=100)
    form_content_edit = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label='Content', max_length=500)
    
    