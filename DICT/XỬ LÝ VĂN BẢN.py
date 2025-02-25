import sys
import re

def format_string(text):
    lines = re.split(r'[.?!]', text)
    res = []
    for line in lines:
        words = line.strip().split()
        if words:
            formatted_line = ' '.join(words).capitalize()
            res.append(formatted_line)
    return res

if __name__ == "__main__":
    text = ""
    for line in sys.stdin:
        text += " " + line.strip()
    sentences = format_string(text)
    for line in sentences:
        print(line)
