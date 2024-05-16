from django.shortcuts import render, redirect
from .forms import DweetForm
from .models import Dweet, Profile, Sentiment
from django.utils import timezone
from django.contrib.auth.models import User


'''*****Choose which deployed model to use*****'''
'''A. locally deployed model'''
# from analysis.trained_model.use_local_model import analyze

'''B. cloud deployed model'''
# from analysis.trained_model.use_online_model import analyze

'''C. Docker deployed model (the container is stored locally)'''
# from django.http import JsonResponse
# import requests
# DOCKER_API_URL = "http://127.0.0.1:3000" # container address
'''***************************'''


def perform_sentiment_analysis(body):
    if body:
        '''A. & B. locally deployd model OR cloud deployed model'''
        # return(analyze(body))

        '''C. Docker deployed model'''
        # data = {"text": body}
        # response = requests.post(f'{DOCKER_API_URL}/analyze_sentiment', json=data)
        # # Check if the request was successful
        # if response.status_code == 200:
        #     # Attempt to parse JSON, handle JSONDecodeError
        #     result = response.json()
        #     sentiment = result.get('sentiment', '')
        #     return sentiment
        # else:
        #     # Handle error
        #     return JsonResponse({'error': 'Failed to analyze sentiment'}, status=500)

    # No model selected or something went wrong
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
    
    # Create a mock user if the current user is not authenticated
    if not request.user.is_authenticated:
        mock_user = User.objects.get_or_create(username='mockuser')[0]
        request.user = mock_user

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