from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for this month!",
    "february": "Work for at leat 20 minutes every day",
    "march": " Learn Django for at leas 20 minutes every day ",
    "april": " Learn Django for at leas 20 minutes every day ",
    "may": "Eat no meat for this month!",
    "june": " Learn Django for at leas 20 minutes every day ",
    "july": " Learn Django for at leas 20 minutes every day ",
    "august": " Learn Django for at leas 20 minutes every day ",
    "september": " Learn Django for at leas 20 minutes every day ",
    "november": " Learn Django for at leas 20 minutes every day ",
    "december": " Learn Django for at leas 20 minutes every day ",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\'{month_path}\'>{capitalized_month}</a></li>"

    response_data = F"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        respond_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(respond_data)
    except:
        return HttpResponseNotFound("<h4>This month is not supported!</h4>")
