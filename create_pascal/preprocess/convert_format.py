import cv2
import os
import re

input_annotations_dir = '/windows/D/workspace/datasets/person-detection/raw_annotations/annotations'
output_annotations_dir = '/windows/D/workspace/datasets/person-detection/raw_annotations/create-pascal-voc-dataset/annotations'
images_dir = '/windows/D/workspace/datasets/person-detection/raw_annotations/frames'
anno_images_dir = '/windows/D/workspace/datasets/person-detection/raw_annotations/anno_frames'

LABEL = 'person'
SKIP_FRAMES = 3

if __name__ == "__main__":
    annotations_list = os.listdir(input_annotations_dir)
    for annotation_file in annotations_list:
        print(annotation_file)
        annotation_file_path = os.path.join(input_annotations_dir,annotation_file) #bonanza.txt
        outputfile = os.path.join(output_annotations_dir,annotation_file)
        fout = open(outputfile,'w')

        #read file and it's contents
        with open(annotation_file_path) as fd:
            lines = fd.readlines()
            for l in range(0, len(lines), SKIP_FRAMES):
                line = lines[l]
                line = line.split(',')
                framenumber = int(line[0])
                frame_seq_number =  '%06d' %(framenumber+1)
                annotation_file = annotation_file.split('.')[0] #remove .txt 
                imagename = annotation_file+'_'+frame_seq_number+'.jpg' #service_000001.jpg
                imagepath = os.path.join(images_dir,imagename) #frames/service_000001.jpg
                img = cv2.imread(imagepath)
                if img is None:
                    continue
                height, width, _ = img.shape
                numboxes = int(line[1])
                write_string = f'{imagepath}'
                for i in range(2, 4*numboxes, 4):
                    x1 = int(line[i])
                    if x1 < 0:
                        x1 = 0
                    y1 = int(line[i+1])
                    w = int(line[i+2]) #width 
                    h = int(line[i+3]) # height 
                    
                    if y1+h > height:
                        y2 = height - y1

                    x2 = x1 + w 
                    y2 =  y1 + h
                    bbox = [x1,y1,x2,y2]  #xyxy
                    bbox = [int(b) for b in bbox] 
                    write_string = f"{write_string} {LABEL} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]} "
                    cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255,0,0), 2)
                # cv2.imshow('', img)
                # print(write_string)
                write_string = re.sub(' +', ' ', write_string)
                fout.write(write_string+'\n')
                # cv2.waitKey(0)
            fout.close()
