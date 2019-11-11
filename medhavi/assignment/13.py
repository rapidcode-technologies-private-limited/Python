while True:
    year=int(input('enter the year'))
    month=int(input('enter the month'))
    if month>12:
        print('invalid month')
        continue
    date=int(input('enter the date'))
    if date>30:
        print('invalid date')
        continue
    nextday=[year,month,date+1]
    print('nextday is [yy,mm,dd] ',nextday )
