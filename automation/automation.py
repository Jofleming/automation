import re

email_reg = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
phone_reg = r'\b\d{3}\D?\d{3}\D?\d{4}'

email_list = []
number_list = []

with open('potential-contacts.txt') as f:
    text_from_file = f.read()

def format_numbers(phone_num):
    formatted_num = phone_num[:3] + '-' + phone_num[3:6] + "-" + phone_num[6:]
    return formatted_num

def strip_numbers(nums):
    num_list = []
    for num in nums:
        naked_nums = re.sub('[-.)(]','', nums)
        if len(num) == 7:
            num = '206' + num
        if naked_nums not in num_list:
            num_list.append(naked_nums)
    return num_list

def find_numbers(text):
    phone_numbers = re.findall(phone_reg, text)
    stripped_nums = strip_numbers(phone_numbers)
    finished_nums = format_numbers(stripped_nums)
    finished_nums.sort()
    for number in finished_nums:
        number_list.append(number)

def write_nums(nums_to_write):
    with open('phone_numbers.txt', 'w') as num_file:
        for number in nums_to_write:
            num_file.write(number)
            num_file.write('\n')
    num_file.close()

def find_emails(text_with_emails):
    emails = re.findall(email_reg, text_with_emails)
    for email in emails:
        if email not in email_list:
            email_list.append(email)
    email_list.sort()


def write_emails(list_of_emails):
    with open('emails.txt', 'w') as email_file:
        for email in list_of_emails:
            email_file.write(email)
            email_file.write('\n')
    email_file.close()
        
find_numbers(text_from_file)
find_emails(text_from_file)
write_nums(number_list)
write_emails(email_list)

