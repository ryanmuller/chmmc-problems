from chmmc.problems.models import Problem, Evaluation, Test
from random import random
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def home(request):
    return render_to_response('home.html', locals())

def do_random_problem(request):
    
    no_eval_problems = Problem.objects.filter(evaluation__isnull=True)
    all_problems = Problem.objects.all()
    
    no_eval_ratio = 1.0*no_eval_problems.count()/all_problems.count()
    
    # "usually" pick a non-evaluated problem
    if no_eval_ratio > 0 and random() < 0.5 + 0.5*no_eval_ratio:
        problem = no_eval_problems.order_by('?')[0]
    else:
        problem = all_problems.order_by('?')[0]
    
    return do_problem(request, problem.id)
    
    
def do_problem(request, problem_id):
    
    problem = get_object_or_404(Problem, pk=problem_id)
    return render_to_response('evaluation.html', locals())


def submit_eval(request):
    
    post = request.POST.copy()
    
    problem = Problem.objects.get(id=post["problem"])
    
    if post["comments"] == "":
        post["comments"] = "None submitted."
    
    Evaluation.objects.create(evaluator=request.user, problem=problem,
                              answer=post["answer"], comments=post["comments"],
                              difficulty=post["difficulty"], time=post["time"])
    
    return render_to_response('eval_result.html', locals())
    
    
def list_problems(request):
    
    problems = Problem.objects.all()
    
    return render_to_response('problems.html', locals())
    
    
def list_feedbacks(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    evaluations = problem.evaluation_set.all()
    
    return render_to_response('feedbacks.html', locals())
    
    
def create_problem(request):
    
    return render_to_response('compose.html', locals())
    
def submit_problem(request):
        
    post = request.POST.copy()

    Problem.objects.create(author=request.user, problem=post["problem"],
                           solution=post["solution"], comments=post["comments"],
                           description=post["description"], category=post["category"])
    
    return render_to_response('create_result.html', locals())
    
def request_test(request):
    
    problems = Problem.objects.all()
    
    return render_to_response('request_test.html', locals())
    
def generate_tex(request):
    post = request.POST.copy()
    
    problems = []
    
    test_name = post["test_name"]
    
    problem_list = post["problem_list"].strip()
    
    for problem_id in problem_list.split(" "):
        problem = Problem.objects.get(id=problem_id)
        problems.append(problem)
            
    tex_type = post["type"]
            
    if tex_type=='problems':
        return render_to_response('test.tex', locals())
    elif tex_type=='solutions':
        return render_to_response('solutions.tex', locals())
        