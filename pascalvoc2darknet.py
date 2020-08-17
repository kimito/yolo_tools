import glob
import xml.etree.ElementTree as ET
from pprint import pprint
import sys

dir = sys.argv[1] if len(sys.argv) > 0 else "./"

def load_labels():
    labels = {}
    count = 0
    with open(dir + "/labels.txt") as label_file:
        for label in label_file.read().splitlines():
            labels[label] = count
            count += 1
    return labels


# main from here

labels = load_labels()

for file in glob.glob(dir + "/Annotations/*.xml"):
    print(file)

    with open(file) as f:
        s = f.read()
        root = ET.fromstring(s)

        img_w = int(root.findall('./size/width')[0].text)
        img_h = int(root.findall('./size/height')[0].text)

        print("  img_w:%i, img_h:%i"%(img_w, img_w))

        anno_filename = str(file).replace(".xml", ".txt")

        with open(anno_filename, mode='w') as f_txt:

            for obj in root.findall('./object'):
                name = obj.findall('./name')[0].text
                name_id = labels[name]

                print(f'    label: {name_id}')

                xmin = float(obj.findall('./bndbox/xmin')[0].text)
                ymin = float(obj.findall('./bndbox/ymin')[0].text)
                xmax = float(obj.findall('./bndbox/xmax')[0].text)
                ymax = float(obj.findall('./bndbox/ymax')[0].text)

                print(f'    ({xmin}, {ymin}, {xmax}, {ymax})')

                w = xmax - xmin
                h = ymax - ymin

                x_center = xmin + w/2.0
                y_center = ymin + h/2.0

                print (f'    ->({x_center/img_w}, {y_center/img_h}, {w/img_w}, {h/img_h})')

                f_txt.write(f'{name_id} {x_center/img_w} {y_center/img_h} {w/img_w} {h/img_h}')



