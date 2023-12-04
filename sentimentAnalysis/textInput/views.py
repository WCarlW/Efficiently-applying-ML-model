from django.shortcuts import render, redirect
from .forms import DweetForm
from .models import Dweet, Profile, Sentiment
from django.utils import timezone

'''Choose which model to use'''
# from analysis.trained_model.use_local_model import analyze

from analysis.trained_model.use_online_model import analyze
'''***************************'''

def perform_sentiment_analysis(body):
    if body:
        return(analyze(body))
    return 'Not Analyzed'

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user

            sentiment = perform_sentiment_analysis(dweet.body)
            sentiment_obj, created = Sentiment.objects.get_or_create(sentiment=sentiment)
            sentiment_obj.analyzed_at = timezone.now()
            sentiment_obj.save()

            dweet.sentiment = sentiment_obj
            dweet.save()
            return redirect("textInput:dashboard")

    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    
    return render(request, "dashboard.html", {"form": form, "dweets": followed_dweets})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "profile.html", {"profile": profile})