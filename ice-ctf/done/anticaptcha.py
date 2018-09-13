#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
from fractions import gcd

session = requests.Session()
r = session.get('https://ysxnjsv35aixgxo-anticaptcha.labs.icec.tf/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
all_tds = soup.find_all('td')
question_tds = [all_tds[i].text for i in range(len(all_tds)) if i % 2 == 0]

question_patterns = [r'Is (\d+) a prime number?',
        r'What is the greatest common divisor of (\d+) and (\d+)?',
        r'What is the (\d+)\D+ word in the following line:.*',
        r'What is the capital of Germany?']

#planets between earth and sun
#hawaii
#color of sky

def is_prime(num):
    for i in range(2, num):
        if (num & i) == 0:
            return False
    else: #called if the loop ends without breaking
        return True

def nth_word(num, string):
    print('in nth word: {}'.format(string))
    return string.split(':')[1].split(' ')[num]

#print(question_patterns)
answers = []
for q in question_tds:
    for p in question_patterns:
        if re.match(p, q):
            break
    else:
        print(q)

    #ans = re.match(question_patterns[0], q)
    #if ans:
    #    print('case 0')
    #    if is_prime(int(ans.group(1))):
    #        answers.append('true')
    #    else:
    #        answers.append('false')
    #    continue
    #
    #ans = re.match(question_patterns[1], q)
    #if ans:
    #    print('case 1')
    #    answers.append(gcd(int(ans.group(1)),int(ans.group(2))))
    #    continue

    #ans = re.match(question_patterns[2], q)
    #if ans:
    #    print('case 2')
    #    answers.append('Mercury')
    #    continue
    #
    #ans = re.match(question_patterns[3], q)
    #if ans:
    #    print('case 3')
    #    answers.append('Steven Spielberg')
    #    continue

    #ans = re.match(question_patterns[4], q)
    #if ans:
    #    print('case 4')
    #    answers.append(nth_word(int(ans.group(1)), q))
    #    continue

    #ans = re.match(question_patterns[5], q)
    #if ans:
    #    print('case 5')
    #    answers.append('Honolulu')
    #    continue

    #ans = re.match(question_patterns[6], q)
    #if ans:
    #    print('case 6')
    #    answers.append('Berlin')
    #    continue

    #print(answers)
    #print(q)
    

