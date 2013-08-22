dokku-controller-agent
======================

This should be run on every server that runs dokku in an environment with [dokku controller](https://github.com/KristianOellegaard/dokku-controller)

Install
-------

```bash
python setup.py install
```

Run
---

Must be root, e.g. sudo

```bash
REDIS_URL=redis://:password@dokku-controller:6379/ python agent.py
```
