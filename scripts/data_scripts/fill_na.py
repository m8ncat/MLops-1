import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("datasets", "stage2", "train.csv")
os.makedirs(os.path.join("datasets", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_transp = []
    arr_cryo = []
    arr_age = []
    arr_vip = []
    arr_spa = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_transp.append(line[0])
        arr_cryo.append(line[1])
        arr_vip.append(line[3])
        arr_spa.append(line[4])
        if line[2]:
            arr_age.append(float(line[2]))
        else:
            arr_age.append(0)

    s = sum(arr_age)

    for i in range(len(arr_age)):
        if arr_age[i] == 0:
            arr_age[i] = round(s / len(arr_age), 2)

    for transported, cryosleep, age, vip, spa in zip(arr_transp, arr_cryo, arr_age, arr_vip, arr_spa):
        fd_out.write("{},{},{},{},{}\n".format(transported, cryosleep, age, vip, spa))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
