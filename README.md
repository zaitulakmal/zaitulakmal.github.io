# Portfolio — Nur Zaitul Akmal binti Romli

Portfolio interaktif satu fail. Tiada build step, tiada `npm install`.

```
portfolio-v2/
├── index.html   ← semua di sini (HTML + CSS + JS)
├── favicon.ico  ← ikon 64px (browser minta /favicon.ico untuk resume.pdf)
├── app-ads.txt  ← verifikasi AdMob — JANGAN buang
├── resume.pdf   ← disalin dari NurZaitulAkmal_Resume.pdf
├── shots/       ← 14 screenshot app sebenar (WebP, 184 KB semua)
└── README.md
```

## Buka secara lokal

```bash
open index.html
```

Atau layan melalui HTTP (disyorkan supaya font Google dimuat sama seperti di produksi):

```bash
cd ~/portfolio-v2 && python3 -m http.server 8080
# http://localhost:8080
```

## Deploy

**GitHub Pages**

```bash
cd ~/portfolio-v2
git init && git add . && git commit -m "portfolio"
gh repo create zaitulakmal.github.io --public --source=. --push
```

Laman terbit di `https://zaitulakmal.github.io`. (Kalau nama repo lain, ia jadi
`https://zaitulakmal.github.io/<nama-repo>/`.)

**Netlify / Vercel** — seret folder ini ke dashboard. Tiada konfigurasi diperlukan.

**Firebase Hosting** — `firebase init hosting`, set public directory kepada `.`,
jawab "No" untuk single-page app rewrite.

## Apa yang interaktif

| Ciri | Nota |
|---|---|
| Medan partikel | Canvas, titik berpaut, menolak jauh dari cursor, jeda bila tab tersembunyi |
| Cursor tersuai | Titik + cincin yang mengekori dengan lerp, membesar atas elemen boleh klik |
| Nama hero | Scramble karakter semasa muat; hover untuk ulang |
| Taip berputar | Senarai peranan menaip sendiri, ikut bahasa aktif |
| Kad projek | Tilt 3D + spotlight ikut posisi cursor |
| Penapis | 9 kategori, kiraan langsung, kad masuk berperingkat |
| Modal kajian kes | Bullet penuh, statistik, pautan; navigasi `←` `→`, tutup `Esc` |
| Command palette | `⌘K` / `Ctrl+K` — cari ikut nama, teknologi, kategori atau organisasi |
| Dwibahasa | Togol EN / MY, disimpan dalam `localStorage` |
| Garis masa | Garis mengisi mengikut scroll, titik menyala bila masuk viewport |
| Kiraan statistik | Nombor naik bila seksyen masuk viewport |
| Butang magnetik | CTA tertarik sedikit ke arah cursor |
| Mod arked | Konami code (`↑↑↓↓←→←→BA`) menukar keseluruhan palet ke cyan |
| Reduced motion | Semua animasi dimatikan kalau OS minta |

## Menyunting kandungan

Semua data ada dalam satu blok `<script>` di bahagian bawah `index.html`:

- `PROJECTS` — senarai projek. Setiap entri ada `blurb`, `detail`, `stats`, `links`,
  dan medan dwibahasa dalam bentuk `{en: "...", ms: "..."}`.
- `JOBS` — pengalaman kerja.
- `SKILLS`, `CERTS`, `FILTERS` — kotak alat, sijil, kategori penapis.
- `T` — semua teks UI untuk kedua-dua bahasa.

Tambah projek = tambah satu objek dalam `PROJECTS`. Penapis, kiraan statistik dan
command palette semuanya terbit sendiri daripada data itu.

## Nota

- Kandungan diambil daripada dua resume PDF dan repo sebenar dalam mesin ini
  (Unity scene/script dikira terus dari `Documents/GitHub/`). LinkedIn tidak
  di-scrape — ia menyekat capaian automatik.
- Warna aksen dikawal oleh token `--hot` / `--hot-rgb`. Jangan letak `filter` pada
  `body` — ia menjadikan `body` containing block untuk semua elemen
  `position:fixed`, yang merosakkan modal, canvas, cursor dan command palette.
- Foto profil belum dimasukkan. Kalau nak, letak fail dalam folder ini dan rujuk
  dari seksyen hero.

## Skop projek

Laman ini memaparkan **12 projek** pilihan:

BioWare · Slimora · EduBuddy · TM Morse Code Challenge · iGnite · EchoLens ·
EchoDots · Lensa Kenduri · Gold Purity Analyzer · ORAVIU · DAWar System ·
Zakat Distribution App

EchoDots = repo `telegram_ucapan`. README repo itu masih templat Flutter kosong,
jadi butiran kajian kes diambil terus dari kod: 13 aset poskad, 6 saluran
WebSocket dalam `message_page.dart`, gateway Node-RED (`nodeRedIp/Port/Path`
dalam `settings_page.dart`), auto-reconnect 5 saat dalam `websocket_service.dart`,
dan `language_provider.dart` untuk ms-MY / en-US.

Nota: `lib/main.dart` tidak set `debugShowCheckedModeBanner: false`, jadi reben
DEBUG merah muncul dalam screenshot. Satu baris dalam `MaterialApp` akan
menghilangkannya untuk kiosk.

Projek lain yang ada dalam mesin tetapi tidak dipaparkan (Slimora, TM Morse
Challenge, IR Academy, DGAS, CutePet, Hot Wheels Racer, Cute Obby, Cat Cafe,
Background Check System, Ilham Integrasi, UM Bookstore, kad jemputan) masih
boleh ditambah semula — salin semula objeknya ke dalam `PROJECTS`.

## Screenshot app

`shots/` ada screenshot sebenar, bukan mockup. Dua orientasi:

**Potret (bingkai telefon)** — medan `shots:[...]`

| App | Sumber | Bilangan |
|---|---|---|
| Slimora | Simulator iPhone 17 Pro | 6 |
| EduBuddy | Simulator iPhone 17 Pro | 6 |
| iGnite | zaitulakmal.github.io/Ignite via laluan bernama | 8 |
| ORAVIU | zaitulakmal.github.io/oralvis-app — element screenshot setiap .phone | 8 |
| Lensa Kenduri | lensa-kenduri.web.app + 3 screenshot telefon sebenar | 6 |


**Landskap (bingkai browser)** — medan `wides:[...]`

iGnite ditangkap dengan deep-link ke laluan dalam `lib/demo_routes.dart`
(`#/home`, `#/device-connected`, `#/treatment`, `#/setup`, `#/session`,
`#/complete`, `#/history`, `#/profile`). Klik dan taip tidak berfungsi pada
Flutter CanvasKit dalam browser tanpa kepala, tetapi hash route berfungsi —
itu cara paling boleh dipercayai untuk menangkap setiap skrin.

Projek boleh set `frame:'photo'` untuk guna rangka foto penuh (tanpa chrome
browser) dan `media:{en,ms}` untuk menamakan jenis media pada lencana — EchoLens
guna kedua-duanya supaya lencananya berbunyi "1 photo", bukan "1 screens".

| Projek | Sumber | Bilangan |
|---|---|---|
| Gold Purity Analyzer | gold-purity-analyzer.netlify.app @1280x800 | 6 |
| BioWare | virtourism.com.my/um/BioWare (Unity WebGL) | 5 |
| EchoDots | Screenshot kiosk Telegram Ucapan (chrome browser dipotong) | 5 |
| EchoLens | Foto pemasangan sebenar di Muzium Telegraf Taiping | 1 |
| TM Morse | tm-morse-challenge.web.app + 3 skrin log masuk sebenar | 7 |
| DAWar | Prototaip Figma (chrome browser dipotong) | 6 |

BioWare: 5 skrin — pilih watak, latihan menembak (kuiz), taklimat Captain Matt,
menu utama, panel Setting.

Kunci untuk masuk gameplay: butang START menu ada pada canvas-relative
**y 0.577**, dan butang START dalam taklimat pada **(0.402, 0.869)** — tetapi
hanya selepas teks taip Captain Matt habis, iaitu **~50 saat** selepas watak
dipilih. Klik lebih awal tiada kesan kerana butang belum wujud.

Skrin kuiz adalah statik dan klik pada sasaran jawapan tidak mendaftar, jadi
soalan kedua dan skrin skor tidak dapat ditangkap secara automatik. Setiap
larian memuat turun 250 MB data Unity.

TM Morse: 4 skrin ditangkap sendiri (pilih peranan, kod pasukan, passcode admin,
papan besar Swiss League) — Student dan Admin berpagar kelayakan sebenar, jadi
3 skrin dalaman (Admin Main Control, Round 1 Audio Decryption, Awards) datang
daripada screenshot log masuk yang dihantar pengguna, dipotong bebas chrome.

Gold Purity Analyzer ditangkap pada **1280x800, bukan lebar telefon** — footernya
tertulis "Mini-PC Professional Edition" dan susun atur bertindih teruk di bawah
500px. Ia app desktop.

Semua imej diubah saiz (860px potret / 900px landskap) dan ditukar ke WebP q76-78.
Banner iklan "Test mode" AdMob dipotong dari screenshot fasting Slimora.

Nak tambah: letak fail dalam `shots/`, kemudian tambah ke `shots:[...]` (potret)
atau `wides:[...]` (landskap). Kad potret ambil 3 yang pertama untuk telefon
bertindih; kad landskap ambil yang pertama untuk tingkap browser; modal papar semua.

## Nota privasi

Dua sumber sengaja tidak digunakan:

- **Album Lensa Kenduri** — halaman `/album` memaparkan gambar tetamu sebenar
  dengan wajah yang boleh dikenali. Ia tidak digunakan; enam skrin lain
  (kamera, pratonton, terima kasih, welcome, host, kad QR) digunakan.

  Skrin kamera perlu tangkapan telefon sebenar — Chrome tanpa kamera render
  corak ujian hijau yang nampak seperti pepijat.
- **DAWar shot 4** — memaparkan foto calon sebenar.

Screenshot DAWar juga dipotong untuk membuang chrome browser, kerana bar tab
mendedahkan tab lain yang terbuka.

## Pautan luar

Hanya destinasi **public** dipautkan. Repo ini private, jadi pautannya dibuang
supaya pelawat tidak dapat 404:

- `zaitulakmal/Atul-BioWare` (BioWare)
- `zaitulakmal/lensa-kenduri` (Lensa Kenduri — pautan laman langsung dikekalkan)

Kalau repo itu ditukar public, pautan boleh dipasang semula dalam `links:[]`
projek berkenaan.
