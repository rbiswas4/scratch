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
    start(name="Hello World Parallel", log_dest=os.path.splitext(__file__)[0] + '.log', execution=execution)

    set_log_level(Level.INFO)

    # Heart of Tigres Program here
    hidden_message = 'Gdkkn\x1fShfqdr\x1fvnqkc '
    print("++++++++++++++++++++++++++++")
    print("Initial Input:")
    print (hidden_message)
    print("++++++++++++++++++++++++++++")

    # Create Decode Tigres Task
    task_decode = Task("Decode", FUNCTION, impl_name=decode, input_types=[str])

    # Create a TaskArray with one our one decode task
    task_array = TaskArray('Decode Tasks', tasks=[task_decode])

    # Create a Tigres InputArray of the character values to decode
    input_array = InputArray("Coded Values", [])

    # Iterate through the message string and add input values for each character
    for c in hidden_message:
        input_values = InputValues("A Coded Value {}".format(c), [c])
        input_array.append(input_values)

    # Run the Tigres Parallel template
    output = parallel('Fast Decoding', task_array, input_array)


    # Check the logs for the decode event
    log_records = query(spec=["event = decode"])
    for record in log_records:
        print(".. decoded {}".format(record.message))

    # Print the output
    print("\n++++++++++++++++++++++++++++")
    print("Final Output:")
    print(''.join(output))
    print("++++++++++++++++++++++++++++")

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
            print(".. State of {} = {} -  {}".format(task_record.name,
                                                     task_record.state,
                                                     task_record.errmsg))
