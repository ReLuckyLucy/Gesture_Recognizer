import cv2
import mediapipe as mp

# 初始化MediaPipe手部检测器
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 打开摄像头
cap = cv2.VideoCapture(0)

# 确保摄像头正常打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 使用MediaPipe的Hand解决方案
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        # 读取视频帧
        ret, frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            break

        # 将BGR图像转换为RGB格式
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 将RGB图像传递给MediaPipe进行手部检测
        results = hands.process(frame_rgb)

        # 检查是否检测到手部标志
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # 绘制每只手的标志
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        # 显示处理后的图像
        cv2.imshow('Hand Landmarks', frame)

        # 按 'q' 键退出q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 释放摄像头资源并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
