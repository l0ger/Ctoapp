from Crypto.pyDes import *


class crypto:
    # can use 16 or 24 byte key
    def triple_des_encrypt(self, data, key="FX0FGHC2QR59VDX4WE8SVFGK"):
        k = triple_des(key,
                       ECB, "\0\0\0\0\0\0\0\0",
                       pad=None, padmode=PAD_PKCS5)
        d = k.encrypt(data)
        return d

    # can use 16 or 24 byte key
    def triple_des_decrypt(self, data, key="FX0FGHC2QR59VDX4WE8SVFGK"):
        k = triple_des(key,
                       ECB, "\0\0\0\0\0\0\0\0",
                       pad=None, padmode=PAD_PKCS5)
        return k.decrypt(k.decrypt(data))
