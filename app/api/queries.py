from api.models import Team, MemberHappiness as Happiness
from django.db.models import Subquery, OuterRef, Max, Q, Count, Avg


def get_happiness_stat(slug):
    subquery = Subquery(
        Happiness.objects.filter(member=OuterRef('member'))
            .annotate(last_happiness=Max('created_at'))
            .values('last_happiness')[:1]
    )

    return Happiness.objects.filter(member__team__slug=slug). \
        filter(created_at=subquery). \
        aggregate(
        happy=Count('happiness', filter=Q(happiness=Happiness.HAPPY)),
        neutral=Count('happiness', filter=Q(happiness=Happiness.NEUTRAL)),
        unhappy=Count('happiness', filter=Q(happiness=Happiness.UNHAPPY)),
        average_happiness=Avg('happiness')
    )
