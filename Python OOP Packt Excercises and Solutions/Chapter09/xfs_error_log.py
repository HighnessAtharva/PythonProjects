import re


def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        if match := re.match(regex, line):
            regex = yield match.groups()[0]


def get_serials(filename):
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        try:
            bus = matcher.send(f"(sd \S+) {re.escape(device)}.*")
            yield matcher.send(f"{bus} \(SERIAL=([^)]*)\)")
            device = matcher.send(ERROR_RE)
        except StopIteration:
            return


for serial_number in get_serials("EXAMPLE_LOG.log"):
    print(serial_number)
