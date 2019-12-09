def get_fuel(module):
  return round(int(module) / 3) - 2

f = open('inputs/1.txt')
content = f.read().splitlines()

total_fuel_count = 0

for module in content:
  remaining_fuel = get_fuel(module)
  fuel = remaining_fuel

  while(remaining_fuel > 0):
    remaining_fuel = get_fuel(remaining_fuel)
    if (remaining_fuel > 0):
      fuel += remaining_fuel
    else:
      break

  total_fuel_count += fuel

print total_fuel_count