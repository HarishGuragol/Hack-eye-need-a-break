# eye-need-a-break

## To run the WebGazer-
```
1. Allow access to camera
2. On the popup click calibrate
3. Follow instructions in the next popup
4. Check console for live data points
5. To set a custom background click on browse
6. Once done you can click on save to download .csv files
```

## Run backend and db

```bash
> pip install -r .\backend\requirements.txt
> python run_server.py
```

**http://localhost:5000/apidocs/** - **api description**


## Deploy

```bash
> sudo ufw allow 8050
> apt install git -y
> git clone https://github.com/HarishGuragol/eye-need-a-break.git
> cd eye-need-a-break
> apt install docker-compose -y
> docker-compose up
```

#### Useful commands
```bash
> docker rm -vf $(docker ps -a -q) // Delete all docker containers
> docker rmi -f $(docker images -a -q) // Delete all docker images
```
It may be useful before new deploy (delete old data)

#### Generate keys
```bash
openssl genrsa 2048 > host.key
chmod 400 host.key
openssl req -new -x509 -nodes -sha256 -days 365 -key host.key -out host.cert
```
