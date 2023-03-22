import base64


def picture_to_base64(path):
    f = open(path, 'rb')
    ls_f = base64.b64encode(f.read())
    f.close()
    return ls_f


def base64_to_picture(bs, path):
    imgdata = base64.b64decode(bs)
    file = open(path, 'wb')
    file.write(imgdata)
    file.close()


if __name__ == '__main__':
    first_path = 'C:\\Users\\95111\\Desktop\\ai_img\\img\\43.jpg'
    bs = picture_to_base64(first_path)
    second_path = 'C:\\Users\\95111\\Desktop\\ai_img\\img\\2.jpg'
    base64_to_picture(bs, second_path)