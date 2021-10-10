from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import render
from django.views import generic
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerAndLoginRequiredMixin
class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse_lazy("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "../templates/landing.html")


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"
    
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
        return queryset

# def lead_list(request):
#     leads = Lead.objects.all()
#     contex={
#         "leads": leads
#     }
#     return render(request, "leads/lead_list.html", contex)

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"
    
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
        return queryset


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context={
#         'lead':lead
#     }
#     return render(request, "leads/lead_detail.html", context)

class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse_lazy("leads:lead-list")

    def form_valid(self,form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead", 
            from_email="cy0378@gmail.com",
            recipient_list=["yuchengzhi2673@hotmail.com"]

        )
        return super(LeadCreateView, self).form_valid(form)

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         # print(request.POST)
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html",context)
class LeadUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        return queryset
    def get_success_url(self):
        return reverse_lazy("leads:lead-list")
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         'form': form,
#         'lead': lead
#     }
#     return render(request, "leads/lead_update.html",context)
class LeadDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
        return queryset
    def get_success_url(self):
        return reverse_lazy("leads:lead-list")

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         'form':form
#     }
#     return render(request, "leads/lead_update.html",context)

# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         print(request.POST)
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent= Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent,
#             )
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html",context)