# python-generate-image

文字を入れた画像の生成を Python で行う実験

## Usage: Python 環境

```sh
$ python main.py [OPTIONS]
```

###

## Usage: Docker Compose 環境

```sh
$ docker-compose up -d
$ docker-compose exec generate python main.py [OPTIONS]
```

## Options

```sh
options:
  -h, --help            show this help message and exit
  -i IMG_NAME, --img-name IMG_NAME
                        Image Name. Please enter the file extension. (default: 'example.jpg')
  --start START         Start time. (default: '19:00')
  --end END             Stop time. (default: '21:00')
  -n ROLE_SESSION_NAME, --role-session-name ROLE_SESSION_NAME
                        AWS Role Session Name.
```
