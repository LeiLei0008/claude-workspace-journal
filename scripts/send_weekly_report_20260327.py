import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from send_email import send_email

html = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>周报 3.21-3.27</title>
</head>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#333;">
<div style="max-width:600px;margin:32px auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08);">

  <!-- Header -->
  <div style="background:#1a73e8;padding:28px 32px;">
    <div style="font-size:13px;color:rgba(255,255,255,0.75);margin-bottom:4px;">2026 · 第 12 周</div>
    <div style="font-size:22px;font-weight:700;color:#fff;">📊 周报 | 3.21–3.27</div>
    <div style="font-size:14px;color:rgba(255,255,255,0.85);margin-top:6px;">旅游 + 停车撑起了这周的账单</div>
  </div>

  <!-- Summary -->
  <div style="padding:24px 32px 0;">
    <p style="margin:0 0 20px;font-size:15px;line-height:1.7;color:#444;">
      这周花了 <strong>¥5,114</strong>，比上周多了 11.2%。主力是一张机票（¥2,160）和一次性补交了三个月停车费（¥1,100）——剥掉这两笔，日常开销其实挺正常的。
    </p>

    <!-- Stats Row -->
    <div style="display:flex;gap:12px;margin-bottom:24px;">
      <div style="flex:1;background:#f0f4ff;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:24px;font-weight:700;color:#1a73e8;">¥5,114</div>
        <div style="font-size:12px;color:#666;margin-top:4px;">本周总支出</div>
      </div>
      <div style="flex:1;background:#fff8f0;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:24px;font-weight:700;color:#f57c00;">+11.2%</div>
        <div style="font-size:12px;color:#666;margin-top:4px;">较上周 ¥4,598</div>
      </div>
      <div style="flex:1;background:#f0fff4;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:24px;font-weight:700;color:#2e7d32;">31</div>
        <div style="font-size:12px;color:#666;margin-top:4px;">本周笔数</div>
      </div>
    </div>

    <!-- Category Breakdown -->
    <h3 style="margin:0 0 12px;font-size:14px;font-weight:600;color:#888;letter-spacing:0.5px;text-transform:uppercase;">分类明细</h3>
    <table style="width:100%;border-collapse:collapse;margin-bottom:24px;">
      <tr style="background:#fafafa;">
        <th style="text-align:left;padding:10px 12px;font-size:13px;color:#666;font-weight:500;border-bottom:1px solid #eee;">类别</th>
        <th style="text-align:right;padding:10px 12px;font-size:13px;color:#666;font-weight:500;border-bottom:1px solid #eee;">金额</th>
        <th style="text-align:right;padding:10px 12px;font-size:13px;color:#666;font-weight:500;border-bottom:1px solid #eee;">占比</th>
        <th style="padding:10px 12px;border-bottom:1px solid #eee;width:120px;"></th>
      </tr>
      <tr>
        <td style="padding:10px 12px;font-size:14px;">✈️ 旅游</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;font-weight:600;">¥2,160</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;color:#888;">42.2%</td>
        <td style="padding:10px 12px;">
          <div style="background:#e3f2fd;border-radius:4px;height:8px;">
            <div style="background:#1a73e8;border-radius:4px;height:8px;width:42.2%;"></div>
          </div>
        </td>
      </tr>
      <tr style="background:#fafafa;">
        <td style="padding:10px 12px;font-size:14px;">🚗 交通费</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;font-weight:600;">¥1,365</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;color:#888;">26.7%</td>
        <td style="padding:10px 12px;">
          <div style="background:#e8f5e9;border-radius:4px;height:8px;">
            <div style="background:#43a047;border-radius:4px;height:8px;width:26.7%;"></div>
          </div>
        </td>
      </tr>
      <tr>
        <td style="padding:10px 12px;font-size:14px;">🍜 吃喝餐费</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;font-weight:600;">¥1,185</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;color:#888;">23.2%</td>
        <td style="padding:10px 12px;">
          <div style="background:#fff3e0;border-radius:4px;height:8px;">
            <div style="background:#fb8c00;border-radius:4px;height:8px;width:23.2%;"></div>
          </div>
        </td>
      </tr>
      <tr style="background:#fafafa;">
        <td style="padding:10px 12px;font-size:14px;">🐱 宠物</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;font-weight:600;">¥335</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;color:#888;">6.6%</td>
        <td style="padding:10px 12px;">
          <div style="background:#fce4ec;border-radius:4px;height:8px;">
            <div style="background:#e91e63;border-radius:4px;height:8px;width:6.6%;"></div>
          </div>
        </td>
      </tr>
      <tr>
        <td style="padding:10px 12px;font-size:14px;">👶 养娃</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;font-weight:600;">¥53</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;color:#888;">1.0%</td>
        <td style="padding:10px 12px;">
          <div style="background:#ede7f6;border-radius:4px;height:8px;">
            <div style="background:#7b1fa2;border-radius:4px;height:8px;width:1%;"></div>
          </div>
        </td>
      </tr>
      <tr style="background:#fafafa;">
        <td style="padding:10px 12px;font-size:14px;">🎮 其他/娱乐</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;font-weight:600;">¥16</td>
        <td style="padding:10px 12px;font-size:14px;text-align:right;color:#888;">0.3%</td>
        <td style="padding:10px 12px;">
          <div style="background:#f5f5f5;border-radius:4px;height:8px;">
            <div style="background:#9e9e9e;border-radius:4px;height:8px;width:0.3%;"></div>
          </div>
        </td>
      </tr>
    </table>

    <!-- Daily Trend -->
    <h3 style="margin:0 0 12px;font-size:14px;font-weight:600;color:#888;letter-spacing:0.5px;text-transform:uppercase;">每日趋势</h3>
    <table style="width:100%;border-collapse:collapse;margin-bottom:24px;">
      <tr>
        <td style="padding:8px 12px;font-size:13px;color:#555;border-bottom:1px solid #f0f0f0;">周六 3/21</td>
        <td style="padding:8px 12px;font-size:13px;text-align:right;font-weight:600;border-bottom:1px solid #f0f0f0;">¥823</td>
        <td style="padding:8px 12px;border-bottom:1px solid #f0f0f0;">
          <div style="background:#e3f2fd;border-radius:3px;height:6px;"><div style="background:#1a73e8;border-radius:3px;height:6px;width:35.3%;"></div></div>
        </td>
      </tr>
      <tr style="background:#fafafa;">
        <td style="padding:8px 12px;font-size:13px;color:#555;border-bottom:1px solid #f0f0f0;">周日 3/22</td>
        <td style="padding:8px 12px;font-size:13px;text-align:right;font-weight:600;color:#e53935;border-bottom:1px solid #f0f0f0;">¥2,334</td>
        <td style="padding:8px 12px;border-bottom:1px solid #f0f0f0;">
          <div style="background:#ffebee;border-radius:3px;height:6px;"><div style="background:#e53935;border-radius:3px;height:6px;width:100%;"></div></div>
        </td>
      </tr>
      <tr>
        <td style="padding:8px 12px;font-size:13px;color:#555;border-bottom:1px solid #f0f0f0;">周一 3/23</td>
        <td style="padding:8px 12px;font-size:13px;text-align:right;font-weight:600;border-bottom:1px solid #f0f0f0;">¥401</td>
        <td style="padding:8px 12px;border-bottom:1px solid #f0f0f0;">
          <div style="background:#e3f2fd;border-radius:3px;height:6px;"><div style="background:#1a73e8;border-radius:3px;height:6px;width:17.2%;"></div></div>
        </td>
      </tr>
      <tr style="background:#fafafa;">
        <td style="padding:8px 12px;font-size:13px;color:#555;border-bottom:1px solid #f0f0f0;">周二 3/24</td>
        <td style="padding:8px 12px;font-size:13px;text-align:right;font-weight:600;border-bottom:1px solid #f0f0f0;">¥154</td>
        <td style="padding:8px 12px;border-bottom:1px solid #f0f0f0;">
          <div style="background:#e3f2fd;border-radius:3px;height:6px;"><div style="background:#1a73e8;border-radius:3px;height:6px;width:6.6%;"></div></div>
        </td>
      </tr>
      <tr>
        <td style="padding:8px 12px;font-size:13px;color:#555;border-bottom:1px solid #f0f0f0;">周三 3/25</td>
        <td style="padding:8px 12px;font-size:13px;text-align:right;font-weight:600;border-bottom:1px solid #f0f0f0;">¥190</td>
        <td style="padding:8px 12px;border-bottom:1px solid #f0f0f0;">
          <div style="background:#e3f2fd;border-radius:3px;height:6px;"><div style="background:#1a73e8;border-radius:3px;height:6px;width:8.1%;"></div></div>
        </td>
      </tr>
      <tr style="background:#fafafa;">
        <td style="padding:8px 12px;font-size:13px;color:#555;border-bottom:1px solid #f0f0f0;">周四 3/26</td>
        <td style="padding:8px 12px;font-size:13px;text-align:right;font-weight:600;border-bottom:1px solid #f0f0f0;">¥49</td>
        <td style="padding:8px 12px;border-bottom:1px solid #f0f0f0;">
          <div style="background:#e3f2fd;border-radius:3px;height:6px;"><div style="background:#1a73e8;border-radius:3px;height:6px;width:2.1%;"></div></div>
        </td>
      </tr>
      <tr>
        <td style="padding:8px 12px;font-size:13px;color:#555;">周五 3/27</td>
        <td style="padding:8px 12px;font-size:13px;text-align:right;font-weight:600;">¥1,164</td>
        <td style="padding:8px 12px;">
          <div style="background:#e3f2fd;border-radius:3px;height:6px;"><div style="background:#1a73e8;border-radius:3px;height:6px;width:49.9%;"></div></div>
        </td>
      </tr>
    </table>

    <!-- Top 5 -->
    <h3 style="margin:0 0 12px;font-size:14px;font-weight:600;color:#888;letter-spacing:0.5px;text-transform:uppercase;">Top 5 单笔</h3>
    <div style="margin-bottom:24px;">
      <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 12px;background:#fff8e1;border-radius:6px;margin-bottom:6px;">
        <span style="font-size:14px;">🥇 机票</span>
        <span style="font-size:14px;font-weight:700;color:#f57f17;">¥2,160</span>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 12px;background:#fafafa;border-radius:6px;margin-bottom:6px;">
        <span style="font-size:14px;">🥈 停车费（3个月）</span>
        <span style="font-size:14px;font-weight:700;color:#666;">¥1,100</span>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 12px;background:#fafafa;border-radius:6px;margin-bottom:6px;">
        <span style="font-size:14px;">🥉 双子烤肉</span>
        <span style="font-size:14px;font-weight:700;color:#666;">¥386</span>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 12px;background:#fafafa;border-radius:6px;margin-bottom:6px;">
        <span style="font-size:14px;">4️⃣ 猫粮</span>
        <span style="font-size:14px;font-weight:700;color:#666;">¥335</span>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 12px;background:#fafafa;border-radius:6px;">
        <span style="font-size:14px;">5️⃣ 下午茶</span>
        <span style="font-size:14px;font-weight:700;color:#666;">¥230</span>
      </div>
    </div>

    <!-- March YTD -->
    <div style="background:#f0f4ff;border-radius:8px;padding:16px;margin-bottom:24px;display:flex;justify-content:space-between;align-items:center;">
      <div>
        <div style="font-size:13px;color:#666;">3月累计支出</div>
        <div style="font-size:22px;font-weight:700;color:#1a73e8;">¥92,002</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:13px;color:#666;">还剩 4 天</div>
        <div style="font-size:13px;color:#888;">月均日消费 ≈ ¥3,407</div>
      </div>
    </div>

    <!-- Insight -->
    <div style="border-left:4px solid #1a73e8;padding:12px 16px;background:#f8f9ff;border-radius:0 8px 8px 0;margin-bottom:32px;">
      <div style="font-size:13px;font-weight:600;color:#1a73e8;margin-bottom:4px;">💡 本周小结</div>
      <div style="font-size:14px;color:#444;line-height:1.6;">
        剔除机票和补缴停车费这两笔「大件」，本周实际日常消费约 <strong>¥1,854</strong>，在正常区间。下周可以关注餐饮是否继续维持在 ¥200/天 以内，旅游归来后记得把出行花销单独归类复盘。
      </div>
    </div>
  </div>

  <!-- Footer -->
  <div style="background:#f8f8f8;padding:16px 32px;text-align:center;border-top:1px solid #eee;">
    <div style="font-size:12px;color:#aaa;">由 Claude Code 自动生成 · 数据来源：飞书多维表格</div>
  </div>

</div>
</body>
</html>"""

subject = "📊 周报 | 3.21-3.27 旅游+停车撑起了这周的账单"
send_email(subject, html)
