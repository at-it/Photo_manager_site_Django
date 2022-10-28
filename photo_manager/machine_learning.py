from sklearn.cluster import KMeans
import numpy as np
from PIL import Image


class DominantColorKMeansPredictor():

    def __init__(self):
        self.km = KMeans(n_clusters=5)

    def get_dominant_color(self, image):
        pixels = self.preprocess_image(image)
        self.km.fit(pixels)
        dominant_colors = self.km.cluster_centers_
        unique, counts = np.unique(self.km.labels_, return_counts=True)
        id = np.argmax(counts)
        dominant_color = [int(i) for i in dominant_colors[id]]
        return dominant_color

    def preprocess_image(self, image, size=(300, 300)):
        image.thumbnail(size)
        pixels = np.array(list(image.getdata()))
        pixels = pixels.reshape(len(pixels), -1)
        return pixels


def rgb2hex(r, g, b):
    return '#{:02X}{:02X}{:02X}'.format(int(r), int(g), int(b))
