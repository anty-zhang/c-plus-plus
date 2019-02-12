
```bash
if false; then
网卡信息查询, 两个命令

1. ethtool

2. lspci

千兆网卡Gigabit（万兆网卡显示为10-Gigabit）

fi

ifconfig | grep Ethernet
enp3s0    Link encap:Ethernet  HWaddr 20:47:47:75:7f:2d  

```

```bash
ethtool enp3s0
Settings for enp3s0:
	Supported ports: [ TP MII ]
	Supported link modes:   10baseT/Half 10baseT/Full 
	                        100baseT/Half 100baseT/Full 
	                        1000baseT/Half 1000baseT/Full 
	Supported pause frame use: No
	Supports auto-negotiation: Yes
	Advertised link modes:  10baseT/Half 10baseT/Full 
	                        100baseT/Half 100baseT/Full 
	                        1000baseT/Full 
	Advertised pause frame use: Symmetric Receive-only
	Advertised auto-negotiation: Yes
	Link partner advertised link modes:  10baseT/Half 10baseT/Full 
	                                     100baseT/Half 100baseT/Full 
	Link partner advertised pause frame use: Symmetric Receive-only
	Link partner advertised auto-negotiation: Yes
	Speed: 100Mb/s
	Duplex: Full
	Port: MII
	PHYAD: 0
	Transceiver: internal
	Auto-negotiation: on
	Current message level: 0x00000033 (51)
			       drv probe ifdown ifup
	Link detected: yes
Cannot get wake-on-lan settings: Operation not permitted

```

```bash
lspci -vvv | grep Ethernet
03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 10)
	Subsystem: Realtek Semiconductor Co., Ltd. RTL8111/8168 PCI Express Gigabit Ethernet controller

```