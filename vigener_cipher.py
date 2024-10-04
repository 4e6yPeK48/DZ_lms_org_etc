def vigener_cipher(word, cipher):
    word = word.lower()
    cipher = cipher.lower() * (len(word) // len(cipher)) + cipher[:len(word) % len(cipher)]
    ans = ''
    for letter in range(len(word)):
        if word[letter].isalpha():
            shift = ord(cipher[letter]) - ord('a')
            ans += chr((ord(word[letter]) - ord('a') + shift) % 26 + ord('a'))
        else:
            ans += word[letter]
    return ans


print(vigener_cipher('hello hellohello', 'key'))
