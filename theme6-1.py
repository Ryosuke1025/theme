import json

# JSON ファイルを開き、データをロード
with open('kabeposter/kabeposter_000000000000_keypoints.json') as f:
    data = json.load(f)

# 人のリストを取得
people = data['people']

# 各人の鼻と首の座標と信頼度を取得して表示
for i, person in enumerate(people):
    keypoints = person['pose_keypoints_2d']

    # 鼻の情報は配列の最初の3要素
    nose_x, nose_y, nose_confidence = keypoints[0:3]
    print(f'Person {i+1}, Nose - X: {nose_x}, Y: {nose_y}, Confidence: {nose_confidence}')

    # 首の情報は配列の4, 5, 6要素
    neck_x, neck_y, neck_confidence = keypoints[3:6]
    print(f'Person {i+1}, Neck - X: {neck_x}, Y: {neck_y}, Confidence: {neck_confidence}')