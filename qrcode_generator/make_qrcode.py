import sys
from argparse import ArgumentParser

from colorit import background, init_colorit
from qrcode import QRCode, constants
from qrcode.image.pil import PilImage
from transliterate import detect_language, slugify


def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--save", default=True)
    parser.add_argument("--console", default=False)
    parser.add_argument("-d", "--data", "--url", default=None)

    return parser


def qrcode_in_terminal(url, image: PilImage) -> None:
    init_colorit()
    size = image.size
    print("===== Your QR-code ======")
    print(f"Text: {url}", end="\n\n")
    for _y in range(size[0]):
        for _x in range(size[1]):
            color = image.getpixel((_y, _x))
            print(
                background(" ", (color,)*3),
                end=""
            )
        print()

    return input("\n Next? (just press enter): ")


def create_qrcode(url: str) -> PilImage:
    qr = QRCode(
        version=2,
        box_size=1,
        border=1,
        # error_correction=constants.ERROR_CORRECT_H,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill="black", back_color="white")


def save_qrcode(name, img: PilImage) -> None:
    text = name.replace("/", "").replace(".", "_").replace(":", "")
    if detect_language(text) == "ru":
        text = slugify(name.strip())

    img.save(f"{text}.png")


def main() -> None:
    data = create_parser().parse_args(sys.argv[1:])
    no_data = False
    urls = data.data

    for datum in [urls]:
        if datum is None:
            no_data = True
            break

        img = create_qrcode(datum)

        if data.console:
            qrcode_in_terminal(datum, img)
        if data.save:
            save_qrcode(datum, img)
            
    else:
        print("Creation Done")

    if no_data:
        print("No data")


if __name__ == "__main__":
    main()
