import re
from itertools import groupby
from Tkconstants import LEFT
from Tkinter import Tk, Text, END


class WorkdaysTk(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.ep = EntryProcessor()
        self.entry = Text(self, height=20, width=27)
        self.entry.pack(side=LEFT)
        self.entry.bind("<<Modified>>", self.init_ep)
        self.entry.focus_set()
        self.out = Text(self, height=20, width=17)
        self.out.pack(side=LEFT)

    def init_ep(self, event):
        if self.entry.edit_modified():
            self.out.delete("1.0", END)
            self.out.insert("1.0", self.ep.process(self.entry.get("1.0", END)))
            self.entry.edit_modified(False)


class EntryProcessor:
    def __init__(self):
        pass

    def process(self, entry):
        return ""

if __name__ == "__main__":
    app = WorkdaysTk()
    app.title('workdays')
    app.mainloop()
