import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_code(data):
    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # QR 코드를 이미지로 변환
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    st.title("QR Code Generator")
    st.write("Enter the text or URL to generate a QR code.")

    # 입력 필드
    input_text = st.text_input("Input text or URL:")

    if st.button("Generate QR Code"):
        if input_text:
            # QR 코드 생성
            qr_image = generate_qr_code(input_text)

            # Streamlit에 QR 코드 이미지 표시
            st.image(qr_image, caption="Generated QR Code", use_column_width=True)

            # QR 코드 다운로드 링크 제공
            buffer = BytesIO()
            qr_image.save(buffer, format="PNG")
            buffer.seek(0)
            st.download_button(
                label="Download QR Code",
                data=buffer,
                file_name="qrcode.png",
                mime="image/png",
            )
        else:
            st.warning("Please enter text or a URL to generate a QR code.")

if __name__ == "__main__":
    main()
