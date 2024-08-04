import subprocess

try:
    # Đọc tệp requirements.txt
    with open('requirements.txt', 'r', encoding='utf-8') as file:
        libs = file.readlines()

    # Loại bỏ các ký tự xuống dòng
    lib_names = [lib.strip().split('==')[0] for lib in libs if lib]
    # print(lib_names)

    # Uninstall từng thư viện
    cmd1 = 'pip uninstall -y '
    for lib_name in lib_names:
        subprocess.run(cmd1 + lib_name)
# except FileNotFoundError:
#     print("File không tồn tại, vui lòng kiểm tra lại tên file")
except Exception as e:
    print(f"Có lỗi xảy ra -->\t{e}")
