from math import floor, ceil

def convert_score(correct_answers):
    """Chuyển đổi số câu đúng sang thang điểm IELTS."""
    score_table = [
        (39, 40, 9.0), (37, 38, 8.5), (35, 36, 8.0), (33, 34, 7.5),
        (30, 32, 7.0), (27, 29, 6.5), (23, 26, 6.0), (20, 22, 5.5),
        (16, 19, 5.0), (13, 15, 4.5), (10, 12, 4.0), (7, 9, 3.5),
        (5, 6, 3.0), (3, 4, 2.5)
    ]
    for low, high, band in score_table:
        if low <= correct_answers <= high:
            return band
    return 1.0  # Nếu dưới 3 câu đúng, trả về 1.0

def round_ielts_score(score):
    decimal_part = score - int(score)
    if decimal_part < 0.25:
        return floor(score)
    elif decimal_part < 0.75:
        return floor(score) + 0.5
    else:
        return ceil(score)

for _ in range(int(input())):
    r, l, s, w = map(float, input().split())
    
    reading_score = convert_score(int(r))
    listening_score = convert_score(int(l))
    
    overall_score = (reading_score + listening_score + s + w) / 4
    rounded_score = round_ielts_score(overall_score)
    
    print(f"{rounded_score:.1f}")