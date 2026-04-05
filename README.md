# BÁO CÁO TIẾN ĐỘ GIỮA KỲ: HỆ THỐNG PHÂN TÍCH CHỨNG KHOÁN (SOA & CLOUD)
**Học phần:** Kiến trúc hướng dịch vụ và Điện toán đám mây  
**Nền tảng triển khai:** Databricks Cloud Platform

---

## 3.1. Thông tin nhóm
*   **Tên đề tài:** Xây dựng hệ thống thu thập và phân tích chỉ số chứng khoán dựa trên kiến trúc SOA và nền tảng Databricks.
*   **Danh sách thành viên:**
    1. [Họ tên của bạn] - [MSSV] (Nhóm trưởng)
    2. [Thành viên 2] - [MSSV]
    3. [Thành viên 3] - [MSSV]
*   **Mục tiêu hệ thống:** 
    *   Xây dựng Data Pipeline tự động thu thập dữ liệu chứng khoán từ Yahoo Finance API.
    *   Xử lý dữ liệu lớn (Big Data) qua các tầng Bronze - Silver - Gold trên Delta Lake.
    *   Cung cấp dữ liệu phân tích (SMA, Volatility) dưới dạng dịch vụ API (JSON) theo chuẩn kiến trúc SOA.

---

## 3.2. Thiết kế kiến trúc hệ thống
*   **Mô hình kiến trúc:** Hệ thống được thiết kế theo mô hình **Kiến trúc hướng dịch vụ (SOA)**, tách biệt giữa tầng xử lý dữ liệu (Data Processing Service) và tầng cung cấp dịch vụ (Data Serving Service).
*   **Sơ đồ kiến trúc tổng thể:** (Chi tiết xem tại Slide 4 trong báo cáo PDF)
    *   **Data Source:** Yahoo Finance API.
    *   **Processing:** Databricks Spark Engine & Delta Lake.
    *   **Integration:** Databricks SQL Warehouse & SQL Connector.
    *   **Serving:** API Service trả về định dạng JSON chuẩn.

---

## 3.3. Tiến độ triển khai trên Databricks
1.  **Workspace/Cluster:** Đã thiết lập Workspace trên Databricks Community Edition, cấu hình Cluster Runtime 13.3 LTS (Spark 3.4.1, Scala 2.12).
2.  **Notebook/Jobs đã tạo:**
    *   `01_ingestion`: Thu thập dữ liệu thô (Bronze).
    *   `02_transformation`: Làm sạch và chuẩn hóa dữ liệu (Silver).
    *   `03_analytics`: Tính toán chỉ số tài chính nâng cao (Gold).
    *   `04_api_service`: Dịch vụ cung cấp dữ liệu JSON (SOA Layer).
3.  **Data ingestion/ETL:** Đã thực hiện nạp dữ liệu thành công cho 10 mã cổ phiếu lớn (FPT, VCB, AAPL, TSLA...).
4.  **Delta Lake/Pipeline:** Thiết lập thành công **Databricks Workflow (Job DAG)** tự động hóa luồng ETL từ Ingestion đến Analytics.

---

## 3.4. Minh chứng thực hiện
*   **Hình ảnh kết quả:** (Chi tiết xem tại Slide 9 trong báo cáo PDF).
*   **Kết quả API (JSON Response):**
```json
{
    "status": 200,
    "symbol": "FPT.VN",
    "data": [
        {
            "date": "2024-04-05",
            "close": 115000.0,
            "sma_20": 112450.0,
            "sma_50": 108900.0
        }
    ]
}
```

---

## 3.5. Khó khăn và vấn đề tồn đọng
1.  **Lỗi kỹ thuật:** Gặp lỗi Encoding Latin-1 khi sử dụng Databricks SQL Connector do tên người dùng chứa ký tự Unicode.
2.  **Giải quyết:** Nhóm đã tối ưu hóa bằng cách sử dụng Spark SQL để truy xuất dữ liệu trực tiếp, đảm bảo tính ổn định của dịch vụ API.
3.  **Tồn đọng:** Chưa triển khai giao diện người dùng (Frontend) và chưa tối ưu hóa hiệu năng truy vấn bằng Z-Order.

---

## 3.6. Kế hoạch đến cuối kỳ
1.  **Danh sách công việc:**
    *   Xây dựng Dashboard trực quan hóa dữ liệu bằng Streamlit/Databricks Dashboards.
    *   Đóng gói API Service bằng Docker.
    *   Triển khai hệ thống cảnh báo biến động giá tự động.
2.  **Timeline dự kiến:**
    *   Tuần 1-2: Hoàn thiện Frontend và Dashboard.
    *   Tuần 3: Đóng gói Docker và tối ưu hóa Delta Lake.
    *   Tuần 4: Kiểm thử toàn diện và viết báo cáo cuối kỳ.

---
**Link GitHub:** [Dán link GitHub của bạn vào đây]
```

