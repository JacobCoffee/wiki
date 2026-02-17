# UpgradingPostgreSQL

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Because many Python services use PostreSQL, this instruction is here.

### Upgrading PostgreSQL from 8.4 to 9.1 

If you have a database running on PostgreSQL 8.4 and you want to update it to 9.1, follow these steps:

1.  Install postgresql-9.1;

2.  Remove the new default cluster using `sudo pg_dropcluster --stop 9.1 main`;

3.  Update the old clusted with `sudo pg_upgradecluster 8.4 main`;

4.  If you get the error:

<!-- -->

    The PostgreSQL server failed to start. Please check the log output:
    FATAL:  could not create shared memory segment: Invalid argument
    DETAIL:  Failed system call was shmget(key=5432001, size=34922496, 03600).
    HINT:  This error usually means that PostgreSQL's request for a shared memory segment exceeded your kernel's SHMMAX parameter.  You can either reduce the request size or reconfigure the kernel with larger SHMMAX.  To reduce the request size (currently 34922496 bytes), reduce PostgreSQL's shared memory usage, perhaps by reducing shared_buffers or max_connections.
            If the request size is already small, it's possible that it is less than your kernel's SHMMIN parameter, in which case raising the request size or reconfiguring SHMMIN is called for.

you check the value of shmmax with `sysctl -a | grep -i shm`. You can change the value permanently adding `kernel.shmmax = 34922496` in `/etc/sysctl.d/30-postgresql-shm.conf` and running `sudo sysctl -p` to apply the changes, or temporarily with `sudo sysctl kernel.shmmax=34922496`.

1.  If everything works with 9.1 you can then remove 8.4;
