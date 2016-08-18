import gevent


class Timer:
    active = None

    def __init__(self):
        pass

    def start(self):
        self.active = True

    def stop(self):
        self.active = False


def set_interval(func, secs):
    timer = Timer()
    timer.start()

    while timer.active:
        gevent.sleep(secs)
        func()

    return timer


def set_timeout(func, secs):
    timer = Timer()

    gevent.sleep(secs)
    if timer.active is None:
        timer.start()
        func()
        timer.stop()

    return timer


def clear_interval(timer):
    timer.stop()


def clear_timeout(timer):
    timer.stop()
