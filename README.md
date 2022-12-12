# EmotionDetection
This project tells the user what facial expression an image is making using image classification
![image](https://user-images.githubusercontent.com/119083331/206937284-7b2f3464-47aa-4009-b40f-ff55016ecf91.png)

## The Algorithm
This project was developed using Jetson Nano. It is a retrained resnet18 model whose dataset consists of many people making various faces, each labelled by their expression. When it is run, it uses the imagenet.py program with the model to determine the expression of an inputted image.

## Running the Project
1. Make sure to have resnet18.onnx and labels.txt from this project downloaded on the Jetson Nano
2. Clone the jetson-inference project from GitHub using "git clone --recursive https://github.com/dusty-nv/jetson-inference" and change directories into it
3. Make sure to have python packages installed using "sudo apt-get install libpython3-dev python3-numpy"
4. Make a build directory and run "cmake ../" in the build directory
5. To classify an image, run "imagenet.py --model=$MODEL/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$LABEL/labels.txt $IMAGE $OUTPUT", where $MODEL is the folder resnet18.onnx is stored, $LABEL is the folder labels.txt is stored, $IMAGE is the image file to classify, and $OUTPUT is the name of the file to output to. See imagenet.py --model=resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=labels.txt happy_test.jpg output.jpg as an example.
6. To see the output, scp the outputted file from the Jetson Nano onto your computer.
