import os

FILENAME = "testfile.txt"
LINE = "Some line of text\n"
LINE_COUNT = 10_000_000



def read_file_readlines():
    """Odczyt pliku przez readlines() – całość do listy"""
    with open(FILENAME, "w") as f:
        f.writelines([LINE] * LINE_COUNT)
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    return lines


def read_file_read():
    """Odczyt pliku przez read() – całość jako jeden string"""
    with open(FILENAME, "w") as f:
        f.writelines([LINE] * LINE_COUNT)
    with open(FILENAME, "r") as f:
        data = f.read()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    return data

def read_file_line_by_line():
    """Odczyt linia po linii w pętli"""
    with open(FILENAME, "w") as f:
        f.writelines([LINE] * LINE_COUNT)
    lines = []
    with open(FILENAME, "r") as f:
        for line in f:
            lines.append(line)
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    return lines


def read_file_using_generator_expression():
    """Odczyt pliku za pomocą wyrażenia generatora"""
    with open(FILENAME, "w") as f:
        f.writelines([LINE] * LINE_COUNT)
    with open(FILENAME, "r") as f:
        lines = list(line for line in f)
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    return lines


def read_file_mmap():
    """Odczyt z wykorzystaniem mmap (wydajny przy dużych plikach)"""
    import mmap
    with open(FILENAME, "w") as f:
        f.writelines([LINE] * LINE_COUNT)
    lines = []
    with open(FILENAME, "r") as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            for line in iter(mm.readline, b""):
                lines.append(line.decode())
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    return lines
