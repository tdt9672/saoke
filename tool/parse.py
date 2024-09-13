import re

def split_data(text):
    """
    Hàm tách dữ liệu thành các dòng dựa trên các mã giao dịch

    Args:
        text: Chuỗi văn bản chứa dữ liệu

    Returns:
        List: Danh sách các dòng dữ liệu
    """

    # Biểu thức chính quy để tìm các mã giao dịch ở đầu dòng
    pattern = r"^(\d{6}\.\d{6}\.\d{6}|VCB\.CTDK|MBVCB|.{34}\.\d{5}\.\d{5}\.Vietcombank|\d{4}.{30}\.|PARTNER\.|IBVCB\.\d{10}|SHGD:\d{8}|.{15}\.3BROTHERS)"
# 0200970405090112202020246WVI059470.37142.122015.Vietcombank
    # Tìm tất cả các vị trí bắt đầu của các dòng dữ liệu
    matches = re.finditer(pattern, text, re.MULTILINE)

    # Tách chuỗi dựa trên các vị trí bắt đầu
    start_positions = [match.start() for match in matches]
    start_positions.append(len(text))  # Thêm vị trí cuối của chuỗi
    data_lines = [text[start:end] for start, end in zip(start_positions[:-1], start_positions[1:])]

    return data_lines

# Ví dụ sử dụng hàm
text = """
MBVCB.6980959124.PHAM THAI DOAN
TRANG chuyen tien.CT tu 0421000551358
PHAM THAI DOAN TRANG toi
0011001932418 MAT TRAN TO QUOC VN -
BAN CUU TRO TW
549738.090924.085954.Ung ho cuu tro bao so
3
PARTNER.DIRECT_DEBITS_VCB.MSE.6639
6117087.20240909.66396117087-0933325109_G
op suc ung ho dong bao lu lut mien bac
020097042209090902262024PKIQ528900.48641
.090227.NGUYEN THI HUYEN TRANG
chuyen tien
447093.090924.090458.Thuy Duong Fan Ninh
Duong Story ung ho ho tro sau bao Yagi
980325.090924.090518.HOANG BAO NGAN
chuyen tien ung ho khac phuc hau qua bao
Yagi
980507.090924.090522.Fan Ninh Duong Story
Stella xin ung ho khac phuc sau bao Yagi
522341.090924.090613.UNG HO CUU TRO DO
BAO YAGI-090924-09:06:13 522341
IBBIZ6019569938.3BROTHERS MEDIA UNG
HO KHAC PHUC HAU QUA BAO SO 3
YAGI
989092.090924.090720.NGUYEN VAN NGOC
chuyen tien
MBVCB.6981028706.NGUYEN HONG
NHUNG ung ho khac phuc hau qua bao so 3
Yagi.CT tu 0351001004373 NGUYEN HONG
NHUNG toi 0011001932418 MAT TRAN TO
QUOC VN - BAN CUU TRO TW
215031.090924.091001.Vuthimai ck
565322.090924.091017.NGUYEN KIM HONG
NGOC chuyen tien
337119.090924.091219.Khoe Dep Japan cung
Quy ACKH ung ho khac phuc sau bao so 3
FT24253019937697
MBVCB.6981071957.HOANG THI KIEU
OANH chuyen tien.CT tu 0021001530417
HOANG THI KIEU OANH toi 0011001932418
MAT TRAN TO QUOC VN - BAN CUU TRO
TW
540073.090924.091251.PHAN THI NHU
PHUONG ung ho cuu tro bao so 3
577482.090924.091301.TRAN DUC NHAT
chuyen tien ung ho khac phuc hau qua bao
yagi
"""

result = split_data(text)
for line in result:
    print(line)
    print('----')