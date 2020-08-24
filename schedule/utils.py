from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None,pk_owner=None):
		self.year = year
		self.month = month
		self.pk_owner = pk_owner
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			print(event.get_html_url)
			d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month,owner_id=self.pk_owner)

		calo = f'<table border="1" cellpadding="55" cellspacing="0" class="calendar">\n'
		calo += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		calo += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			calo += f'{self.formatweek(week, events)}\n'
		return calo

class CalendarDirect(HTMLCalendar):
	def __init__(self, year=None, month=None,pk_owner=None):
		self.year = year
		self.month = month
		self.pk_owner = pk_owner
		super(CalendarDirect, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month,owner_id=self.pk_owner)

		calo = f'<table border="1" cellpadding="40" cellspacing="0" class="calendar">\n'
		calo += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		calo += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			calo += f'{self.formatweek(week, events)}\n'
		return calo
