import random

alphas = 'abcdefghijklmnopqrstuvwxyz'
cap_alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()'


def generate_password(
    length=12,
    use_alphas=True,
    use_cap_alphas=True,
    use_numbers=True,
    use_symbols=True,
):
    all = ''
    if use_alphas:
        all += alphas
    if use_cap_alphas:
        all += cap_alphas
    if use_numbers:
        all += numbers
    if use_symbols:
        all += symbols
    return ''.join(random.sample(all, length))