import numpy as np
import re

def load_data(output="lines", header=0, footer=None, **kwargs):
        filename = "test.txt"
        if output == "raw":
            s = open(filename).read()
            return s if s[-1] != "\n" else s[:-1]
        lines = open(filename).readlines()[header:footer]
        if output == "lines":
            return [x.strip() for x in lines]
        if output == "int":
            regex = re.compile("-?\d+")
            integers = [[int(x) for x in re.findall(regex, line)] for line in lines]
            return [integer for integer in integers if integer]
        if output == "np":
            if "delimiter" not in kwargs:
                kwargs["delimiter"] = ","
            return np.loadtxt(filename, dtype=int, **kwargs)
        if output == "chararray":
            return np.array([[char for char in line.strip()] for line in lines])