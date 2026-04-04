import os

# Danh sách các thư mục cần tạo
folders = [
    "databricks/notebooks",
    "services/api_gateway",
    "services/user_service",
    "services/portfolio_service",
    "services/stock_service",
    "services/prediction_service",
    "frontend/src"
]

# Danh sách các file cần tạo
files = {
    ".gitignore": "venv/\n__pycache__/\n.env\n.DS_Store",
    "README.md": "# Stock Analysis & Prediction System\n\nDự án giữa kỳ môn Kiến trúc hướng dịch vụ.",
    "docker-compose.yml": "# Cấu hình Docker cho cuối kỳ",
    "databricks/requirements.txt": "yfinance\npandas\npyspark",
    "databricks/notebooks/01_ingest_bronze.py": "# Code kéo data từ Yahoo Finance",
    "databricks/notebooks/02_etl_silver.py": "# Code PySpark làm sạch data",
    "databricks/notebooks/03_train_model.py": "# Code train AI",
    "services/user_service/main.py": "# FastAPI User Service",
    "services/user_service/requirements.txt": "fastapi\nuvicorn\nsqlalchemy",
}

# Tạo thư mục
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Đã tạo thư mục: {folder}")

# Tạo file
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"📄 Đã tạo file: {filepath}")

print("\n✅ HOÀN TẤT! Cấu trúc dự án đã sẵn sàng.")