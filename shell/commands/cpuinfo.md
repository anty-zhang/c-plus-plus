
[TOC]

# /proc/cpuinfo

```bash
# 查看物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
grep "physical id" /proc/cpuinfo | sort -u | wc -l

# 查看每个物理CPU核数
cat /proc/cpuinfo| grep "cpu cores"| uniq
grep "core id" /proc/cpuinfo | sort -u | wc -l

# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l

查看总内存大小
grep MemTotal /proc/meminfo

查看 CPU 型号
dmidecode -s processor-version

# 查看 CPU 的详细信息
cat /proc/cpuinfo
```