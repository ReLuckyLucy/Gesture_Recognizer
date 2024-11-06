# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import os
import sys

# 抑制 TensorFlow 和 MediaPipe 的日志输出
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 初始化 MediaPipe 的 Hands 和绘制模块
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# 加载手势识别模型
try:
    base_options = python.BaseOptions(model_asset_path='model\gesture_recognizer.task')
    #base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)
except Exception as e:
    print(f"加载手势识别模型时出错: {e}")
    sys.exit()

def recognize_and_display(frame):
    # 将图像转换为 RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # 识别手势
    recognition_result = recognizer.recognize(image)

    # 提取并显示手势和关键点
    if recognition_result.gestures:
        top_gesture = recognition_result.gestures[0][0]
        hand_landmarks_list = recognition_result.hand_landmarks

        # 显示手势类别和分数
        cv2.putText(frame, f'{top_gesture.category_name} ({top_gesture.score:.2f})',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # 在图像上绘制关键点
        for hand_landmarks in hand_landmarks_list:
            if hasattr(hand_landmarks, 'landmark'):  # 确保 hand_landmarks 是符合条件的对象
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,  # 单个 hand_landmarks
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

    return frame

def main():
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("错误：无法打开摄像头。")
        sys.exit()

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("错误：无法捕获帧。")
            break

        # 识别并显示手势
        frame = recognize_and_display(frame)

        # 显示处理后的帧
        cv2.imshow("Gesture Recognition", frame)

        # 按下 'q' 键退出
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
