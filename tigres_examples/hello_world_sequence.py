#!/usr/bin/env python
"""
My Tigres Program
"""

import os
import sys

from tigres import *
from tigres.utils import Execution, State, TigresException


def hello():
    """

    :return: Hello
    :rtype: str
    """
    log_trace('input', function='hello', message='No inputs')
    output = "Hello"
    log_trace('output', function='hello', message=output)
    return output


def salutation(greeting, name):
    """

    :param greeting: A greeting
    :param name: The name to greet
    :return: personalized greeting or salutation
    """
    log_trace('input', function='salutation', message='greeting={}, name={}'.format(greeting, name))
    output = "{} {}".format(greeting, name)
    log_trace('output', function='salutation', message=output)
    return output


def world(salutation):
    """

    :param salutation: a greeting
    :return: Greeting to the world
    """
    log_trace('input', function='world', message='salutation={}'.format(salutation))
    output = "{} World!".format(salutation)
    log_trace('output', function='world', message=output)
    return output


def main(execution):
    # Setup up the Tigres Program using __file__ to build the log file name
    start(name="Hello World Sequence", log_dest=os.path.splitext(__file__)[0] + '.log', execution=execution)

    # Heart of Tigres Program here
    set_log_level(Level.INFO)

    # Heart of Tigres Program here
    print("\n++++++++++++++++++++++++++++")
    print("Initial Input:")
    print(None)
    print("++++++++++++++++++++++++++++\n")

    # Create a TaskArray
    task_array = TaskArray('Hello World Tasks')

    # Create an InputArray
    input_array = InputArray("Hello World Inputs")

    # The Hello Task and its inputs
    task_array.append(Task("Hello", FUNCTION, impl_name=hello))
    input_array.append([])

    # The Salutation Task and its inputs
    task_array.append(Task("Salutation", FUNCTION, impl_name=salutation, input_types=[str, str]))
    input_array.append([PREVIOUS, "Tigres"])

    # The World Task and its inputs
    task_array.append(Task("world", FUNCTION, impl_name=world, input_types=[str]))
    input_array.append([PREVIOUS])

    # Run the Tigres Sequence template
    output = sequence('Hello World', task_array, input_array)




    # Check the logs for the decode event
    log_records = query(spec=["{} ~ .*put".format(Keyword.EVENT)])
    for record in log_records:
        print(".. function: {}, {}: {}".format(record["function"], record.event, record.message))

    # Print the output
    print("\n++++++++++++++++++++++++++++")
    print("Final Output:")
    print(output)
    print("++++++++++++++++++++++++++++")

    # Create a DOT (plain text graph) file
    dot_execution()


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

