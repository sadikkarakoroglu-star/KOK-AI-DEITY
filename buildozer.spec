[app]
title = Hesap Makinesi
package.name = kokai
package.domain = org.sayga
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0.0
requirements = python3,kivy,android
orientation = portrait

# 🛡️ SIBER IZINLER
android.permissions = INTERNET, VIBRATE, CAMERA, ACCESS_WIFI_STATE, ACCESS_FINE_LOCATION

# 🏗️ DERLEME AYARLARI (Garantili Stabilite)
android.api = 34
android.minapi = 21
android.ndk = 26.1.10909125
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a
icon.filename = icon.png
