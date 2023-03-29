def email_slicer(emails: list) -> None:
    for email in emails:
        if '@' in email:
            usr, domain = email.split('@')
            extension = domain.split('.')[1]
            print(f'Username: {usr}')
            print(f'Domain: {domain}')
            print(f'Extension: {extension}')

email_slicer(['john.doe@yahoo.com', 'jane.doe@hotmail.com','john.doe@proton.me'])
