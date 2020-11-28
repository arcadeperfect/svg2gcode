from optimise import optimise_path, auto_scale, concatenate, remove_redundant_lines
from svg2gcode import get_shapes, shapes_2_gcode
from os.path import join
from json import dump as jdump, load as jload
from utils import *

# def write(output_file_name, data):
#     with open(output_file_name, 'w+') as output_file:
#         output_file.write(data)

def dump(outfile, data):
    with open(outfile, 'w+') as o:
        jdump(data, o)


def read(infile):
    with open(infile) as i:
        return jload(i)

proj_location = "/bish/projects/plots/noiseField"
svg_location = join(proj_location, "svg")
json_location = join(proj_location, "json")
gcode_location = join(proj_location, "gcode")
#
# svg_file = "test_shapes.svg"
svg_file = "1.svg"
# svg_file = "square.svg"

svg_path = join(svg_location, svg_file)
file_name = svg_file.split(".")[0]

shapes_file = f"{file_name}_shapes.json"
shapes_path = join(json_location, shapes_file)

optimised_shapes_file = f"{file_name}_optimised.json"
optimised_shapes_path = join(json_location, optimised_shapes_file)

concatenated_shapes_file = f"{file_name}_optimised.json"
concatenated_shapes_path = join(json_location, concatenated_shapes_file)

scaled_shapes_file = f"{file_name}_scaled.json"
scaled_shapes_path = join(json_location, scaled_shapes_file)

version = 9

gcode_output_file = f"{file_name}_v{version}.gcode"
gcode_output_path = join(gcode_location, gcode_output_file)

print(proj_location)
print(svg_location)
print(json_location)
print(gcode_location)
print(svg_path)
print(shapes_path)
print(optimised_shapes_path)
print(scaled_shapes_path)
print(concatenated_shapes_path)
print(gcode_output_path)

# auto_scale = False
#
# shapes = get_shapes(svg_path)                                         #parse svg
# dump(shapes_path, shapes)                                             #dump parsed svg to json
current = read(shapes_path)

# tempCurrent = []
# for x,i in enumerate(current):
#     if x%10 == 0:
#         tempCurrent.append(i)
# current = tempCurrent
#
# new_order = optimise_path(current)                                    #optimise json shapes
# dump(optimised_shapes_path, new_order)                                #dunmp optimised shapes
# current = read(optimised_shapes_path)

# jnew_order = read(optimised_shapes_path)                              #read optimised shapes
#

#flip xy
# for a,i in enumerate(current):
#     for b,j in enumerate(i):
#
#         c = current[a][b]
#         c.reverse()
#         current[a][b] = c
#         print(current[a][b])


scaled_shapes = auto_scale(current, 205, 268)

new_maxX = 0
new_maxY = 0
for i in scaled_shapes:
    new_maxX = max(new_maxX, max(i[0][0], i[-1][0]))
    new_maxY = max(new_maxY, max(i[0][-1], i[-1][-1]))
print("new max!!!!!!")
print(new_maxX, new_maxY)
current = scaled_shapes

# concat_shapes = concatenate(current, 0.35)
# current = concat_shapes

# remove_reundant = remove_redundant_lines(current, 0.4)
#
commands = shapes_2_gcode(current, test_boundries=False)                                 #generate gcode commands


write_gcode(gcode_output_path, commands)                              #write gcode file
