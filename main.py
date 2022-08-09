from send_email import send_batch_test_mail, send_test_mail
import time
from copy import deepcopy


def open_as_list(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i]= line.rstrip()
    lines = list(set(lines))
    return lines


def generate_aliases(address):
    """Input an address, return a list of aliaes
    """
    at_position = address.rfind('@')
    aliases_list = list()
    characters_range = 2 
    for i in range(97, 97+characters_range):
        new_aliases = address[:at_position] + '+' + chr(i) + address[at_position:]
        aliases_list.append(new_aliases)
        # new_aliases_2 = address[:at_position] + '+' + chr(i) + chr(i+1) + address[at_position:]
        # aliases_list.append(new_aliases_2)
    return aliases_list


def main():
    addrs_file = './addresses.txt'
    addrs_list = open_as_list(addrs_file)

    # Add aliases
    addrs_list_2 = deepcopy(addrs_list)
    for mail in addrs_list_2:
        aliases_list = generate_aliases(mail)
        addrs_list.extend(aliases_list)

    start_log = time.time()
    # Start sending mails
    print(addrs_list)
    send_test_mail(addrs_list)
    end_log = time.time()
    print(f"Sending {len(addrs_list)} emails took {(end_log - start_log):.3f} seconds")


if __name__ == '__main__':
    main()

