def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        personalized = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            personalized = personalized.replace(f"{{{key}}}", str(value))

        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")