def is_palindrome(text: str) -> bool:
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]

if __name__ == '__main__':
    sample = input('Enter text: ')
    if is_palindrome(sample):
        print('Palindrome text')
    else:
        print('Not a palindrome text')
