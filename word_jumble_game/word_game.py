from tkinter import Tk, Button, Label, Entry, Frame, END, PhotoImage, LEFT, FLAT
import random
from tkinter import messagebox

def main():
    def start_page():
        
        def main_game():

            window = Tk()
            window.geometry("500x500+500+100")
            window.resizable(0, 0)
            window.title("Word Shuffle Game")
            window.configure(background="#040402")
            window.iconbitmap(r'wordicon.ico')

            img1 = PhotoImage(file="back-btn.png")

            main_words = [
                'grammar', 'sunrise', 'firefly', 'garden', 'airplane', 'fireplace', 'virtual', 'acoustic', 'quartz', 'jungle', 'opaque',
                'juice', 'chocolate', 'ice', 'france', 'xylophone', 'turkey', 'xenon', 'purple', 'umbrella', 'night', 'hammer', 'hoe',
                'happiness', 'mexico', 'honeycomb', 'illusion', 'lyrics', 'electricity', 'pajamas', 'india', 'quicksilver', 'tree', 
                'artificial', 'zambia', 'spain', 'wales', 'violet', 'avalanche', 'paintbrush', 'canada', 'whirlpool', 'daisy', 'banana', 
                'thunderstorm', 'giraffe', 'yogurt', 'earthquake', 'rose', 'lemonade', 'penguin', 'beetle', 'flamingo', 'dinosaur', 
                'yemen', 'bicycle', 'vietnam', 'sunshine', 'unicorn', 'denmark', 'whirlwind', 'holland', 'house', 'elephant', 'kite', 
                'wine', 'volleyball', 'yacht', 'eggplant', 'europe', 'fountain', 'sunflower', 'kangaroo', 'mountain', 'beach', 'eagle', 
                'zebra', 'octopus', 'ninja', 'blueberry', 'blossom', 'koala', 'africa', 'knight', 'yoga', 'jackrabbit', 'ukraine', 
                'helicopter', 'germany', 'rocket', 'peru', 'guitar', 'ballet', 'egypt', 'jazz', 'violin', 'iceberg', 'oasis', 'worth',
                'yeast', 'island', 'ostrich', 'monsoon', 'quicksand', 'australia', 'carousel', 'fish', 'zodiac', 'caterpillar', 'poem',
                'hologram', 'astronaut', 'dandelion', 'moonlight', 'laos', 'butterfly', 'camera', 'gold', 'norway', 'notebook', 'qatar', 
                'vortex', 'fireworks', 'paradise', 'asparagus', 'lighthouse', 'dog', 'kiwi', 'dragonfly', 'quilt', 'leather', 'jigsaw', 
                'harmony', 'naive', 'goat', 'sailboat', 'lullaby', 'brazil', 'parrot', 'hiking', 'tornado', 'pizza', 'russia', 'exes',
                'volcano', 'diamond', 'rainforest', 'octagon', 'lagoon', 'program', 'kenya', 'yarn', 'jamboree', 'ocean', 'sun', 'aid',
                'sandcastle', 'moon', 'gemstone', 'lion', 'whisper', 'cinnamon', 'rainbow', 'oman', 'enigma', 'apple', 'gazelle', 'she',
                'blueprint', 'glitter', 'ice cream', 'atom', 'falcon', 'marathon', 'zephyr', 'dolphin', 'waterfall', 'carrot', 'nor',
                'queen', 'thunderbolt', 'yellow', 'rattlesnake', 'orange', 'glacier', 'emerald', 'japan', 'cupcake', 'mermaid', 'rig',
                'treasure', 'tiger', 'fire', 'watermelon', 'quadrant', 'eclipse', 'theory', 'golf', 'spicy', 'flavor', 'cuisine', 'tourist',
                'explore', 'rhythm', 'genre', 'chord', 'dessert', 'recipe', 'thread', 'premiere', 'prose', 'skiing', 'abstract', 'realism',
                'augment', 'algorithm', 'encryption', 'accessories', 'couture', 'haute', 'literate', 'salmon', 'peach', 'cascade'
            ]
            
            rand_num = random.randrange(0, len(main_words))
            rand_word = main_words[rand_num]

            previous_word = ''
            hint_count = 0
            points = 1

            break_word = list(rand_word)
            random.shuffle(break_word)

            shuffled_word = ""
            for letters in break_word:
                shuffled_word += letters

            while shuffled_word == rand_word:
                current_word = list(shuffled_word)
                random.shuffle(current_word)
                shuffled_word = ''.join(current_word)

            def reshuffle_btn():
                nonlocal rand_word
                original_word = word.cget("text")
                shuffled_word = original_word
                while shuffled_word == original_word or shuffled_word == rand_word:
                    current_word = list(original_word)
                    random.shuffle(current_word)
                    shuffled_word = ''.join(current_word)
                word.config(text=shuffled_word)

            def check():
                nonlocal points, rand_word, hint_count, score, rand_num, shuffled_word
                user_word = get_input.get().lower()
                if user_word == rand_word:
                    points += 5
                    score.config(text="Score: " + str(points))
                    random_message = random.choice(["Great job!", "Well done!", "Awesome!", "Excellent!", "Fantastic!", "Amazing work!", "Keep it up!", "Yummy!", "Fresh!"])
                    messagebox.showinfo('Correct ✅', random_message)
                    rand_num = random.randrange(0, len(main_words))
                    rand_word = main_words[rand_num]
                    break_word = list(rand_word)
                    random.shuffle(break_word)
                    shuffled_word = ""
                    for letters in break_word:
                        shuffled_word += letters
                    word.configure(text=shuffled_word)
                    get_input.delete(0, END)
                    hint_count = 0
                    hint_label.config(text="HINT ▶")
                elif not get_input.get():
                    messagebox.showerror('Error', 'Empty Word')
                    get_input.delete(0, END)
                else:
                    if points < 2:
                        show_message("Game Will End if Score Is Below ZERO!")
                    if points < 1:
                        messagebox.showerror('Exit', 'Game Over - Better Luck Next Time')
                        window.destroy()
                        start_page()
                    else:
                        messagebox.showerror('Error', 'Incorrect Answer')
                        get_input.delete(0, END)
                        points -= 1
                        score.config(text=f"Score: {str(points)}")

            def show_hint(word, count):
                nonlocal hint_count, points
                hint_count = count

                word_length = len(word)

                if hint_count >= word_length:
                    show_message("Max hint word!", color='blue')

                if count < word_length:
                    for answer in main_words:
                        if len(answer) == word_length and all(letter in answer for letter in word):
                            if points < 1:
                                show_message("Not enough points!")
                            else:
                                hint_label.config(text=f"{hint_label['text']} {answer[hint_count].upper()}")
                                hint_count += 1
                                points -= 1
                            score.config(text=f"Score: {str(points)}")
                            break

            def show_message(message, color='#faf202'):
                message_label.config(text=message, fg=color)
                window.after(3000, lambda: message_label.config(text=""))
            
            def skip_word():
                nonlocal rand_num, points, score, previous_word, rand_word
                previous_word = rand_word
                response = messagebox.askyesno('Warning', 'You will lose 4 points. Do you wish to proceed?')
                if response:
                    if points < 5:
                        show_message("Not enough points!")
                        return
                    points -= 4
                    score.config(text=f"Score: {str(points)}")
                    rand_num = random.randrange(0, len(main_words))
                    rand_word = main_words[rand_num]
                    break_word = list(rand_word)
                    random.shuffle(break_word)
                    shuffled_word = ""
                    for letters in break_word:
                        shuffled_word += letters
                    word.configure(text=shuffled_word)
                    get_input.delete(0, END)
                    hint_label.config(text="HINT ▶")
                    show_message(f"Previous Answer: {previous_word.upper()}")

            def back_button():
                window.destroy()
                start_page()

            nav_label = Frame(window, bg="#040402")
            nav_label.pack(fill='x')

            back_btn = Button(nav_label, image=img1, bg="#040402", border=0, justify='center', command=back_button, relief=FLAT)
            back_btn.pack(side=LEFT, padx=(10, 85))
                
            score = Label(nav_label, text=f"Score: {str(points)}", pady=10, bg="#040402", fg="#decac0", font="Titillium 13 bold")
            score.pack(side=LEFT, padx=(85, 10))

            word = Label(window, text=shuffled_word, pady=10, bg="#040402", fg="#decac0", font="Titillium 35 bold")
            word.pack()

            message_label = Label(window, text="", bg="#040402", font="Titillium 13 bold")
            message_label.pack()

            get_input = Entry(window, font="none 26 bold", bg="#decac0", bd=10, justify='center')
            get_input.pack()

            hint_label = Label(window, text="HINT ▶", pady=10, bg="#040402", fg="#decac0", font="Titillium 13 bold")
            hint_label.pack()

            button_frame = Frame(window, bg="#040402")  # Create a frame to hold the buttons
            button_frame.pack(pady=20)  # Pack the frame with some padding

            shuffle = Button(button_frame, text="🔀 Shuffle", width=14, bd=4, font=("", 13), bg="#ad8d76", command=reshuffle_btn)
            shuffle.grid(row=0, column=0, padx=10, pady=10)  # Pack the shuffle button to the left with padding

            submit = Button(button_frame, text="✅ Submit", width=14, bd=4, font=("", 13), bg="#ad8d76", command=check)
            submit.grid(row=0, column=1, padx=10, pady=10)  # Pack the submit button to the right with padding
            window.bind('<Return>', lambda event=None: submit.invoke())

            hint = Button(button_frame, text="ℹ️ Hint", width=14, bd=4, font=("", 13), bg="#ad8d76", command= lambda: show_hint(word.cget("text"), hint_count))
            hint.grid(row=1, column=0, padx=10, pady=10)  # Pack the hint button at the top with padding

            skip = Button(button_frame, text="⏩ Skip", width=14, bd=4, font=("", 13), bg="#ad8d76", command=skip_word)
            skip.grid(row=1, column=1, padx=10, pady=10)  # Pack the skip button at the top with padding

            window.mainloop()

        def show_game():
            main_window.destroy()
            main_game()

        main_window = Tk()
        main_window.geometry("500x500+500+100")
        main_window.resizable(0, 0)
        main_window.title("Word Game")
        main_window.configure(background="#040402")
        main_window.iconbitmap(r'wordicon.ico')

        img0 = PhotoImage(file="wordgame.png")

        image_label = Label(main_window, image=img0, bg="#040402")
        image_label.pack(pady=(50, 0))

        creator_label = Frame(main_window, bg="#040402")
        creator_label.pack()
        
        madeby_label = Label(creator_label, text="made by", pady=10, bg="#040402", fg="#decac0", font="dubai 13 bold")
        madeby_label.pack(side=LEFT)

        names_label = Label(creator_label, text="FHFJ Squad", pady=10, bg="#040402", fg="#decac0", font="Ravie 13 bold")
        names_label.pack(side=LEFT)

        start_btn = Button(main_window, text="Start", width=14, bd=4, bg="#ad8d76", font=("", 10, 'bold',), cursor="hand2", command=show_game)
        start_btn.pack(pady=(35, 10))

        exit_btn = Button(main_window, text="Exit", width=14, bd=4, bg="#ad8d76", font=("", 10, 'bold',), cursor="hand2", command=lambda: main_window.destroy() if messagebox.askyesno('Exit', 'Are you sure you want to exit?') else None)
        exit_btn.pack(pady=(10))

        main_window.mainloop()

    start_page()
if __name__ == "__main__":
    main()
