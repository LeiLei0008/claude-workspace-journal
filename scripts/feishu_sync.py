#!/usr/bin/env python3
"""
飞书多维表格同步脚本
拉取 wiki 下的 bitable 账本数据，保存为 JSON 和 CSV
"""

import json
import csv
import os
import sys
from datetime import datetime

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import (
    ListAppTableFieldRequest,
    ListAppTableRecordRequest,
)

# ── 凭证配置 ──────────────────────────────────────────────────────────────────
APP_ID = "cli_a94ce1b66d39dccc"
APP_SECRET = "LTt9LQzZXPF1KYW6BkwyIfTILvxLYRz0"

WIKI_TOKEN = "F6IpwKg6airhlFk5XOJccpjRnOc"
TABLE_ID = "tblA0gPUrUYPCH7y"
VIEW_ID = "vewT4Ez58R"

OUTPUT_DIR = os.path.expanduser("~/claude-workspace-journal/feishu-data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── 初始化客户端 ───────────────────────────────────────────────────────────────
client = lark.Client.builder() \
    .app_id(APP_ID) \
    .app_secret(APP_SECRET) \
    .log_level(lark.LogLevel.ERROR) \
    .build()


def get_bitable_app_token(wiki_token: str) -> str:
    """Wiki token 在此场景下即为 bitable app_token，直接返回"""
    print(f"[1/4] 使用 wiki token 作为 bitable app_token: {wiki_token}")
    return wiki_token


def list_fields(app_token: str, table_id: str) -> list[dict]:
    """列出表的所有字段"""
    print(f"[2/4] 拉取字段结构 table={table_id}")
    fields = []
    page_token = None
    while True:
        builder = ListAppTableFieldRequest.builder() \
            .app_token(app_token) \
            .table_id(table_id) \
            .page_size(100)
        if page_token:
            builder = builder.page_token(page_token)
        resp = client.bitable.v1.app_table_field.list(builder.build())
        if not resp.success():
            raise RuntimeError(f"字段 API 错误 code={resp.code} msg={resp.msg}")
        for f in resp.data.items:
            fields.append({"field_id": f.field_id, "field_name": f.field_name, "type": f.type})
        if not resp.data.has_more:
            break
        page_token = resp.data.page_token
    print(f"    共 {len(fields)} 个字段")
    return fields


def list_records(app_token: str, table_id: str, view_id: str) -> list[dict]:
    """拉取所有记录（自动翻页）"""
    print(f"[3/4] 拉取记录 view={view_id}")
    records = []
    page_token = None
    while True:
        builder = ListAppTableRecordRequest.builder() \
            .app_token(app_token) \
            .table_id(table_id) \
            .view_id(view_id) \
            .page_size(100)
        if page_token:
            builder = builder.page_token(page_token)
        resp = client.bitable.v1.app_table_record.list(builder.build())
        if not resp.success():
            raise RuntimeError(f"记录 API 错误 code={resp.code} msg={resp.msg}")
        if resp.data.items:
            for r in resp.data.items:
                records.append({"record_id": r.record_id, "fields": r.fields})
        if not resp.data.has_more:
            break
        page_token = resp.data.page_token
    print(f"    共 {len(records)} 条记录")
    return records


def save_json(data: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    print(f"    JSON 已保存: {path}")


def save_csv(fields: list[dict], records: list[dict], path: str):
    field_names = [f["field_name"] for f in fields]
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["record_id"] + field_names, extrasaction="ignore")
        writer.writeheader()
        for r in records:
            row = {"record_id": r["record_id"]}
            for fn in field_names:
                val = r["fields"].get(fn, "")
                # 多值字段（人员、多选等）转字符串
                if isinstance(val, list):
                    val = "; ".join(
                        item.get("text", item.get("name", str(item))) if isinstance(item, dict) else str(item)
                        for item in val
                    )
                elif isinstance(val, dict):
                    val = val.get("text", str(val))
                row[fn] = val
            writer.writerow(row)
    print(f"    CSV 已保存: {path}")


def main():
    today = datetime.now().strftime("%Y%m%d")

    # 步骤 1：wiki → app_token
    app_token = get_bitable_app_token(WIKI_TOKEN)

    # 步骤 2：字段结构
    fields = list_fields(app_token, TABLE_ID)

    # 步骤 3：拉取记录
    records = list_records(app_token, TABLE_ID, VIEW_ID)

    # 步骤 4：保存
    print(f"[4/4] 保存数据")
    json_path = os.path.join(OUTPUT_DIR, f"2026_ledger_{today}.json")
    csv_path  = os.path.join(OUTPUT_DIR, f"2026_ledger_{today}.csv")
    save_json({"app_token": app_token, "table_id": TABLE_ID,
               "synced_at": datetime.now().isoformat(),
               "fields": fields, "records": records}, json_path)
    save_csv(fields, records, csv_path)

    # ── 预览 ─────────────────────────────────────────────────────────────────
    print("\n" + "═" * 60)
    print("字段结构：")
    for f in fields:
        print(f"  [{f['type']:>3}] {f['field_name']}  (id={f['field_id']})")

    print(f"\n总记录数：{len(records)}")
    print("\n前 10 条记录预览：")
    for i, r in enumerate(records[:10], 1):
        print(f"\n  [{i}] record_id={r['record_id']}")
        for k, v in r["fields"].items():
            disp = str(v)[:80] + ("…" if len(str(v)) > 80 else "")
            print(f"       {k}: {disp}")

    print("\n" + "═" * 60)
    print("同步完成 ✓")
    return json_path, csv_path


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"\n[错误] {e}", file=sys.stderr)
        sys.exit(1)
