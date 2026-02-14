lists=[]
with open("C:/Users/pongredd/OneDrive - Capgemini/Desktop/Python/python/day24/names.txt", 'r') as f:

    for i in f.readlines():
        lists.append(i.strip())

with open("C:/Users/pongredd/OneDrive - Capgemini/Desktop/Python/python/day24/email.txt", 'r') as read:
    new_str = read.read()
    for i in lists:
       email= new_str.replace("Name",i.strip())
       letter_name=f'letter_for_{i}.docx'
       print(letter_name)
       try:
           with open(letter_name,'w',encoding='utf-8') as welcome_mail:
               welcome_mail.write(email)
               print('Letter created successful')
               welcome_mail.close()
       except FileExistsError:
           print(FileExistsError)


