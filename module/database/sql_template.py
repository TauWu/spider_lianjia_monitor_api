count_house_info_sql = """
select
    count(1)
from
    lianjia_house_info%s
%s
"""

count_house_stat_sql = """
select
    count(1)
from
    lianjia_house_stat_json%s
"""