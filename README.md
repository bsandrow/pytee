pytee
=====

    import pytee

    tee = pytee.create_tee([ '/tmp/tee-test-1', '/tmp/tee-test-2' ], mode='a')
    print >>tee, "a" * 100000,
    tee.close()

    # Need to wait for the child process to finish writing to the file(s)
    # before we can measure the amount of data written to the file(s).
    os.wait()

    for filename in files:
        with open(filename, 'r') as fh:
            chars = len(fh.read())
            print "File '%s' has %d chars" % (filename, chars)

The purpose of **create_tee()** is to allow the unix 'tee' utility to be easily
emulated within Python. If spawns a child process that listens for data on a
pipe, and wraps the write end of that pipe in a file object. This allows it to
be used seamlessly where ever file ojects are used, even in places likes
subprocess.Popen() where a fileno is required.

Roadmap
=======

 * Create a Tee object that implements all of the file-like object trappings.
   (Keep around the `create_tee()` function for seamless compatibility).

 * Possibly create a 'comm channel' to communicate commands to the child
   process (add/remove files from the list).

Author
======

Brandon Sandrowicz <brandon@sandrowicz.org>

License
=======

BSD 3-clause license. See LICENSE file for terms.
