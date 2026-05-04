[app]
title = Super AI Automation
package.name = superai
package.domain = org.shubham
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Direct permissions, no extra text
android.permissions = INTERNET, REQUEST_INSTALL_PACKAGES, BIND_ACCESSIBILITY_SERVICE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, SYSTEM_ALERT_WINDOW

requirements = python3,kivy,requests,pyjnius

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

