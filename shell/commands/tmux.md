# tmux 基本配置

```bash
# reference: https://github.com/xuxiaodong/tmuxen/blob/master/_tmux.conf
# 取消默认引导键 Ctrl-B 的绑定
unbind C-b

# 设定新的引导键为 Ctrl-A
set -g prefix C-a
bind a send-prefix

# split window
unbind '"'
bind - splitw -v # vertical split (prefix -)
unbind %
bind | splitw -h # horizontal split (prefix |)

# select pane
bind k selectp -U # above (prefix k)
bind j selectp -D # below (prefix j)
bind h selectp -L # left (prefix h)
bind l selectp -R # right (prefix l)

# resize pane
bind -r ^k resizep -U 10 # upward (prefix Ctrl+k)
bind -r ^j resizep -D 10 # downward (prefix Ctrl+j)
bind -r ^h resizep -L 10 # to the left (prefix Ctrl+h)
bind -r ^l resizep -R 10 # to the right (prefix Ctrl+l)

# swap pane
bind ^u swapp -U # swap with the previous pane (prefix Ctrl+u)
bind ^d swapp -D # swap with the next pane (prefix Ctrl+d)

# select layout
bind , select-layout even-vertical
bind . select-layout even-horizontal

# misc
bind e lastp  # select the last pane (prefix e)
bind ^e last  # select the last window (prefix Ctrl+e)
bind q killp  # kill pane (prefix q)
bind ^q killw # kill window (prefix Ctrl+q)

# copy mode
bind Escape copy-mode               # enter copy mode (prefix Escape)
bind ^p pasteb                      # paste buffer (prefix Ctrl+p)
unbind -T copy-mode-vi Space
bind -T copy-mode-vi v send -X begin-selection   # select (v)
bind -T copy-mode-vi y send -X copy-pipe "xclip" # copy (y)

# app
bind ! splitw htop                                  # htop (prefix !)
bind m command-prompt "splitw 'exec man %%'"        # man (prefix m)
bind % command-prompt "splitw 'exec perldoc -t %%'" # perl doc (prefix %)
bind / command-prompt "splitw 'exec ri %%'"         # ruby doc (prefix /)

set -g default-terminal "screen-256color"
set -g base-index 1
set -g pane-base-index 1
setw -g automatic-rename off
set-option -g allow-rename off
set -g status-position bottom
set -g history-limit 65535

# 启用鼠标
set -g mouse on

# <prefix>r
bind r source-file ~/.tmux.conf \; display-message "Config reloaded"

```

# tmux 基本使用

```bash
# 安装
brew install tmux       # OSX
pacman -S tmux          # archlinux
apt-get install tmux    # Ubuntu
yum install tmux        # Centos

# 设置生效：重启或者执行如下命令
tmux source ~/.tmux.conf

# window -- 窗口操作
:new<CR> # 创建新的 Session，其中 : 是进入 Tmux 命令行的快捷键
<prefix>c    # 可以创建新的窗口（Window）
<prefix>w  # list windows
<prefix>n    # next window
<prefix>p    # previous window
<prefix>f    # find window
<prefix>,    # name window
<prefix> &   # kill window

# panes--窗格操作
<prefix> %    # vertical split
# <prefix>"    # 垂直分割窗口
<prefix>o      # swap panes
<prefix>q 		# show pane numbers
<prefix>x 		# kill pane
<prefix> { 		# move the current pane left
<prefix> } 		# move the currnet pane right
<prefix> z 		# 最大化当前窗格，再次执行可恢复原来大小
<prefix>; 	 # 选择上次使用的窗格
<space>  # 切换 Pane 布局

# session -- 会话操作
tmux new -s myname    # 创建一个新的 session
<prefix>$   # 重命名当前Session
<prefix>s 	# 选择绘画列表
<prefix>d    # 退出当前Session的快捷键是
tmux a -t myname  (or at, or attach)     # 根据Session的名字切到工作环境
tmux kill-session -t foo # 删除名称为 foo 的会话
tmux kill-server # 删除所有的会话
tmux -L AnyName -f /path/to/.tmux.conf
alias tmux-cuixuewei="tmux -L cuixuewei -f /path/to/.tmux.conf"

# help
<prefix>? 		# list shortcuts
tmux show -g 	# 查看当前tmux设置
d        # detach，退出 Tmux Session，回到父级 Shell
t        # 显示一个时钟，:)

```