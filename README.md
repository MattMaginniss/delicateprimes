# Delicate Primes

A little repo of python code to calculate and print out a list of all digitally delicate primes

## What is it?

A digitally delicate prime number is a prime number where if you change any of the digits to any other digit, it is no longer a prime number.

Example. 3 is a prime number, but it is not delicate as if you change the 3 to a 7, its still a prime number.

However, if you take the first digit from the list of [delicate primes](delicate-primes.txt) 294001, if you change any one of those 6 digits to any other digit, there is no prime number you can create with it. It will always be a number divisible by something.

Take `294001` and change the 1 in the ones place and turn it to 2, its now divisible by 2.

Take `294001` and change the 4 in the thousands place and turn it to a 7 it is now `297001` it is divisble by `43` and `6907`.

## Where are you at now?

We are officially at `91356` Digitally Delicate Primes
