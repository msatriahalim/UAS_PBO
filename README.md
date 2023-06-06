# TUGAS UAS MATA KULIAH PEMROGRAMAN BERBASIS OBJEK

Anggota Kelompok:
- G1A020036 - Fadhilla Ilham Robbani
- G1A022028 - Damianus Christopher Samosir 
- G1A022080 - M Satria Halim

## Penjelasan Source Code


```py
import random # Mengimpor standard library random untuk membantu membuat random choice

class Hangman: # Membuat kelas Hangman
    def __init__(self):
        self.word_list = ["python", "hangman", "pohon", "programming", "gitar", "kertas"]  # Daftar kata yang mungkin
        self.chosen_word = random.choice(self.word_list)  # Memilih kata secara acak dari word_list
        self.guessed_letters = []  # Daftar huruf yang sudah ditebak
        self.tries = 6  # Jumlah kesempatan yang tersedia
```
Kode program di atas adalah implementasi permainan "Hangman" dalam Python. Pada baris pertama, kami mengimpor pustaka standar random. Pustaka ini akan digunakan untuk membantu dalam memilih kata secara acak. Kemudian, kami mendefinisikan sebuah kelas bernama Hangman. Kelas ini akan merepresentasikan permainan Hangman dan menyimpan semua variabel dan metode yang diperlukan. Di dalam kelas Hangman, kami memiliki metode __init__. Metode ini merupakan konstruktor yang akan dijalankan saat sebuah objek dari kelas `Hangman` dibuat. Pada metode __init__, terdapat atribut word_list yang merupakan sebuah daftar (list) yang berisi beberapa kata yang mungkin akan digunakan dalam permainan. Kata-kata ini telah ditentukan terlebih dahulu dalam kode. Untuk memilih kata secara acak dari daftar word_list menggunakan fungsi random.choice. Kata yang dipilih akan disimpan dalam atribut `chosen_word`. Lalu setelah itu, kami membuat atribut guessed_letters yang merupakan sebuah daftar kosong. Di sinilah kami akan menyimpan huruf-huruf yang sudah ditebak oleh pemain. Kemudian yang terakhir, kami membuat atribut tries yang merupakan sebuah angka. Atribut ini akan menyimpan jumlah kesempatan yang tersisa bagi pemain untuk menebak kata. Dalam kode ini, kami memberi pemain 6 kesempatan. Setiap kali pemain menebak salah, nilai atribut tries akan dikurangi satu. Jika pemain gagal menebak kata dalam enam kesempatan, pemain kalah.



```py   
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
```

 Kode di atas adalah implementasi dari fungsi `play()` dalam kelas `Hangman`. Fungsi ini bertanggung jawab untuk menjalankan permainan Hangman dengan mengatur jalannya permainan, berinteraksi dengan pemain, dan memberikan umpan balik setelah setiap tebakan. Pada baris pertama, kami mendefinisikan fungsi `play()` dengan menggunakan sintaks `def play(self):`. Ini mengindikasikan bahwa fungsi `play()` adalah metode dari kelas `Hangman`, dan parameter `self` mengacu pada objek saat ini yang sedang menggunakan metode tersebut. 
Selanjutnya, kami menggunakan pernyataan while self.tries > 0: untuk membuat perulangan `while`. Permainan akan berlanjut selama masih ada kesempatan (`self.tries > 0`). Di dalam perulangan `while`, kami menginisialisasi variabel `word_status` sebagai string kosong. Variabel ini akan digunakan untuk menyimpan status kata yang sedang ditebak, di mana huruf yang sudah ditebak akan ditampilkan dan huruf yang belum ditebak akan digantikan dengan garis bawah (`_`). 

Selanjutnya, kami menggunakan pernyataan `for letter in self.chosen_word:` untuk iterasi melalui setiap huruf dalam kata yang dipilih. Di dalam loop `for`, kami menggunakan pernyataan `if letter in self.guessed_letters:` untuk memeriksa apakah huruf telah ditebak sebelumnya dan ada dalam daftar `self.guessed_letters`. Jika huruf sudah ditebak, maka kami tambahkan huruf tersebut ke dalam `word_status` dengan menggunakan pernyataan `word_status += letter`. Ini akan menampilkan huruf yang sudah ditebak pada posisi yang sesuai dalam `word_status`. Jika huruf belum ditebak, maka kami tambahkan garis bawah (`_`) ke dalam `word_status` dengan menggunakan pernyataan `word_status += "_"`. Ini menunjukkan huruf yang belum ditebak. 

Setelah selesai iterasi melalui semua huruf dalam kata yang dipilih, kami menggunakan pernyataan `if word_status == self.chosen_word:` untuk memeriksa apakah `word_status` sama dengan kata yang dipilih. Jika benar, berarti pemain telah berhasil menebak seluruh kata. Jika `word_status` sama dengan kata yang dipilih, kode akan mencetak pesan "Congratulations! You guessed the word:" diikuti dengan kata yang benar (`self.chosen_word`) menggunakan pernyataan `print("Congratulations! You guessed the word:", self.chosen_word)`. Kemudian, kami menggunakan pernyataan `break` untuk menghentikan permainan. Jika `word_status` tidak sama dengan kata yang dipilih, artinya pemain belum berhasil menebak seluruh kata, kode akan melanjutkan permainan dengan menampilkan state hangman saat ini menggunakan metode `display_hangman()`.

Selanjutnya, kode mencetak pesan "Guess the word:" diikuti dengan `word_status` yang merupakan status kata yang sedang ditebak saat ini. Pesan ini memberikan petunjuk kepada pemain tentang kata yang harus mereka tebak. Selanjutnya, kode akan mencetak pesan "Tries left:" diikuti dengan jumlah kesempatan yang tersisa (self.tries). Pesan ini memberikan informasi kepada pemain tentang jumlah kesempatan yang masih tersedia. Setelah itu, kode akan meminta pemain memasukkan huruf tebakan menggunakan pernyataan guess = input("Enter a letter: ").lower(). 

Pemain diminta untuk memasukkan satu huruf sebagai tebakan. Fungsi lower() digunakan untuk mengubah huruf menjadi huruf kecil, sehingga pemain dapat memasukkan huruf dalam format apapun (huruf besar atau huruf kecil).

Selanjutnya ada kode yang bertanggung jawab untuk memvalidasi tebakan pemain, memberikan umpan balik terkait tebakan tersebut, dan mengatur jalannya permainan saat pemain melakukan tebakan. Pada baris pertama, kami menggunakan pernyataan `if len(guess) != 1:` untuk memeriksa apakah pemain memasukkan lebih dari satu huruf sebagai tebakan. Jika kondisi ini terpenuhi, artinya pemain memasukkan lebih dari satu huruf, maka akan mencetak pesan kesalahan menggunakan pernyataan `print("Please enter a single letter.")`. Pesan ini memberi tahu pemain bahwa mereka harus memasukkan hanya satu huruf sebagai tebakan. 

Setelah mencetak pesan kesalahan, kode menggunakan pernyataan `continue` untuk melanjutkan iterasi berikutnya dalam perulangan `while`. Pada baris berikutnya, kami menggunakan pernyataan `if guess in self.guessed_letters:` untuk memeriksa apakah huruf tebakan yang dimasukkan oleh pemain sudah pernah ditebak sebelumnya dan ada dalam daftar `self.guessed_letters`. Jika huruf sudah ditebak sebelumnya, maka kode akan mencetak pesan kesalahan menggunakan pernyataan `print("You've already guessed that letter.")`. Pesan ini memberi tahu pemain bahwa mereka sudah menebak huruf tersebut sebelumnya. Setelah mencetak pesan kesalahan, kode menggunakan pernyataan `continue` untuk melanjutkan iterasi berikutnya dalam perulangan `while`. 

Selanjutnya, kami menggunakan pernyataan `if guess not in self.chosen_word:` untuk memeriksa apakah huruf tebakan yang dimasukkan oleh pemain tidak ada dalam kata yang dipilih (`self.chosen_word`). Jika huruf tebakan salah, maka kode akan mencetak pesan "Wrong guess!" menggunakan pernyataan `print("Wrong guess!")`. Pesan ini memberi tahu pemain bahwa huruf tebakan mereka salah. Setelah mencetak pesan, kode mengurangi jumlah kesempatan yang tersisa (`self.tries -= 1`) karena pemain melakukan tebakan yang salah. Pada baris terakhir dalam blok `if`, kami menggunakan pernyataan `self.guessed_letters.append(guess)` untuk menambahkan huruf tebakan (`guess`) ke dalam daftar `self.guessed_letters`. Dengan melakukan ini, huruf tebakan tersebut akan dicatat sebagai huruf yang sudah ditebak

Jika perulangan `while` selesai tanpa pernyataan `break` terpanggil, berarti pemain telah menggunakan semua kesempatan yang tersedia dan tidak berhasil menebak kata yang benar. Pada blok `else` yang terakhir, kode mencetak state hangman terakhir menggunakan metode `display_hangman()` dengan pernyataan `self.display_hangman()`. Selanjutnya, kode mencetak pesan "Game over! The word was" diikuti dengan kata yang benar (`self.chosen_word`) menggunakan pernyataan `print("Game over! The word was", self.chosen_word)`. Pesan ini memberitahu pemain bahwa permainan telah berakhir dan menampilkan kata yang benar yang harus mereka tebak.


```py    
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
```

Kode di atas adalah implementasi dari fungsi `display_hangman()` dalam kelas `Hangman`. Fungsi ini bertanggung jawab untuk menampilkan representasi visual dari state hangman berdasarkan jumlah kesempatan yang tersisa. Pada awalnya, kami mendefinisikan sebuah daftar bernama `hangman_states`. Daftar ini berisi beberapa representasi visual dari state hangman dalam bentuk ASCII art. Setiap elemen dalam daftar adalah string yang mewakili gambar hangman pada setiap state yang berbeda. 

Selanjutnya, kami menggunakan pernyataan `print(hangman_states[6 - self.tries])` untuk mencetak state hangman yang sesuai dengan jumlah kesempatan yang tersisa. Pernyataan ini menggunakan indeks dalam daftar `hangman_states` untuk memilih elemen yang sesuai dengan kesempatan yang tersisa (`6 - self.tries`). Dalam permainan Hangman, terdapat 6 kesempatan yang tersedia sebelum pemain kalah. Jadi, jika `self.tries` memiliki nilai 6, maka indeks yang akan diambil adalah 0 (elemen pertama dalam daftar `hangman_states`). Jika `self.tries` memiliki nilai 5, maka indeks yang diambil adalah 1 (elemen kedua dalam daftar), dan seterusnya. Indeks yang dipilih akan menampilkan representasi visual dari state hangman yang sesuai dengan kesempatan yang tersisa.



```py
game = Hangman() #Mendefinisikan objek Hangman
game.play() # Memanggil method play untuk memulai permainan

```

Kode di atas terdiri dari dua baris yang berfungsi untuk membuat objek dari kelas `Hangman` dan memulai permainan Hangman. Pada baris pertama, kami mendefinisikan variabel `game` dan menginisialisasinya dengan objek dari kelas `Hangman` dengan menggunakan sintaks `Hangman()`. Dengan melakukan ini, kode membuat sebuah objek baru yang merupakan instance dari kelas `Hangman`. Variabel `game` akan mereferensikan objek ini sehingga kita dapat mengakses metode dan atribut dari kelas `Hangman`.

Pada baris kedua, kode memanggil metode `play()` pada objek `game` yang telah dibuat sebelumnya. Metode `play()` adalah salah satu metode yang didefinisikan dalam kelas `Hangman` dan berfungsi untuk memulai jalannya permainan Hangman. Dengan memanggil metode `play()`, permainan Hangman dimulai dan logika permainan dijalankan.
Dengan demikian, dengan dua baris kode tersebut, kami membuat objek `game` dari kelas `Hangman` dan memulai permainan Hangman dengan memanggil metode `play()`. Permainan akan berjalan sesuai dengan logika yang telah diimplementasikan dalam kelas `Hangman`, termasuk pemilihan kata secara acak, interaksi dengan pemain, dan pengecekan tebakan pemain hingga pemain berhasil menebak kata atau kesempatan habis.
