from django.contrib import admin

from branch_change.models import userpost

import csv
from django.http import HttpResponse
# Register your models here.
from branch_change.models import userpost






class userpostadmin(admin.ModelAdmin):
	class Meta:
		model = userpost

admin.site.register(userpost,userpostadmin)


