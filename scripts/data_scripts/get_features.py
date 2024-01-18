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
        p_housing_age = line[3]
        p_total_rooms = line[4]
        p_income = line[8]
        p_house_value = line[9]
        p_ocean_proximity = line[10]

        fd_out.write("{},{},{},{},{}\n".format(p_housing_age, p_total_rooms, p_income, p_house_value, p_ocean_proximity))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
