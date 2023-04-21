# Вьюсеты
___
## Описание
ViewSet - это класс в Django REST Framework, который позволяет сократить количество представлений CRUD для одного ресурса. Вместо того, чтобы писать отдельные представления под каждое действие CRUD мы можем написать ViewSet для какого-либо ресурса (модели) в целом и прописать отдельные действия CRUD в его методах.
## Serializer
Модельный сериализатор - это сериализатор на базе встроенного класса ModelSerializer.
```angular2html
class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'descriptions']

```

## class PostView(ModelViewSet):

```
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
```
## URL 
url путь передаем pk для просмотра **одной записи**
```angular2html
router = routers.DefaultRouter()
router.register('posts', PostView)


urlpatterns = [
    path('', include(router.urls)),
]
```
# Postman
Пример запроса:
```angular2html
GET http://127.0.0.1:8000/api/posts/
```
Ответ:
```angular2html
{
[
    {
        "id": 18,
        "descriptions": "3"
    },
    {
        "id": 19,
        "descriptions": "3"
    },
    {
        "id": 14,
        "descriptions": "2"
    },
    {
        "id": 16,
        "descriptions": "3"
    },
    {
        "id": 17,
        "descriptions": "3"
    },
    {
        "id": 13,
        "descriptions": "1"
    },
    {
        "id": 15,
        "descriptions": "Новое описание"
    }
]
```
Пример запроса при несуществующим id:
```angular2html
GET http://127.0.0.1:8000/api/posts/1
```
Ответ:
```angular2html
{
    "detail": "Not found."
}
```

# Postman
Пример запроса: 
```angular2html
DELETE  http://127.0.0.1:8000/api/tracker/delete/2/
```
Ответ возвращает ключ:
```angular2html
{
    "pk": 15
}
```
В случае неправильного запроса:
```angular2html
{
    "detail": "Not found."
}
```
# Postman
Пример запроса: 
```angular2html
PUT  http://127.0.0.1:8000/api/tracker/update/16/
```
raw(JSON):
```angular2html

{
    "description": "Project number 16",
}
```
Ответ:
Поменяются значения project</br>
В случае неправильного запроса:
```angular2html
{
    "detail": "Not found."
}
```
# Настройте права доступа в API: 

```angular2html
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        elif self.action in ['create', 'like', 'unlike', 'destroy']:
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        else:
            return [AllowAny()]
AllowAny - класс разрешений, настроенный глобально по умолчанию. Разрешает любые запросы всем.

IsAdminUser - проверяет, является ли пользователь админом - т.е. имеет ли он доступ в админ-панель. Несмотря на название, проверяет галочку is_staff, на глядя на is_superuser.

IsAuthenticatedOrReadOnly - комбинированный класс, который проверяет, аутентифицирован ли пользователь, или даёт доступ только на просмотр.

```

# Нужно в запрос передавать токен без этого работать не будет
 
