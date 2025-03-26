import json
from argparse import ArgumentParser as ArgParser
from argparse import ArgumentTypeError


def main():
    # Create a parser
    parser = ArgParser(description="CLI task tracker")
    
    # Add arguments
    subparsers = parser.add_subparsers(dest="commands",  required=True)

    add_parser = subparsers.add_parser("add",         help="Add a new item")
    add_parser.add_argument("item", type=validate_quotes, help='Item to add')
    
    delete_parser = subparsers.add_parser("delete", help="Delete an existing item by its id")
    delete_parser.add_argument("item_id", type=int, help= 'item_id to delete the item')
    
    # Parse arguments
    args = parser.parse_args()
    
    # perform the task
    do_task(args)
    
    
def do_task(args):
    id = 0
    data = {}
    if args.commands == "add":
        try: 
           with open("tasks.json", "r") as file:
               data = json.load(file)
               id = int(max(n for n in data.keys()))
        except (FileNotFoundError, json.JSONDecodeError):
           with open("tasks.json", "w") as file:
               json.dump({}, file, indent=4)
       
        with open("tasks.json", "w") as file:
             id += 1
             _data = data
             _data[int(id)] = {"id": id, "task": args.item}
             json.dump(data, file, indent=4)
             print(f"{args.item} is added sucessfully")
    elif args.commands == "delete":
         item = data.pop(args.item_id)
         print(f"{item} is deleted sucessfully")  
   
       
def validate_quotes(value):
    """Ensure the input is wrapped in quotes."""
    # print(f"Received input: {value}")  # Debugging print
    
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value  # Input is properly quoted
    
    raise ArgumentTypeError('Argument must be enclosed in quotes, e.g., "apple" or \'apple\'')


if __name__ == "__main__":
    main()