# FEI OS useful utils
from . import errmsg

__all__ = ["out", "outline", "run", "runbatch","load_cmd"]


def out(txt: str):
    """Print function within line."""
    print(txt, end="")


def outline(txt: str):
    """Normal print function."""
    print(txt, end="\n")


def run(tl: list[str]):
    """Run a list of commands given."""
    for line in tl:
        if line.startswith("#"):
            continue
        elif line[:4] == "outl":
            if len(line) == 4:
                print("")
                continue
            else:
                if line[4] == " ":
                    print(line[5:])
                    continue
                else:
                    print(errmsg.ERR_SPACES)
                    return 2
        elif line[:3] == "out":
            if len(line) == 3:
                print("",end="")
                continue
            if line[3] != " ":
                print(errmsg.ERR_SPACES)
                return 2
            else:
                print(line[4:])
                continue
        elif line[:4] == "exit":
            return 0
        else:
            print(errmsg.ERR_NO_COMMAND)
            return 2


def runbatch(pof):
    """Read a batch script and execute it."""
    try:
        f = open(pof,'r')
    except FileNotFoundError:
        print(errmsg.ERR_NO_FILE)
        return 2
    except UnicodeDecodeError as e:
        print(errmsg.ERR_ENCODING(e))
    except OSError:
        print(errmsg.FATAL_OS)
        return 255
    except Exception:
        print(errmsg.FATAL_UNKNOWN)
        return 255
    content = f.readlines()
    ret = run(content)
    return ret


def load_ext(extpth,*,extt="python"):
    if extt != "python":
        outline("""It seems you're not using a python extension.
        We'll soon support other extensions.
        """)
        return 3
    else:
        import subprocess
        ret = subprocess.call(f'py {extpth}')
        return ret


def load_cmd(cmd : str):
    """Load a cmd."""
    if cmd[0] == "#":
        return
    elif cmd[:4] == "outl":
        if len(cmd) == 4:
            print("")
            return
        else:
            if cmd[4] == " ":
                print(cmd[5:])
                return
            else:
                print(errmsg.ERR_SPACES)
                return
    elif cmd[:3] == "out":
        if len(cmd) == 3:
            print("")
            return
        if cmd[3] == " ":
            print(cmd[4:],end="")
        else:
            print(errmsg.ERR_SPACES)
            return
    elif cmd[:3] == "run":
        if len(cmd) == 3:
            print(errmsg.ERR_NOT_SPECIFIC_SCRIPT)
            return
        elif cmd[3] != " ":
            print(errmsg.ERR_SPACES)
            return
        else:
            runbatch(cmd[4:])
            return
    elif cmd[:4] == "exit":
        if len(cmd) >= 5:
            exit(cmd[5:])
        else:
            exit()
    elif cmd == "":
        return
    else:
        print(errmsg.ERR_NO_COMMAND)
        return
    return