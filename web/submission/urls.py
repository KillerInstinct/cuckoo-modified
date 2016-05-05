# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from django.conf.urls import url
from submission.views import index, status

urlpatterns = [
    url(r"^$", index),
    url(r"status/(?P<task_id>\d+)/$", status),
]
