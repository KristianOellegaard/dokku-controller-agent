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

Run it properly
---------------

```bash
curl https://raw.github.com/KristianOellegaard/dokku-controller-agent/master/upstart-dokku-controller-agent.conf > /etc/init/dokku-controller-agent.conf
```

Now open ``/etc/init/dokku-controller-agent.conf`` and change REDIS_URL and the path to agent.py
