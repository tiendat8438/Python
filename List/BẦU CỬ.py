from collections import Counter

def find_second_winner(N, M, votes):
    vote_counts = Counter(votes)
    
    # Lấy danh sách số phiếu theo thứ tự giảm dần
    sorted_votes = sorted(vote_counts.items(), key=lambda x: (-x[1], x[0]))
    
    if len(sorted_votes) < 2:
        return "NONE"
    
    first_count = sorted_votes[0][1]  # Số phiếu cao nhất
    second_candidates = [x for x in sorted_votes if x[1] < first_count]
    
    if not second_candidates:
        return "NONE"
    
    return second_candidates[0][0]  # Trả về ứng viên có số phiếu nhiều thứ hai


N, M = map(int, input().split())
votes = list(map(int, input().split()))
print(find_second_winner(N, M, votes))
