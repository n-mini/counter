from django.views.generic.edit import FormView

from . import forms

class Index(FormView):

    form_class = forms.TextForm
    template_name = 'index.html'

    def form_valid(self, form):
        data = form.cleaned_data
        text = len(data['text'])

        ctxt = self.get_context_data(text=text,form=form)
        return self.render_to_response(ctxt)
