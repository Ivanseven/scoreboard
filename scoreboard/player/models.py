from django.contrib.auth.models import User
from django.db.models import Sum

class Player(User):
    class Meta:
        proxy = True

    @property
    def score(self):
        score = self.score_set.aggregate(Sum('score'))['score__sum']
        score = score if score != None else 0
        return score

