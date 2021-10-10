from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail
class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)

class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse_lazy("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password("yuchengzhi1") 
        user.save()
        Agent.objects.create(
            user = user,
            organization = self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent',
            message="this is a message!",
            from_email="sdsd@123.com",
            recipient_list=[user.email]

        )
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)

class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse_lazy("agents:agent-list")
    def get_queryset(self):
        return Agent.objects.all()

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_success_url(self):
        return reverse_lazy("agents:agent-list")
    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)