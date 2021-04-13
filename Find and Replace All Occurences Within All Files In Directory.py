import os


# Enter text to be replaced with. Can be a docstring/multiline
replacement = ""

# Enter the directory path. Change \ (if any) to /
for dname, dirs, files in os.walk("E:/GITHUB/w3resource.com-python-exercises/Javascript"):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
       # Enter text to find and then replace.
        s = s.replace("Go to the editor.", replacement)
        with open(fpath, "w") as f:
            f.write(s)
