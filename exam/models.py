from django.db import models

# Create your models here.
class Examination(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=100)
    maximum_subjects = models.IntegerField()

    def __str__(self):
        return self.alias



class Subject(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    score_weight = models.DecimalField(decimal_places=2, max_digits=4)
    is_compulsory = models.BooleanField()

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score_weight = models.DecimalField(decimal_places=2, max_digits=4)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL(), null=True)
    detail = models.TextField()

    def get_options(self):
        return self.answer_set.all()

    def get_random_options(self):
        return self.answer_set.all().order_by('?')



class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.TextField()
    is_right = models.BooleanField()

    
# class QuizSetup(models.Model):
#     question_size = models.IntegerField()
#     is_sample = models.BooleanField()
#     is_random_questions = models.BooleanField()
#     is_random_options = models.BooleanField()
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

#     def make_quiz_questions_random(self):
#         self.is_random_questions = True
#         self.save()

#     def make_quiz_questions_unrandom(self):
#         self.is_random_questions = False
#         self.save()

#     def get_question_list(self):
#         if self.is_random_questions:
#             return Question.objects.filter(subject=self.subject).order_by('?')
#         return Question.objects.filter(subject=self.subject)


# class QuestionSet(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.PROTECT())
#     selected_option = models.ForeignKey(
#         Option, on_delete=models.SET_NULL(), blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)



# class UserQuiz(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE())
#     quiz = models.ForeignKey(QuizSetup)