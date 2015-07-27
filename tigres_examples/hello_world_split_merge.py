#!/usr/bin/env python
"""
My Tigres Program
"""

import os
import sys

from tigres import *
from tigres.utils import Execution, State, TigresException


def main(execution):
    # Setup up the Tigres Program using __file__ to build the log file name
    start(name="Hello World Parallel Split Merge",
          log_dest=os.path.splitext(__file__)[0] + '.log', execution=execution)

    set_log_level(Level.INFO)

    # Heart of Tigres Program here
    message = 'Hello Tigres world!'
    print("++++++++++++++++++++++++++++")
    print("Initial Input:")
    print(message)
    print("++++++++++++++++++++++++++++\n")

    # ########################################################
    # Setting up a Split Template for encoding the message
    #########################################################

    # Create a Task for parsing the string
    task_to_list = Task("String to List", FUNCTION,
                        impl_name=lambda x: x, input_types=[str])
    input_string = InputValues("String to encode", [message])

    # Create a Task Array for the encode_string tasks
    task_encode = Task("Encode", FUNCTION, impl_name=encode, input_types=[str])
    task_array_encode = TaskArray('Encoding Tasks', tasks=[task_encode])

    # We create an empty input array that will be implicitly filled with the
    # PREVIOUS  task's output. The output of the of the split task must be iterable
    input_array_encode = InputArray("String Values", [])
    tmpoutput = split("Fast Encoding", task_to_list,
                      input_string, task_array_encode, input_array_encode)

    # Print the output
    print("\n++++++++++++++++++++++++++++")
    print("Intermediate Output:")
    print(tmpoutput)
    print("++++++++++++++++++++++++++++\n")





    #########################################################
    # Setting up a Merge Template for decoding the message
    #########################################################

    # Create Decode Tigres Task
    task_decode = Task("Decode", FUNCTION, impl_name=decode, input_types=[str])
    # Create a TaskArray with one our one decode_string task
    task_array = TaskArray('Decoding Tasks', tasks=[task_decode])
    # Run the Tigres Split template
    output = merge('Fast Decoding', task_array, None,
                   Task("To String", FUNCTION, impl_name=lambda x: ''.join(x)))

    # Print the output
    print("\n++++++++++++++++++++++++++++")
    print("Final Output:")
    print output
    print("++++++++++++++++++++++++++++\n")

    log_records = query(spec=["event ~ ..code"])
    for record in log_records:
        print(".. {}d {}".format(record.event, record.message))

    # Create DOT (plain text graph) file
    dot_execution()


def decode(value):
    if isinstance(value, int):
        ordinal = value
    else:
        ordinal = ord(str(value))
    ordinal += 1
    log_debug("decode", message="{} to {}".format(value, unichr(ordinal)))
    return unichr(ordinal)


def encode(value):
    if isinstance(value, int):
        ordinal = value
    else:
        ordinal = ord(str(value))
    ordinal -= 1
    log_debug("encode", message="{} to {}".format(value, unichr(ordinal)))
    return unichr(ordinal)


if __name__ == "__main__":
    # Simple Usage Here
    if len(sys.argv) <= 1:
        print("Usage: {} ({})>".format(sys.argv[0], "|".join(Execution.LOOKUP.keys())))
        exit()
    try:
        main(Execution.get(sys.argv[1]))
    except TigresException as e:
        print(e)
        task_check = check('task', state=State.FAIL)
        for task_record in task_check:
            print(".. State of {} = {} -  {}".format(task_record.name, task_record.state, task_record.errmsg))

