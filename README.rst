==
so
==

Use micc to create a python module from c++ that uses another shared library

look at so/cpp_sl/CMakeLists.txt to see how that works.
Note that::

    > ldd sl.cpython-38-x86_64-linux-gnu.so
        linux-vdso.so.1 (0x00007ffcf0570000)
        libshrd.so => /home/bert/workspace/so/so/shrd/libshrd.so (0x00007f977c64e000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f977c45b000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f977c440000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f977c24e000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f977c0fd000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f977c66d000)

does show linkage with ``libshrd.so``.

* Free software: MIT license
* Documentation: https://so.readthedocs.io.


Features
--------

* TODO
