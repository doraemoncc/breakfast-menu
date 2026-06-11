#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

# 创建画布 - 卡通风格暖色背景
W, H = 1080, 1920
img = Image.new('RGB', (W, H), '#FFF5F0')
draw = ImageDraw.Draw(img)

# 尝试加载可爱字体
def get_font(size):
    fonts = [
        '/System/Library/Fonts/PingFang.ttc',
        '/System/Library/Fonts/STHeiti Light.ttc',
        '/System/Library/Fonts/Hiragino Sans GB.ttc',
        '/Library/Fonts/Arial Unicode.ttf',
    ]
    for f in fonts:
        if os.path.exists(f):
            try:
                return ImageFont.truetype(f, size)
            except:
                pass
    return ImageFont.load_default()

font_title = get_font(85)
font_subtitle = get_font(38)
font_name = get_font(52)
font_detail = get_font(34)
font_small = get_font(30)
font_tag = get_font(26)

# 彩虹色系
CARD_COLORS = [
    ('#FF8FA3', '#FFF0F3'),  # 粉红
    ('#FFB347', '#FFFAEB'),  # 橙黄
    ('#FF8FA3', '#FFF0F3'),  # 粉红
    ('#FFB347', '#FFFAEB'),  # 橙黄
    ('#FF8FA3', '#FFF0F3'),  # 粉红
    ('#FFB347', '#FFFAEB'),  # 橙黄
]

# ===== 装饰性圆点背景 =====
import random
random.seed(42)
for _ in range(30):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(20, 60)
    c = random.choice(['#FFE4E8', '#FFF3D0', '#E8F4FF'])
    draw.ellipse([x-r, y-r, x+r, y+r], fill=c)

# ===== 顶部标题区 =====
# 标题背景
draw.rounded_rectangle([40, 30, W-40, 210], radius=40, fill='#FF6B6B')
draw.rounded_rectangle([40, 30, W-40, 210], radius=40, outline='#FF4757', width=3)

# 标题文字
draw.text((W//2, 80), '🍽️ 明天早餐吃什么？', font=font_title, fill='white', anchor='mm')
draw.text((W//2, 145), '每晚选好，第二天元气满满！', font=font_subtitle, fill='#FFE4E8', anchor='mm')

# ===== 菜单卡片 =====
menus = [
    {'num': '1', 'emoji': '🍙', 'name': '饭团', 'options': '肉松 / 鳕鱼肠 / 虾仁', 'sub': '🍇 水果  +  🥛 温水', 'border': '#FF6B6B', 'bg': '#FFF0F3'},
    {'num': '2', 'emoji': '🍗', 'name': '蜜汁鸡翅', 'options': '', 'sub': '🥣 小米粥 + 🍅 西红柿', 'border': '#FFB347', 'bg': '#FFFAEB'},
    {'num': '3', 'emoji': '🍕', 'name': '小披萨', 'options': '大虾 / 鸡米花 / 玉米粒 / 芝士', 'sub': '🍇 水果', 'border': '#FF6B6B', 'bg': '#FFF0F3'},
    {'num': '4', 'emoji': '🥧', 'name': '蛋挞套餐', 'options': '', 'sub': '🥣 小米粥 + 水果', 'border': '#FFB347', 'bg': '#FFFAEB'},
    {'num': '5', 'emoji': '🍞', 'name': '烤馒头', 'options': '+ 奶酪', 'sub': '🍳 蛋白质 + 水果', 'border': '#FF6B6B', 'bg': '#FFF0F3'},
    {'num': '6', 'emoji': '🥞', 'name': '糖饼', 'options': '', 'sub': '🥣 小米粥', 'border': '#FFB347', 'bg': '#FFFAEB'},
]

start_y = 240
card_h = 250
gap = 16
L_MARGIN = 50
R_MARGIN = W - 50
CARD_W = R_MARGIN - L_MARGIN

for i, m in enumerate(menus):
    y = start_y + i * (card_h + gap)
    
    # 卡片背景
    draw.rounded_rectangle([L_MARGIN, y, R_MARGIN, y+card_h], radius=28, fill=m['bg'])
    draw.rounded_rectangle([L_MARGIN, y, R_MARGIN, y+card_h], radius=28, outline=m['border'], width=4)
    
    # 编号圆
    nx = L_MARGIN + 60
    ny = y + card_h // 2
    R = 38
    draw.ellipse([nx-R, ny-R, nx+R, ny+R], fill=m['border'])
    draw.ellipse([nx-R+3, ny-R+3, nx+R-3, ny+R-3], outline='white', width=3)
    draw.text((nx, ny), m['num'], font=get_font(44), fill='white', anchor='mm')
    
    # 主文字区
    tx = L_MARGIN + 130
    # 食物名
    draw.text((tx, y+28), f"{m['emoji']} {m['name']}", font=font_name, fill='#333333')
    
    # 选项标签
    if m['options']:
        opt_y = y + 95
        draw.text((tx, opt_y), f"可选：{m['options']}", font=font_detail, fill='#999999')
        sub_y = y + 148
    else:
        sub_y = y + 120
    
    # 配菜
    draw.text((tx, sub_y), f"配：{m['sub']}", font=font_small, fill='#AAAAAA')
    
    # 右侧小装饰
    rx = R_MARGIN - 70
    draw.text((rx, ny), '⭐', font=get_font(40), fill=m['border'], anchor='mm')

# ===== 底部装饰 =====
fy = H - 130
draw.text((W//2, fy), '✿ ✿ ✿', font=get_font(32), fill='#FFD0D0', anchor='mm')
draw.text((W//2, fy + 50), '猫巴士 🚌 出品', font=get_font(26), fill='#CCCCCC', anchor='mm')

# 保存
out = '/Users/wangjing/WorkBuddy/Claw/breakfast-menu-v2.png'
img.save(out, 'PNG', quality=95)
print(f'Done: {out}')
