import tkinter as tk

class App(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.card = 0
    self.canvas = tk.Canvas(self, width=800,height=600)
    self.canvas.pack()
    self.pack()
    self.cards = {}
    self.term_list = []
    print(len(self.cards))
    self.create_widgets()
    self.canvas.create_rectangle(30,200,390,420,fill='#fff')
    self.canvas.create_rectangle(410,200,770,420,fill='#fff')
    card_no = tk.Label(self, text = self.card)
    self.card_no_text = self.canvas.create_window(30, 20, window = card_no)

  def create_widgets(self):
    #Add card button
    self.add_button = tk.Button(self)
    self.add_button['text'] = 'Add Card'
    self.add_button['command'] = self.add_card
    self.canvas.create_window(625, 20, window=self.add_button)

     # remove buttom
    self.remove_button = tk.Button(self)
    self.remove_button['text'] = 'Remove Card'
    self.remove_button['command'] = self.test

    self.next_button = tk.Button(self)
    self.next_button['text']= 'Next'
    self.next_button['command'] = self.next_card
    self.canvas.create_window(360,100, window=self.next_button)

    self.back_button = tk.Button(self) #button that goes backwards
    self.back_button['text'] = 'Back'
    self.back_button['command'] = self.previous_card
    self.canvas.create_window(440, 100, window=self.back_button)

    #Text Boxes
    self.term = tk.Entry(self)
    self.canvas.create_window(275, 20, window=self.term)
    
    self.definition = tk.Entry(self)
    self.canvas.create_window(470, 20, window=self.definition)
  
  def next_card(self):
    if self.card + 2 > len(self.cards):
      return
    self.card += 1
    self.refresh()   
    pass
  
  def previous_card(self):
    if self.card - 1 < 0:
      return
    self.card -= 1
    self.refresh()
    pass

  def refresh(self):
    self.canvas.create_rectangle(30,200,390,420,fill='#fff')
    self.canvas.create_rectangle(410,200,770,420,fill='#fff')
    term = self.term_list[self.card]
    word = tk.Label(self, text = term)
    self.term_card = self.canvas.create_window(210, 310, window=word)
    definition = tk.Label(self, text = self.cards[term])
    self.definition_card = self.canvas.create_window(590, 310, window = definition)
    card_no = tk.Label(self, text = self.card)
    self.card_no_text = self.canvas.create_window(30, 20, window = card_no)
    print("%s: %s" % (term, self.cards[term]))
    print(self.term_list)
  
  def add_card(self):
    self.key = self.term.get()
    self.defi = self.definition.get()
    if len(self.cards) - 1 > 50:
      print('limit reached')
      return
    if self.key is None or self.defi is None:
      return
    self.cards[self.key] = self.defi
    self.term_list = list(self.cards)
    self.refresh()
    word = tk.Label(self, text = self.key)
    self.term_card = self.canvas.create_window(210, 310, window=word)
    definition = tk.Label(self, text = self.defi)
    self.definition_card = self.canvas.create_window(590, 310, window = definition)
    self.card = len(self.term_list) - 1
    self.card += 1
    pass

  
  def test(self):
    print('test')
  
root = tk.Tk()
root.geometry('800x600')
root.title('Quizlet Clone')
root.resizable(False, False)
app = App(master=root)
app.mainloop()