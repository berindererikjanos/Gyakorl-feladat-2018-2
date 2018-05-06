#months = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
months = {'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'}
num = range(1,13)
month_dict = dict(zip(months, nums))
print(month_dict)
str = input('Adjon meg egy dátumot: ')
ls = str.split('-')
if int(ls[2]) <= 18:
     year = '20' +ls[2]
else:
     year = '19' + ls[2]
     
print(year,month_dict[ls[1]], ls[0])
