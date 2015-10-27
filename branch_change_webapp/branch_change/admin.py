from django.contrib import admin

from branch_change.models import userpost

import csv
from django.http import HttpResponse
# Register your models here.
from branch_change.models import allocated_branch

from django.http import HttpResponseRedirect

from django.utils.translation import ugettext_lazy as _

from branch_change.models import branch_stats


class userpostadmin(admin.ModelAdmin):
	class Meta:
		model = userpost

admin.site.register(userpost,userpostadmin)


class allocated_branchadmin(admin.ModelAdmin):
	class Meta:
		model = allocated_branch

admin.site.register(allocated_branch,allocated_branchadmin)


class branch_statsadmin(admin.ModelAdmin):
	class Meta:
		model = branch_stats

admin.site.register(branch_stats,branch_statsadmin)