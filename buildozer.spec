
name: K-OS-FINAL-BUILD
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install Buildozer
        run: |
          sudo apt update
          sudo apt install -y build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
          pip3 install --user --upgrade buildozer cython virtualenv
      - name: Build APK
        run: |
          cp calculator_mask.py main.py
          export PATH=$PATH:$HOME/.local/bin
          yes | buildozer -v android debug
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: KOK-AI-FINAL-APK
          path: bin/*.apk
