# Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
def bt1(a):
    if a % 3 == 0 and a > 50 and a < 100:
        return True
    else:
        return False
    
# in n lần chữ được nhập vào
def bt2(input, so_lan):
    i = 1
    while i <= so_lan:
        print(input)
        i += 1 

# nhập vào n trả về danh sách các số lẻ nhỏ hơn n
def list_soLe_beHonN(n):
    kq = []
    i = n - 1
    while (i > 0):
        if i % 3 == 1:
            kq.append(i)
        i -= 1
    return kq

#  tổng n số nguyên đầu tiên
def sum_n_soDauTien(n):
    if (n == 0):
        return 0
    else:
        return n + sum_n_soDauTien(n - 1)
    
# in ra các ước của N
def uoc_cuaN(n):
    kq = []
    soChia = n
    while soChia > 0:
        if n % soChia == 0:
            kq.append(soChia)
        soChia -= 1 
    kq.sort()
    return kq

# giao 2 tập hợp
def giao(a, b):
    kq = []
    for x in a:
        for y in b:
            if x == y:
                kq.append(x)
                break
            else:
                continue
    kq.sort()
    return kq

# in ra các ước của a và b
def uoc_chung(a, b):
    uocCuaA = uoc_cuaN(a)
    uocCuaB = uoc_cuaN(b)
    kq = giao(uocCuaA, uocCuaB)
    kq.sort()
    return kq


# 7 kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    uoc = uoc_cuaN(n)
    return len(uoc) == 2

# số chữ số của n
def so_chu_so(n):
    number_str = str(n)
    return len(number_str)

# tính tổng các chữa số của n
def tong_cac_chu_so(n):
    if (n < 10):
        return n
    else:
        return n % 10 + tong_cac_chu_so(n // 10)

# tính tổng các số trong chuỗi vs: 1, 3, 5, 7: return 16
def tong_cac_so_trong_chuoi(s):
    listNumber = s.split(", ")
    kq = 0
    for x in listNumber:    
        kq += int(x)
    return kq
print(tong_cac_so_trong_chuoi("3, 5, 7, 10, 0"))