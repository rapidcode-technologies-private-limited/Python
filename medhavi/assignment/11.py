month=input('enter the month')
day=int(input('enter the day'))
if month in (january,february,):
    season='winter'
elif month in (march,april,may):
    season='spring'
elif month in (june,july,august):
    season='summer'
elif month in (september,november):
    season='autumn'
print("Season is",season)
