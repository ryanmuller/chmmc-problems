from django.db import models
from django.contrib.auth.models import User 

class Problem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    description = models.CharField(max_length=400, null=True, blank=True)
    problem = models.TextField()
    solution = models.TextField(null=True, blank=True)
    comments = models.CharField(max_length=400, null=True, blank=True)
    category = models.CharField(max_length=15)
    
    def __unicode__(self):
        return "Problem: %s" % self.description
        
    def contains_solution(self):
        return self.solution != None
        
    def num_evals(self):
        return self.evaluation_set.count
        
    def avg_time(self):
        total_time = 0
        n = 0
        for evaluation in self.evaluation_set.all():
            total_time += evaluation.time
            n += 1
            
        if n == 0:
            return -1
        
        return total_time / n

    def avg_difficulty(self):
        total_diff = 0
        n = 0
        for evaluation in self.evaluation_set.all():
            total_diff += evaluation.difficulty
            n += 1
        
        if n == 0:
            return -1
        
        return total_diff / n
    
class Evaluation(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    problem = models.ForeignKey(Problem)
    evaluator = models.ForeignKey(User)
    answer = models.CharField(max_length=100, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    difficulty = models.PositiveSmallIntegerField(null=True, blank=True)
    time = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    
    def __unicode__(self):
        return "Evaluation of %s by %s" % (self.problem.id, self.evaluator)
        
class Test(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32)
    instructions = models.TextField()
    problem_id_list = models.CommaSeparatedIntegerField(max_length=200)