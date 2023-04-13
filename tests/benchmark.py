#!/usr/bin/env python3
import time
from contextlib import contextmanager

from panda import Panda
from panda.tests.hitl.helpers import get_random_can_messages


@contextmanager
def print_time(desc):
  start = time.perf_counter()
  yield
  end = time.perf_counter()
  print(f"{end - start:.2f}s - {desc}")


if __name__ == "__main__":
  with print_time("Panda()"):
    p = Panda()

  fxn = [
    'reset',
    'reconnect',
    'up_to_date',
    'health',
    #'flash',
  ]
  for f in fxn:
    with print_time(f"Panda.{f}()"):
      getattr(p, f)()


  for n in range(6):
    msgs = get_random_can_messages(int(10**n))
    with print_time(f"Panda.can_send_many() - {len(msgs)} msgs"):
      p.can_send_many(msgs)
