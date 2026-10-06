## Tạo commit message

Mỗi khi được yêu cầu tạo commit message:

- Dùng MCP Git gọi git_log với max_count=20 để đọc commit gần nhất.
- Dùng git_status và git_diff_staged để đọc các thay đổi đã stage.
- Theo phong cách phổ biến của commit gần đây:
  ngôn ngữ, prefix, scope, cách viết tiêu đề và phần body.
- Nội dung message phải mô tả đúng thay đổi hiện tại.
- Nếu chưa có thay đổi được stage, thông báo cho người dùng.
- Chỉ đề xuất message; không tự tạo commit.
