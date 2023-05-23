from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Post
#class PostBaseForm(forms.Form):
#    CATEGORY_CHOICES =[
#        ('1','일반'),
#        ('2','계정'),
#    ]
#    image = forms.ImageField(label='이미지')
#    content = forms.CharField(label='내용',widget=forms.Textarea, required=True)
#    category = forms.ChoiceField(label='카테고리',choices=CATEGORY_CHOICES)

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  '__all__'

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields=['image','content']

    def cleaned_content(self) -> Optional[Dict[str,Any]]:
        data = self.cleaned_data["content"]
        if "비속어" == data:
            raise forms.ValidationError("비속어는 사용 불가!")

        return data
    
class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields=['image','content']

class PostDetailForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields['content'].widget.attrs['disabled'] = True
