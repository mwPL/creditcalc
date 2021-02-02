import math
import argparse

'''
print('Enter the loan principal:')
amount = int(input())
print('What do you want to calculate?')
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
choice = input()
if choice == 'm':
    print('Enter the monthly payment:')
    payment = int(input())
    length = math.ceil(amount / payment)
    print(f'It will take {length} {"month" if length < 2 else "months"} to repay the loan')
else:
    if choice == 'p':
        print('Enter the number of months:')
        months = int(input())
        monthly = math.ceil(amount / months)
        lastpayment = amount - (months - 1) * monthly
        answer = f'Your monthly payment = {monthly}' if lastpayment == monthly \
            else f'Your monthly payment = {monthly} and the last payment = {lastpayment}.'
        print(answer)
'''
'''
print('What do you want to calculate?')
print('type "n" for number of monthly payments,\ntype "a" for annuity monthly payment amount,'
      ' \ntype "p" for loan principal:')
'''

parser = argparse.ArgumentParser()

# number of payments working ok. Just need argparse
def number_of_payments(loan, monthly, interest):
    '''
    print('Enter the loan principal:')
    loan = int(input())
    print('Enter the monthly payment:')
    monthly = int(input())
    print('Enter the loan interest:')
    interest = float(input())
    '''
    monthly_interest = (interest / 100) / 12
    #print(monthly_interest)
    number_of_months = math.ceil(math.log((monthly / (monthly - monthly_interest * loan)), (1 + monthly_interest)))
    #print(number_of_months)
    years = number_of_months // 12
    months = number_of_months % 12
    if months == 0:
        word_month = ''
    elif months == 1:
        word_month = '1 month'
    else:
        word_month = f'{months} months'
    if years < 1:
        word_year = ''
    elif years == 1 and months < 1:
        word_year = '1 year'
    elif years == 1 and months > 0:
        word_year = '1 year and'
    elif years > 1 and months == 0:
        word_year = f'{years} years'
    else:
        word_year = f'{years} years and'
    answer = " ".join(f'It will take {word_year} {word_month} to repay this loan!'.split())
    print(answer)
    overpayment = (monthly * number_of_months) - loan
    print(f'Overpayment = {math.ceil(overpayment)}')

# monthly payment working. Just need to add argparse
def monthly_payment(loan, period, interest):
    '''
    print('Enter the loan principal:')
    loan = int(input())
    print('Enter the number of periods:')
    period = int(input())
    print('Enter the loan interest:')
    interest = float(input())
    '''
    monthly_interest = (interest / 100) / 12
    annuity = loan * (monthly_interest * math.pow((1 + monthly_interest), period)) / (math.pow((1 + monthly_interest), period) -1)
    print(f'Your annuity payment = {math.ceil(annuity)}!')
    overpayment = (math.ceil(annuity) * period) - loan
    print(f'Overpayment = {math.ceil(overpayment)}')

# loan_principal calculations correct. Just need to add argparse
def loan_principal(annuity, period, interest):
    '''
    print('Enter the annuity payment:')
    annuity = float(input())
    print('Enter the number of periods:')
    period = int(input())
    print('Enter the loan interest:')
    interest = float(input())
    '''
    monthly_interest = (interest / 100) / 12
    principal = annuity / ((monthly_interest * math.pow((1 + monthly_interest), period))/(math.pow((1 + monthly_interest), period) - 1))
    print(f'Your loan principal = {int(principal)}!')
    overpayment = (annuity * period) - principal
    print(f'Overpayment = {math.ceil(overpayment)}')

# diff_payment calculations correct. Just need to add argparse
def diff_payment(loan, period, interest):
    '''
    print('Enter the loan principal:')
    loan = int(input())
    print('Enter the number of periods:')
    period = int(input())
    print('Enter the loan interest:')
    interest = float(input())
    '''
    monthly_interest = (interest / 100) / 12
    # mpay = (loan / period) + monthly_interest * (loan - (loan * (month -1)) / period)
    total_payments = 0
    for month in range(1, period + 1):
        mpay = math.ceil((loan / period) + monthly_interest * (loan - (loan * (month - 1)) / period))
        print(f'Month {month}: payment is {mpay}')
        total_payments += mpay
    print(f'Overpayment = {total_payments - loan}')


parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest", default=-999)
args = parser.parse_args()
'''
print(f'Type {args.type}')
payment = int(args.payment)
print(f'Payment type: {type(payment)} , {payment}')
print(args.principal)
print(args.periods)
print(args.interest)
'''
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest

if args.type == 'diff':
    print('diff methods')
    if type(payment) == str:
        print('Incorrect parameters (type)')
    else:
        print(f'principal {type(principal)}, interest {type(interest)}, periods {type(periods)}')
        if float(principal) < 0 or float(interest) < 0 or int(periods) < 0:
            print('Incorrect parameters (negative')
        else:
            diff_payment(int(principal), int(periods), float(interest))
elif args.type == 'annuity':
    print('annuity methods')
    if float(interest) < 0:
        print('Incorrect parameters (int<0)')
    else:
        if type(principal) == str and type(periods) == str:
            if int(principal) < 0 or int(periods) < 0:
                print('Incorrect parameters (<0)')
            else:
                monthly_payment(int(principal), int(periods), float(interest))
        elif type(payment) == str and type(periods) == str:
            if float(payment) < 0 or int(periods) < 0:
                print('Incorrect parameters (<0')
            else:
                loan_principal(int(payment), int(periods), float(interest))
        elif type(principal) == str and type(payment) == str:
            if int(principal) < 0 or int(payment) < 0:
                print('Incorrect parameters (<0)')
            else:
                number_of_payments(int(principal), int(payment), float(interest))
        else:
            print('Incorrect parameters')

else:
    print('Incorrect parameters')


#number_of_payments()
#monthly_payment()

'''
option = input()
if option == 'n':
    number_of_payments()
elif option == 'a':
    monthly_payment()
elif option == 'p':
    loan_principal()
'''