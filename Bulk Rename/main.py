import os


def main():
    i = 0
    # Never use back slash for declaring the path, always replace them with a front slash like below.
    # Also, do not forget the final front slash.
    path = "E:/ToTransfer/"
    for filename in os.listdir(path):
        my_dest = "img"+str(i)+".png"
        my_source = path+filename
        my_dest = path+my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    main()
