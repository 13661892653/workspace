# -*- coding: utf-8 -*-
import re

str = " 4 收藏"
collect_match = re.match(".*?(\d+).*",str)
if collect_match:
    print(collect_match.group(1))
