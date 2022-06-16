from tkinter import *
from tkinter import ttk
from model import *
from controler import *

class tkinterGUI:
    def __init__(self):
        pass
    #------------------------------------------------------------------------------------------------------------------------------
    def popup(self, Text):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Text)
        screen.resizable(0, 0)
        Label(screen, text=Text, font="Times 15", height=len(Text.split("\n")) + 1, padx=10, pady=10).pack()
        Button(screen, text="Ok", padx=15, pady=5, command=lambda: screen.destroy()).pack()
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def confirm_screen(self, Text:str, function):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Text)
        screen.resizable(0, 0)
        #Returning option
        def selected_option(option:int):
            screen.destroy()
            if option:
                function()
        Label(screen, text=Text, font="Times 15", width=20).grid(row=0, columnspan=2)
        Button(screen, text="Sim", padx=15, pady=5, command=lambda: selected_option(1)).grid(row=1, column=0)
        Button(screen, text="Não", padx=15, pady=5, command=lambda: selected_option(0)).grid(row=1, column=1)
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def text_input_screen(self, Title, Instruction, function, first_button_text="Confirmar"):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Title)
        screen.resizable(0, 0)
        def exit(textinput):
            function(textinput)
            screen.destroy()
        Label(screen, text=Title, font="Times 15", width=20).grid(row=0, columnspan=2)
        Label(screen, text=Instruction, width=30, anchor=W).grid(row=1, columnspan=2)
        entry = Entry(screen, width=30)
        entry.focus()
        entry.grid(row=2, columnspan=2)
        Button(screen, text=first_button_text, padx=5, command=lambda: exit(entry.get())).grid(row=3, column=0)
        Button(screen, text="Cancelar", padx=5, command=lambda: screen.destroy()).grid(row=3, column=1)
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def combobox_screen(self, Title, Instruction, Options, function, first_button_text="Escolher"):
        screen = Toplevel()
        screen.grab_set()
        screen.title(Title)
        screen.resizable(0, 0)
        def exit(option):
            function(option)
            screen.destroy()
        Label(screen, text=Title, font="Times 15", width=20).grid(row=0, columnspan=2)
        Label(screen, text=Instruction, width=30, anchor=W).grid(row=1, columnspan=2)
        Partys = ttk.Combobox(screen, state="readonly", values=Options)
        Partys.current(0)
        Partys.grid(row=2, columnspan=2)
        Button(screen, text=first_button_text, padx=5, command=lambda: exit(Partys.get())).grid(row=3, column=0)
        Button(screen, text="Cancelar", padx=5, command=lambda: screen.destroy()).grid(row=3, column=1)
        screen.mainloop()

class app(tkinterGUI):
    def __init__(self):
        super().__init__()
        hide_all_windows()
        self.root = Tk()
        self.main_menu()
    #------------------------------------------------------------------------------------------------------------------------------    
    def main_menu(self):
        self.root.title("MainMenu")
        self.root.geometry("%dx%d+0+0" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.overrideredirect(True)

        #Elements
        title = Label(
            self.root,
            text="SysGremio",
            font="Times 35 bold",
            width=100,
            height=6,
            anchor=N,
            pady=20
        )
        
        start_election = Button(
            self.root,
            text="Iniciar votação",
            font="Times 12",
            padx=20,
            command=lambda: self.voting_menu()
        )

        change_partys = Button(
            self.root,
            text="Alterar chapas",
            font="Times 12",
            padx=20,
            command=lambda: self.settings_page()
        )
        
        exit = Button(
            self.root,
            text="Sair",
            font="Times 12",
            padx=20,
            command=lambda: self.root.destroy()

        )

        #Layout
        title.pack()
        start_election.pack()
        Label(self.root, text="").pack()
        change_partys.pack()
        Label(self.root, text="").pack()
        exit.pack()
        Label(self.root, text="Desenvolvido pelo curso de informática.", font="Times 12", height=16, pady=5, anchor=S).pack()

        #Mainloop
        self.root.mainloop()
    
    #------------------------------------------------------------------------------------------------------------------------------
    def voting_menu(self):
        self.election = election()
        n_partys = len(self.election.partys)
        if n_partys < 2:
            self.popup(("Não há chapas registradas!\nAdicione as chapas antes de\niniciar a votação." if n_partys == 0 else "Há apenas uma chapa registrada!\nSão necessárias no mínimo\nduas chapas para começar."))
        screen = Toplevel()
        screen.title("VotingMenu")
        screen.geometry("%dx%d+0+0" % (screen.winfo_screenwidth(), screen.winfo_screenheight()))
        screen.overrideredirect(True)

        #Checking password
        def check_password(Password, mode):
            #self.election
            def next_window():
                screen.destroy()
                self.election_result_screen()
            if Password == "":
                if mode: #vote
                    self.voting_screen()
                else: #finish 
                    self.confirm_screen("Finalizar votação?", lambda: next_window())
                    
            else:
                self.popup("Senha inválida")

        #Elements
        title = Label(
            screen,
            text="Votação",
            font="Times 35 bold",
            width=100,
            height=6,
            anchor=N,
            pady=20
        )

        password = Entry(
            screen,
            show="*"
        )
        
        vote = Button(
            screen,
            text="Votar",
            font="Times 12",
            padx=20,
            command=lambda: check_password(password.get(), 1)
        )

        finish_election = Button(
            screen,
            text="Finalizar votação",
            font="Times 12",
            padx=20,
            command=lambda: check_password(password.get(), 0)
        )
        
        #Layout
        title.pack()
        Label(screen, text="Digite a senha para finalizar a votação:", font="Times 12").pack()
        password.pack()
        password.focus()
        Label(screen, text="").pack()
        vote.pack()
        Label(screen, text="").pack()
        finish_election.pack()
        Label(screen, text="Desenvolvido pelo curso de informática.", font="Times 12", height=16, pady=5, anchor=S).pack()

        #Mainloop
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def voting_screen(self):
        screen = Toplevel()
        screen.title("VotingScreen")
        screen.geometry("%dx%d+0+0" % (screen.winfo_screenwidth(), screen.winfo_screenheight()))
        screen.overrideredirect(True)
        #Aditioning partys
        array = []
        for party in self.election.partys:
            array.append(party.name)
        
        #Confirm vote
        def confirm_vote():
            self.election.vote(Partys["values"].index(Partys.get()) + 1)
            screen.destroy()

        #Elements
        title = Label(
            screen,
            text="Vote consciente",
            font="Times 35 bold",
            width=100,
            height=6,
            anchor=N,
            pady=20
        )

        Partys = ttk.Combobox(
            screen,
            state="readonly",
            values=array
        )
        Partys.current(0)
        
        vote = Button(
            screen,
            text="Votar",
            font="Times 12",
            padx=20,
            command=lambda: self.confirm_screen("Confirmar voto?", lambda: confirm_vote())
        )

        #Layout
        title.pack()
        Label(screen, text="Selecione sua chapa e aperte em votar:", font="Times 12").pack()
        Partys.pack()
        Label(screen, text="").pack()
        vote.pack()
        Label(screen, text="").pack()
        Label(screen, text="Desenvolvido pelo curso de informática.", font="Times 12", height=16, pady=5, anchor=S).pack()

        #Mainloop
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def election_result_screen(self):
        screen = Toplevel()
        screen.title("ElectionResult")
        screen.geometry("%dx%d+0+0" % (screen.winfo_screenwidth(), screen.winfo_screenheight()))
        screen.overrideredirect(True)

        #Elements
        title = Label(
            screen,
            text="Resultado da Votação",
            font="Times 35 bold",
            width=100,
            height=6,
            anchor=N,
            pady=20
        )

        result = Label(
            screen,
            text="".join(self.election.pr.read(0)),
            font="Times 12", 
            height=len(self.election.pr.read(0)),
            anchor=N
        )
        
        back = Button(
            screen,
            text="Voltar ao menu",
            font="Times 12",
            padx=20,
            command=lambda: screen.destroy()
        )
        
        #Layout
        title.pack()
        result.pack()
        Label(screen, text="").pack()
        back.pack()
        Label(screen, text="").pack()
        Label(screen, text="Desenvolvido pelo curso de informática.", font="Times 12", height=16, pady=5, anchor=S).pack()

        #Mainloop
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    def settings_page(self):
        screen = Toplevel()
        screen.title("Settings")
        screen.geometry("%dx%d+0+0" % (screen.winfo_screenwidth(), screen.winfo_screenheight()))
        screen.overrideredirect(True)

        #Elements
        title = Label(
            screen,
            text="Alterar chapas",
            font="Times 35 bold",
            width=100,
            height=6,
            anchor=N,
            pady=20
        )

        add = Button(
            screen,
            text="Adicionar chapa",
            font="Times 12",
            padx=20,
            command=lambda: self.text_input_screen("Adicionar chapa", "Digite o nome da nova chapa:", add_party)
        )

        delete = Button(
            screen,
            text="Deletar chapa",
            font="Times 12",
            padx=20,
            command=lambda: self.combobox_screen("Excluir chapa", "Escolha a chapa para excluir:", partys.read(0), del_party, "Excluir")
        )
        
        back = Button(
            screen,
            text="Voltar ao menu",
            font="Times 12",
            padx=20,
            command=lambda: screen.destroy()
        )
        
        #Layout
        title.pack()
        add.pack()
        Label(screen, text="").pack()
        delete.pack()
        Label(screen, text="").pack()
        back.pack()
        Label(screen, text="").pack()
        Label(screen, text="Desenvolvido pelo curso de informática.", font="Times 12", height=16, pady=5, anchor=S).pack()

        #Mainloop
        screen.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------
    

app = app()



        
