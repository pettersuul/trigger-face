# average-face

## Setup
Open terminal in root-folder (trigger-face/average-face/)

Run following commands:

`python3 -m venv venv`
Generates virtual environment

`source venv/bin/activate`
Activates virtual environment

`pip install cmake`
`pip install -r requirements.txt`
Installs dependencies

`source deactivate`
Exits virtual environment

## Run script
### Generation only
`source venv/bin/activate`
Activates virtual environment

`python generate.py`
This will grab images from subfolder "dataset/multiple" and generate an image (average-face.jpg) in the root folder.

`python generate.py path/to/folder`
This will substitude the default dataset-folder with the specified folder ("path/to/folder")

### View images
This version will show images with generated landmarks during the generation process, aka CSI-mode.

`source venv/bin/activate`
Activates virtual environment

`python view.py`
This will grab images from subfolder "dataset/multiple" and generate an image (average-face.jpg) in the root folder.

`python view.py path/to/folder`
This will substitute the default dataset-folder with the specified folder ("path/to/folder")

# 3D-mesh

## Setup
Open terminal in root-folder (trigger-face/3d-mesh/)

Run following commands:

`python3 -m venv venv`
Generates virtual environment

`source venv/bin/activate`
Activates virtual environment

`pip install -r requirements.txt`
Installs dependencies

`source deactivate`
Exits virtual environment

## Run script

### Live-view

This version will use your camera and overlay a AI-generated 3D-mesh. This outputs nothing and is only used for visualizing.

`source venv/bin/activate`  
Activates virtual environment

`python camera.py`
Runs script and opens window for camera-view. Esc-button closes window and script.

### Generate images with mesh

This version will show and save images with a 3D-mesh overlay.

`source venv/bin/activate`
Activates virtual environment

`python images.py`
This will grab images from subfolder "dataset/multiple" and generate images in the subfolder "tmp"

`python view.py path/to/folder`
This will substitute the default dataset-folder with the specified folder ("path/to/folder"). The script closes automatically when done.

`python view.py path/to/folder/image.jpg`
This will substitute the default dataset-folder with a single specified image. The script closes when image-window is closed.

### Generate 3D-plot
This version generates a 3D-plot which can be rotated.

`source venv/bin/activate`
Activates virtual environment

`python 3d-plot.py`
This will generate a 3D-plot from "dataset/average/trigger-average.jpg".

`python python 3d-plot.py /path/to/folder/image.jpg`
This will specify which image to use to generate 3D-plot.
