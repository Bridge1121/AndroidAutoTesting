import os
import shutil
import subprocess

def run_tests():
    # 清理上次的测试结果
    if os.path.exists("allure-results"):
        shutil.rmtree("allure-results")
    if os.path.exists("allure-report"):
        shutil.rmtree("allure-report")

    # 运行 pytest 测试
    print("📦 Running pytest...")
    pytest_result = subprocess.run(["pytest", "case/", "--alluredir=allure-results"])
    if pytest_result.returncode != 0:
        print("Some tests failed.")
    else:
        print("All tests passed.")

    # 生成 Allure 报告
    print("📄 Generating Allure report...")
    subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"])

    # 打开 Allure 报告
    print("🌐 Opening Allure report...")
    subprocess.run(["allure", "open", "allure-report"])

if __name__ == "__main__":
    run_tests()
