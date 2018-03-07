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

detail_house_info_sql = """
select
    id, house_title, insert_date, district, 
    community_id, community_name, house_type,
    house_type_new, house_area, orientation,
    distinct_name, house_floor, house_create_year,
    see_count, house_price, sale_date, sale_date_new,
    extra_info_select, basic_info, house_tags,
    house_feature, position, see_stat_total,
    see_stat_weekly, community_sold_count,
    busi_sold_count
from
    lianjia_house_info{date}
where
    house_id = '{house_id}'
"""

detail_house_stat_sql = """
select
    id, insert_date, house_stat_json
from
    lianjia_house_stat_json{date}
where
    house_id = '{house_id}'
"""