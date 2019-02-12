# 函数

## 注意事项

- 函数一结束就取返回值. $?变量会返回执行的最后一条命令的退出状态码
- 退出状态码必须在0-255之间
- 局部变量,在变量前面加上local

## source 创建脚本库


```bash
# 向函数传递数组

function testArray {
    echo "The parameters are: $@"
    newArr=$1
    echo "The receive array is ${newArr[*]}"
}

myarray=(1,2,3,4)
echo "The original array is: ${myarray[*]}"

testArray $myarray
The original array is: 1,2,3,4
The parameters are: 1,2,3,4
The receive array is 1,2,3,4
In [9]:
%%bash

# 向函数传递数组

testArray() {
    local newarray
    newarray=(`echo "$@"`)
    echo "The new array value is: ${newarray[*]}"
}

myarray=(1,2,3,4)
echo "The original array is: ${myarray[*]}"

testArray ${myarray[*]}
The original array is: 1,2,3,4
The new array value is: 1,2,3,4
In [50]:
%%bash
# 从函数返回数组

function arrFun {
    local oriArr
    local newArr
    local elements
    local i
    echo $#
    
    oriArr=(`echo "$@"`)
    newArr=(`echo "$@"`)
    elements=$[ $# - 1 ]
    
#     for ((i=0; i <= $elements; i++))
#     {
#         newArr[$i]=$[ ${oriArr[$i]} * 2 ]
    
#     }
    
    echo "the arrFun return array: ${newArr[*]}"
    echo ${newArr[*]}
}


myarr=(1,2,3,4)
# echo "The original array is: ${myarr[*]}"

arg1=`echo ${myarr[*]}`
result=`arrFun $arg1`

arrFun $arg1

# echo "The result array is: ${result[*]}"
1
the arrFun return array: 1,2,3,4
1,2,3,4

```