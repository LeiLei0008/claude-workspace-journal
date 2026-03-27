import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from send_email import send_email

html = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,sans-serif;color:#1a1a2e;">
<div style="max-width:620px;margin:24px auto;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.08);">

  <!-- ── HEADER ── -->
  <div style="background:linear-gradient(135deg,#1565c0 0%,#1976d2 60%,#42a5f5 100%);padding:28px 32px 24px;">
    <div style="font-size:12px;color:rgba(255,255,255,0.65);letter-spacing:1px;text-transform:uppercase;margin-bottom:6px;">2026 · 第12周 · 3月21日—3月27日</div>
    <div style="font-size:20px;font-weight:700;color:#fff;line-height:1.3;">📊 消费周报</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.8);margin-top:4px;">旅游 + 停车撑起了这周的账单</div>
  </div>

  <!-- ── 1. SUMMARY CARDS ── -->
  <div style="padding:24px 32px 0;">
    <div style="font-size:11px;font-weight:700;color:#90a4ae;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">本周概览</div>
    <table style="width:100%;border-spacing:8px;border-collapse:separate;margin:0 -8px;">
      <tr>
        <td style="background:#e3f2fd;border-radius:10px;padding:14px 16px;width:25%;">
          <div style="font-size:11px;color:#1565c0;font-weight:600;margin-bottom:4px;">总支出</div>
          <div style="font-size:22px;font-weight:800;color:#1565c0;">¥5,114</div>
        </td>
        <td style="background:#fff3e0;border-radius:10px;padding:14px 16px;width:25%;">
          <div style="font-size:11px;color:#e65100;font-weight:600;margin-bottom:4px;">环比上周</div>
          <div style="font-size:22px;font-weight:800;color:#e65100;">+11.2%</div>
          <div style="font-size:11px;color:#bf360c;">上周 ¥4,598</div>
        </td>
        <td style="background:#e8f5e9;border-radius:10px;padding:14px 16px;width:25%;">
          <div style="font-size:11px;color:#2e7d32;font-weight:600;margin-bottom:4px;">3月累计</div>
          <div style="font-size:22px;font-weight:800;color:#2e7d32;">¥92,003</div>
        </td>
        <td style="background:#f3e5f5;border-radius:10px;padding:14px 16px;width:25%;">
          <div style="font-size:11px;color:#6a1b9a;font-weight:600;margin-bottom:4px;">日均消费</div>
          <div style="font-size:22px;font-weight:800;color:#6a1b9a;">¥3,407</div>
          <div style="font-size:11px;color:#4a148c;">27天均值</div>
        </td>
      </tr>
    </table>
  </div>

  <!-- ── 2. CATEGORY TABLE ── -->
  <div style="padding:24px 32px 0;">
    <div style="font-size:11px;font-weight:700;color:#90a4ae;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">分类汇总</div>
    <table style="width:100%;border-collapse:collapse;font-size:13px;">
      <thead>
        <tr style="background:#f5f7fa;">
          <th style="text-align:left;padding:9px 12px;color:#78909c;font-weight:600;border-bottom:2px solid #eceff1;">分类</th>
          <th style="text-align:right;padding:9px 12px;color:#78909c;font-weight:600;border-bottom:2px solid #eceff1;">本周</th>
          <th style="text-align:right;padding:9px 12px;color:#78909c;font-weight:600;border-bottom:2px solid #eceff1;">占比</th>
          <th style="text-align:right;padding:9px 12px;color:#78909c;font-weight:600;border-bottom:2px solid #eceff1;">上周</th>
          <th style="text-align:right;padding:9px 12px;color:#78909c;font-weight:600;border-bottom:2px solid #eceff1;">变化</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid #f0f4f8;">
          <td style="padding:10px 12px;">✈️ 旅游</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;">¥2,160</td>
          <td style="padding:10px 12px;text-align:right;color:#78909c;">42.2%</td>
          <td style="padding:10px 12px;text-align:right;color:#bbb;">¥0</td>
          <td style="padding:10px 12px;text-align:right;color:#e53935;font-weight:600;">新增</td>
        </tr>
        <tr style="background:#fafcff;border-bottom:1px solid #f0f4f8;">
          <td style="padding:10px 12px;">🚗 交通费</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;">¥1,365</td>
          <td style="padding:10px 12px;text-align:right;color:#78909c;">26.7%</td>
          <td style="padding:10px 12px;text-align:right;color:#bbb;">¥261</td>
          <td style="padding:10px 12px;text-align:right;color:#e53935;font-weight:600;">+¥1,104</td>
        </tr>
        <tr style="border-bottom:1px solid #f0f4f8;">
          <td style="padding:10px 12px;">🍜 餐饮吃喝</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;">¥1,185</td>
          <td style="padding:10px 12px;text-align:right;color:#78909c;">23.2%</td>
          <td style="padding:10px 12px;text-align:right;color:#bbb;">¥720</td>
          <td style="padding:10px 12px;text-align:right;color:#e53935;font-weight:600;">+¥465</td>
        </tr>
        <tr style="background:#fafcff;border-bottom:1px solid #f0f4f8;">
          <td style="padding:10px 12px;">🐱 宠物</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;">¥335</td>
          <td style="padding:10px 12px;text-align:right;color:#78909c;">6.6%</td>
          <td style="padding:10px 12px;text-align:right;color:#bbb;">¥0</td>
          <td style="padding:10px 12px;text-align:right;color:#e53935;font-weight:600;">新增</td>
        </tr>
        <tr style="border-bottom:1px solid #f0f4f8;">
          <td style="padding:10px 12px;">👶 养娃</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;">¥53</td>
          <td style="padding:10px 12px;text-align:right;color:#78909c;">1.0%</td>
          <td style="padding:10px 12px;text-align:right;color:#bbb;">¥819</td>
          <td style="padding:10px 12px;text-align:right;color:#43a047;font-weight:600;">-¥766</td>
        </tr>
        <tr style="background:#fafcff;">
          <td style="padding:10px 12px;">🎮 其他/娱乐</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;">¥16</td>
          <td style="padding:10px 12px;text-align:right;color:#78909c;">0.3%</td>
          <td style="padding:10px 12px;text-align:right;color:#bbb;">¥797</td>
          <td style="padding:10px 12px;text-align:right;color:#43a047;font-weight:600;">-¥781</td>
        </tr>
      </tbody>
      <tfoot>
        <tr style="background:#e8edf5;border-top:2px solid #dce3ed;">
          <td style="padding:10px 12px;font-weight:700;">合计</td>
          <td style="padding:10px 12px;text-align:right;font-weight:800;color:#1565c0;">¥5,114</td>
          <td style="padding:10px 12px;text-align:right;color:#78909c;">100%</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;color:#555;">¥2,597</td>
          <td style="padding:10px 12px;text-align:right;font-weight:700;color:#e53935;">+¥2,517</td>
        </tr>
      </tfoot>
    </table>
    <div style="font-size:11px;color:#90a4ae;margin-top:6px;padding:0 4px;">⚠️ 上周数据为可比分类口径，已剔除医疗 ¥350、人情往来 ¥315、线上购物 ¥465 等无可比项</div>
  </div>

  <!-- ── 3. DAILY TREND ── -->
  <div style="padding:24px 32px 0;">
    <div style="font-size:11px;font-weight:700;color:#90a4ae;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">每日趋势</div>
    <table style="width:100%;border-collapse:collapse;font-size:13px;">
      <!-- max bar = ¥2334, scale to 180px -->
      <tr style="border-bottom:1px solid #f0f4f8;">
        <td style="padding:7px 0;color:#555;width:70px;">周六 3/21</td>
        <td style="padding:7px 8px;">
          <div style="height:16px;background:#bbdefb;border-radius:3px;overflow:hidden;">
            <div style="height:16px;background:#1976d2;border-radius:3px;width:63px;" title="¥823"></div>
          </div>
        </td>
        <td style="padding:7px 0;text-align:right;font-weight:600;width:60px;">¥823</td>
      </tr>
      <tr style="border-bottom:1px solid #f0f4f8;background:#fafcff;">
        <td style="padding:7px 0;color:#555;">周日 3/22</td>
        <td style="padding:7px 8px;">
          <div style="height:16px;background:#ffcdd2;border-radius:3px;overflow:hidden;">
            <div style="height:16px;background:#e53935;border-radius:3px;width:180px;" title="¥2334 最高"></div>
          </div>
        </td>
        <td style="padding:7px 0;text-align:right;font-weight:700;color:#e53935;">¥2,334</td>
      </tr>
      <tr style="border-bottom:1px solid #f0f4f8;">
        <td style="padding:7px 0;color:#555;">周一 3/23</td>
        <td style="padding:7px 8px;">
          <div style="height:16px;background:#bbdefb;border-radius:3px;overflow:hidden;">
            <div style="height:16px;background:#1976d2;border-radius:3px;width:31px;" title="¥401"></div>
          </div>
        </td>
        <td style="padding:7px 0;text-align:right;font-weight:600;">¥401</td>
      </tr>
      <tr style="border-bottom:1px solid #f0f4f8;background:#fafcff;">
        <td style="padding:7px 0;color:#555;">周二 3/24</td>
        <td style="padding:7px 8px;">
          <div style="height:16px;background:#bbdefb;border-radius:3px;overflow:hidden;">
            <div style="height:16px;background:#1976d2;border-radius:3px;width:12px;" title="¥154"></div>
          </div>
        </td>
        <td style="padding:7px 0;text-align:right;font-weight:600;">¥154</td>
      </tr>
      <tr style="border-bottom:1px solid #f0f4f8;">
        <td style="padding:7px 0;color:#555;">周三 3/25</td>
        <td style="padding:7px 8px;">
          <div style="height:16px;background:#bbdefb;border-radius:3px;overflow:hidden;">
            <div style="height:16px;background:#1976d2;border-radius:3px;width:15px;" title="¥190"></div>
          </div>
        </td>
        <td style="padding:7px 0;text-align:right;font-weight:600;">¥190</td>
      </tr>
      <tr style="border-bottom:1px solid #f0f4f8;background:#fafcff;">
        <td style="padding:7px 0;color:#555;">周四 3/26</td>
        <td style="padding:7px 8px;">
          <div style="height:16px;background:#bbdefb;border-radius:3px;overflow:hidden;">
            <div style="height:16px;background:#90caf9;border-radius:3px;width:4px;" title="¥49 最低"></div>
          </div>
        </td>
        <td style="padding:7px 0;text-align:right;font-weight:600;color:#90a4ae;">¥49</td>
      </tr>
      <tr>
        <td style="padding:7px 0;color:#555;">周五 3/27</td>
        <td style="padding:7px 8px;">
          <div style="height:16px;background:#bbdefb;border-radius:3px;overflow:hidden;">
            <div style="height:16px;background:#1565c0;border-radius:3px;width:90px;" title="¥1164"></div>
          </div>
        </td>
        <td style="padding:7px 0;text-align:right;font-weight:600;">¥1,164</td>
      </tr>
    </table>
  </div>

  <!-- ── 4. TOP 5 ── -->
  <div style="padding:24px 32px 0;">
    <div style="font-size:11px;font-weight:700;color:#90a4ae;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">Top 5 单笔支出</div>
    <table style="width:100%;border-collapse:collapse;font-size:13px;">
      <tr style="border-bottom:1px solid #f0f4f8;">
        <td style="padding:9px 0;width:24px;font-weight:700;color:#ffd600;">🥇</td>
        <td style="padding:9px 8px;">机票 <span style="color:#90a4ae;font-size:12px;">3/22</span></td>
        <td style="padding:9px 0;text-align:right;font-size:13px;color:#888;">旅游</td>
        <td style="padding:9px 0 9px 12px;text-align:right;font-weight:800;font-size:15px;color:#1565c0;">¥2,160</td>
      </tr>
      <tr style="background:#fafcff;border-bottom:1px solid #f0f4f8;">
        <td style="padding:9px 0;font-weight:700;color:#b0bec5;">🥈</td>
        <td style="padding:9px 8px;">停车费（3个月）<span style="color:#90a4ae;font-size:12px;">3/27</span></td>
        <td style="padding:9px 0;text-align:right;font-size:13px;color:#888;">交通</td>
        <td style="padding:9px 0 9px 12px;text-align:right;font-weight:700;">¥1,100</td>
      </tr>
      <tr style="border-bottom:1px solid #f0f4f8;">
        <td style="padding:9px 0;font-weight:700;color:#cd7f32;">🥉</td>
        <td style="padding:9px 8px;">双子烤肉 <span style="color:#90a4ae;font-size:12px;">3/21</span></td>
        <td style="padding:9px 0;text-align:right;font-size:13px;color:#888;">餐饮</td>
        <td style="padding:9px 0 9px 12px;text-align:right;font-weight:700;">¥386</td>
      </tr>
      <tr style="background:#fafcff;border-bottom:1px solid #f0f4f8;">
        <td style="padding:9px 0;">4️⃣</td>
        <td style="padding:9px 8px;">猫粮 <span style="color:#90a4ae;font-size:12px;">3/23</span></td>
        <td style="padding:9px 0;text-align:right;font-size:13px;color:#888;">宠物</td>
        <td style="padding:9px 0 9px 12px;text-align:right;font-weight:700;">¥335</td>
      </tr>
      <tr>
        <td style="padding:9px 0;">5️⃣</td>
        <td style="padding:9px 8px;">下午茶 <span style="color:#90a4ae;font-size:12px;">3/21</span></td>
        <td style="padding:9px 0;text-align:right;font-size:13px;color:#888;">餐饮</td>
        <td style="padding:9px 0 9px 12px;text-align:right;font-weight:700;">¥230</td>
      </tr>
    </table>
  </div>

  <!-- ── 5. MONTH BUDGET PROGRESS ── -->
  <div style="padding:24px 32px 0;">
    <div style="font-size:11px;font-weight:700;color:#90a4ae;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">3月预算进度</div>
    <div style="background:#f5f7fa;border-radius:10px;padding:16px 20px;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
        <div>
          <div style="font-size:13px;color:#555;">已过 27 天 · 累计 <strong>¥92,003</strong></div>
          <div style="font-size:12px;color:#90a4ae;margin-top:2px;">日均 ¥3,407 · 按此速率月底预计 <strong style="color:#e53935;">¥105,617</strong></div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:11px;color:#90a4ae;">月进度</div>
          <div style="font-size:18px;font-weight:800;color:#1565c0;">87.1%</div>
        </div>
      </div>
      <!-- Progress bar -->
      <div style="background:#dde3ea;border-radius:6px;height:10px;overflow:hidden;">
        <div style="background:linear-gradient(90deg,#1976d2,#42a5f5);border-radius:6px;height:10px;width:87.1%;"></div>
      </div>
      <div style="display:flex;justify-content:space-between;font-size:11px;color:#90a4ae;margin-top:5px;">
        <span>3月1日</span>
        <span>今天 3/27 (87.1%)</span>
        <span>3月31日</span>
      </div>
      <div style="margin-top:10px;padding:10px 12px;background:#fff8e1;border-radius:6px;border-left:3px solid #ffc107;">
        <div style="font-size:12px;color:#795548;line-height:1.5;">
          ⚡ 月底预计 <strong>¥105,617</strong>，剩余 4 天若控制在 ¥800/天，可将月总额压至 <strong>¥95,203</strong>
        </div>
      </div>
    </div>
  </div>

  <!-- ── 6. INSIGHTS ── -->
  <div style="padding:24px 32px 32px;">
    <div style="font-size:11px;font-weight:700;color:#90a4ae;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;">消费建议</div>
    <div style="background:#e8f5e9;border-radius:10px;padding:14px 16px;margin-bottom:10px;border-left:4px solid #43a047;">
      <div style="font-size:13px;font-weight:700;color:#2e7d32;margin-bottom:4px;">💡 大额支出要提前归类</div>
      <div style="font-size:13px;color:#388e3c;line-height:1.6;">
        机票（¥2,160）和季度停车费（¥1,100）合占 63.7%。建议每月初单独列"计划性大额支出"预算槽，避免周报数字虚高，也方便月末复盘真实日常消费水平。
      </div>
    </div>
    <div style="background:#fff3e0;border-radius:10px;padding:14px 16px;border-left:4px solid #fb8c00;">
      <div style="font-size:13px;font-weight:700;color:#e65100;margin-bottom:4px;">🍜 餐饮仍是最大可控项</div>
      <div style="font-size:13px;color:#bf360c;line-height:1.6;">
        本周餐饮 ¥1,185，周末两天贡献 ¥816（占 68.9%）。旅游归来后，下周工作日餐饮若能维持在 ¥150/天 以内，全周餐饮可控制在 ¥900 以下。
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <div style="background:#f5f7fa;padding:14px 32px;text-align:center;border-top:1px solid #eceff1;">
    <div style="font-size:11px;color:#b0bec5;">由 Claude Code 自动生成 · 数据来源：飞书多维表格 · 2026-03-27</div>
  </div>

</div>
</body>
</html>"""

subject = "📊 消费周报 | 3.21-3.27 本周 ¥5,114 · 3月累计 ¥92,003"
send_email(subject, html)
