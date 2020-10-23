# [Create custom COCO data set for object detection]
## Quick start

### Usage
- Run the `voc2coco.py` script to generate a COCO data formatted JSON file for you.
```sh
python3 voc2coco.py ./data/VOC/Annotations ./data/coco/output.json
```
- Run the `voc2coco_TrainTestSplit.py` to generate COCO data formatted JSON file for test images or Train images
```sh
python3 voc2coco_TrainTestSplit.py ./data/VOC/Annotations ./data/coco/output_test.json ./data/VOC/ImageSets/Main/test.txt
python3 voc2coco_TrainTestSplit.py ./data/VOC/Annotations ./data/coco/output_train.json ./data/VOC/ImageSets/Main/trainval.txt
```
- Run the Jupyter notebook `COCO_Image_Viewer.ipynb` to visualize the coco annotations. 
