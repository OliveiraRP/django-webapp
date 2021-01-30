from django.shortcuts import render
from django.db import connection
from collections import namedtuple

# Create your views here.
def index_view(request, *args, **kwargs):

	return render(request, "index.html", {})


def namedtuplefetchall(cursor):
	desc = cursor.description
	nt_result = namedtuple('Result', [col[0] for col in desc])
	return [nt_result(*row) for row in cursor.fetchall()]


def changelog_view(request, *args, **kwargs):

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM log_db")
		log = namedtuplefetchall(cursor)

	if request.method == 'POST':
		with connection.cursor() as cursor:
			cursor.execute("CALL revert_changes('postgres')")

	context = {
		"log": log,
	}

	return render(request, "changelog.html", context)