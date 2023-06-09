# import sys
#
# inname, outname = sys.argv[1:3]
#
# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         for l in infile:
#             if "WARNING" in l:
#                 outfile.write(l.replace("WARNING", ""))


class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.readline()
        while l and "WARNING" not in l:
            l = self.insequence.readline()
        if not l:
            raise StopIteration
        return l.replace("WARNING", "")

inname = "sample_log.txt"
outname = "remove_warning_clas.txt"
with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = WarningFilter(infile)
        for l in filter:
            outfile.write(l)



def warning_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            yield l.replace("WARNING", "")

with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warning_filter(infile)
        for l in filter:
            outfile.write(l)

inname = "sample_log.txt"
outname = "remove_debug.txt"
def debug_filter(infilename):
    with open(infilename) as infile:
        yield from (
            l.replace("DEBUG", "") for l in infile if "DEBUG" in l
        )
filter = debug_filter(inname)
with open(outname, "w") as outfile:
    for l in filter:
        outfile.write(l)