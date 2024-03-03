principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print('month', 'total paid', 'principal')

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    if month >= extra_payment_start_month and month<= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    total_paid = total_paid + payment
    if principal<0:
        total_paid=total_paid+principal
        principal=0
    ##print (month, round(total_paid,2), round(principal,2))
    print(f'{month} {total_paid:0.2f} {principal:0.2f}')
    
total_paid=total_paid +principal

print(f'Total paid: {total_paid:0.2f}')
#print('Total paid:', round(total_paid,2))
print(f'Months: {month}')
#print('Months:', month)