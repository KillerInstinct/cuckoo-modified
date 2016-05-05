# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file "docs/LICENSE" for copying permission.

from django.conf.urls import url
from compare.views import left, both, hash_search

urlpatterns = [
    url(r"^(?P<left_id>\d+)/$", left),
    url(r"^(?P<left_id>\d+)/(?P<right_id>\d+)/$", both),
    url(r"^(?P<left_id>\d+)/(?P<right_hash>\w+)/$", hash_search),
]
