# until

```bash
格式
until test cmds
    do
        cmds
    done

```


# example

```bash
val=100

until [ $val -eq 0 ]
do
    echo $val
    val=$[ $val - 25 ]
done

# output
100
75
50
25

```