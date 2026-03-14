from playwright.sync_api import sync_playwright

def analyze_styles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print("正在访问网站...")
        page.goto('https://johnfolio-fx8g3hkq.manus.space/')
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(5000)

        # 滚动到各个section
        print("滚动页面...")

        # 获取主要section的信息
        sections = [
            ("Hero", "section:has-text('Hello')"),
            ("About", "section:has-text('About')"),
            ("Skills", "section:has-text('Skills')"),
            ("Projects", "section:has-text('Projects')"),
            ("Contact", "section:has-text('Contact')")
        ]

        for name, selector in sections:
            print(f"\n=== {name} Section ===")
            try:
                section = page.locator(selector).first
                if section.count() > 0:
                    # 获取背景色
                    bg = section.evaluate("el => getComputedStyle(el).backgroundColor")
                    print(f"背景色: {bg}")

                    # 获取字体颜色
                    color = section.evaluate("el => getComputedStyle(el).color")
                    print(f"字体颜色: {color}")

                    # 获取字体大小
                    font_size = section.evaluate("el => getComputedStyle(el).fontSize")
                    print(f"字体大小: {font_size}")

                    # 获取字体
                    font = section.evaluate("el => getComputedStyle(el).fontFamily")
                    print(f"字体: {font}")

            except Exception as e:
                print(f"Error: {e}")

        # 获取所有颜色值
        print("\n=== 页面颜色值 ===")
        colors = page.evaluate("""
            () => {
                const colors = new Set();
                const elements = document.querySelectorAll('*');
                elements.forEach(el => {
                    const style = getComputedStyle(el);
                    if (style.backgroundColor && style.backgroundColor !== 'rgba(0, 0, 0, 0)') {
                        colors.add('bg: ' + style.backgroundColor);
                    }
                    if (style.color && style.color !== 'rgba(0, 0, 0, 0)') {
                        colors.add('color: ' + style.color);
                    }
                });
                return Array.from(colors);
            }
        """)
        for color in colors[:30]:
            print(color)

        # 获取按钮样式
        print("\n=== 按钮样式 ===")
        buttons = page.locator('button, a:has-text("View"), a:has-text("Contact")').all()
        for btn in buttons[:5]:
            text = btn.inner_text()
            bg = btn.evaluate("el => getComputedStyle(el).backgroundColor")
            color = btn.evaluate("el => getComputedStyle(el).color")
            radius = btn.evaluate("el => getComputedStyle(el).borderRadius")
            print(f"按钮: {text}")
            print(f"  背景: {bg}")
            print(f"  文字颜色: {color}")
            print(f"  圆角: {radius}")

        # 获取卡片样式
        print("\n=== 卡片样式 ===")
        cards = page.locator('[class*="card"], [class*="project"], [class*="skill"]').all()
        for card in cards[:3]:
            bg = card.evaluate("el => getComputedStyle(el).backgroundColor")
            radius = card.evaluate("el => getComputedStyle(el).borderRadius")
            shadow = card.evaluate("el => getComputedStyle(el).boxShadow")
            print(f"卡片背景: {bg}")
            print(f"圆角: {radius}")
            print(f"阴影: {shadow}")

        # 获取动画信息
        print("\n=== 动画效果 ===")
        animations = page.evaluate("""
            () => {
                const style = document.createElement('style');
                style.innerHTML = '';
                const sheets = document.styleSheets;
                const anims = [];
                try {
                    for (let sheet of sheets) {
                        try {
                            const rules = sheet.cssRules || sheet.rules;
                            for (let rule of rules) {
                                if (rule.type === CSSRule.KEYFRAMES_RULE) {
                                    anims.push(rule.name);
                                }
                                if (rule.cssText && rule.cssText.includes('animation')) {
                                    anims.push(rule.cssText.substring(0, 200));
                                }
                            }
                        } catch(e) {}
                    }
                } catch(e) {}
                return anims.slice(0, 20);
            }
        """)
        for anim in animations:
            print(f"- {anim[:100]}...")

        # 获取JS动画库
        print("\n=== 使用的JS库 ===")
        scripts = page.evaluate("""
            () => {
                const scripts = document.querySelectorAll('script[src]');
                return Array.from(scripts).map(s => s.src).filter(s => s);
            }
        """)
        for script in scripts:
            print(f"- {script}")

        # 获取所有class名
        print("\n=== 页面Class列表 ===")
        classes = page.evaluate("""
            () => {
                const classes = new Set();
                document.querySelectorAll('[class]').forEach(el => {
                    el.classList.forEach(c => classes.add(c));
                });
                return Array.from(classes).slice(0, 50);
            }
        """)
        for cls in classes:
            print(f"- {cls}")

        browser.close()

if __name__ == '__main__':
    analyze_styles()
