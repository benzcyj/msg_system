class Controller:

    def compare_data(self,line,item):
        list = line.split()
        for i in list:
            if item == i or "｜" + item == i:
                return 1

    def search_print_data(self,line,count):
        if count == 0:
            print("地区　　　　　　｜年份　　　｜固定电话用户数（万）｜移动电话用户数（万）｜互联网用户数（万）｜通信固定资产投入（万）｜通信业收入（万）｜信息服务收入（万）｜信息产品收入（万）")
            print("－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－")
        print(line)

    def search_data(self,item):
        """
        输入需要查找的关键字进行全文匹配
        :param item:
        :return: list0:有关键字的行去掉空格后组成一个列表,所有列表组成的列表
        """
        list0 = []
        list1 = []
        count = 0
        f = open("msg.txt","r")
        for line in f:
            if self.compare_data(line,item) == 1:
                l = line.split()
                list0.append(l)
                list1.append(line)
                self.search_print_data(line, count)
                count += 1
        return count,list0,list1

    def add_data(self,b0,b1,b2,b3,b4,b5,b6,b7,b8):
        f = open("msg.txt","a")
        part0 = b0 + (8-len(b0)) * "　"
        part1 = "｜" + b1 + (5-len(b1)) * "　"
        part2 = "｜" + b2 + (10-len(b2)) * "　"
        part3 = "｜" + b3 + (10-len(b3)) * "　"
        part4 = "｜" + b4 + (9-len(b4)) * "　"
        part5 = "｜" + b5 + (11-len(b5)) * "　"
        part6 = "｜" + b6 + (8-len(b6)) * "　"
        part7 = "｜" + b7 + (9-len(b7)) * "　"
        part8 = "｜" + b8 + (9-len(b8)) * "　"
        f.write("\n%s%s%s%s%s%s%s%s%s"%(part0,part1,part2,part3,part4,part5,part6,part7,part8))

    def select_result(self,list):
        l = []
        count = 0
        for i in list: # i:地区名(如北京)
            f = open("msg.txt", "r")
            for line in f:
                if i in line:
                    l.append(line)
                    count += 1
        return count,l

    def alter_search_data(self,item):
        list0 = []
        list1 = []
        count = 0
        f = open("msg.txt","r")
        for line in f:
            if self.compare_data(line,item) == 1:
                l = line.split()
                list0.append(l)
                list1.append(line)
                count += 1
        return count,list0,list1

    def select_data(self,list):
        """
        把列表中的每个列表的第一个元素放入一个空列表
        :param list:
        :return:
        """
        l = []
        for i in list:
            l.append(i[0])
        return l

    def select_aim(self,list,item):
        for i in list:
            if item in i or "｜" + item in i:
                return i[0]

    def delet_data(self,item):
        count = -1
        f = open('msg.txt', 'r+')
        l = f.readlines()
        for line in l:
            count += 1
            if item in line:
                break
        l[count] = ''
        f.close()
        f = open('msg.txt', 'w+')
        f.writelines(l)
        f.close()

    def item_make_line(self,list):
        l = []
        for i in list:
            part0 = i[0] + (8 - len(i[0])) * "　"
            part1 = i[1] + (6 - len(i[1])) * "　"
            part2 = i[2] + (11 - len(i[2])) * "　"
            part3 = i[3] + (11 - len(i[3])) * "　"
            part4 = i[4] + (10 - len(i[4])) * "　"
            part5 = i[5] + (12 - len(i[5])) * "　"
            part6 = i[6] + (9 - len(i[6])) * "　"
            part7 = i[7] + (10 - len(i[7])) * "　"
            part8 = i[8] + (10 - len(i[8])) * "　"
            line = "\n%s%s%s%s%s%s%s%s%s"%(part0,part1,part2,part3,part4,part5,part6,part7,part8)
            l.append(line)
        return l

    def alter_data(self,b0,b1,b2,b3,b4,b5,b6,b7,b8):
        f = open("msg.txt", "a")
        part0 = b0 + (8 - len(b0)) * "　"
        part1 = b1 + (6 - len(b1)) * "　"
        part2 = b2 + (11 - len(b2)) * "　"
        part3 = b3 + (11 - len(b3)) * "　"
        part4 = b4 + (10 - len(b4)) * "　"
        part5 = b5 + (12 - len(b5)) * "　"
        part6 = b6 + (9 - len(b6)) * "　"
        part7 = b7 + (10 - len(b7)) * "　"
        part8 = b8 + (10 - len(b8)) * "　"
        f.write("\n%s%s%s%s%s%s%s%s%s" % (part0, part1, part2, part3, part4, part5, part6, part7, part8))

    def alter_built_data(self,list,item,num):
        list2 = []
        for j in range(len(list)):
            if j == num and num == 0:
                list2.append(item)
            elif j == num:
                list2.append("｜%s" % item)
            else:
                list2.append(list[j])
        return list2

    def result_pritn(self,list,count):
        print("地区　　　　　　｜年份　　　｜固定电话用户数（万）｜移动电话用户数（万）｜互联网用户数（万）｜通信固定资产投入（万）｜通信业收入（万）｜信息服务收入（万）｜信息产品收入（万）")
        print("－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－")
        for line in list:
            print(line)
            count += 1
        return count
