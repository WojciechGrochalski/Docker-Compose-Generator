from cryptography.fernet import Fernet
import onetimepad
import sys

letterPL = [260, 262, 280, 321, 323, 211, 246, 377, 379, 261, 263, 281, 322, 324, 243, 347, 378, 380,
            164, 143, 168, 157, 227, 224, 151, 141, 189, 165, 134, 169, 136, 228, 162, 152, 171, 190]
keyForOT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tempus augue eu nisl ornare, non sagittis nunc sollicitudin. Mauris vehicula malesuada vestibulum. Etiam dictum semper risus, a sollicitudin quam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus ut dapibus orci, a cursus libero. Fusce quis accumsan nibh. Nam tristique lorem condimentum turpis mollis, a placerat augue pretium. Aliquam ultricies sed ligula in egestas." \
           "Maecenas lobortis at lorem non laoreet. Donec velit erat, pharetra vel justo cursus, mattis cursus ipsum. Phasellus ullamcorper tincidunt convallis. In hac habitasse platea dictumst. Integer tempor nulla diam, at tempor nisi mollis eu. Nulla aliquet nisi sed malesuada lacinia. Integer eget mollis orci, id congue massa. Quisque quam risus, consequat vitae placerat id, egestas in urna. Praesent at feugiat ante. Sed hendrerit quis nulla sit amet scelerisque. Duis ut metus dictum, scelerisque nunc condimentum, facilisis ipsum. Donec pharetra in ex sed mollis. Integer congue consequat turpis, eu tristique velit blandit sit amet. Aliquam laoreet enim eu nisi varius, id aliquet elit fermentum. Maecenas nisi ex, egestas at consequat ac, dapibus quis ipsum." \
           "Suspendisse euismod elit a auctor venenatis. Sed bibendum, mi sit amet accumsan finibus, elit mauris tempor lorem, nec tincidunt ipsum dolor vitae odio. Duis eget nisi a nisi mollis aliquet id ut elit. Vestibulum iaculis ex sed eleifend pretium. Maecenas elementum, nulla nec suscipit gravida, tellus neque convallis augue, at volutpat odio quam quis arcu. Phasellus accumsan lacus quis sapien ultricies placerat. Ut dictum malesuada tellus, non ornare urna porttitor eget. Aenean hendrerit diam urna, pretium sodales lacus congue vitae. In id egestas ipsum. Integer lobortis interdum urna, quis efficitur dolor condimentum quis. Vivamus fermentum fermentum sem, nec tristique sapien tempor a. Integer euismod eleifend massa, sed rutrum nunc. Proin vel justo dui. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed semper leo id tortor sollicitudin, nec laoreet ex condimentum." \
           "Aliquam consequat placerat ornare. Cras in libero accumsan, dapibus neque eget, ullamcorper leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus non aliquet enim. Integer faucibus purus vel ex viverra, in semper nulla mattis. Aliquam laoreet tristique cursus. Vestibulum a molestie mi, nec pulvinar orci. Nulla imperdiet, lacus quis molestie euismod, est quam condimentum erat, non imperdiet massa enim non sapien. Aliquam mauris sapien, dignissim in malesuada quis, malesuada a mauris. Ut gravida quis metus et vehicula. Integer nibh ante, ornare in massa in, aliquam malesuada tellus." \
           "Etiam nibh magna, congue id nibh efficitur, ullamcorper tempus purus. Fusce sodales felis lorem. Duis non iaculis nibh, in vulputate leo. Suspendisse nec ligula cursus, sodales justo quis, varius nibh. Etiam imperdiet molestie lorem, ac vulputate justo mollis quis. Phasellus ullamcorper lacinia dui non tempus. Aenean laoreet maximus erat, a tristique tortor. Fusce scelerisque vitae lorem a accumsan. Integer risus velit, ultricies vitae erat id, dignissim accumsan massa. Suspendisse condimentum dui in suscipit maximus. Donec ornare blandit sapien, quis vehicula lacus auctor ut. Quisque elementum sit amet lectus vitae condimentum. Ut diam velit, ullamcorper et purus sit amet, consectetur venenatis sapien. Vestibulum a turpis pretium, elementum lectus nec, dapibus nunc. Proin eget risus velit. "


def EncryptFile(choosenAlgorithm, text, pattern, key):
    if (choosenAlgorithm == 'Cesar'):
        return EncryptCE(text, pattern)
    if (choosenAlgorithm == 'Fernet'):
        return EncryptFE(text, key)
    if (choosenAlgorithm == 'OneTime'):
        return EncryptONETIME(text, keyForOT)


def DecryptFile(choosenAlgorithm, text, pattern, key):
    if (choosenAlgorithm == 'Cesar'):
        return DecryptCE(text, pattern)
    if (choosenAlgorithm == 'Fernet'):
        return DecryptFE(text, key)
    if (choosenAlgorithm == 'OneTime'):
        return DecryptONETIME(text, keyForOT)


def EncryptFE(text, key):
    text = bytes(text, 'UTF-8')
    f = Fernet(key)
    token = f.encrypt(text)
    return token


def DecryptFE(text, key):
    try:
        text = bytes(text, 'UTF-8')
    except:
        print("error")
    f = Fernet(key)
    try:
        text = f.decrypt(text)
        text = str(text, 'utf-8')
    except:
        text = str(sys.exc_info()[0])

    return text


def EncryptONETIME(text, key):
    return onetimepad.encrypt(text, key)


def DecryptONETIME(text, key):
    try:
        text = onetimepad.decrypt(text, key)
    except:
        text = str(sys.exc_info()[0])
    return text


def EncryptCE(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            sign = ord(char)
            if (65 > sign > 31):
                result += chr(sign + s)
            elif (sign == 10):
                result += chr(252)
            elif (sign > 122):
                for k in letterPL:
                    if (sign == k):
                        result += chr(k)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def DecryptCE(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            sign = ord(char)
            if (sign < 65):
                result += chr(sign - s)
            elif (sign == 252):
                result += '\n'
            elif (sign > 200):
                for k in letterPL:
                    if (k == sign):
                        result += chr(k)
            else:
                result += chr((ord(char) - s - 97) % 26 + 97)
    return result
