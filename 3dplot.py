import pandas
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 


def plot3D(csv_points_filename):
    points = pandas.read_csv(csv_points_filename)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = points['x'].values
    y = points['y'].values
    z = points['z'].values
    ax.scatter(x, y, z, c='r', marker='o')
    plt.show()