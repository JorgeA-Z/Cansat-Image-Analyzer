import canlyzer as cn
import os
def main():
    
    dir_list =  os.listdir(r'C:\Users\52322\Desktop\Cansat-Image-Analyzer\Input')

    for i in dir_list:
        analisis = cn.Canlyzer(fr'C:\Users\52322\Desktop\Cansat-Image-Analyzer\Input\{i}', (55, 150), i.replace('.jpg', ''), fr'C:\Users\52322\Desktop\Cansat-Image-Analyzer\Output')
        analisis.canny()
        analisis.histograma()
        analisis.espectrogramas()

main()