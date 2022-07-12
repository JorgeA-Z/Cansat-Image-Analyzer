import cv2
import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt
class Canlyzer:
    def __init__(self, path, treshoold, name, out):
        self.path = path
        self.treshoold = treshoold
        self.name = name
        self.out = out
    def canny(self):
        original = cv2.imread(self.path)
        
        gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

        gauss = cv2.GaussianBlur(gris, (5,5), 0)
        
        canny = cv2.Canny(gauss, self.treshoold[0], self.treshoold[1])
        cv2.imwrite(fr'{self.out}\{self.name}_canny.jpg', canny)

    def histograma(self):
        imagen = skimage.io.imread(self.path)

        colors = ("red", "green", "blue")
        channel_ids = (0, 1, 2)

        # create the histogram plot, with three lines, one for
        # each color
        plt.figure()
        plt.xlim([0, 256])
        for channel_id, c in zip(channel_ids, colors):
            histogram, bin_edges = np.histogram(
                imagen[:, :, channel_id], bins=256, range=(0, 256)
            )
            plt.plot(bin_edges[0:-1], histogram, color=c)

        plt.title("Color Histograma")
        plt.xlabel("Color value")
        plt.ylabel("Pixel count")

        plt.savefig(fr'{self.out}\{self.name}_histogram.jpg')

    def espectrogramas(self):
        original = cv2.imread(self.path)

        imagenHSV = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        
        imagenGray = cv2.cvtColor(original, cv2.COLOR_BGRA2GRAY)
        
        imagenGray = cv2.cvtColor(imagenGray, cv2.COLOR_GRAY2BGR)
        

        blueAlto = np.array([125, 255, 255], np.uint8)
        blueBajo = np.array([100, 100, 20], np.uint8)

        greenAlto = np.array([95, 255, 255], np.uint8)
        greenBajo = np.array([45, 100, 20], np.uint8)
        

        blueMask = cv2.inRange(imagenHSV, blueBajo, blueAlto)

        greenMask = cv2.inRange(imagenHSV, greenBajo, greenAlto)

        maskF = cv2.add(blueMask, greenMask)

        mask = cv2.bitwise_and(original, original, mask=maskF)

        invMask = cv2.bitwise_not(maskF)
        grayMask = cv2.bitwise_and(imagenGray, imagenGray, mask=invMask)
        MaskComparation = cv2.add(grayMask, mask)

        #Fondo en grises

        blueDetected = cv2.bitwise_and(original, original, mask=blueMask)

        invMask = cv2.bitwise_not(blueMask)
        grayBlue = cv2.bitwise_and(imagenGray, imagenGray, mask=invMask)
        blueComparation = cv2.add(grayBlue, blueDetected)

        greenDetected = cv2.bitwise_and(original, original, mask=greenMask)

        invMask = cv2.bitwise_not(greenMask)
        grayGreen = cv2.bitwise_and(imagenGray, imagenGray, mask=invMask)
        greenComparation = cv2.add(grayGreen, greenDetected)

        cv2.imwrite(fr'{self.out}\{self.name}_combination_comparacion.jpg', MaskComparation)
        cv2.imwrite(fr'{self.out}\{self.name}_comparacion.jpg', mask)
        cv2.imwrite(fr'{self.out}\{self.name}_verde.jpg', greenMask)
        cv2.imwrite(fr'{self.out}\{self.name}_azul.jpg', blueMask)
        cv2.imwrite(fr'{self.out}\{self.name}_gray_azul.jpg', grayBlue)
        cv2.imwrite(fr'{self.out}\{self.name}_blue_comparation.jpg', blueComparation)
        cv2.imwrite(fr'{self.out}\{self.name}_gray_green.jpg', grayGreen)
        cv2.imwrite(fr'{self.out}\{self.name}_green_comparation.jpg', greenComparation)

        