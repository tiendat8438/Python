import string

if __name__ == '__main__':
    n = int(input()) 
    len_list = ''.join(str(len(input().split())) for _ in range(n))
    len_list = len_list.replace('7777', '2').replace('68', '1')
    while '11' in len_list:
        len_list = len_list.replace('11', '1')
    print(len(len_list), *len_list, sep = '\n')