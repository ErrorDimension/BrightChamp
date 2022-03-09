principal = int(input('principal (usd) : '))
time = int(input('time (in years) : '))
rate = input('rate (percentage recommended) : ')

if rate.find('.'):  # check if user chose decimal
    rate = float(rate)

if rate < 1:
    rate *= 100

simpleInterest = (principal * rate * time) / 100

print('Total money (includes simple interest) :',
      int(simpleInterest + principal), '(usd)')
