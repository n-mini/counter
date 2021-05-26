from django import forms

widget_textarea = forms.Textarea(
    attrs={
        'class' :'form-control w-80'
    }
)


class TextForm(forms.Form):

    text = forms.CharField(label='カウントしたい文字列', widget=widget_textarea, max_length=2000)
