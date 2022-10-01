def dayOfProgrammer(year):
    # Write your code here
    day = ''
    month = '09'
    if 1700 <=  year < 1918:
        if year % 4 == 0:
            day = '12' 
        else:
            day = '13'
    elif year == 1918:
        day = '26'
    elif 1918 < year <= 2700:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            day = '12'
        else:
            day = '13'
    date = f'{day}.{month}.{year}'
    return date