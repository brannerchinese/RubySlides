class View
    self.MESSAGES = {'welcome': '\nThis program models a cup of coffee. \n\n' +
                       'Your options are:\n' +
                       '  fill\n' +
                       '  empty\n' +
                       '  gulp\n' +
                       '  sip\n' +
                       '  exit',
                     'sorry': 'Sorry, I don't know that command.',
                     'goodbye': 'End of program.'.
                     None: 'Not possible at this time.'}

    def display(msg)
        if msg in self.MESSAGES:
            print(self.MESSAGES[msg])
        else
            print(msg)

    def get_input
        return input('What do you want to do? ')
