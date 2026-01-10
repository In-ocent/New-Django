from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "<h1>Eat no meat for this month!</h1>",
    "february": "<h1>Work for at leat 20 minutes every day</h1>",
    "march": "<h1> Learn Django for at leas 20 minutes every day </h1>",
    "april": "<h1> Learn Django for at leas 20 minutes every day </h1>",
    "may": "<h1>Eat no meat for this month!</h1>",
    "june": "<h1> Learn Django for at leas 20 minutes every day </h1>",
    "july": "<h1> Learn Django for at leas 20 minutes every day </h1>",
    "august": "<h1> Learn Django for at leas 20 minutes every day </h1>",
    "september": "<h1> Learn Django for at leas 20 minutes every day </h1>",
    "november": "<h1> Learn Django for at leas 20 minutes every day </h1>",
    "december": "<h1> Learn Django for at leas 20 minutes every day </h1>",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
