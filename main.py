import sys, json, yaml

def parse():

    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    return sys.argv[1], sys.argv[2]

def load_json(input):
    try:
        with open(input, 'r') as f:
            data = json.load(f)
        print("JSON data loaded successfully")
        return data
    
    except Exception as e:
        print(f"Failed to load JSON file: {e}")
        sys.exit(1)

def save_json(data, output):
    try:
        with open(output, 'w') as f:
            json.dump(data, f, indent=4)
        print("JSON data saved successfully")

    except Exception as e:
        print(f"Failed to save JSON file: {e}")
        sys.exit(1)

def load_yaml(input):
    try:
        with open(input, 'r') as f:
            data = yaml.safe_load(f)
        print("YAML data loaded successfully")
        return data
    
    except Exception as e:
        print(f"Failed to load YAML file: {e}")
        sys.exit(1)

def save_yaml(data, output):
    try:
        with open(output, 'w') as f:
            yaml.safe_dump(data, f)
        print("YAML data saved successfully")

    except Exception as e:
        print(f"Failed to save YAML file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input, output = parse()
    print(f"Input file: {input}, Output file: {output}")
    if input.endswith('.json'):
        data = load_json(input)
        if output.endswith('.json'):
            save_json(data, output)
        elif output.endswith('.yml') or output.endswith('.yaml'):
            save_yaml(data, output)
    elif input.endswith('.yml') or input.endswith('.yaml'):
        data = load_yaml(input)
        if output.endswith('.json'):
            save_json(data, output)
        elif output.endswith('.yml') or output.endswith('.yaml'):
            save_yaml(data, output)