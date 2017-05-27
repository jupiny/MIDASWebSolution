from django.views.generic. base import View
from django.shortcuts import get_object_or_404, render

from date.models import Date


class DateDetailView(View):
    template_name = 'date/detail.html'

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date = get_object_or_404(Date, date=date)
        return render(
            request,
            'date/detail.html',
            context={
                'breakfast_meal': date.breakfast_meal,
                'lunch_meal': date.lunch_meal,
                'dinner_meal': date.dinner_meal,
                'year': year,
                'month': month,
                'day': day,
             }
        )