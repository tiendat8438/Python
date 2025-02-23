# Hàm làm ngắn thông báo
def shorten_s(s, limit=100):
    if len(s) <= limit:
        return s
    shortened_s = ''
    words = s.split()
    for word in words:
        if len(shortened_s) + len(word) + 1 <= limit:
            shortened_s += word + ' '
        else: break
    return shortened_s.strip()
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        print(shorten_s(s))
