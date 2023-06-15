def is_palindrome(value):
    if len(value) == 0:
        return False
    if len(value) % 2 != 0:
        return False
    l = int(len(value) / 2)
    a = value[:l]
    b = value[l:][::-1]
    print(value, a==b)

is_palindrome('лепсспел')
is_palindrome('helloworld')
