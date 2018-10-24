def get_initials(name):

    name_list = name.split()

    initials = ""
    for part in name_list:
        initials += (part[0])
        initials = initials.upper()
    return initials

def main():
    get_initials("Ozzie Smith")
    get_initials("Bonnie blair")
    get_initials("George")
    get_initials("Daniel Day Lewis")

if __name__ == '__main__':
    main()