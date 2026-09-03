# Portfolio — Nur Zaitul Akmal binti Romli

Portfolio interaktif satu fail. Tiada build step, tiada `npm install`.

```
portfolio-v2/
├── index.html   ← semua di sini (HTML + CSS + JS)
├── favicon.ico  ← ikon 64px (browser minta /favicon.ico untuk resume.pdf)
├── app-ads.txt  ← verifikasi AdMob — JANGAN buang
├── resume.pdf   ← disalin dari NurZaitulAkmal_Resume.pdf
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

## Belum dimasukkan

- `isnetportal` — repo di bawah akaun orang lain (`hazree82`), peranan tidak dapat
  disahkan dari kod.
- `telegram_ucapan` — repo Wariscan, README masih templat Flutter kosong.
- Repo EZCare — dikecualikan atas permintaan.
