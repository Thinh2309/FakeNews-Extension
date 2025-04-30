# Fake News Detection - Chrome Extension và Flask API

Dự án này bao gồm một ứng dụng Flask API để nhận diện tin giả kết hợp với một Chrome Extension để phát hiện tin giả trực tiếp từ trình duyệt. Dưới đây là hướng dẫn chi tiết về cách cài đặt và sử dụng cả hai thành phần của dự án.

## Các Yêu Cầu

- **Python 3.8+**
- **Pip (để cài đặt các thư viện cần thiết)**
- **Git (để quản lý mã nguồn)**
- **Google Chrome (để sử dụng Chrome Extension)**

## Cài Đặt Môi Trường

### 1. Clone Dự Án từ GitHub

Clone dự án từ GitHub vào máy tính của bạn:
```bash
git clone https://github.com/Thinh2309/FakeNews.git
cd FakeNews
```
### 2. Cài Đặt Môi Trường Ảo và Các Thư Viện
2.1. Tạo môi trường ảo:

```bash
python -m venv myenv
```
2.2. Kích hoạt môi trường ảo:

Windows:
```bash
.\myenv\Scripts\activate
```
Mac/Linux:

```bash
source myenv/bin/activate
```
2.3. Cài đặt các thư viện yêu cầu:

```bash
pip install -r requirements.txt
```
### 3. Cài Đặt Git LFS (Git Large File Storage)
Dự án này có thể chứa các file lớn như mô hình đã huấn luyện. Để tải và làm việc với các file lớn này, bạn cần cài đặt Git LFS:

Cài đặt Git LFS: Git LFS installation
Sau khi cài đặt, hãy chạy:
```bash
git lfs install
```
### 4. Ứng Dụng Flask API (app.py)
Cấu Hình và Chạy Flask API
Trong thư mục chứa dự án, chạy ứng dụng Flask:
```bash
python app.py
```
Flask sẽ bắt đầu chạy tại địa chỉ http://127.0.0.1:5000/ (hoặc địa chỉ khác tùy cấu hình của bạn). Bạn có thể kiểm tra API bằng cách gửi yêu cầu HTTP đến API này.
