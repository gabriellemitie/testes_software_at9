from datetime import datetime

from task_manager.repository import TaskRepository
from task_manager.task import Task, Priority


def test_save_atribui_id_and_calls_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = Task(None, "Teste", "Desc", Priority.BAIXA, datetime.now())
    resultado = repo.save(task)

    assert resultado.id == 1
    mock_storage.add.assert_called_once_with(1, task)


def test_save_with_existing_id_calls_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = Task(42, "T", "D", Priority.MEDIA, datetime.now())
    resultado = repo.save(task)

    assert resultado.id == 42
    mock_storage.add.assert_called_once_with(42, task)


def test_find_by_id_delegates_to_storage(mocker):
    mock_storage = mocker.Mock()
    expected = object()
    mock_storage.get.return_value = expected

    repo = TaskRepository(mock_storage)
    res = repo.find_by_id(5)

    mock_storage.get.assert_called_once_with(5)
    assert res is expected


def test_find_all_and_delete_delegates_to_storage(mocker):
    mock_storage = mocker.Mock()
    items = [object(), object()]
    mock_storage.get_all.return_value = items
    mock_storage.delete.return_value = items[0]

    repo = TaskRepository(mock_storage)

    all_items = repo.find_all()
    mock_storage.get_all.assert_called_once()
    assert all_items == items

    deleted = repo.delete(1)
    mock_storage.delete.assert_called_once_with(1)
    assert deleted is items[0]
from datetime import datetime

from task_manager.repository import TaskRepository
from task_manager.task import Task, Priority


def test_save_atribui_id_and_calls_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = Task(None, "Teste", "Desc", Priority.BAIXA, datetime.now())
    resultado = repo.save(task)

    assert resultado.id == 1
    mock_storage.add.assert_called_once_with(1, task)


def test_save_with_existing_id_calls_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    task = Task(42, "T", "D", Priority.MEDIA, datetime.now())
    resultado = repo.save(task)

    assert resultado.id == 42
    mock_storage.add.assert_called_once_with(42, task)


def test_find_by_id_delegates_to_storage(mocker):
    mock_storage = mocker.Mock()
    expected = object()
    mock_storage.get.return_value = expected

    repo = TaskRepository(mock_storage)
    res = repo.find_by_id(5)

    mock_storage.get.assert_called_once_with(5)
    assert res is expected


def test_find_all_and_delete_delegates_to_storage(mocker):
    mock_storage = mocker.Mock()
    items = [object(), object()]
    mock_storage.get_all.return_value = items
    mock_storage.delete.return_value = items[0]

    repo = TaskRepository(mock_storage)

    all_items = repo.find_all()
    mock_storage.get_all.assert_called_once()
    assert all_items == items

    deleted = repo.delete(1)
    mock_storage.delete.assert_called_once_with(1)
    assert deleted is items[0]
def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc",
    Priority.BAIXA, datetime.now())
    resultado = repo.save(task)
    assert resultado.id == 1
    mock_storage.add.assert_called_once()