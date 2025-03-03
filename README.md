<div align="center">
 <img alt="logo" height="200px" src="img\logo.png">
</div>

# gesture_recognizer
基于谷歌的mediapipe框架下的手势识别器

<p align="center">
    <img alt="GitHub" src="https://img.shields.io/github/license/ReLuckyLucy/Gesture_Recognizer">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/ReLuckyLucy/Gesture_Recognizer">
    <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/ReLuckyLucy/Gesture_Recognizer?include_prereleases">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/ReLuckyLucy/Gesture_Recognizer">
</p>
<p align="center">
    <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/ReLuckyLucy/Gesture_Recognizer">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/ReLuckyLucy/Gesture_Recognizer">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/ReLuckyLucy/Gesture_Recognizer?style=social">
</p>

## ⌨️部署
```
conda create --name gesture python=3.12

conda activate gesture

pip install -r requirements.txt
```

## 💯下载模型
```
!wget -q https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task
```

## 🕹️运行（图片模式）
```
python hand_photo_landmarker.py
```
<div align="center">
 <img src="img\woman_hands.png">
</div>

## 🕹️运行（视频模式）
```
python hand_video_landmarker.py
```
手部特征点模型包可检测已检测到的手部区域内 21 个手指节坐标的关键点定位。该模型基于大约 3 万张真实图像以及对各种背景施加的几个渲染的合成手部模型进行了训练。

手部特征点模型包包含一个手掌检测模型和一个手部特征点检测模型。手掌检测模型在输入图片中定位手部，手部特征点检测模型可识别手掌检测模型定义的被剪裁手掌图片上的特定手部特征点。

<div align="center">
 <img src="img\hand-landmarks.png">
</div>

由于运行手掌检测模型非常耗时，因此在视频或直播跑步模式下，手部特征点会在一帧中使用手部特征点模型定义的边界框，以便为后续帧定位手部区域。仅当手部特征点模型不再识别出手部的存在或未能跟踪画面中的手部时，手部特征点才会重新触发手掌检测模型。这样可以减少手动标志器触发手掌检测模型的次数。




## 🎯下载识别手势模型
```
!wget -q https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task
```
## 🕹️运行（手势模式）
```
python hand_video_landmarker.py
```
>下载现成的模型。此模型可以识别 7 种手势：👍 🤟 ✌️ ☝️ ✊ 👋 👎

更多详情请访问：https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker/index?hl=zh-cn

