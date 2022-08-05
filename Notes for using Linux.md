Linux notes
================
Notes for some common problems in Linux

**1. How to mount**
- Start by creating the mount point, it can be any location you want:

```
	sudo mkdir /mnt/iso
```

- Mount the ISO file to the mount point by typing the following mount command:

```
	sudo mount /path/to/image.iso /mnt/iso -o loop
```

- Unmount the ISO file by using the umount command followed by the directory where the image has been mounted:

```
	sudo umount /mnt/iso
```

**2.  USB drive**
- List usb devices: ```lsusb```

- List usb drive: ```lsblk ```

- Format usb:

	```
	sudo mkfs.exfat /dev/sda1
	```

- Create a bootable usb

	- Use ```fdisk``` to partition the usb, if it's not partitioned yet (only show ```/dev/sda```, no ```/dev/sda1```)

	- Unmount the usb:

	```
		umount /dev/sda1
	```

	- Use ```dd``` and then ```sync``` to create bootable usb:

	```
		sudo dd if=path/to/input.iso of=/dev/sda status=progress && sync
	```
**3. Keyboard shortcuts**

- Command to open speedtest-cli in another terminal window in Xfce4:
```
xfce4-terminal -x sh -c "speedtest; bash"
```

**4. Fix Ibus can’t work in offices**

- Creat a ~/.xprofile file, then paste the following:

```
	export GTK_IM_MODULE=ibus	
	export QT_IM_MODULE=ibus
	export XMODIFIERS=@im=ibus
	# Dành cho những phần mềm dựa trên qt4
	export QT4_IM_MODULE=ibus
	# Dành cho những phần mềm dùng thư viện đồ họa clutter/OpenGL
	export CLUTTER_IM_MODULE=ibus
	export GLFW_IM_MODULE=ibus
	#chịu:
	export XIM_PROGRAM=/usr/bin/ibus-daemon
```

**5. Port**
- See all port: ```ss -tulw```
- See a specific port, e.g. port 5000: ```lsof -i:5000```
