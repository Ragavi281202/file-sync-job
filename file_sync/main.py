def run(config: dict) -> bool:
    try:
        print("Running File Sync Job")

        file_name = config.get("file_name")
        directory = config.get("directory", "/tmp")

        if not file_name:
            raise ValueError("file_name is required")

        full_path = f"{directory}/{file_name}"

        with open(full_path, "w") as f:
            f.write("Hello from File Sync Job")

        print(f"File created at {full_path}")

        return True

    except Exception as e:
        print("Error:", str(e))
        return False
