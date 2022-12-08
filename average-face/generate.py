import sys, os
from facer import facer
from matplotlib import pyplot as plt

# Load face images
input = "dataset/multiple"

if len(sys.argv) > 3:
    print('Too many inputs')
    sys.exit()
try:
    if sys.argv[1]:
        arg = sys.argv[1]
        if os.path.isdir(input):
            input = arg
        else:
            print('Invalid input file: ' + arg)
            sys.exit()
except:
    print('No input defined, using default input')

print('input: ' + input)


images = facer.load_images(input)

# Detect landmarks for each face
landmarks, faces = facer.detect_face_landmarks(images)

# Use  the detected landmarks to create an average face
average_face = facer.create_average_face(faces, landmarks, save_image=True, view=False)

# View the composite image
plt.imshow(average_face)
plt.axis('off')
plt.show()
