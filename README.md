# gevent-timer

pip install gevent_timer

related:
- [gevent-ticker](https://github.com/tejasmanohar/gevent-ticker)

# usage

```python
import gevent_timer as timer

def do():
  print("hi")

# execute do() every 100 seconds
interval = timer.set_interval(do, 100)

# stop after 305 seconds
timeout = timer.set_timeout(lambda: timer.clear_interval(interval), 305)

# nah, scratch that. let's keep running do()
timer.clear_timeout(timeout)
```
