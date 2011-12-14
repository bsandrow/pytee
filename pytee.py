import sys
import os

valid_modes = ['a','w']

def create_tee(files, mode, buffer_size=128):
        if mode not in valid_modes:
            raise IOError("Only valid modes to create_tee() are: %s" % ', '.join(valid_modes))

        tee_list = []
        for file in files:
            if type(file) == str:
                fp = open(file, mode)
                tee_list.append(fp)
            else:
                tee_list.append(file)

        pipe_read, pipe_write = os.pipe()
        pid = os.fork()
        if pid == 0:
            # Child -- Read bytes from the pipe and write them to the specified
            #          files.
            try:
                # Close parent's end of the pipe
                os.close(pipe_write)

                bytes = os.read(pipe_read, buffer_size)
                while(bytes):
                    for file in tee_list:
                        file.write(bytes)
                        file.flush()
                        # TODO maybe add in fsync() here if the fileno() method
                        # exists on file

                    bytes = os.read(pipe_read, buffer_size)
            except:
                pass
            finally:
                os._exit(255)
        else:
            # Parent -- Return a file object wrapper around the pipe to the
            #           child.
            return os.fdopen(pipe_write,'w')

if __name__ == '__main__':
    files     = [ '/tmp/tee-test-1', '/tmp/tee-test-2' ]
    num_chars = 100000

    print "Writing %d chars to files (using create_tee):" % num_chars
    for file in files:
        print "  %s" % file
    print

    tee = create_tee(files,mode='a')
    print >>tee, "a" * num_chars,
    tee.close()
    os.wait()

    for filename in files:
        with open(filename, 'r') as fh:
            chars = len(fh.read())
            print "File '%s' has %d chars" % (filename, chars)
