from playwright.sync_api import sync_playwright
import os

def scrape_website_full():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print("正在访问网站...")
        page.goto('https://johnfolio-fx8g3hkq.manus.space/')

        print("等待页面加载...")
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(5000)

        # 滚动加载所有内容
        print("滚动页面加载所有内容...")
        for i in range(3):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(2000)

        # 获取页面完整高度
        height = page.evaluate("document.body.scrollHeight")
        print(f"页面高度: {height}px")

        # 分段截图
        screenshot_path = 'D:/exam_prep_2026/shikongzhijiang.top/website_full.png'
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"完整截图已保存到: {screenshot_path}")

        # 获取所有文本内容
        print("\n=== 完整页面文本内容 ===")
        body_text = page.locator('body').inner_text()
        with open('D:/exam_prep_2026/shikongzhijiang.top/full_text.txt', 'w', encoding='utf-8') as f:
            f.write(body_text)
        print(body_text)

        # 获取所有链接
        print("\n=== 所有页面链接 ===")
        links = page.locator('a').all()
        with open('D:/exam_prep_2026/shikongzhijiang.top/all_links.txt', 'w', encoding='utf-8') as f:
            for link in links:
                href = link.get_attribute('href')
                text = link.inner_text()
                if href:
                    f.write(f"{text}: {href}\n")
                    print(f"- {text}: {href}")

        # 获取所有图片
        print("\n=== 所有图片 ===")
        images = page.locator('img').all()
        for img in images:
            src = img.get_attribute('src')
            alt = img.get_attribute('alt')
            print(f"- {alt}: {src}")

        # 获取CSS样式信息
        print("\n=== 页面样式分析 ===")
        # 获取背景色
        bg_color = page.evaluate("getComputedStyle(document.body).backgroundColor")
        print(f"背景色: {bg_color}")

        # 获取字体
        font_family = page.evaluate("getComputedStyle(document.body).fontFamily")
        print(f"字体: {font_family}")

        # 获取所有section/区块
        print("\n=== 页面区块结构 ===")
        sections = page.locator('section, div[id], div[class]').all()
        for i, section in enumerate(sections[:30]):
            try:
                id_attr = section.get_attribute('id')
                class_attr = section.get_attribute('class')
                text = section.inner_text()[:100]
                if id_attr or class_attr:
                    print(f"\n区块 {i+1}:")
                    print(f"  ID: {id_attr}")
                    print(f"  Class: {class_attr}")
                    print(f"  内容: {text}...")
            except:
                pass

        # 保存完整HTML
        html_path = 'D:/exam_prep_2026/shikongzhijiang.top/full_page.html'
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(page.content())
        print(f"\n完整HTML已保存到: {html_path}")

        browser.close()
        print("\n=== 完成 ===")

if __name__ == '__main__':
    scrape_website_full()
