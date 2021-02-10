import random, string
def random_url(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
