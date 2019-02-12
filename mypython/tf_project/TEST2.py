
import json

TEST_STR = """深圳 |   12027 |  0.5992350544607965|      20834|                           20190109|        didi38
福州市 | 166 |    0.5783132530120482|      287|                             20190110|        didi38
温州市 | 196 |    0.5|     305|                             20190110|        didi38
深圳 |   25547 |  0.5812032723998904|      45103|                           20190110|        didi38
西安市 | 257 |    0.6147859922178989|      461|                             20190110|        didi38
温州市 | 3922 |   0.5073941866394697|      6543|                            20190111|        didi38
深圳 |   35871 |  0.5795768169273229|      65153|                           20190111|        didi38
西安市 | 5094 |   0.5944248135060856|      9129|                            20190111|        didi38
福州市 | 3825 |   0.5518954248366013|      6425|                            20190111|        didi38
深圳 |   42677 |  0.5963399489186213|      76879|                           20190112|        didi38
西安市 | 6814 |   0.5992075139418843|      12374|                           20190112|        didi38
福州市 | 6038 |   0.5525008280887711|      10305|                           20190112|        didi38
温州市 | 5557 |   0.5108871693359727|      9288|                            20190112|        didi38
温州市 | 6283 |   0.5083558809485914|      10639|                           20190113|        didi38
深圳 |   42586 |  0.6036490865542666|      77181|                           20190113|        didi38
西安市 | 6917 |   0.6002602284227266|      12345|                           20190113|        didi38
福州市 | 6168 |   0.5625810635538262|      10559|                           20190113|        didi38"""


city_list = ['深圳', '西安市', '福州市', '温州市']
# city_list = ['深圳']

for city in city_list:
    city_info_result = []
    for item in TEST_STR.split("\n"):
        item_list = item.split("|")
        if city == item_list[0].strip():
            city_info_result.append((item_list[0].strip(), item_list[1].strip(), item_list[2].strip(), item_list[3].strip(), item_list[4].strip()))

    city_info_sort_result = sorted(city_info_result, key=lambda x: x[4], reverse=False)

    sim_list = []
    total_count = []
    total_all = []

    for d in city_info_sort_result:
        sim_list.append(d[2])
        total_count.append(d[1])
        total_all.append(d[3])

    print("\t".join(sim_list))
    print("\t".join(total_count))
    print("\t".join(total_all))

#
# event_type_dict = {
#     "0": "首次发起请求",
#     "1": "偏航",
#     "2": "修改目的地",
#     "4": "到达目的地",
#     "5": "动态避堵/多路线",
#     "6": "主辅路切换",
#     "7": "乘客行程中多路线",
# }
#
# json_str = """{"5":"1","4":"3","0":"1","1":"1"}"""
#
# json_obj = json.loads(json_str)
#
# print(type(json_obj))
#
# json_obj_sort = sorted(json_obj.items(), key=lambda x: x[0])
#
# event_result_list = []
#
# for item in json_obj_sort:
#     event_result_list.append(event_type_dict[item[0]] + "-" + item[1])
#
# print("|".join(event_result_list))
