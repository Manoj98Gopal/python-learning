
import qrcode


def create_qr_code():

    user_input = input("Enter the text or Url :")
    file_name = input("Enter the file name :")

    if (not user_input):
        return

    img = qrcode.make(user_input)
    img.save(file_name)

    print(f"QR code saved as {file_name}")


create_qr_code()
