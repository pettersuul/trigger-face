import os, sys
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

# Select target_input
folder = True
target_input = 'dataset/multiple'
files_input = []
target_output = 'tmp'
files_output = []

if len(sys.argv) > 2:
    print('Too many inputs')
    sys.exit()
try:
    if sys.argv[1]:
        target_input = sys.argv[1]
        if os.path.isdir(target_input):
            folder = True
        elif os.path.isfile(target_input):
            folder = False
except:
    print('No target_input defined, using default target_input')

print('target_input: ' + target_input)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# Colors are BGR, not RGB
drawing_spec_tesselation = mp_drawing.DrawingSpec(color=(150,255,150), thickness=1, circle_radius=1)
drawing_spec_contours = mp_drawing.DrawingSpec(color=(255,255,255), thickness=1, circle_radius=1)

# assign files
if folder == True:
    for filename in os.listdir(target_input):
        f = os.path.join(target_input, filename)
        if os.path.isfile(f) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            files_input.append(f)
else:
    files_input.append(target_input)

print('Found ' + str(len(files_input)) + ' images')

with mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5) as face_mesh:
  for idx, file in enumerate(files_input):
    # Show file index and name
    print(str(idx + 1) + ' of ' + str(len(files_input)), file)
    image = cv2.imread(file)
    # Convert the BGR image to RGB before processing.
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print and draw face mesh landmarks on the image.
    if not results.multi_face_landmarks:
      continue
    annotated_image = image.copy()
    for face_landmarks in results.multi_face_landmarks:
      #print('face_landmarks:', face_landmarks)
      mp_drawing.draw_landmarks(
          image=annotated_image,
          landmark_list=face_landmarks,
          connections=mp_face_mesh.FACEMESH_TESSELATION,
          landmark_drawing_spec=None,
          connection_drawing_spec=drawing_spec_tesselation #mp_drawing_styles.get_default_face_mesh_tesselation_style()
          )
      mp_drawing.draw_landmarks(
          image=annotated_image,
          landmark_list=face_landmarks,
          connections=mp_face_mesh.FACEMESH_CONTOURS,
          landmark_drawing_spec=None,
          connection_drawing_spec=drawing_spec_contours #mp_drawing_styles.get_default_face_mesh_contours_style()
          )


    cv2.imwrite('tmp/' + str(idx) + '.png', annotated_image)
    image = cv2.imread('tmp/' + str(idx) + '.png')
    cv2.imshow('image', image)
    if len(files_input) > 1:
        cv2.waitKey(250)
    else:
        cv2.waitKey(0) & 0xFF == 27
