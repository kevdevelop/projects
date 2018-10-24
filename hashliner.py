def linelen(n):
    start = ''
    for i in range(n):
        start = start + '#'
    row = int(input("How many rows to print? "))
    for i in range(1, row+1):
        print (start)

def main():
    print(linelen(int(input("How long should each line be?: "))))
    
if __name__ == "__main__":
    main()