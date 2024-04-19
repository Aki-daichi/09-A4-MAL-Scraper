// // Mendapatkan elemen dengan kelas .home-section
// const homeSection = document.querySelector('.home-section');

// // Membuat fungsi untuk menerapkan animasi ketika elemen terlihat
// function animateOnVisible(entries, observer) {
//     entries.forEach(entry => {
//         if (entry.isIntersecting) {
//             // Menerapkan animasi saat elemen terlihat
//             entry.target.style.transform = 'translateX(0)';
//             entry.target.style.opacity = 1;
//         } else {
//             // Kembalikan elemen ke posisi semula saat tidak terlihat
//             entry.target.style.transform = 'translateX(100%)';
//             entry.target.style.opacity = 0;
//         }
//     });
// }

// // Membuat observer menggunakan Intersection Observer API
// const observer = new IntersectionObserver(animateOnVisible, {
//     threshold: 0.1 // Mengatur ambang batas 10% untuk memicu animasi
// });

// // Memulai pengamatan untuk elemen .home-section
// observer.observe(homeSection);
