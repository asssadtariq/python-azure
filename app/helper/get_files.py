import os

def get_latest_files(directory):
    try:
        files: dict[str, list] = {}
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if not os.path.isfile(file_path):
                continue

            creation_time = int(str(os.path.getctime(file_path)).split(".")[0])

            if creation_time not in files.keys():
                files[creation_time] = [filename]
                continue

            files[creation_time].append(filename)

        # extract the latest files

        # sort the object keys
        reverse_order_object_keys = sorted(files.keys(), reverse=True)

        # in case no file found return empty list
        if not reverse_order_object_keys:
            print("No data found in ", files)
            return []

        # get the latest files
        latest_datetime = reverse_order_object_keys[0]

        return files[latest_datetime]

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
