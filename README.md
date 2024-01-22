# Events REST API app with realtime chat

## Description
### Tecnhology stack
- Django
- Django REST framework
- SimpleJWT
- django-channels
- redis
- postgresql

### Launch
1. Clone repository
```
git clone https://github.com/yuwisasha/Events.git
```
2. Build and launch container
```
docker compose up -d
```
3. Apply migrations
From Docker desktop you can open an image of events-app and exec ```python app/manage.py migrate``` or using terminal
```
docker compose exec app bash
```
```
python app/manage.py migrate
```

### API [documentation](https://web.postman.co/workspace/Events~b6cf44fc-099a-45c3-b3d7-f1c34351cb13/documentation/29232915-2b462b55-6fb2-4c01-bb2a-51bffa9ebac5) and WebSocket example
