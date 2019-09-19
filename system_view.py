import os
from unit1.project.msg_system.system_controller import Controller

class SystemView:

    def __init__(self):
        self.__controller = Controller()

    def __print_view(self):
        os.system("clear")
        f = open("msg.txt","r")
        for line in f:
            print(line)

    def start(self):
        self.__print_view()

    def update(self):
        while True:
            try:
                print("可执行的操作:")
                print("1.新增数据条目")
                print("2.查找数据条目")
                print("3.修改数据条目")
                print("4.删除数据条目")
                a = int(input("请输入要执行的操作的序号:"))
                if a == 1:
                    b0 = input("请输入地区:")
                    b1 = input("请输入年份:")
                    b2 = input("请输入固定电话用户数(万):")
                    b3 = input("请输入移动电话用户数(万):")
                    b4 = input("请输入互联网用户数(万):")
                    b5 = input("请输入通信固定资产投入(万):")
                    b6 = input("请输入通信业收入(万):")
                    b7 = input("请输入信息服务收入(万):")
                    b8 = input("请输入信息产品收入(万):")
                    self.__controller.add_data(b0,b1,b2,b3,b4,b5,b6,b7,b8)
                elif a == 2:
                    c = input("请输入需要查找的数据(可按地区,年份,指标名称等查找):")
                    self.__controller.search_data(c)
                elif a == 3:
                    d0 = input("请输入需要修改的数据条目所包含的关键字(如北京,２０１９等):")
                    if self.__controller.search_data(d0)[0] > 1:
                        while True:
                            count = 0
                            if count == 0:
                                result_list = self.__controller.alter_search_data(d0)[1]
                            else:
                                result_list = new_result_list
                                self.__controller.item_make_line(new_result_list)
                            d1 = input("请增加关键字继续查询:")
                            new_result_list = []
                            for item in result_list:
                                if d1 in item or "｜" + d1 in item:
                                    new_result_list.append(item)
                            if len(new_result_list) > 1:
                                list0 = self.__controller.item_make_line(new_result_list)
                                count += self.__controller.result_pritn(list0,count)
                                continue
                            elif len(new_result_list) == 1:
                                list0 = self.__controller.item_make_line(new_result_list)
                                count += self.__controller.result_pritn(list0, count)
                                list1 = list0[0].split()
                                self.__controller.delet_data(list1[0])
                                d2 = input("请输入需要修改的信息(输入地区,年份,固定电话用户数等):")
                                num = -1
                                for i in ["地区","年份","固定电话用户数","移动电话用户数","互联网用户数",
                                          "通信固定资产投入","通信业收入","信息服务收入","信息产品收入"]:
                                    num += 1
                                    if i == d2:
                                        d3 = input("将'%s'对应的数据改为:"%d2)
                                        list2 = self.__controller.alter_built_data(list1,d3,num)
                                        self.__controller.alter_data(list2[0],list2[1],list2[2],list2[3],list2[4],
                                                                   list2[5],list2[6],list2[7],list2[8])
                                        print("修改成功!")
                                        # self.__print_view()
                                        break
                            break
                    else:
                        list1 = self.__controller.alter_search_data(d0)[1][0]
                        self.__controller.delet_data(list1[0])
                        d3 = input("请输入需要修改的信息(输入地区,年份,固定电话用户数等):")
                        num = -1
                        for i in ["地区", "年份", "固定电话用户数", "移动电话用户数", "互联网用户数",
                                  "通信固定资产投入", "通信业收入", "信息服务收入", "信息产品收入"]:
                            num += 1
                            if i == d3:
                                d4 = input("将'%s'改为:" % d3)
                                list2 = self.__controller.alter_built_data(list1, d4, num)
                                self.__controller.alter_data(list2[0], list2[1], list2[2], list2[3], list2[4],
                                                             list2[5], list2[6], list2[7], list2[8])
                                print("修改成功!")
                                self.__print_view()
                                break
                elif a == 4:
                    while True:
                        d0 = input("请输入需要删除的数据条目所包含的关键字(输入北京,２０１９等):")
                        if self.__controller.search_data(d0)[0] > 1:
                            while True:
                                count = 0
                                if count == 0:
                                    result_list = self.__controller.alter_search_data(d0)[1]
                                else:
                                    result_list = new_result_list
                                    self.__controller.item_make_line(new_result_list)
                                d1 = input("请增加关键字继续查询:")
                                new_result_list = []
                                for item in result_list:
                                    if d1 in item or "｜" + d1 in item:
                                        new_result_list.append(item)
                                if len(new_result_list) > 1:
                                    list0 = self.__controller.item_make_line(new_result_list)
                                    count += self.__controller.result_pritn(list0, count)
                                    continue
                                elif len(new_result_list) == 1:
                                    list0 = self.__controller.item_make_line(new_result_list)
                                    count += self.__controller.result_pritn(list0, count)
                                    list1 = list0[0].split()
                                    d2 = input("是否确认删除此条数据条目(是/否)?")
                                    if d2 == "是":
                                        self.__controller.delet_data(list1[0])
                                        print("删除成功!")
                                        break
                                    elif d2 == "不是":
                                        continue
                        else:
                            list1 = self.__controller.alter_search_data(d0)[1][0]
                            d2 = input("是否确认删除此条数据条目(是/否)?")
                            if d2 == "是":
                                self.__controller.delet_data(list1[0])
                                print("删除成功!")
                                break
                            elif d2 == "不是":
                                continue

            except:
                print("输入有误,请重新输入:")
                continue
            self.__print_view()

