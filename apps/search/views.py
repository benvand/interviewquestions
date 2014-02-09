__author__ = 'ben'
from django.views.generic import ListView, TemplateView, FormView

from forms import SearchForm

from apps.justdifferentusers.models import IQUser
from apps.quest.models import Question





# class SearchView(TemplateView):
#     # form_class = SearchForm
#     context_object_name = "results"
#     template_name = "search/search.html"
#
#     def get_queryset(self):
#         return (None,)
#
#     def get_context_data(self, **kwargs):
#         context = super(TemplateView, self).get_context_data()
#         context.update(form = SearchForm
#         )
#         return context


class SearchView(FormView):
    form_class = SearchForm
    context_object_name = "results"
    template_name = "search/search.html"

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        if kwargs.has_key('filled_form'):
            extra_context = {}
            extra_context.update(by_username = IQUser.objects.filter(username = kwargs['filled_form'].cleaned_data['username']))
            extra_context.update(by_emails = IQUser.objects.filter(email = kwargs['filled_form'].cleaned_data['email']))
            extra_context.update(by_question = [])
            for i in Question.objects.all():
                for word in [word.strip() for word in kwargs['filled_form'].cleaned_data['question'].split(' ')]:
                    if word and word in i.question:
                        extra_context['by_question'].append(i)
            context.update(extra_context)
        print context
        return context

    def get(self, request, *args, **kwargs):
        filled_form = self.form_class(request.GET)
        #Don't clean data if nothing was submitted
        if filled_form.has_changed():
            #don't do processing if errors
            if filled_form.is_valid():
                return self.render_to_response(self.get_context_data(filled_form=filled_form, form = filled_form))
        return super(FormView, self).get(self, request ,*args, **kwargs)
