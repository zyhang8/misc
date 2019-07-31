# -*- coding: utf-8 -*-
# @Time    : 2019-05-30 18:54
# @Author  : zyh
# @File    : distance_match.py
# @Software: PyCharm

import csv
import os
from geopy.distance import geodesic

ports_list = []
allports_t4f_list = []
min_20 = []  # 小于20的列表


# excel : =(LEFT(B2,FIND("°",B2)-1))+MID(B2,FIND("°",B2)+1,FIND("'",B2)-FIND("°",B2)-1)/60+MID(B2,FIND("'",B2)+1,FIND("""",B2)-FIND("'",B2)-1)/3600

def csv_process(filepath, filepaths):
    with open(filepath, mode='r', encoding='utf-8', newline='') as a, open(filepaths, mode='r', encoding='utf-8',
                                                                           newline='') as b, open("result_t4f.csv",
                                                                                                  "w") as c:
        # 此处读取到的数据是将每行数据当做列表返回的
        reader = csv.reader(a)
        reader1 = csv.reader(b)
        writer = csv.writer(c)
        writer.writerow(["Seq", "station", "lat", "lon", "country", "gloss_number", "distance"])
        for row in reader:
            # 此时输出的是一行行的列表
            ports_list.append(row)
        for row1 in reader1:
            # 此时输出的是一行行的列表
            allports_t4f_list.append(row1)
        # print(allports_t4f_list)
        # print(ports_list)
        # print(len(allports_t4f_list))
        q = 0
        p = 0
        for k in range(1, len(allports_t4f_list)):
            if allports_t4f_list[k][1].find("S") != -1:
                allports_t4f_list[k][3] = '-' + allports_t4f_list[k][3]
                # q += 1
                # print(allports_t4f_list[k][3])
            if allports_t4f_list[k][2].find("W") != -1:
                allports_t4f_list[k][4] = '-' + allports_t4f_list[k][4]
        # print(allports_t4f_list)
        # p += 1
        # print(allports_t4f_list[k][4])
        # print(k)
        # print(q)
        # print(p)
        for i in range(0, len(ports_list)):
            if ports_list[i][2].find("S") != -1:
                ports_list[i][7] = '-' + ports_list[i][7]
                # print(ports_list[i][6])
            if ports_list[i][3].find("W") != -1:
                ports_list[i][8] = '-' + ports_list[i][8]
                # print(ports_list[i][7])
            # print(allports_t4f_list[1][3])
            # print(allports_t4f_list[1][4])
            min_distance = geodesic((ports_list[i][7], ports_list[i][8]),
                                    (allports_t4f_list[1][3], allports_t4f_list[1][4]))
            min_index = []
            # print(min_distance)
            for j in range(1, len(allports_t4f_list)):
                t = geodesic((ports_list[i][7], ports_list[i][8]), (allports_t4f_list[j][3], allports_t4f_list[j][4]))
                # print(t)
                if t <= min_distance:
                    min_distance = t
                    min_index.append(j)
            # min_index = min_index[-1]
            # print(j)
            print(i)
            print(min_index[-1])
            # print(i)
            print(min_distance)
            if min_distance < 20:
                min_20.append(min_distance)
            if min_distance < float(ports_list[i][6]):
                writer.writerows([[ports_list[i][0], ports_list[i][1], ports_list[i][2],
                                   ports_list[i][3],
                                   ports_list[i][4], " ", min_distance]])
            else:
                writer.writerows([[ports_list[i][0], ports_list[i][1], ports_list[i][2],
                                   ports_list[i][3],
                                   ports_list[i][4], " ", ports_list[i][6]]])
            # print(allports_t4f_list[min_index][0])
        # print(ports_list)
        print(len(min_20))


def csv_test(filepath, filepaths):
    name, index = os.path.splitext(filepath)
    name1, index1 = os.path.splitext(filepaths)
    if index == '.csv' and index1 == '.csv':
        csv_process(filepath, filepaths)


def main():
    filepath = 'matched_ports.csv'
    filepaths = 'allports_t4f.csv'
    csv_test(filepath, filepaths)


if __name__ == '__main__':
    main()
