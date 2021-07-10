# RSA Digital Signature scheme and Attacks on it

I'm Long. This is my project in Encryption and algorithm complexity subject at term 20202, Hanoi University of Science and Technology.<br />
Other creators: Tam Vu Thi, Dang Hai Nguyen, Hoang Pham Huy, Hieu Nguyen Quang.

#### Table of contents
1. [RSA scheme](#scheme)
2. [Attacks on RSA Digital Signature scheme](#attack)

# <a name="scheme"></a> RSA scheme

Have you ever wondered that the person you are chatting with is really your friend? If one day you received a text message asking you to buy a 500000VND phone card, what would you do? If she really is your friend, it is ok, because she will repay you. But if her account is hacked, you will be lost 500000VND. So, we need a way to authenticate ourselves on the internet. This project I will present about RSA digital signature.

This diagram illustrates the process of digitally signing a message RSA. With data source, you use hashing function to hash your data to small size. After that, you will encrypt hash using your private key. Only you know what your private key is. And you will send your digital signed data to receiver. 

At receiver’s side, he is decrypt signature using public key, and he has hash value 1. And he also uses hashing function to hash data what is sent to, he has hash value 2. If hash value 1 equal hash value 2, verification successful, else verification failed. Everyone knows your public key, so everyone can verify your digital signed data.

![alt text](https://github.com/longhoangphi225/RSA-Digital-Signature/blob/main/RSA_Scheme.png)

# <a name="attack"></a> Attacks on RSA Digital Signature scheme

Digital signatures are very secure, but they can still be hacked. See report for more details.
