f = open('inputs/1.txt')
content = f.read().splitlines()

total_fuel_count = 0

for module in content:
  total_fuel_count += round(int(module) / 3) - 2

print total_fuel_count