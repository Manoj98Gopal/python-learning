
import qrcode

# my code
def create_qr_code():

    user_input = input("Enter the text or Url :")
    file_name = input("Enter the file name :")

    if (not user_input):
        return

    img = qrcode.make(user_input)
    img.save(file_name)

    print(f"QR code saved as {file_name}")


# create_qr_code()

# mosh code
def create_qr_code_advance():
    
    user_input = input("Enter the text or Url :").strip()
    file_name = input("Enter the file name :").strip()
    
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(user_input)
    
    image = qr.make_image(fill_color='red', back_color='white')
    image.save(file_name)
    
    print(f"QR code save as {file_name}")
    


create_qr_code_advance()