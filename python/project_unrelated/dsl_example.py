class Appointment:
    def __init__(self, with_person, on_day, at_time, for_duration):
        self.with_person = with_person
        self.on_day = on_day
        self.at_time = at_time
        self.for_duration = for_duration
        
    def __str__(self):
        return f"Appointment with {self.with_person} on {self.on_day} at {self.at_time} for {self.for_duration}"
        
def parse_appointment(code):
    lines = code.strip().split("\n")
    appointment = None
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("appointment"):
            appointment = Appointment(None, None, None, None)
        elif line.startswith("with"):
            appointment.with_person = line.split("\"")[1]
        elif line.startswith("on"):
            appointment.on_day = line.split("\"")[1]
        elif line.startswith("at"):
            appointment.at_time = line.split("\"")[1]
        elif line.startswith("for"):
            appointment.for_duration = line.split("\"")[1]
    
    return appointment


with open("appointments.dsl", "r") as file:
    meetings = file.read().split("end")[:-1]

for meeting in meetings:
    appointment = parse_appointment(meeting)
    print(appointment)
