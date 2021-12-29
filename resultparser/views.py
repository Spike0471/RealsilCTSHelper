from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q

from .models import SimpleQA

# Create your views here.
def index(request):
    project = request.POST.get('Project')
    testsuite = request.POST.get('TestSuite')
    module = request.POST.get('Module')
    testcase = request.POST.get('Testcase')
    failure = request.POST.get('Failure')
    reason = request.POST.get('Reason')
    dbno = request.POST.get('DailyBuild')
    if project is not None and testsuite is not None and module is not None and testcase is not None and failure is not None and reason is not None:
        qaInst = SimpleQA()
        qaInst.project = project
        qaInst.test_suite = testsuite
        qaInst.key1 = module
        qaInst.key2 = testcase
        qaInst.failure = failure
        qaInst.reason = reason
        if dbno is not None:
            qaInst.dbno = dbno
        qaInst.save()
    context = {}
    return render(request,'resultparser/index.html',context)

def record(request):
    context = {}
    return render(request,'resultparser/record.html',context)

def search(request):
    context = {}
    return render(request,'resultparser/search.html',context)

def result(request):
    project = request.POST.get('Project')
    testsuite = request.POST.get('TestSuite')
    module = request.POST.get('Module')
    testcase = request.POST.get('Testcase')
    qas = SimpleQA.objects.filter(Q(project__exact=project) & Q(test_suite__exact=testsuite) & Q(key1__exact=module) & Q(key2__exact=testcase))
    context = {
        'Project' : project,
        'TestSuite': testsuite,
        'Module' : module,
        'Testcase' : testcase,
        'QAMatches' : qas,
        }
    return render(request,'resultparser/result.html',context)
