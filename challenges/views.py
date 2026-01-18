from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
    "december": None,
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


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
        respond_data = render_to_string('challenges/challenge.html')
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        raise Http404("404.html")
