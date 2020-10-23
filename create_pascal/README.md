## CREATE PASCAL VOC 2007 DATASET

Create VOC 2007 dataset using text files
<!-- Refactor all the project ! Now it's more efficient and the structure is more clear.  -->

<!-- [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) -->

### Usage

1. Get your dataset annotations file, parse and save it to two files `Train_annotations.txt` and `Test_annotations.txt`, file name doesn't matter.

2. Your annotations file must have the format like this:

    `image_full_path object1_class x1_min y1_min x1_max y1_max object2_class x2_min y2_min x2_max y2_max...`
    
    * You can check `examples/Train_annotation.txt` file to understand the annotation format more clearly.
    * Place the text files inside `Train` and `Test` folders respectively.
    


3. Edit your dataset config and run file；
   
    * Run the `convertToVOC.py` to generate VOC dataset
    ```sh
    python3 convertToVOC.py /path/to/Annotations /path/to/output
    ```