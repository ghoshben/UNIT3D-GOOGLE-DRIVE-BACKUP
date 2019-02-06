# Unit3D automated Google Drive database backup


#  Features!

  - Run the script once .it ll make your database backuped up to google drive every day


To DO:
  - backing up the whole unit3d site 
  - Automated restore
  - migration


### Installation

Install python 3 by

Install the dependencies and devDependencies and start the server.

```sh
$ sudo apt-get install -y python3-pip
$ pip3 install PyDrive
$ git clone https://github.com/ghoshben/UNIT3D-GOOGLE-DRIVE-BACKUP.git
$ cd /UNIT3D-GOOGLE-DRIVE-BACKUP
```

#### Create Google Authintication json
 - Go to [APIs Console](https://console.developers.google.com/iam-admin/projects) and make your own project.
 - Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
 - Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
 - Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished
 

| Field | Value |
| ------ | ------ |
| Application type | Web application |
| Name  | Any Name |
| Authorized JavaScript origins | http://localhost:8080 |
| Authorized redirect URI | http://localhost:8080/ |

- Click ‘Download JSON’ on the right side of Client ID to download client secret
- Rename the file to “client_secrets.json” and place it in your working directory

```sh
$ sh tb.sh
```
