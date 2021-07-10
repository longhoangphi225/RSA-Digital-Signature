import random
import time
import numpy as np
from hashlib import sha256
import math
from tqdm import tqdm
import multiprocessing as mp


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Thuật toán Euclid mở rộng
def extended_gcd(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Nghịch đảo mod không tồn tại')
    return x % m


def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Cả 2 số p và q đều phải là số nguyên tố.')
    elif p == q:
        raise ValueError('2 số p và q phải khác nhau')

    N = p * q
    phi = (p - 1) * (q - 1)

    # Chọn số nguyên e sao cho e and phi(n) là 2 số nguyên tố cùng nhau
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Sử dụng thuật toán Euclid mở rộng tìm d để tạo khóa Private
    d = modinv(e, phi)

    # Return khóa công khai và khóa public
    return (N, e), (N, d)


def encrypt(privatek, mabam_h):
    N, key = privatek

    # Chuyển đổi từng chữ cái trong bản rõ thành các số dựa trên bảng mã Unicode
    # và mã hóa bằng công thức s =  h ^ d mod N

    numberRepr = [ord(char) for char in mabam_h]
    print("Biểu diễn số của tin nhắn đã băm qua bản mã Unicode trước khi mã hóa: ")
    print(numberRepr)
    chukyso_s = [pow(ord(char), key, N) for char in mabam_h]
    # ciphertext = ""
    # ciphertext += [chr(item) for item in chukyso_s]
    # Return the array of bytes
    return chukyso_s


def decrypt(publick, received_sign):
    n, key = publick

    # sinh ra mã băm dựa trên chũ ký số
    numberRepr = [pow(char, key, n) for char in received_sign]
    mabam_h = [chr(pow(char, key, n)) for char in received_sign]

    print("Biểu diễn số của mã băm được giải mã từ chữ ký số s được gửi tới: ")
    print(numberRepr)

    return ''.join(mabam_h)


def verify(receivedHashed, receivedmessage):
    ourHashed = hashFunction(receivedmessage)
    print("Mã băm của tin nhắn nhận được: ", ourHashed)
    if receivedHashed == ourHashed:
        print("Xác thực thành công: ", )
        print(receivedHashed, " = ", ourHashed)
    else:

        print("Xác thực thất bại: ")
        print(receivedHashed, " != ", ourHashed)


# Tấn công chữ kí số do sử dụng chung modulo N
# parameter truyền vào là N và khóa công khai e1 của đối tượng cần tấn công

def Attack_CommonModulo(e1, n):
    print("\n\nBắt đầu quá trình tìm mã khóa bí mật......................................")
    time.sleep(2)
    print("Number of processors: ", mp.cpu_count())
    print()
    for i in tqdm(range(0, 100), desc="Requesting memory: ", unit="MB"):
        time.sleep(0.001)
    print()
    print("Khởi tạo các tham số cần thiết...............................")
    for i in tqdm(range(0, 100), desc="Loading parameters: ", unit="MB"):
        time.sleep(0.001)
    time.sleep(1)
    print()
    time.sleep(1)
    print("Public key của đối tượng e1 = ", e1)
    time.sleep(1)
    print()
    print("Đang tính căn bậc 2 không tầm thường của n = ", n)
    b = 1
    for i in tqdm(range(2, n), desc="Calculating: ", unit="MB"):
        if pow(i, 2, n) == 1:
            b = i
            print("\nCăn bậc 2 không tầm thường của n là b = ", b)
            break
    print("Tính toán các số nguyên tố p and q dùng để tạo khóa RSA ban đầu................")
    for i in tqdm(range(0, 100), desc="Calculating: "):
        time.sleep(0.01)
    print()
    p =gcd(b + 1, n)
    q = round(n / p)
    print("p = ", p)
    print("q = ", q)
    print("\nBắt đầu quá trình tính toán khóa bí mật d1 của đối tượng.............. ")
    phi = (p - 1) * (q - 1)
    d1 = modinv(e1, phi)
    for i in tqdm(range(0, 100), desc="Calculating: ", unit="MB"):
        time.sleep(0.01)
    print()
    time.sleep(2)
    print("Khóa bí mật d1 là ", d1)


if __name__ == '__main__':
    p = int(input("Hãy nhập một số nguyên tố (17, 19, 23, v.vv...): "))
    q = int(input("Hãy nhập một số nguyên tố khác (Không phải số đầu tiên): "))
    n = p * q
    phi = (p - 1) * (q - 1)
    print()
    print("Bắt đầu tạo khóa Public và Private . . .")

    # for i in tqdm(range(0, 100), desc="Generating Key: ", unit="MB"):
    #     time.sleep(.05)
    # print()

    public, private = generate_keypair(p, q)
    print("Khóa 1 Public là: ", public, "      Private là: ", private)
    x = input("\n\nBấm phím bất kì để tiếp tục..................")

    Attack_CommonModulo(public[1], n)
    # Attack_CommonModulo(19, 187)
