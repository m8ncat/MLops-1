import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("datasets", "stage1", "train.csv")
os.makedirs(os.path.join("datasets", "stage1"), exist_ok=True)

def process_data(fd_in, fd_out):
    fd_in.readline()
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        transported = line[13]
        cryosleep = line[2]
        age = line[5]
        vip = line[6]
        spa = line[10]
        fd_out.write("{},{},{},{},{}\n".format(transported, cryosleep, age, vip, spa))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
