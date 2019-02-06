crontab -l > techbangla
echo "* * * * * /usr/local/bin/python3 UNIT3D-GOOGLE-DRIVE-BACKUP/backup.py" >> techbangla
crontab techbangla
rm techbangla
