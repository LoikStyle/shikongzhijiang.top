from playwright.sync_api import sync_playwright
import os

def scrape_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("正在访问网站...")
        page.goto('https://johnfolio-fx8g3hkq.manus.space/')

        print("等待页面加载...")
        page.wait_for_load_state('networkidle')

        # 等待一下确保动画完成
        page.wait_for_timeout(3000)

        # 截图
        screenshot_path = 'D:/exam_prep_2026/shikongzhijiang.top/website_screenshot.png'
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"截图已保存到: {screenshot_path}")

        # 获取页面内容
        content = page.content()

        # 保存HTML
        html_path = 'D:/exam_prep_2026/shikongzhijiang.top/website_content.html'
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"HTML已保存到: {html_path}")

        # 获取主要元素的文本内容
        print("\n=== 页面文本内容 ===")
        body_text = page.locator('body').inner_text()
        print(body_text[:2000])  # 打印前2000字符

        # 获取所有链接
        print("\n=== 页面链接 ===")
        links = page.locator('a').all()
        for link in links[:20]:
            href = link.get_attribute('href')
            text = link.inner_text()
            if href:
                print(f"- {text}: {href}")

        browser.close()
        print("\n完成!")

if __name__ == '__main__':
    scrape_website()
