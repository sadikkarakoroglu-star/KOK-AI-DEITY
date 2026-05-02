[app]
title = KOK-AI-DEITY
package.name = kokai
package.domain = org.sayga
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0.0

# Gereksinimler (Virgül sonrası boşluk bırakma, numpy derleme hatası verirse silip dene)
requirements = python3,kivy,android,requests,numpy

orientation = portrait
android.permissions = INTERNET,VIBRATE,CAMERA,WRITE_EXTERNAL_STORAGE

# Android Ayarları
android.api = 34
android.minapi = 21
android.accept_sdk_license = True

# İşlemci Mimarileri (Geniş uyumluluk için)
android.archs = armeabi-v7a, arm64-v8a

# Logcat filtresi (Hataları daha rahat görmen için)
android.logcat_filters = *:S python:D

# İkon dosyası ana dizinde olmalı
icon.filename = icon.png
