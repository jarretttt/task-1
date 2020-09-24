class start:
    def menu(self):
        while True:
            choice = input('请输入数字选择功能：1.加密 2.解密 3.退出')
            if choice == '1':
                code = caesar_encrypt('realText','step')
                print(''.join(code))
            elif choice == '2':
                code = caesar_decrypt('realText','step')
                print(''.join(code))
            else:
                print('感谢使用')
                break

def caesar_encrypt(realText,step):

    realText = input('请输入待加密文字：')
    step = int(input('请输入偏移量（默认偏移量为3）：'))

    outText = []
    cryptText = []

    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in realText:
        if i in uppercase:
            index = uppercase.index(i)
            crypting = (index + step)%26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif i in lowercase:
            index = lowercase.index(i)
            crypting = (index + step)%26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText

def caesar_decrypt(realText,step):

    realText = input('请输入待解密文字：')
    step = int(input('请输入偏移量（默认偏移量为3）：'))

    outText = []
    cryptText = []

    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in realText:
        if i in uppercase:
            index = uppercase.index(i)
            crypting = (index - step)%26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif i in lowercase:
            index = lowercase.index(i)
            crypting = (index - step)%26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText

a = start()
a.menu()