def check_is_cut_vertex(adj_list, start, end, vertex_to_remove, n):
    """
    Kiểm tra xem đỉnh vertex_to_remove có phải là đỉnh thắt trên đường đi từ start đến end không.
    Nếu sau khi xóa vertex_to_remove, không còn đường từ start đến end nữa => Nó là đỉnh thắt."""
    queue = [start]  # Dùng danh sách như stack (DFS)
    visited = [False] * (n + 1)  # Mảng đánh dấu các đỉnh đã thăm
    visited[start] = True
    while queue:
        current = queue.pop()  # Lấy phần tử cuối cùng (giống ngăn xếp)    
        # Nếu tìm thấy end, nghĩa là vẫn còn đường đi
        if current == end:
            return False          
        # Kiểm tra các đỉnh kề
        for neighbor in adj_list[current]:
            if not visited[neighbor] and neighbor != vertex_to_remove:
                queue.append(neighbor)
                visited[neighbor] = True
    return True  # Nếu không tìm thấy đường đến end, đỉnh vertex_to_remove là đỉnh thắt


if __name__ == "__main__":
    test_cases = int(input())  # Số lượng bộ test
    for _ in range(test_cases):
        # Đọc số đỉnh (n), số cạnh (m), đỉnh bắt đầu (u), đỉnh kết thúc (v)
        n, m, u, v = map(int, input().split())
        # Dùng dictionary để lưu danh sách kề (đồ thị có hướng)
        adj_list = {i: [] for i in range(1, n + 1)}
        # Nhập danh sách cạnh
        for _ in range(m):
            x, y = map(int, input().split())
            adj_list[x].append(y)
        count = 0  # Biến đếm số đỉnh thắt
        # Kiểm tra từng đỉnh i xem có phải là đỉnh thắt không
        for i in range(1, n + 1):
            if i != u and i != v:  # Không xét chính u và v
                if check_is_cut_vertex(adj_list, u, v, i, n):
                    count += 1
        print(count)  # Xuất kết quả cho từng bộ test
