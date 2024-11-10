# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:31:00 2024

@author: ahmed
"""

from tabulate import tabulate
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

while True:
    try:
        Prior = float(input('Enter your prior | What is the percentage of affected people: '))
        if 0 < Prior < 100:
            Prior /= 100
            break
        else:
            print('Please enter a valid number between 0 and 100.')
    except ValueError:
        print('Invalid input. Please enter a number.')

while True:
    try:
        Sensitivity = float(input('Enter your Sensitivity | What is the true positive result for users: '))
        if 0 < Sensitivity < 100:
            Sensitivity /= 100
            break
        else:
            print('Please enter a valid number between 0 and 100.')
    except ValueError:
        print('Invalid input. Please enter a number.')
while True:
    try:
        Specificity = float(input('Enter your Specificity | What is the true negative result for non-users: '))
        if 0 < Specificity < 100:
            Specificity /= 100
            break
        else:
            print('Please enter a valid number between 0 and 100.')
    except ValueError:
        print('Invalid input. Please enter a number.')
while True:
    try:
        Test_number = int(input('Enter the number of test conducted:'))
        if Test_number> 0:
            break
        else:
            print('Please enter a valid number')
    except ValueError:
            print('Invalid')


print('Percentage of affected people: ' + str(Prior * 100)+ '%')
print('Percentage of True Positive| Sensitivity of your test: ' + str(Sensitivity * 100)+ '%')
print('Percentage of True Negative| Specificity of your test: ' + str(Specificity * 100)+ '%')
print('Number of test conducted=' + str(Test_number))

Users = Prior
Non_users = 1 - Prior

results_alltest = []

for test in range(1,Test_number + 1):
    U_test = Users * Sensitivity
    Non_U_test = (1-Specificity) * Non_users
    sum_test = U_test+Non_U_test
    User_normalize= U_test/sum_test
    Non_U_normalize= Non_U_test/sum_test
    
    results_alltest.append([test, User_normalize * 100 , Non_U_normalize * 100])
    
    Users = User_normalize
    Non_users = Non_U_normalize

print('Result for your conducted number of tests:')
head = ['Test Number','User|Affected (%)','Non_User|Not Affected (%)']
print(tabulate(results_alltest, headers=head, tablefmt='grid'))

#plot
test_numbers = [i[0] for i in results_alltest]
affected_user = [i[1] for i in results_alltest]

plt.figure(figsize=(10, 6))
plt.plot(test_numbers, affected_user, marker='o', color='red', linestyle='--', linewidth=2, markersize=5)
plt.xlabel('Test Number')
plt.ylabel('User|Affected Probability (%)')
plt.title('Test Number vs. Affected Probability')
plt.grid(True)
plt.show()
