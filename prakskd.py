# Implementasi Affine Cipher di Python
 
# Algoritma Euclidean yang Diperluas untuk menemukan invers modular
# misalnya: modinv(7, 26) = 15
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 
 
# Fungsi enkripsi affine cipher
# returns the cipher text
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# Fungsi deskripsi affine cipher 
# returns original text
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 
# kode program untuk menguji fungsi diatas
def main():
    # Mendeklarasikan tex dan key
    text = 'INEZ LAURENSYA'
    key = [7,3]
 
    # Memnggil Fungsi enkripsi
    affine_encrypted_text = affine_encrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
 
    # Memanggil fungsi dekripsi
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) ))
 
 
if __name__ == '__main__':
    main()

