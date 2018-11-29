from recur import recur

if __name__ == '__main__':

    while True:
        start = int(input("start: "))
        end = int(input("end: "))
        weekdays = int(input("weekdays: "))
        result = recur(start, end, weekdays)
        print(result)
