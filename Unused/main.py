# add description and rename it

import json
from argparse import SUPPRESS, ArgumentTypeError

from MyArgumentParser import ArgumentParser as ArgParser


def main():
    args, parsers = make_parsers()

    # perform the task
    do_task(args, parsers)


def make_parsers():
    # Create a parser
    parser = ArgParser(description="CLI task tracker", usage=SUPPRESS)

    # Add arguments
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new task", usage=SUPPRESS)
    add_parser.add_argument("item", type=str, help='Item to add')

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete an existing task by its id", usage=SUPPRESS)
    delete_parser.add_argument("task_id", help='task_id to delete the item')  # type int

    # Update
    update_parser = subparsers.add_parser("update", help="Update an existing task by its id", usage=SUPPRESS)
    update_parser.add_argument("item_id", type=int, help='task_id to update the task')
    update_parser.add_argument("updated_task", type=str, help='The new task to replace the old one')

    # List
    list_parser = subparsers.add_parser("list", help="Delete an existing task by its id", usage=SUPPRESS)
    list_parser.add_argument("options", type=str, choices=["in-progress", "done", "undone", "all"],
                             help="Options: in-progress, done, undone, all", nargs="?"  # to make it optional, or add -
                             )

    # Mark
    mark_parser = subparsers.add_parser("mark", usage=SUPPRESS,
                                        help="Mark an existing item by its id as either in-progress or done")
    mark_parser.add_argument("task_id", type=int, help='task_id to be marked')
    mark_parser.add_argument("as", type=str, choices=["in-progress", "done"],
                             help="Options: done, in-progress", nargs="?")

    # Parse arguments
    args = parser.parse_args()

    return args, parser


def do_task(args, parser):
    data = get_data()
    task_id = get_id(data)
    if args.command == "add":
        add_task(args.item, task_id, data)
    elif args.command == "delete":  # then (6) test delete when it is as done
        try:
            args.task_id = int(args.task_id)
        except ValueError:
            report_error("ID must be an integer", parser, "Type")
        else:
            delete_task(args.task_id, data, parser)
    elif args.command == "update":  # then (3) add this
        item = data.pop(args.task_id)
        print(f"{item} is updated successfully")
    elif args.command == "list":
        list_tasks(data)
    elif args.command == "mark":  # then (5) add this -as done-, then (7) add - as in progress-
        item = data.pop(args.task_id)
        print(f"{item} is  marked as... successfully")
    else:
        pass

    # then (8) add the rest of the features from roadmap like adding time ...


def get_data():  # and test this
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        with open("tasks.json", "w") as file:
            json.dump({}, file, indent=4)
            return {}


def get_id(data):
    existing_ids = [int(key[1:]) for key in data.keys()]  # Extract numerical IDs from keys
    for num in range(1, len(data) + 1):
        if num not in existing_ids:  # Check for the first missing number
            return num
    return len(data) + 1  # If no missing values


def add_task(item, task_id, data):
    data[f"t{task_id}"] = {"id": task_id, "task": item}
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
    print(f"{item} is added successfully (ID: {task_id})")


def delete_task(task_id, data, parser):
    try:
        item = data.pop(f"t{task_id}")
    except KeyError:
        report_error(f"No task is associated with the ID {task_id}.", parser, "Index")  # error
    else:
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"{item["task"]} is deleted successfully")


def sort_dict_data(task_dict):
    return int(task_dict[0][1:])


def list_tasks(data):
    # noinspection PyTypeChecker
    for _, task_dict in sorted(data.items(), key=sort_dict_data):
        print(f"{task_dict["id"]}. {task_dict["task"]}")


def report_error(message, parser, error_type=None):
    parser.error(message, error_type)


if __name__ == "__main__":
    main()
    # complete readme
