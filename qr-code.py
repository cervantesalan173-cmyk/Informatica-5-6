import qrcode

def main():
    song = "https://www.youtube.com/watch?v=r9L4AseD-aA&list=RDr9L4AseD-aA&start_radio=1"
    qr = qrcode.QRCode(version = 1, box_size = 5, border=5)
    qr.add_data(song)
    qr.make(fit=True)

    ing = qr.make_image(fill_color = "blue", back_color = "white")
    ing.save("youtube-qr.png")


    if __name__== "__main_":
        main()
