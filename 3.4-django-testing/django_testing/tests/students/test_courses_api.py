from model_bakery import baker
import pytest
from rest_framework.test import APIClient

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    # Данная фикстура будет возвращать функцию,
    # котоорая умеет создавать конкретный объект
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# проверка получения первого курса (retrieve-логика):
@pytest.mark.django_db
def test_retrive(course_factory, client):

    course = course_factory()  # создаем курс через фабрику;

    # строим урл и делаем запрос через тестовый клиент;
    response = client.get(f"/api/v1/courses/{course.id}/")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    # проверяем, что вернулся именно тот курс, который запрашивали;
    assert data["id"] == course.id
    assert data["name"] == course.name


# проверка получения списка курсов (list-логика):
@pytest.mark.django_db
def test_list(course_factory, client):

    courses = course_factory(_quantity=10)  # создаем курсы через фабрику;

    # строим урл и делаем запрос через тестовый клиент;
    response = client.get(f"/api/v1/courses/")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data[0], dict)
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert isinstance(c, dict)
        assert c["id"] == courses[i].id
        assert c["name"] == courses[i].name


# проверка фильтрации списка курсов по id:
@pytest.mark.django_db
def test_filter_id(course_factory, client):
    courses = course_factory(_quantity=10)  # создаем курсы через фабрику;

    # передать ID одного курса в фильтр, проверить результат запроса с фильтром;
    course = courses[3]
    response = client.get(f"/api/v1/courses/", data={"id": course.id})
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["id"] == course.id
    assert data[0]["name"] == course.name


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_name(course_factory, client):
    courses = course_factory(_quantity=10)  # создаем курсы через фабрику;

    # передать name одного курса в фильтр, проверить результат запроса с фильтром;
    course = courses[3]
    response = client.get(f"/api/v1/courses/", data={"name": course.name})
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["id"] == course.id
    assert data[0]["name"] == course.name


# тест успешного создания курса:
@pytest.mark.django_db
def test_create(course_factory, client):

    assert Course.objects.count() == 0
    name = "tesr course name"
    response = client.post(f"/api/v1/courses/", data={"name": name})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == name
    assert Course.objects.count() == 1
    assert Course.objects.first().name == name


# тест успешного обновления курса:
@pytest.mark.django_db
def test_update(course_factory, client):
    course = course_factory()  # создаем курс через фабрику;
    # сначала через фабрику создаём, потом обновляем JSON-данными;
    assert Course.objects.count() == 1
    name = "updated course name"
    response = client.patch(f"/api/v1/courses/{course.id}/", data={"name": name})
    assert response.status_code == 200
    assert Course.objects.count() == 1
    assert Course.objects.first().name == name


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete(course_factory, client):
    course = course_factory()  # создаем курс через фабрику;
    assert Course.objects.count() == 1
    response = client.delete(f"/api/v1/courses/{course.id}/")
    assert response.status_code == 204
    assert Course.objects.count() == 0
