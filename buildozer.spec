[app]
title = پیام‌رسان رحمانی
package.name = rahmanrahmati
package.domain = org.rahman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
icon.filename = %(source.dir)s/00000000d2d081f4b18b53df52baf767.png
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 31.0.0
android.accept_sdk_license = True
