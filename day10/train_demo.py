import pandas as pd
from sklearn.model_selection import train_test_split

data = [
    ("Computer not starting", "hardware"),
    ("Screen is broken", "hardware"),
    ("Keyboard is not working", "hardware"),
    ("Mouse is not working", "hardware"),

    ("Request for refund", "billing"),
    ("charge twice", "billing"),
    ("Hóa đơn thanh toán bị sai", "billing"),
    ("Cần kiểm tra phí thanh toán", "billing"),

    ("Không đăng nhập được tài khoản", "account"),
    ("Tôi quên mật khẩu tài khoản", "account"),
    ("Cần thay đổi email tài khoản", "account"),
    ("Tài khoản của tôi bị khóa", "account"),
]

