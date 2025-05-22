#配置参数
def get_capabilities():
    return {
        "platformName": "Android",
        "deviceName": "AINOTEA224042300042",
        "automationName": "UiAutomator2",
        "appPackage": "com.aispeech.tablet",
        "appActivity": "com.aispeech.tablet.MainActivity",
        "noReset": True,#启动 App 时不重置应用数据（不清除登录、设置、缓存等），第一次运行测试建议设为false
        "unicodeKeyboard": True,#使用 Appium 提供的 Unicode 输入法（可输入中文）
        "resetKeyboard": True,#测试结束后还原为系统默认输入法
        "newCommandTimeout": 6000,#如果 Appium 在这段时间内没收到新命令，就断开连接（默认60秒）
        "autoGrantPermissions": True,#自动授予应用权限（如相机、存储等），无需手动点确认
        "skipUnlock": True,
        # "unlockType": "pin",
        # "unlockKey": "0000",
        # "skipUnlock": True,#跳过自动解锁屏幕的步骤（默认会尝试滑动解锁）
        "skipDeviceInitialization": True,#跳过设备初始化（如输入法设置、权限设置），可提高启动速度
    }

appium_server_url = "http://localhost:4723"