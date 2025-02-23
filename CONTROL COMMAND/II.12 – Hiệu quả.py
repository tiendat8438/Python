if __name__ == '__main__':
    a0, b0, c0 = map(int, input("Bắt đầu lúc ").split())
    a1, b1, c1 = map(int, input("Kết thúc lúc ").split())
    start_time = a0 * 3600 + b0 * 60 + c0
    end_time = a1 * 3600 + b1 * 60 + c1
    if end_time >= start_time:
        duration = end_time - start_time
    else:
        duration = (24 * 3600) - start_time + end_time
    print(f'Thời gian thực hiện chương trình:{duration}')
