# Contains constants used by other files

constants = {
    'help': str("CSV : summarized csv file\n"
                   "(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license\n"
                   "USAGE: lua seen.lua [OPTIONS]\n"
                   "OPTIONS:\n"
                   " -e  --eg        start-up example                      = nothing\n"
                   " -d  --dump      on test failure, exit with stack dump = false\n"
                   " -f  --file      file with csv data                    = ../data/auto93.csv\n"
                   " -h  --help      show help                             = false\n"
                   " -n  --nums      number of nums to keep                = 512\n"
                   " -s  --seed      random number seed                    = 10019\n"
                   " -S  --Seperator feild seperator                       = ,\n"
    )
}


def getConstant(key: str):
    """
    Returns constant from the constants dict based on the input
    @key: key to match the value from dict
    """
    return constants[key]
