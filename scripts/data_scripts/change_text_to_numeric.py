import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("datasets", "stage3", "train.csv")
os.makedirs(os.path.join("datasets", "stage3"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_housing_age = []
    arr_total_rooms = []
    arr_income = []
    arr_house_value = []
    arr_ocean_proximity = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_housing_age.append(line[0])
        arr_total_rooms.append(line[1])
        arr_income.append(line[2])
        arr_house_value.append(line[3])
        arr_ocean_proximity.append(line[4])

    for i in range(len(arr_ocean_proximity)):
        if arr_ocean_proximity[i] == 'NEAR BAY':
            arr_ocean_proximity[i] = 0
        elif arr_ocean_proximity[i] == '<1H OCEAN':
            arr_ocean_proximity[i] = 1
        elif arr_ocean_proximity[i] == 'INLAND':
            arr_ocean_proximity[i] = 2
        elif arr_ocean_proximity[i] == '-':
            arr_ocean_proximity[i] = 3
        elif arr_ocean_proximity[i] == 'NEAR OCEAN':
            arr_ocean_proximity[i] = 4
        elif arr_ocean_proximity[i] == 'ISLAND':
            arr_ocean_proximity[i] = 5

    for p_housing_age, p_total_rooms, p_income, p_house_value, p_ocean_proximity  in zip(arr_housing_age, arr_total_rooms, arr_income, arr_house_value, arr_ocean_proximity):
        fd_out.write("{},{},{},{},{}\n".format(p_housing_age, p_total_rooms, p_income, p_house_value, p_ocean_proximity))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
