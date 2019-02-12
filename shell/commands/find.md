
```bash
find / -name "core.*" | grep "\.[0-9]\+$" | xargs -n100 rm -f

```