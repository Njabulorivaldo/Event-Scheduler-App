class Event:

    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

    def display_info(self):

        wrapped_description = self.wrap_text(self.description, 30)
        lines = wrapped_description.split('\n')
        print("{:<15} | {:<30} | {:<15} | {:<10}".format(self.title, lines[0], self.date, self.time))
        for line in lines[1:]:
            print("{:<15} | {:<30} | {:<15} | {:<10}".format("", line, "", ""))

        print("-" * 80)

    @staticmethod
    def wrap_text(text, width):
        #Method to wrap the description around for good tabular fit

        wrapped_lines = []
        for i in range(0, len(text), width):
            wrapped_lines.append(text[i:i+width])
        return '\n'.join(wrapped_lines)

