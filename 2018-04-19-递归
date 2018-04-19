def parse_list(lis):
    new_list = []
    def parse(lis):
        for i in lis:
            if type(i) is int:
                new_list.append(i)
            else:
                parse(i)
    parse(lis)
    return new_list

L = [1,[2,3,4],[5],6,7,[8,[9]]]  #列表嵌套转换成单列表
parse_list(L)

def print_list(lis):
    for i in lis:
        if type(i) is int:
            print(i,end = " ")
        else:
            print_list(i)

L = [1,[2,3,4],[5],6,7,[8,[9]]]  #列表嵌套里面的每个元素打印
print_list(L)

def sum_list(lis):
    a = 0
    for i in lis:
        if type(i) is int:
            a += i
        else:
            a += sum_list(i)
    return a

L = [1,[2,3,4],[5],6,7,[8,[9]]]  #列表嵌套里面所有元素求和
sum_list(L)
