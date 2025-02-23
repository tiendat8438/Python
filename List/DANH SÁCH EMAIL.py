def email_handling(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        emails = set(email.strip().lower() for email in f if email.strip())
    sorted_email = sorted(emails)
    for email in sorted_email:
        print(email)

email_handling("CONTACT.in")