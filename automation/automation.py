from faker import Faker
import shutil
import re

email_regex = '([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})"gm'

phone_regex = 'r"[\d+]?[\d+]?[\d+]?[-]?[(]?[0-9]{3}[)]?[ ,-.]?[0-9]{3}[ ,-.]?[0-9]{4}[x]?[\d+]?[\d+]?[\d+]?[\d+]?[\d+]?[\d+]?[\d+]?"gm'

fake = Faker('en_US')

def get_document(path):
    with open(path, 'r') as file:
        text = file.read()
    return text





def open_file_get_string(regex_search)
with open("../potential-contacts.txt", 'w') as f:
    f.write(potential_contacts)

# for phone number found https://stackoverflow.com/questions/33158774/regex-validation-for-north-american-phone-numbers
# [(]?[0-9]{3}[)]?[ ,-]?[0-9]{3}[ ,-]?[0-9]{4}
# new modified version to match the feature asks
# [\d+]?[\d+]?[\d+]?[-]?[(]?[0-9]{3}[)]?[ ,-.]?[0-9]{3}[ ,-.]?[0-9]{4}[x]?[\d+]?[\d+]?[\d+]?[\d+]?[\d+]?[\d+]?[\d+]?

# for email found https://regexlib.com/Search.aspx?k=email&AspxAutoDetectCookieSupport=1
# ([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})