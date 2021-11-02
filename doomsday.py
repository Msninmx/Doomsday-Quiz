def main():
    from random import randint

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    year = randint(1800, 2100)
    month = months[randint(0, 11)]
    day = randint(1, 31)
    doomsday = 0
    dDate = 0
    leapYear = False

    if year % 4 != 0:
        leapYear = False
    elif year % 100 != 0:
        leapYear = True
    elif year % 400:
        leapYear = False
    else:
        leapYear = True

    if month == "Februrary":
        if leapYear == True:
            day -= 2
        else:
            day -= 3
    elif month not in ["January", "March", "May", "July", "August", "October", "December"]:
        day -= 1

    lastDigits = year % 100
    a = lastDigits // 12
    b = lastDigits - a*12
    c = b // 4
    d = 0
    if year >= 1800 and year < 1899:
        d = 5
    elif year >= 1900 and year < 1999:
        d = 3
    elif year >= 2000 and year < 2099:
        d = 2
    elif year >= 2100 and year < 2199:
        d = 0
        date = "is"

    doomsday = (a+b+c+d) % 7

    if month == months[0]:
        if leapYear == True:
            dDate = 4
        else:
            dDate = 3

        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[1]:
        if leapYear == True:
            dDate = 29
        else:
            dDate = 28

        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[2]:
        dDate = 7
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[3]:
        dDate = 4
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[4]:
        dDate = 9
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[5]:
        dDate = 6
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[6]:
        dDate = 11
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[7]:
        dDate = 8
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[8]:
        dDate = 5
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[9]:
        dDate = 10
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[10]:
        dDate = 7
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1
    elif month == months[11]:
        dDate = 12
        while dDate != day:
            if dDate < day:
                dDate += 1
                doomsday += 1
            else:
                dDate -= 1
                doomsday -= 1

    doomsday %= 7
    ans = input(f"What day is {month} {day} {year}? ")
    if ans == weekdays[doomsday]:
        print("Good")
    else:
        print("Bad")

if __name__ == "__main__":
    main()
