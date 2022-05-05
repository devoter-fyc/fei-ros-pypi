def out(text):
    print(text,end="")
    return 0

def outl(text):
    print(text,end="\n")
    return 0

def runexec(pof,isbytes=False):
    assert isbytes is not True , "The bytes executables are not supported yet."
    a = open(pof,"r+")
    a.seek(0)
    p = a.readlines()
    j = 0
    for i in p:
        i = i.strip("\n")
        p[j] = i
        j += 1
    run(p)
    return 0

def run(cmds:list[str]):
    for cmd in cmds:
        CMD_LIST[cmd]()
    return 0

def log(text,level):
    import logging
    logging.basicConfig(level=logging.INFO)
    LEVELS = {"DEBUG":10,"INFO":20,"WARNING":30,"ERROR":40,"CRITICAL":50}
    finalLevel = LEVELS[level]
    logging.log(finalLevel, text)
    return 0

CMD_LIST = {"out":out,"outl":outl,"runbat":runexec,"runcmds":run,"log":log}