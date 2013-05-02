# MouseTrap GUI Test
# from: /app/debug.py
# The debug module of mouseTrap
# debug_test.py

import logging # an integrated logging system

modules = {}

class StreamFileHandler(logging.Handler):
    
    def emit(self, record):
        final_msg = "%s: %s - %s" % (record.levelname, record.name, record.getMessage())
        print(final_msg)

def checkModule( module ):
    """
    Get's a new logger for modules.

    Arguments:
    - module: The module requesting a logger.
    """

    level = logging.DEBUG

    formatter = logging.Formatter("%(levelname)s: %(name)s -> %(message)s")

    cli = StreamFileHandler( )
    cli.setLevel( level )
    cli.setFormatter(formatter)

    modules[module] = logging.getLogger( module )
    modules[module].addHandler(cli)
    modules[module].setLevel( level  )

def debug( module, message ):
    """
    Print DEBUG level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

	# if the module is not already in the "modules" list,
	# add it and it's info to the list
    if module not in modules:
        checkModule(module)

	# run debug on the module
    modules[module].debug(message)


def info( module, message ):
    """
    Print INFO level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

	# run info on the module
    modules[module].info(message)


def warning( module, message ):
    """
    Print WARNING level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

	# run warning on the module
    modules[module].warning(message)


def error( module, message ):
    """
    Print ERROR level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

	# run error on the module
    modules[module].error(message)


def critical( module, message ):
    """
    Print CRITICAL level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

	# run critical on the module
    modules[module].critical(message)


def exception( module, message ):
    """
    Print EXCEPTION level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

	# run exception on the module
    modules[module].exception(message)
	
#############################################################################

# The following code has been borrowed from the following URL:
#
# http://www.dalkescientific.com/writings/diary/archive/ \
#                                     2005/04/20/tracing_python_code.html
#
import linecache # random access to text lines
				 # allows one to get any line from any file
				 
def traceit(frame, event, arg):
    """
    Line tracing utility to output all lines as they are executed by
    the interpreter.  This is to be used by sys.settrace and is for
    debugging purposes.

    Arguments:
    - frame: is the current stack frame
    - event: 'call', 'line', 'return', 'exception', 'c_call', 'c_return',
             or 'c_exception'
    - arg:   depends on the event type (see docs for sys.settrace)

    Returns traceit
    """

    if event == "line":
        lineno = frame.f_lineno
        filename = frame.f_globals["__file__"]
        if (filename.endswith(".pyc") or
            filename.endswith(".pyo")):
            filename = filename[:-1]
        name = frame.f_globals["__name__"]
        if name == "gettext" \
           or name == "locale" \
           or name == "posixpath" \
           or name == "UserDict":
            return traceit
        line = linecache.getline(filename, lineno)
        debug("ALL", "TRACE %s:%s: %s" % (name, lineno, line.rstrip()))
    return traceit

#if debugLevel == EXTREME:
#    sys.settrace(traceit)