import re

def read_contacts(file_path):
    contacts = []
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    date = None
    for line in lines:
        line = line.strip()
        if re.match(r"Ngay \d{2}/\d{2}/\d{4}", line):
            date = line.split(" ")[1]
        elif re.match(r"\d{10}", line):
            if contacts and "phone" not in contacts[-1]:
                contacts[-1]["phone"] = line
                contacts[-1]["date"] = date
        else:
            contacts.append({"name": line})
    return contacts

def write_sorted_contacts(contacts, output_path):
    contacts = [c for c in contacts if "phone" in c]
    contacts.sort(key=lambda x: x["name"])
    
    with open(output_path, "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(f"{contact['name']}: {contact['phone']} {contact['date']}\n")

def main():
    input_file = "SOTAY.txt"
    output_file = "DIENTHOAI.txt"
    contacts = read_contacts(input_file)
    write_sorted_contacts(contacts, output_file)
    # print("Danh bạ đã được sắp xếp và lưu vào DIENTHOAI.txt")
    with open(output_file, "r", encoding="utf-8") as file:
        # print("\nNội dung của DIENTHOAI.txt:")
        print(file.read())

if __name__ == "__main__":
    main()
