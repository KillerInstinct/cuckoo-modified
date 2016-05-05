# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file "docs/LICENSE" for copying permission.

from django.conf.urls import url
from analysis.views import (index, report, surialert, surihttp, suritls, surifiles, antivirus, shrike, remove, chunk, filtered_chunk,
                             search_behavior, search, pending, procdump, pcapstream, comments)


urlpatterns = [
    url(r"^$", index),
    url(r"^page/(?P<page>\d+)/$", index),
    url(r"^(?P<task_id>\d+)/$", report),
    url(r"^surialert/(?P<task_id>\d+)/$", surialert),
    url(r"^surihttp/(?P<task_id>\d+)/$", surihttp),
    url(r"^suritls/(?P<task_id>\d+)/$", suritls),
    url(r"^surifiles/(?P<task_id>\d+)/$", surifiles),
    url(r"^antivirus/(?P<task_id>\d+)/$", antivirus),
    url(r"^shrike/(?P<task_id>\d+)/$", shrike),
    url(r"^remove/(?P<task_id>\d+)/$", remove),
    url(r"^chunk/(?P<task_id>\d+)/(?P<pid>\d+)/(?P<pagenum>\d+)/$", chunk),
    url(r"^filtered/(?P<task_id>\d+)/(?P<pid>\d+)/(?P<category>\w+)/(?P<apilist>[!]?[A-Za-z_0-9,%]*)/$", filtered_chunk),
    url(r"^search/(?P<task_id>\d+)/$", search_behavior),
    url(r"^search/$", search),
    url(r"^pending/$", pending),
    url(r"^procdump/(?P<task_id>\d+)/(?P<process_id>\d+)/(?P<start>\w+)/(?P<end>\w+)/$", procdump),
    url(r"^(?P<task_id>\d+)/pcapstream/(?P<conntuple>[.,\w]+)/$", pcapstream),
    url(r"^(?P<task_id>\d+)/comments/$", comments),
]
