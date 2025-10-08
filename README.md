project di pws: https://muhammad-fadhil43-fajarwearshop.pbp.cs.ui.ac.id/


Tugas 2:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= tahap awal yang saya lakukan adalah dimulai dari tutorial 0, yaitu dengan instalasi Django dan inisiasi Django, karena ini perlu dikarenakan dalam proyek ini saya memakai Django, dengan menggunakan python -m venv env lalu env\Scripts\activate, dan jangan lupa untuk membuat file txt bernama requirements.txt dengan ada beberapa isi nya seperti di tutorial, dan tidak lupa untuk setting databse name, host, port, user, password, schema, dan productionnya, di tutorial 0 ini saya agak sedikit kesulitan di pws nya karena nama dari repository saya ada huruf besarnya. Setelah saya membuat sebuah proyek Django yang baru untuk tugas kali ini, saya lanjut ke Membuat aplikasi dengan nama main pada proyek tersebut dengan cara jalanin perintah python manage.py startapp main, ini bakalan ngebentuk folder baru bernama main di folder proyek tadi. Dan juga tidak lupa menaruh main itu di installed Apps yang ada di settings.py, karena settings.py ini bisa dikatakan pusat semua konfigurasinya ada disini. Dan juga membuat template untuk proyek saya dengan tipe file html, dan mengubah models.py, disini untuk kategorinya di proyek saya ada futsal shoes, footbal shoes, dan socks, karena FajarWearShop rencanannya sebagai toko menjual sepatu untuk olahraga bola kaki. Kemudian yang diperlukan di models.py adalah nama, harga, deskripsi, kategori, thumbnail, sold_count, is_feature, dan di models.py ini saya punya fungsi yaitu def __str_(self), yang dimana untuk mengembalikan nama saya, dan def ifbesstsller, jika kategori produk itu terjual lebih dari 50 kali dia termasuk produk yang bestseller, dan def yang terakhir adalah increment_sales(self), untuk ketika ada pembelian, hitung jumlah terjual produk tersebut. Kemudia di makemigration dan di migrate karena saya telah mengubah file models.py ini bersifat wajib setiap kali ada perubahan. Kemudian saya melakukan routing di urls.py untuk mengirim informasi permintaan web server dari client, dan saya tidak melakukan Django test karena belum perlu pada saat kali ini, kemudia saya melakukan commit dan push semua pekerjaan saya ke daalam repository github saya.s

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
= ![jawaban](no2.jpg)

3. Jelaskan peran settings.py dalam proyek Django!
= di dalam proyek Django, setting.py berperan sebagai wadah konfigurasi semua pengaturan atau set up setup pada aplikasi kita, jadi pas proyek Django dijalanin pakai env, Django bakalan membaca file settings.py itu seperti alur aplikasinya gimana. Dan juga settings.py ini bisa dikatakan sebagai otak nya Django, karena kalau mau ubah apapun, harus ada perubahan pada file settings.py ini.

4. Bagaimana cara kerja migrasi database di Django?
= migrasi database di Django seperti memori atau stack, jadi semisal kita merubah file models.py dia akan mencatat dan setelah kita merubah atau memodifikasi file models.py kita diwajibkan untuk menjalankan make migration dan juga migrate, jika tidak dijalankan perubahan yang dibuat di models.py tidak akan dikirim ke databasenya.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
= menurut saya karena di Django kita sudah langsung dapat banyak template dan framework-framework lainnya, yang dimana ini memudahkan saya dan yang lain untuk belajar platform melali Django, dan juga Django mempunyai dokumentasi yang lengkap dan jelas sehingga memudahkan saya untuk belajar dan terus memahami jikalau saya bingung saya bukak Django documentation di Chrome.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
= feedback untuk asdos tutorial 1 cukup baik di discord ketika ada yang menanyakan langsung dijawab oleh asdos asdos, keren asdosnyaa.....

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tugas 3:
 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 = karena kita memerlukan data delivery dalam pemngimplementasian sebuah platform karena data itu merupakan inti dari setiap proses yang terjadi di dalamnya. Jika transformasi datanya baik maka nantinya code code dan program kita akan berjalan lancar dikarenkan data-data yang kita udah buat terkirim dengan baik dan tidak ada error di dalamnya, sebaliknya jika data datanya tidak terdelivery dengan baik, maka request requestnya akan tidak terpenuhi dan akan menyebabkan error pada proyek kita.

 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
 =  yang lebih baik menurut saya adalah JSON, dikarenakan strukturnya yang lebih ringkas, mudah dibaca, dan cepat diproses oleh komputer. JSON cukup pakai kurung kurawal atau kurung siku sehingga lebih singkat dan tidak boros. JSON juga menurut saya lebih cepat diproses komputer dan langsung didukung oleh JavaScript, jadi lebih praktis dipakai di web maupun aplikasi. Karena ringan dan mudah diintegrasikan dengan berbagai bahasa pemrograman, JSON jadi pilihan utama untuk API modern. Sementara XML masih dipakai di beberapa sistem lama atau kebutuhan khusus, untuk aplikasi masa kini JSON jauh lebih efisien dan nyaman digunakan.


 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 = setau saya, di Django, is_valid() dipakai untuk ngecek apakah data yang terkirim lewat form itu sudah sesuai aturan yang kita tentukan di form atau model. Nantinya, jika hasil booelannya true, maka data-data tersebut itu itu valid, sebaliknya jika hasil dari booelannya itu false, maka nanti Django bakalan nyiapin pesan error biar bisa ditampilin ke user, jadi kita butuh is_valid() supaya data yang masuk ke sistem tetap aman, rapi, dan sesuai aturan, jadi nggak asal masuk ke databsenya, istilah lainnya agar tidak ada data yang salah masuk ke database.

 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 = kita butuh csrf_token di form Django supaya aplikasi tetap aman dari serangan yang namanya CSRF(Cross-Site Request Forgery). Kalau dari form ini tidak pakai csrf_token, orang jahat bisa bikin form palsu di website lain. Misalnya kita lagi login aplikasi, lalu tanpa sadar klik link atau isi form di situs jebakan. karena engga ada perlindungan, server menganggap itu, sebagai request, padahal isinya berbahaya, nah makanya ada yang namanya phising.

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 = cara saya untuk mengimplementasikan checklistnya ialah yang pertama pertama memang mengikuti tutorial, tetapi sembari mengikuti tutorial itu, saya mempelajari perlakuan perlakuan dari code code proyek saya, saya mengikuti pada tutorial 2, dengan mengubah bagian bagian dari yang namanya news menjadi products yang diamana jika tidak diganti code oodenya tidak bakalan tersambung. Dan juga tidak lupa untuk membuat direktori baru bernaman templates, yang dimana templates ini akan diisin dengan file html yang akan menampilkan Create_product sama product_detail. Dan juga mengubah bagian fields sesuai dengan di models, serta menggunakan xml dan json, dan mengecek apakah data nya terkirim dengan baik di postman, kurang lebih begitu saya dalam mengerjakan tugas 3 kali ini, lumayan ada error nya sedikit dikarenakan lumayan banyak kesalahan penamaan yang tidak sesuai dan menyebabkan error pada proyek saya, tapi overall aman, so far so good.

 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
= sangat baik sejauh ini, saya bertanya dan kakak kakak asdos menjawab dengan sangat baik dan ramah, good job untuk asdos dan tim dosen semangatt.

  - Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
  ![Show_Xml](ShowXml.jpg)
  ![Show_Jason](ShowJason.jpg)
  ![Show_Xml_by_Id](ShowXmlbyId.jpg)
  ![Show_Jason_by_Id](ShowJasonbyId.jpg)

  
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tugas 4:
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
= Django AuthenticationForm adalah form bawaan yang digunakan untuk proses login user atau pengguna. form ini secara otomatis memvalidasi data yang dimasukkan oleh user, seperti mencocokkan username dan password dengan data yang tersimpan di dalam database sekaligus memastikan akun itu masih aktif atau tidak. Untuk kelebihan dari Authentication form ini sendiri adalah kemudahannya karena langsung tersedia tanpa perlu membuat form baru dari awal, keamanannya sudah terjamin oleh Django karena validasi password dilakukan dengan aman, serta sudah terintegrasi dengan sistem autentikasi Django sehingga bisa langsung digunakan untuk login session. Untuk kekurangannya Django Autehntication ini masih kurang fleksibel jika ingin mengubah cara login, misalnya email sama password, nah itu jika kita ingin mengubahnya harus disesusaikan dengan desain web agar match satu sama lain.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
= Autentikasi adalah proses untuk memastikan identitas seorang pengguna, misalnya dengan meminta email dan password, kalo bener valid, berarti login sukses. Kalau Otorisasi adalah proses untuk menentukan apa saja yang boleh dilakukan oleh user atau pengguna setelah berhasil diautentikasi. Contohnya, ada user atau pengguna yang hanya boleh melihat, tetapi tidak boleh mengedit ataupun menghapus, seperti di google docs. Dalam Django, proses autentikasi diatur oleh authentication system yang ada di django.contrib.auth. Sistem ini menyediakan form login (AuthenticationForm), fungsi authenticate() untuk memeriksa username dan password, serta login() untuk membuat session pengguna yang sudah terverifikasi. Setelah autentikasi berhasil, Django akan beralih ke otorisasi, yaitu mengatur hak akses pengguna. Django menggunakan permission system yang juga ada di django.contrib.auth. Setiap model bisa memiliki izin khusus, misalnya “tambah data”, “ubah data”, atau “hapus data”, dan izin ini bisa diberikan ke user atau kelompok user (group). Dengan begitu, Django bisa memastikan hanya pengguna yang memiliki izin tertentu yang boleh melakukan aksi tertentu.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
= Session memiliki kelebihan yang dimana lebih aman karena data penting tidak disimpan langsung di browser pengguna, dan kapasitas penyimpanannya bisa lebih besar karena ditaruh di server. Untuk kekurangannya, Session membebani server karena semua data user atau pengguna disimpan di sana, dan otomatis kalo banyak user yang aktif, servernya pasti jadi lag atau berat.
Untuk Cookies, dia mempunyai kelebihan yang dimana tidak terlalu membebani server karena datanya disimpan di client, mudah digunakan untuk menyimpan preferensi pengguna, tapi cookies punya kekurangan yaitu kapasitas penyimpanannya yang terbatas, serta lebih rentan terhadap manipulasi atau pencurian jika tidak diamankan atau di backup.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
= Penggunaan cookies tidak sepenuhnya aman karena berisiko dicuri lewat XSS, disadap tanpa HTTPS, atau dimanipulasi oleh pengguna. Django mengatasinya dengan menyediakan opsi HttpOnly agar cookie tidak bisa diakses JavaScript, Secure agar hanya terkirim lewat HTTPS, serta enkripsi pada session cookie dan penggunaan CSRF token.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= cara saya untuk mengimplementasikan checklist cheslistnya ialah dengan cara teliti, dan mempelajari dari tutorial step step nya dari mana terus kemana dan ini maksudnya apa, yang dimana pada tugas 4 ini, menambahkan autentikasi dan otoriasi dengan menambahkan fungsi baru di views.py, register, login, logout, dan seperti biasa ditaruh di urls.py. Terus pada tugas 4 ini juga membuat akun dan product yang dibuat itu tersinkronisasi dan pengguna lain tidak dapat melihat product yang dibuat oleh pengguna yang lain, pada tugas kali ini, saya membuat 2 akun dan membuat masing masing 3 produk di dalam akun tersebut, dan mengecek apakah di akun yang tidak membuat produk tersebut ada produk tersebut di myproduct, jika tidak ada berarti antar akun dan produk unik dan sudah tersinkronisasi, begitu saya dalam mengerjakan tugas 4 PBP pada kesempatan kali ini.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tugas 5:
 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
= jika ada banyak CSS selector yang mengatur elemen yang sama, urutan prioritasnya adalah inline style yang paling kuat, lalu ID selector, terus class/pseudo-class/attribute selector, dan yang paling lemah element/tag selector. Dan kalau prioritasnya sama, yang dipakai adalah aturan yang ditulis paling akhir di CSS.

 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
= karena responsive design membuat tampilan website bisa menyesuaikan ukuran layar perangkat apapun, baik itu handphone, tablet, maupun laptop. Jadi user atau pengguna tetap nyaman membaca dan memakai aplikasinya tanpa harus zoom in dan zoom out atau scroll kesana kesini.

 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
= Margin digunakan untuk memberi jarak luar antara elemen dengan elemen lain di sekitarnya, border adalah garis tepi yang membatasi elemen dengan lingkungannya, sedangkan padding digunakan untuk memberi jarak antara isi elemen (seperti teks atau gambar) dengan garis tepinya. Misalnya, saat kita menulis margin: 20px; border: 2px solid black; padding: 15px;, maka elemen akan memiliki jarak 20px dari elemen lain, dikelilingi garis tepi hitam setebal 2px, serta memberi ruang 15px antara isi elemen dengan garis tepi tersebut.

 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
= Flexbox dan Grid Layout itu sama-sama cara buat ngatur tampilan elemen di web biar lebih rapi dan enak dilihat. Flexbox biasanya dipakai buat ngatur elemen secara satu arah aja, entah itu ke samping (baris) atau ke bawah (kolom). Jadi misalnya mau bikin navbar, daftar produk, atau card yang bisa menyesuaikan ukuran layar, flexbox ini cocok banget. Nah kalau Grid Layout, dia lebih ke dua arah, bisa ngatur baris sekaligus kolom. Grid ini enaknya dipakai kalau kita mau bikin layout yang lebih kompleks, kayak tampilan halaman utama web, dashboard, atau galeri foto. Singkatnya, flexbox lebih gampang buat ngatur layout yang simpel dan sebaris, sedangkan grid lebih kuat kalau dipakai buat struktur halaman yang besar dan terorganisir. Jadi, biasanya flexbox dipakai buat komponen kecil, sedangkan grid dipakai buat kerangka besar dari halaman web.

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
 = cara saya mengimplementasikan checklist yaitu dengan cara memahami tutorialnya dan maksud tiap step itu apa, pada tugas 5 kali ini, saya mengubah FajarWearShop dengan penambahan design pada halaman login, halaman main serta halam detail produk, yang dimana disini menggunakan html dan css sebagai designnya, dengan menambahkan file baru, yang sebelumnya tampilan website FajarWearShop putih polos, jadi ada warnnanya dan lebih menarik. dan juga diatur oleh grid layout, margin, border, dan padding. Dan pada akhirnya saya berhasil untuk mengubah tampilan web saya yaitu FajarWearShop menjadi lebih menarik dan enak dipandang, dan juga, adanya responsive design, yang dimana disini saya paham bahwasanya jika websitenya dibuka menggunakan laptop, dia akan mneyesuaikan halamannya, serta jika dibuka dengan hp, dia akan menyesuaikannya juga, ini menjadi konsep penting di aplikasi web, darisini saya paham bahwa itu sangat perlu untuk memudahkan user dalam melihat website kita, dan pada akhirnya tugas 5 saya kali ini selesai.

 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tugas 6: 
1. Apa perbedaan antara synchronous request dan asynchronous request?
= Synchronous request mengharuskan browser menunggu respon dari server sebelum bisa melanjutkan aktivitas lain, sehingga setiap aksi user memicu reload halaman penuh. Sedangkan asynchronous request, seperti yang dilakukan menggunakan AJAX, memungkinkan browser mengirim request ke server di background dan hanya memperbarui bagian tertentu dari halaman tanpa reload, membuat interaksi terasa lebih cepat dan responsif.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
= AJAX bekerja di Django dengan JavaScript mengirim request (misal pakai fetch() atau $.ajax()) ke endpoint view tertentu. View ini memproses request dan mengembalikan respon dalam format JSON menggunakan JsonResponse(). Setelah itu, JavaScript menerima data JSON tersebut dan memperbarui tampilan halaman secara dinamis sesuai kebutuhan, tanpa reload seluruh halaman.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
= Keuntungan utama AJAX adalah halaman tidak perlu reload penuh sehingga lebih cepat, interaktif, dan hemat bandwidth. AJAX juga memungkinkan update data secara real-time, membuat website terasa lebih modern dan smooth, serta meningkatkan responsivitas dan kenyamanan pengguna.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
= Keamanan AJAX untuk fitur sensitif seperti Login dan Register dapat dijaga dengan menyertakan CSRF token di setiap request POST, melakukan validasi input di server-side, menggunakan HTTPS, menghindari pengiriman data sensitif di URL, serta membatasi rate request untuk mencegah serangan brute force.

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
= AJAX meningkatkan pengalaman pengguna karena interaksi menjadi lebih cepat, halaman lebih responsif, dan pengguna dapat mengakses informasi atau melakukan aksi tanpa menunggu reload halaman. Hal ini membuat website terasa lebih nyaman, modern, dan interaktif dibandingkan dengan render halaman biasa.

 