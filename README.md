# Simple Chatbot Discord dengan Groq AI

Bot Discord ini adalah asisten pribadi berbasis AI yang mampu memproses teks dan gambar. Bot ini menggunakan Groq API untuk mendukung interaksi yang cerdas dan fleksibel dengan pengguna. Selain itu, bot mendukung bahasa Indonesia, membuatnya relevan bagi komunitas lokal.

## Fitur

- Kemampuan chat dengan AI menggunakan model dari Groq API
- Analisis gambar dengan pertanyaan kustom
- Mendukung bahasa Indonesia
- Respon real-time dengan indikator pengetikan

## Perintah Bot

1. `!ask [pertanyaan]`
   - Dapat digunakan untuk bertanya tentang apa saja
   - Bisa analisa sebuah teks panjang
   - Contoh: 
   
        `!ask Buatkan saya program membuat segitiga di python`

2. `!analyze [pertanyaan opsional]`
   - Khusus untuk menganalisis gambar
   - Pertanyaan bersifat opsional
   - Contoh: 

        `!analyze Berapa orang yang ada di gambar ini?`

        `!analyze`

## Cara Kerja

### Komponen Utama
1. **Groq API Integration**
   - Menggunakan model `llama-3.2-90b-vision-preview` (bisa menggunakan model lainnya)
   - Mendukung input teks dan gambar
   - Memberikan respons yang kontekstual

2. **Discord Bot**
   - Menggunakan discord.py
   - Memanfaatkan sistem commands
   - Mendukung pengiriman gambar

### Fungsi Utama

1. `analyze_image()`
   - Memproses URL gambar
   - Menerima pertanyaan kustom
   - Mengembalikan analisis dari Groq AI

2. `send_message_to_discord()`
   - Memproses pesan teks
   - Menggunakan persona AI yang telah ditentukan
   - Memberikan respons yang personal

## Konfigurasi

Diperlukan file `.env` yang berisi:
```
GROQ_API_KEY=your_groq_api_key 
DISCORD_TOKEN=your_discord_token
```

## Instalasi

1. Clone Repository ini
2. Install dependencies :
    ```bash
    pip install -r requirements.txt
    ```
3. Buat file `.env`
4. jalankan bot dengan cara:
    ```bash
    python app.py
    ```
    atau
    ```bash
    python3 app.py
    ```


## Tambahan

1. Anda bisa mengganti **system prompt** sesuai dengan keinginan masing-masing, dengan cara:
    ```python
    async def send_message_to_discord(message_content):
        chat_completion = groq.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "<Ubah sesuai dengan preferensi>",
                },
                {
                    "role": "user",
                    "content": message_content,
                }
            ],
            model="llama-3.2-90b-vision-preview", # bisa di ubah sesuai dengan model yang diinginkan.
        )
        
        return chat_completion.choices[0].message.content
    ```

    Anda bisa mengganti pada bagian `content` di `"role" : "system"` sesuai dengan keinginan mu.
    Sebagai contoh **system prompt** saya adalah:
    ```txt
    You are Mira, my super cool personal assistant, always ready to help and can speak Indonesian. You have extensive knowledge about machine learning, but you can also have casual conversations about anything.
    ```