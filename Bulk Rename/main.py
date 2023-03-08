import os


def main():
    # Never use back slash for declaring the path, always replace them with a front slash like below.
    # Also, do not forget the final front slash.
    path = "E:/ToTransfer/"
    for i, filename in enumerate(os.listdir(path)):
        my_dest = f"img{str(i)}.png"
        my_source = path+filename
        my_dest = path+my_dest
        os.rename(my_source, my_dest)


if __name__ == "__main__":
    main()
