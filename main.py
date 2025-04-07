# add description and rename it

import json
import sys
from typing import Dict

# fix bugs


def main():
    args, do = extract_args()
    print(args)  # debug

    # perform the task
    execute_command(args, do)


def extract_args():  # Needs refactoring
    raw_args = sys.argv[1:]
    args: Dict = {}
    # Create a parser
    if raw_args[0] == "-h":
        print("""CLI task tracker""")  # Add the help message

    elif raw_args[0] == "add":
        args["command"] = "add"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) != 2:
                report_error(f"Wrong number of arguments is provided {len(raw_args) - 1}."
                             + " Provide only 1 argument.", "Argument")
                return args, False
            else:
                task = raw_args[1]
                args["args"] = [task]
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
                return args, False
            else:
                print("Add a new task\n" + "Usage: add task\n "
                      + "Note if there is a space in the input task wrap it in a quotes")

    elif raw_args[0] == "delete":
        args["command"] = "delete"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) != 2:
                report_error(f"Wrong number of arguments is provided {len(raw_args) - 1}."
                             + " Provide only 1 argument.", "Argument")
                return args, False
            else:
                task_id_to_delete = raw_args[1]
                try:
                    task_id_to_delete = int(task_id_to_delete)
                except ValueError:
                    report_error("ID must be an integer", "Type")
                    return args, False
                else:
                    args["args"] = [task_id_to_delete]
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
                return args, False
            else:
                print("Delete an existing task by its ID\n" + "Usage: delete ID")

    elif raw_args[0] == "update":
        args["command"] = "update"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) != 3:
                report_error(f"Wrong number of arguments is provided {len(raw_args) - 1}."
                             + " Provide only 2 arguments.", "Argument")
                return args, False
            else:
                args["args"] = []
                task_id = raw_args[1]
                try:
                    task_id = int(task_id)
                except ValueError:
                    report_error("ID must be an integer", "Type")
                    return args, False
                else:
                    args["args"].append(task_id)

                new_task = raw_args[2]
                args["args"].append(new_task)
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
                return args, False
            else:
                print("Update an existing task by its id. The new task will replace the old one.\n"
                      + "Usage: update ID new-task")

    elif raw_args[0] == "list":
        args["command"] = "list"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) == 1:
                args["args"] = ["all"]  # default "all"
            elif len(raw_args) == 2:
                choices = ["all", "in-progress", "done", "todo"]  # "to-do" == "undone"
                if raw_args[1] not in choices:
                    report_error("Invalid status choose from: [all, in-progress, done, todo]",
                                 "InvalidChoice")
                    return args, False
                else:
                    args["args"] = [raw_args[1]]  # Optional
            else:
                report_error(f"Wrong number of arguments is provided.", "Argument")
                return args, False
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
                return args, False
            else:
                print("List the tasks by the given status. If no status provided all tasks will be listed\n"
                      + "Usage: list [status]\n" + "Available status choices: in-progress, done, todo, all")

    elif raw_args[0] == "mark":
        args["command"] = "mark"
        if "-h" not in raw_args[1:] or "--help" not in raw_args[1:]:
            if len(raw_args) == 2:
                # ID argument
                task_id_to_mark = raw_args[1]
                try:
                    task_id_to_mark = int(task_id_to_mark)
                except ValueError:
                    report_error("ID must be an integer", "Type")
                    return args, False
                else:
                    args["args"] = [task_id_to_mark]

                # Status argument
                args["args"].append("done")  # Optional, default "done"

            elif len(raw_args) == 3:
                args["command"] = "mark"

                # ID argument
                task_id_to_mark = raw_args[1]
                try:
                    task_id_to_mark = int(task_id_to_mark)
                except ValueError:
                    report_error("ID must be an integer", "Type")
                    return args, False
                else:
                    args["args"] = [task_id_to_mark]

                # Status argument
                choices = ["in-progress", "done", "todo"]
                # the last one to return the task to the basic state if it was marked by mistake
                if raw_args[2] not in choices:
                    report_error("Invalid status choose from: [in-progress, done, todo]",
                                 "InvalidChoice")
                    return args, False
                else:
                    args["args"].append(raw_args[2])  # Optional
            else:
                report_error(f"Wrong number of arguments is provided.", "Argument")
                return args, False
        else:
            if len(raw_args) != 2:
                report_error(f"Arbitrary arguments are provided with help option.", "Argument")
                return args, False
            else:
                print("Mark the tasks as in-progress, done, or todo." +
                      " If no choice provided the task will be marked as done\n"
                      + "Usage: mark [as]\n" + "Available choices: in-progress, done, or todo")
    else:
        report_error("No such argument.\n" + "Choose from: [add, delete, update, list, or mark]", "Argument")

    return args, True


def execute_command(args, do):
    data = get_data()
    task_id = get_id(data)
    if args["command"] == "add":
        if do:
            add_task(args["args"][0], task_id, data)
    elif args["command"] == "delete":
        if do:
            delete_task(args["args"][0], data)
    elif args["command"] == "update":
        if do:
            update_task(args["args"][0], args["args"][1], data)
    elif args["command"] == "list":
        if do:
            list_tasks(data, args["args"][0])
    elif args["command"] == "mark":
        if do:
            mark_task(data, args["args"][0], args["args"][1])
    else:
        pass
        # No need to do anything, because extract_args reports error and ignore the invalid command

    # then (8) add the rest of the features from roadmap like adding time ...


def get_data():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        write_to_json("tasks.json", {})
        return {}


def get_id(data):
    existing_ids = [int(key[1:]) for key in data.keys()]  # Extract numerical IDs from keys
    for num in range(1, len(data) + 1):
        if num not in existing_ids:  # Check for the first missing number
            return num
    return len(data) + 1  # If no missing values


def write_to_json(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def add_task(item, task_id, data):
    data[f"t{task_id}"] = {"id": task_id, "task": item, "status": "todo"}
    write_to_json("tasks.json", data)
    print(f"Successfully added {item} (ID: {task_id})")


def delete_task(task_id, data):
    try:
        item = data.pop(f"t{task_id}")
    except KeyError:
        report_error(f"No task is associated with the ID {task_id}.", "ID")  # error
    else:
        write_to_json("tasks.json", data)
        print(f"Successfully deleted {item['task']}")


def update_task(task_id, new_task, data):
    old = data[f"t{task_id}"]["task"]
    try:
        data[f"t{task_id}"]["task"] = new_task
    except KeyError:
        report_error(f"No task is associated with the ID {task_id}.", "ID")
    else:
        write_to_json("tasks.json", data)
        print(f"Successfully updated '{old}' to '{data[f't{task_id}']['task']}'!")


def sort_dict_data(task_dict):
    return int(task_dict[0][1:])


def list_tasks(data, status):
    # noinspection PyTypeChecker
    sorted_data = sorted(data.items(), key=sort_dict_data)
    if status == "all":
        for _, task_dict in sorted_data:
            print(f"{task_dict["id"]}. {task_dict["task"]} - {task_dict["status"]}")
    else:
        tasks = []
        for _, task_dict in sorted_data:
            if task_dict["status"] == status:
                tasks.append(task_dict)

        if tasks:
            for task in tasks:
                print(f"{task["id"]}. {task["task"]}")
        else:
            print(f"No tasks marked as {status} to be listed.")


def mark_task(data, task_id, new_status):
    data[f"t{task_id}"]["status"] = new_status
    write_to_json("tasks.json", data)
    print(f"Successfully marked {data[f"t{task_id}"]["task"]} as {new_status}!")


def report_error(message, error_type=None):
    sys.stderr.write(f"{error_type if error_type else ""}Error: {message}\n")


if __name__ == "__main__":
    main()
    # complete readme
