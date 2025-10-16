from typing import Optional, List


class TaskRepository:

    def __init__(self, storage):
        self.storage = storage
        self._next_id = 1

    def save(self, task):
        if getattr(task, "id", None) is None:
            task.id = self._next_id
            self._next_id += 1

        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id) -> Optional[object]:
        return self.storage.get(id)

    def find_all(self) -> List[object]:
        return self.storage.get_all()

    def delete(self, id) -> Optional[object]:
        return self.storage.delete(id)
