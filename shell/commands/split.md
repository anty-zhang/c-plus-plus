
# split

```bash
-b：值为每一输出档案的大小，单位为 byte。 
-C：每一输出档中，单行的最大 byte 数。 
-d：使用数字作为后缀。 
-l：值为每一输出档的列数大小。
# 根据文件的行数来分割文件，例如把文件分割成每个包含10行的小文件
split -l 10 date.file

# 分割10k大小文件
split -b 10k data.file

# -d 数字后缀
# -a 指定数字长度
split -b 10k data.file -d -a 3

# 指定文件前缀名
split -b 10k data.file -d -a 3 my_split_name

```