from datetime import date

day, mon, year = input('Enter DOB (DD-MM-YYY):').split('-')
birthday = date(int(year), int(mon), int(day))
today = date.today()
delta = today - birthday
earth_days = delta.days

print(f'Mercury: {int(int(earth_days)/88)} Years')
print(f'Venus: {int(int(earth_days)/225)} Years')
print(f'Earth: {int(int(earth_days)/365)} Years')
print(f'Mars: {int(int(earth_days)/687)} Years')
print(f'Jupiter: {int(int(earth_days)/(11.8*365))} Years')
print(f'Saturn: {int(int(earth_days)/(29.4*365))} Years')
print(f'Uranus: {int(int(earth_days)/(84*365))} Years')
print(f'Neptune: {int(int(earth_days)/(164*365))} Years')
print(f'Pluto(dwarf planet): {int(int(earth_days)/(248*365))} Years')
