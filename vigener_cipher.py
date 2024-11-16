def vigener_cipher(word, cipher):
    word = word.lower()
    cipher = cipher.lower()
    ans = ''

    for i, letter in enumerate(word):
        if letter.isalpha():
            shift = ord(cipher[i % len(cipher)]) - ord('a')
            ans += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        else:
            ans += letter

    return ans


print(vigener_cipher('hello hello hello', 'key'))
