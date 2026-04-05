# Bước 1: Sử dụng Python hình ảnh nhẹ (slim) làm nền tảng
FROM python:3.12-slim

# Bước 2: Thiết lập thư mục làm việc trong container
WORKDIR /app

# Bước 3: Sao chép file danh sách thư viện vào container
COPY requirements.txt .

# Bước 4: Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Bước 5: Sao chép toàn bộ mã nguồn API vào container
COPY . .

# Bước 6: Mở cổng 8000 (cổng mặc định của FastAPI)
EXPOSE 8000

# Bước 7: Lệnh để chạy API Service khi container khởi động
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]