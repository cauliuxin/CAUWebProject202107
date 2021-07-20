from django.db import connection
from django.shortcuts import render

from webapp import myquery
import json


# Create your views here.
def index_page(request):
    return render(request, "index.html", locals())


def city_page(request):
    city = "北京"
    cursor = connection.cursor()

    # 1.计算出某城市的月薪中位数及其排名/岗位需求量及其排名/应届生需求量及其排名
    MdS, MSrnk, TD, TDrnk, ND, NDrnk = myquery.query1(cursor, city)

    # 2.计算出某城市的应届生需求量最大的n个岗位
    top_job_list = myquery.query2(cursor, city, 20)
    top1 = top_job_list[0]  # 需求量最大的岗位1
    top2 = top_job_list[1]  # 需求量最大的岗位2
    top3 = top_job_list[2]  # 需求量最大的岗位3
    top4 = top_job_list[3]  # 需求量最大的岗位4
    top5 = top_job_list[4]  # 需求量最大的岗位5

    # 3.计算出Top5岗位的 月薪与学历要求的关系
    AR_MSM_lists = myquery.query3(cursor, city, top_job_list, 5)  # 5个岗位的学历要求 与月薪的关系
    AR_MSM1 = AR_MSM_lists[0]
    AR_MSM2 = AR_MSM_lists[1]
    AR_MSM3 = AR_MSM_lists[2]
    AR_MSM4 = AR_MSM_lists[3]
    AR_MSM5 = AR_MSM_lists[4]

    # 4.计算出Top5岗位的 月薪与工作年限的关系
    WY_MSM_lists = myquery.query4(cursor, city, top_job_list, 5)  # 5个岗位的工作年限 与月薪的关系
    WY_MSM1 = WY_MSM_lists[0]
    WY_MSM2 = WY_MSM_lists[1]
    WY_MSM3 = WY_MSM_lists[2]
    WY_MSM4 = WY_MSM_lists[3]
    WY_MSM5 = WY_MSM_lists[4]

    # 5.计算应届生需求量最大的前80个岗位的详细信息
    data = myquery.query5(cursor,city,top_job_list,20)
    # hang = len(data)
    # zpage = 2

    # 6.查看某个城市某个岗位的岗位描述词云图
    # myquery.query6(cursor, city, top1)

    return render(request, "city.html", locals())
