name: Build APK

on:
  workflow_dispatch:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install system dependencies
        run: |
          sudo apt update
          sudo apt install -y git zip unzip openjdk-17-jdk python3-pip \
            autoconf libtool pkg-config zlib1g-dev libncurses-dev \
            cmake libffi-dev libssl-dev

      - name: Install buildozer (pinned stable versions)
        run: |
          pip3 install --upgrade "pip==24.0"
          pip3 install "buildozer==1.5.0" "cython==0.29.36" "python-for-android==2024.1.21"

      - name: Build APK
        run: |
          yes | buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: app-apk
          path: bin/*.apk
