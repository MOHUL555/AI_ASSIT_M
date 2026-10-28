# Prime Number Checker

A simple Python program that checks whether an integer is prime.

## Requirements

- Python 3

## Run

From the project directory, run:

```powershell
python .\prime_checker.py
```

Enter an integer when prompted. The program reports whether it is prime. Values
less than 2 are not prime, and non-integer input displays an error message.

## How it works

The program checks whether the number is divisible by any odd integer from 3
through its square root. If no divisor is found, the number is prime. It handles
2 separately and skips even divisors.
