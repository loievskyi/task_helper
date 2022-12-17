class BaseClientTaskCourier(object):
    """
    Base class for the client side of task helpers.

    The inherited class should provide the ability to:
    Client side methods:
        - get_task_result - returns task retuls, if it exists.
        - wait_for_task_result - Waits for the task result to appear.
        - add_task_to_queue - adds a task to the queue for processing.
        - check_for_done - Checks if the task has completed.
    """

    def get_task_result(self, queue_name, task_id, delete_data=True):
        """Returns task retuls, if it exists.
        Otherwise, raises exceptions.TaskResultDoesNotExist
        Client side method."""
        raise NotImplementedError

    def wait_for_task_result(
            self, queue_name, task_id, delete_data=True, timeout=None):
        """Waits for the task result to appear, and then returns it.
        Raises TimeoutError in case of timeout.
        Client side method"""
        raise NotImplementedError

    def add_task_to_queue(self, queue_name, task_data):
        """Put the task in the queue for processing.
        Client side method."""
        raise NotImplementedError

    def check_for_done(self, queue_name, task_id):
        """Checks if the task has completed.
        Returns True - if task is done (successful or unsuccessful),
        or False if there is no task result yet."""
        raise NotImplementedError


class BaseWorkerTaskCourier(object):
    """
    Base class for the worker side of task helpers.

    The inherited class should provide the ability to:
    Worker side methods:
        - get_tasks - pops tasks from queue and returns it.
        - get_task - returns one task from queue.
        - wait_for_task - waits for task and returns it.
        - return_task_result - returns result to the client side.
    """

    def get_tasks(self, queue_name, max_count):
        """Pops tasks from queue and returns it. The number of task which
        depends on max_count and the number of elements in the queue.
        Worker side method."""
        raise NotImplementedError

    def get_task(self, queue_name):
        """Returns one task from the queue. If task doesn't exists,
        raises exceptions.TaskDoesNotExist.
        Worker side method."""
        raise NotImplementedError

    def wait_for_task(self, queue_name, timeout=None):
        """Returns one task from queue as tuple (task_id, task_data).
        If timeout is None (default), then waits task indefinitely.
        Raises TimeoutError in case of timeout.
        Worker side method."""
        raise NotImplementedError

    def return_task_result(self, queue_name, task_id, task_result):
        """Return the result of processing the task to the client.
        Worker side method."""
        raise NotImplementedError


class BaseClientWorkerTaskCourier(
        BaseWorkerTaskCourier, BaseClientTaskCourier):
    """
    Base class for the client and worker sides of task helpers.
    The inherited class should provide the ability to:

    Client side methods:
        - get_task_result - returns task retuls, if it exists.
        - wait_for_task_result - Waits for the task result to appear.
        - add_task_to_queue - adds a task to the queue for processing.
        - check_for_done - Checks if the task has completed.

    Worker side methods:
        - get_tasks - pops tasks from queue and returns it.
        - get_task - returns one task from queue.
        - wait_for_task - waits for task and returns it.
        - return_task_result - returns result to the client side.
    """
    pass
