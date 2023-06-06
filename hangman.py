import random # Mengimpor standard library random untuk membantu membuat random choice

class Hangman: # Membuat kelas Hangman
    def __init__(self):
        self.word_list = ["python", "hangman", "pohon", "programming", "gitar", "kertas"]  # Daftar kata yang mungkin
        self.chosen_word = random.choice(self.word_list)  # Memilih kata secara acak dari word_list
        self.guessed_letters = []  # Daftar huruf yang sudah ditebak
        self.tries = 6  # Jumlah kesempatan yang tersedia

    def play(self): # Membuat fungsi play
        while self.tries > 0:  # Selama masih ada kesempatan
            word_status = ""  # Variabel word_status untuk menyimpan status kata yang sedang ditebak
            for letter in self.chosen_word:
                if letter in self.guessed_letters:  # Jika huruf sudah ditebak
                    word_status += letter  # Tambahkan huruf ke status kata atau variabel word_status
                else:
                    word_status += "_"  # Tambahkan garis bawah untuk huruf yang belum ditebak

            if word_status == self.chosen_word:  # Jika status kata sama dengan kata yang dipilih
                print("Congratulations! You guessed the word:", self.chosen_word)  # Tampilkan pesan berhasil menebak
                break  # Hentikan permainan

            self.display_hangman()  # Tampilkan state hangman
            print("Guess the word:", word_status)  # Tampilkan status kata yang sedang ditebak
            print("Tries left:", self.tries)  # Tampilkan jumlah kesempatan yang tersisa

            guess = input("Enter a letter: ").lower()  # Minta pemain memasukkan huruf tebakan

            if len(guess) != 1:  # Jika pemain memasukkan lebih dari satu huruf
                print("Please enter a single letter.")  # Tampilkan pesan kesalahan
                continue  # Lanjut ke iterasi berikutnya

            if guess in self.guessed_letters:  # Jika huruf sudah ditebak sebelumnya
                print("You've already guessed that letter.")  # Tampilkan pesan kesalahan
                continue  # Lanjut ke iterasi berikutnya

            if guess not in self.chosen_word:  # Jika huruf tidak ada dalam kata yang dipilih
                print("Wrong guess!")  # Tampilkan pesan bahwa tebakan salah
                self.tries -= 1  # Kurangi jumlah kesempatan

            self.guessed_letters.append(guess)  # Tambahkan huruf tebakan ke daftar huruf yang sudah ditebak

        else:  # Jika loop while selesai tanpa break
            self.display_hangman()  # Tampilkan state hangman terakhir
            print("Game over! The word was", self.chosen_word)  # Tampilkan pesan bahwa permainan berakhir dan kata yang benar

    def display_hangman(self):
        hangman_states = [  # Daftar state hangman dalam bentuk ASCII art
            """
               _______
              |/      |
              |      
              |      
              |       
              |      
              |
             _|_
            |   |______
            |          |
            |__________|
            """,
            """
               _______
              |/      |
              |      (_)
              |      
              |       
              |      
              |
             _|_
            |   |______
            |          |
            |__________|
            """,
            """
               _______
              |/      |
              |      (_)
              |       |
              |       |
              |       
              |
             _|_
            |   |______
            |          |
            |__________|
            """,
            """
               _______
              |/      |
              |      (_)
              |      \\|
              |       |
              |       
              |
             _|_
            |   |______
            |          |
            |__________|
            """,
            """
               _______
              |/      |
              |      (_)
              |      \\|/
              |       |
              |       
              |
             _|_
            |   |______
            |          |
            |__________|
            """,
            """
               _______
              |/      |
              |      (_)
              |      \\|/
              |       |
              |      / 
              |
             _|_
            |   |______
            |          |
            |__________|
            """,
            """
               _______
              |/      |
              |      (_)
              |      \\|/
              |       |
              |      / \\
              |
             _|_
            |   |______
            |          |
            |__________|
            """
        ]

        print(hangman_states[6 -  self.tries]) # Mencetak state dari kode ASCII Hangman sesuai dengan kesempatan yang tersisa

game = Hangman() #Mendefinisikan objek Hangman
game.play() # Memanggil method play untuk memulai permainan
