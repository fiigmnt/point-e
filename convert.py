import sys
import numpy
from numpy import load
# numpy.set_printoptions(threshold=sys.maxsize)

data = load('./model.npz')
files = data.files

points = data['coords']
red = data['R']
green = data['G']
blue = data['B']

data = ""
vertex_count = red.size

for i, point in enumerate(points):
    data = data + f"{point[0]} {point[1]} {point[2]} 0 0 0 {int(red[i] * 255)} {int(green[i] * 255)} {int(blue[i] * 255)} 2552\n"


header = f'''ply
format ascii 1.0
element vertex {vertex_count}
property float x
property float y
property float z
property float nx
property float ny
property float nz
property uchar red
property uchar green
property uchar blue
property uchar alpha
element face 0
property list uchar int vertex_indices
end_header
'''

with open('model.ply', 'w') as f:
    f.write(header)
    f.write(data)
