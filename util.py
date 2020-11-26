import matplotlib.pyplot as plt
import numpy as np
import os


current_dir = os.getcwd()
png_path = current_dir + '/output/png'
if not os.path.exists(png_path):
    os.makedirs(png_path)


def plot_regret(figure_name):
    fig = plt.figure()
    x = range(10)
    y = np.cumsum(np.random.random(10))
    plt.plot(x, y, color='k')
    save_figure(figure_name)


def save_figure(figure_name):
    plt.savefig(png_path + '/' + figure_name)