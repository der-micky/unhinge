# unhinge
Remove devices other than /boot from system under linux.

## What for
If you have created a "hot stick" to work from an bootable USB drive, system updates might destroy the boot partition on the machine where you plugged your stick into as well as the bootloader on your stick. That's becoz' of an error in updating GRUB. So what we do is removing all other harddrives from the system other than our USB stick.

We can automate this script on boot via crontab or start it manually.

If you want your drives back you need a reboot (don't forget to disable the script if it's running on startup).

## Tested under
- Kali Linux 2024