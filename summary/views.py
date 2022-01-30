from django.shortcuts import render

from datetime import date
from django.contrib.auth.decorators import login_required
from summary.models import Summary
from .algorithms.scoring import scoring_algorithm
from .algorithms.frequency import extraction, frequency_algorithm

# Create your views here.
def index(request):
    return render(request, 'summary/index.html')


def summary_page(request):
    url = request.GET.get('url')
    long_text = request.GET.get('long-text')
    sentence_no = int(request.GET.get('number'))
    algorithm = request.GET.get('algorithm')
    result_list = []

    if url:
        long_text = extraction.extract(url)  # text extraction using BS
        original_text = url
    else:
        original_text = long_text

    if algorithm == '1':
        result_list = scoring_algorithm.scoring_main(long_text, sentence_no)
    elif algorithm == '2':
        result_list = frequency_algorithm.frequency_main(long_text, sentence_no)

    summary = ' '.join(result_list)

    context = {'data': summary, 'original_text': original_text}
    return render(request, "summary/index.html", context)

@login_required
def save_summary(request):
    summary = request.POST.get('summary')
    topic = request.POST.get('topic')
    if len(topic) < 50:
        heading = topic
    else:
        heading = topic[:50] + '...'

    summaryTb = Summary(user=request.user, body=summary, original_link=heading, data_created=date.today())
    summaryTb.save()
    context = {'message': 'success'}
    return render(request, "summary/index.html", context)


def history(request):
    summary = Summary.objects.filter(user=request.user).order_by('-id')
    context = {'data': summary}
    return render(request, "summary/history.html", context)


def history_topic(request):
    if request.method == 'GET':
        topic = request.GET.get('topic')
        summary = request.GET.get('body')
        context = {'topic': topic, 'body': summary}
        return render(request, "summary/history_topic.html", context)
