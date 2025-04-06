# add description and rename it

import json
import sys


def main():
    args = extract_args()

    # perform the task
    do_task(args)


def extract_args():
    raw_args = sys.argv[1:]
    args = {}
    # Create a parser
    if raw_args[0] == "-h":
        print("""CLI task tracker""")  # Add the help message
    elif raw_args[0] == "add":
        args["command"] = "add"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) != 2:
                report_error(f"Wrong number of arguments is provided {len(raw_args) - 1}."
                             + " Provide only 1 argument.", "Argument")
            else:
                task = raw_args[1]
                args["args"] = [task]
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
            else:
                print("Add a new task\n" + "Usage: add task\n "
                      + "Note if there is a space in the input task wrap it in a quotes")
    elif raw_args[0] == "delete":
        args["command"] = "delete"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) != 2:
                report_error(f"Wrong number of arguments is provided {len(raw_args) - 1}."
                             + " Provide only 1 argument.", "Argument")
            else:
                task_id_to_delete = raw_args[1]
                try:
                    task_id_to_delete = int(task_id_to_delete)
                except ValueError:
                    report_error("ID must be an integer", "Type")
                else:
                    args["args"] = [task_id_to_delete]
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
            else:
                print("Delete an existing task by its ID\n" + "Usage: delete ID")

    elif raw_args[0] == "update":
        args["command"] = "update"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) != 3:
                report_error(f"Wrong number of arguments is provided {len(raw_args) - 1}."
                             + " Provide only 2 arguments.", "Argument")
            else:
                args["args"] = []
                task_id = raw_args[1]
                try:
                    task_id = int(task_id)
                except ValueError:
                    report_error("ID must be an integer", "Type")
                else:
                    args["args"].append(task_id)

                new_task = raw_args[2]
                args["args"].append(new_task)
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
            else:
                print("Update an existing task by its id. The new task will replace the old one.\n"
                      + "Usage: update ID new-task")
    elif raw_args[0] == "list":
        if len(raw_args) == 1:
            args["command"] = "list"
        elif len(raw_args) == 2:
            args["args"] = [raw_args[1]]
        else:
            pass # error
    elif raw_args[0] == "mark":
        pass
    else:
        report_error("No such argument.\n" + "Choose from: [add, delete, update, list, or mark]", "Argument")

    """list_parser = subparsers.add_parser("list", help="Delete an existing task by its id", usage=SUPPRESS)
    list_parser.add_argument("options", type=str, choices=["in-progress", "done", "undone", "all"],
                             help="Options: in-progress, done, undone, all", nargs="?"  # to make it optional, or add -
                             )

    mark_parser = subparsers.add_parser("mark", usage=SUPPRESS,
                                        help="Mark an existing item by its id as either in-progress or done")
    mark_parser.add_argument("task_id", type=int, help='task_id to be marked')
    mark_parser.add_argument("as", type=str, choices=["in-progress", "done"],
                             help="Options: done, in-progress", nargs="?")

    # Parse arguments
    args = parser.parse_args()"""

    return args


def do_task(args):
    data = get_data()
    task_id = get_id(data)
    if args["command"] == "add":
        add_task(args["args"][0], task_id, data)
    elif args["command"] == "delete":  # then (6) test delete when it is as done
        delete_task(args["args"][0], data)
    elif args["command"] == "update":  # then (3) add this
        update_task(args["args"][0], args["args"][1], data)
    elif args["command"] == "list":
        list_tasks(data)
    elif args["command"] == "mark":  # then (5) add this -as done-, then (7) add - as in progress-
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
    print(f"Successfully added {item} (ID: {task_id})")


def delete_task(task_id, data):
    try:
        item = data.pop(f"t{task_id}")
    except KeyError:
        report_error(f"No task is associated with the ID {task_id}.", "ID")  # error
    else:
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Successfully deleted {item['task']}")


def update_task(task_id, new_task, data):
    old = data[f"t{task_id}"]["task"]
    try:
        data[f"t{task_id}"]["task"] = new_task
    except KeyError:
        report_error(f"No task is associated with the ID {task_id}.", "ID")
    else:
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Successfully updated '{old}' to '{data[f't{task_id}']['task']}'!")


def sort_dict_data(task_dict):
    return int(task_dict[0][1:])


def list_tasks(data):
    # noinspection PyTypeChecker
    for _, task_dict in sorted(data.items(), key=sort_dict_data):
        print(f"{task_dict["id"]}. {task_dict["task"]}")


def report_error(message, error_type=None):
    sys.stderr.write(f"{error_type if error_type else ""}Error: {message}\n")


if __name__ == "__main__":
    main()
    # complete readme
