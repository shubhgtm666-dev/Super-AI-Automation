[app]
title = Super AI Automation
package.name = superai
package.domain = org.shubham
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Sabse important permissions automation ke liye
android.permissions = INTERNET, REQUEST_INSTALL_PACKAGES, BIND_ACCESSIBILITY_SERVICE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, SYSTEM_ALERT_WINDOW

# Pyjnius zaroori hai phone control ke liye
requirements = python3,kivy,requests,pyjnius

orientation = portrait
fullscreen = 0

# Fast build ke liye sirf ek arch rakha hai
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

# Accessibility Service Configuration
android.services = MyAIService:service.py
