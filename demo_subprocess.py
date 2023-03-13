from subprocess import (
    run,
    PIPE,
    STDOUT,
    Popen,
    TimeoutExpired,
    CalledProcessError,
    SubprocessError
)

"""
subprocess.run
"""
def call_run(cmd):
    try:
        output = run(cmd, capture_output=True)
    except CalledProcessError as ex:
        # An error occurs with the command to execute
        print(ex)
    except TimeoutExpired as ex:
        # Timeout issue
        print(f"Timeout was raised while executing command : {ex}")
    except SubprocessError as ex:
        # Any other Subprocess exception
        print(f"Subprocess exception : {ex}")
    except Exception as ex:
        # Any other exception
        print(ex)
    else:
        # Everything when fine !
        print(output)
        print(output.returncode)
        print(output.stdout)
        return output.stdout, output.returncode
    return None, None


"""
subprocess.Popen
"""
def call_Popen(cmd: List[str]):
    output, ret, rt_proc = None, None, None
    try:
        rt_proc = Popen(
            cmd,
            stdout=PIPE,
            stderr=STDOUT
        )
        output, ret = rt_proc.communicate()
    except Exception as e:
        if rt_proc is not None and rt_proc.poll() is None:
            # We do not leave zombies behind
            rt_proc.kill()
            rt_proc.wait()
    else:
        if rt_proc.returncode != 0:
            # An error occurs during the process excution
            print(f"Returned value is {rt_proc.returncode} : an error occurs !")
    return output, rt_proc.returncode if rt_proc is not None else rt_proc.returncode

def main():
    # Please update "lo0" to something else
    cmd = ["ifconfig", "lo0"]
    output, returncode = call_run(cmd)
    print(output, returncode)
    output, process = call_Popen(cmd)
    print(output, process)


if __name__ == "__main__":
    main()