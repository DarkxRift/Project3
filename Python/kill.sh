ps aux | grep -i "mjpg_streamer" | awk '{print $2}' | xargs sudo kill -9

