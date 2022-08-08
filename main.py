from send_email import send_batch_mails
import time
from copy import deepcopy

def open_textfile(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        # lines[i]= line.strip('\n')
        lines[i]= line.rstrip()
    lines = list(set(lines))
    return lines


def generate_aliases(address):
    at_position = address.rfind('@')
    aliases_list = list()
    # for i in range(97, 123):
    for i in range(97, 122):
        new_aliases = address[:at_position] + '+' + chr(i) + address[at_position:]
        new_aliases_2 = address[:at_position] + '+' + chr(i) + chr(i+1) + address[at_position:]
        aliases_list.append(new_aliases)
        aliases_list.append(new_aliases_2)
    return aliases_list


def main():
    mails_file = './real_mails.txt'
    mails_list = open_textfile(mails_file)
    mails_list_2 = deepcopy(mails_list)
    for mail in mails_list_2:
        aliases_list = generate_aliases(mail)
        mails_list.extend(aliases_list)
    start_log = time.time()
    send_batch_mails(mails_list)
    end_log = time.time()
    print(f"Sending {len(mails_list)} emails took {(end_log - start_log):.3f} seconds")


if __name__ == '__main__':
    main()

