# voicevox_ros
## 動作確認環境
- Ubuntu22.04
- ROS 2 Humble

## 環境セットアップ
1. 公式サイトからvoicevoxをインストールする
2. ros2ワークスペースに本パッケージをクローンする
   ```bash
   mkdir -p ~/voicevox_ws/src && ~/voicevox_ws/src
   ```
   ```bash
   git clone 
   ```
3. ビルドする
   ```bash
   cd ~/voicevox_ws
   ```
   ```bash
   colcon build
   ```

## 動作確認
1. voicevoxを起動する（voicevoxを起動するとローカルにサーバが立つ）
2. voicevox_rosを起動する
   ```bash
   ros2 run voicevox_ros voicevox_ros
   ```
3. サービスをコールする
   ```bash
   ros2 service call /speak voicevox_msgs/srv/Speak "{text: \"こんにちは\"}"
   ```
