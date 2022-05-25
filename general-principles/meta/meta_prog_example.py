p = []
for i in range(10):
    p.append(f'print {i}') # 注：用到格式串，这显然是高版本py3

my_interactive_py2_command = \
p[1]+ '; raw_input("Press Enter"); \\\n' + \
p[2]+ '; raw_input("Press Enter"); \\\n' + \
p[5]+ '; raw_input("Press Enter"); \\\n' + \
p[9]

print(my_interactive_py2_command)