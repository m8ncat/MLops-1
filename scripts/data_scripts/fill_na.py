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
    arr_housing_age = []
    arr_total_rooms = []
    arr_income = []
    arr_house_value = []
    arr_ocean_proximity = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_total_rooms.append(line[1])
        arr_income.append(line[2])
        arr_house_value.append(line[3])
        arr_ocean_proximity.append(line[4])
        if line[0] != 'NA':
            arr_housing_age.append(float(line[0]))
        else:
            arr_housing_age.append(0)

    s = sum(arr_housing_age)

    for i in range(len(arr_housing_age)):
        if arr_housing_age[i] == 0:
            arr_housing_age[i] = round(s / len(arr_housing_age), 3)

    for p_housing_age, p_total_rooms, p_income, p_house_value, p_ocean_proximity in zip(arr_housing_age, arr_total_rooms, arr_income, arr_house_value, arr_ocean_proximity):
        fd_out.write("{},{},{},{},{}\n".format(p_housing_age, p_total_rooms, p_income, p_house_value, p_ocean_proximity))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
