from django.shortcuts import render
# main page
def polls(request):
    return render(request, "poll/polls.html")

# result page
def result(request):
    return render(request, "poll/result.html")