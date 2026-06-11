#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# 创建画布
width, height = 1080, 1920
img = Image.new('RGB', (width, height), '#FFF8E1')
draw = ImageDraw.Draw(img)

# 字体设置（使用系统字体）
try:
    font_title = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 80)
    font_subtitle = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 40)
    font_name = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 50)
    font_detail = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 36)
    font_small = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 32)
    font_footer = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', 28)
except:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_name = ImageFont.load_default()
    font_detail = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_footer = ImageFont.load_default()

# 颜色
colors = {
    'pink': '#FF6B6B',
    'yellow': '#FFD93D',
    'green': '#6BCB77',
    'blue': '#4D96FF',
    'orange': '#FF9F45',
    'purple': '#9B59B6',
    'text': '#333333',
    'subtext': '#666666',
}

# 标题
draw.text((width//2, 100), '🍽️ 明天早餐吃什么？', font=font_title, fill=colors['pink'], anchor='mm')
draw.text((width//2, 180), '每晚选好，第二天元气满满！', font=font_subtitle, fill=colors['subtext'], anchor='mm')

# 菜单数据
menus = [
    {'num': '1', 'emoji': '🍙', 'name': '饭团', 'tags': ['肉松', '鳕鱼肠', '虾仁'], 'sub': '水果 + 温水', 'color': colors['pink']},
    {'num': '2', 'emoji': '🍗', 'name': '蜜汁鸡翅', 'tags': [], 'sub': '小米粥 + 西红柿', 'color': colors['orange']},
    {'num': '3', 'emoji': '🍕', 'name': '小披萨', 'tags': ['大虾', '鸡米花', '玉米粒', '芝士'], 'sub': '水果', 'color': colors['pink']},
    {'num': '4', 'emoji': '🥧', 'name': '蛋挞套餐', 'tags': [], 'sub': '小米粥 + 水果', 'color': colors['orange']},
    {'num': '5', 'emoji': '🍞', 'name': '烤馒头', 'tags': ['奶酪'], 'sub': '蛋白质 + 水果', 'color': colors['pink']},
    {'num': '6', 'emoji': '🥞', 'name': '糖饼', 'tags': [], 'sub': '小米粥', 'color': colors['orange']},
]

# 绘制菜单卡片
start_y = 260
card_height = 230
gap = 20

for i, menu in enumerate(menus):
    y = start_y + i * (card_height + gap)
    x = 60
    card_width = width - 120

    # 卡片背景
    draw.rounded_rectangle([x, y, x+card_width, y+card_height], radius=30, fill='white', outline=menu['color'], width=4)

    # 圆形编号
    circle_x = x + 50
    circle_y = y + card_height//2
    draw.ellipse([circle_x-40, circle_y-40, circle_x+40, circle_y+40], fill=menu['color'])
    draw.text((circle_x, circle_y), menu['num'], font=font_name, fill='white', anchor='mm')

    # 食物名
    text_x = x + 110
    draw.text((text_x, y + 30), f"{menu['emoji']} {menu['name']}", font=font_name, fill=colors['text'])

    # 标签
    tag_y = y + 95
    if menu['tags']:
        tags_text = ' / '.join(menu['tags'])
        draw.text((text_x, tag_y), f"可选：{tags_text}", font=font_detail, fill='#888888')
        tag_y += 50
    else:
        tag_y += 20

    # 配菜
    draw.text((text_x, tag_y), f"配：{menu['sub']}", font=font_small, fill='#999999')

# 底部装饰
footer_y = height - 150
draw.text((width//2, footer_y), '━━━━━━━━━━━━━━━━━', font=font_footer, fill='#DDDDDD', anchor='mm')
draw.text((width//2, footer_y + 50), '猫巴士 🚌 出品', font=font_footer, fill='#CCCCCC', anchor='mm')

# 保存
output_path = '/Users/wangjing/WorkBuddy/Claw/breakfast-menu.png'
img.save(output_path, 'PNG')
print(f'图片已保存到: {output_path}')
