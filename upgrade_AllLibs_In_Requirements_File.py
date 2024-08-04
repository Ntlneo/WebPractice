import subprocess

# Ghi các lib ra file requirements.txt
with open('requirements.txt', 'w', encoding='utf-8') as file:
    cmd2 = 'pip freeze'
    subprocess.run(cmd2, stdout=file)

# Đọc tệp requirements.txt
with open('requirements.txt', 'r', encoding='utf-8') as file:
    libs = file.readlines()

# Loại bỏ các ký tự xuống dòng
lib_names = [lib.strip().split('==')[0] for lib in libs]

# Nâng cấp từng thư viện
cmd1 = 'pip install --upgrade '
for lib_name in lib_names:
    subprocess.run(cmd1 + lib_name)

# Cập nhật các thư viện mới upgrade vào lại file requirements
with open('requirements.txt', 'w', encoding='utf-8') as file:
    cmd2 = 'pip freeze'
    subprocess.run(cmd2, stdout=file)

