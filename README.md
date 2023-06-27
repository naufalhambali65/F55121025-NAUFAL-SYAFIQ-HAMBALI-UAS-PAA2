Nama : Naufal Syafiq Hambali
NIM  : F55121035
UAS PAA 2 KELAS A

1. Analisa Algoritma bubble sort dan insertion sort
    Untuk melakukan analisis algoritma, kita perlu memahami kompleksitas waktu dari masing-masing algoritma pengurutan (Bubble Sort dan Insertion Sort) terlebih dahulu.
    Kompleksitas waktu untuk Bubble Sort:
    •	Worst Case: O(n^2)
    •	Best Case: O(n) (jika array sudah terurut)
    •	Average Case: O(n^2)
    Kompleksitas waktu untuk Insertion Sort:
    •	Worst Case: O(n^2)
    •	Best Case: O(n) (jika array sudah terurut)
    •	Average Case: O(n^2)
    Analisis Algoritma:
    1.	Worst Case:
    •	Ketika array tidak terurut secara terbalik, baik Bubble Sort maupun Insertion Sort akan memerlukan jumlah iterasi yang maksimum.
    •	Jumlah elemen yang harus dibandingkan dan digeser pada setiap iterasi adalah maksimum.
    2.	Best Case:
    •	Ketika array sudah terurut secara ascending, baik Bubble Sort maupun Insertion Sort akan memiliki kompleksitas waktu terbaik.
    •	Dalam kasus terbaik, algoritma hanya perlu melakukan satu iterasi untuk memeriksa bahwa array sudah terurut.
    3.	Average Case:
    •	Average case terjadi ketika array tidak terurut secara terbalik tetapi juga tidak terurut secara terurut.
    •	Pada average case, baik Bubble Sort maupun Insertion Sort memerlukan jumlah iterasi dan pergeseran yang sedang.
    Kesimpulan:
    •	Dalam kedua algoritma, worst case terjadi ketika array terurut secara terbalik, yang menghasilkan kompleksitas waktu O(n^2).
    •	Best case terjadi ketika array sudah terurut, menghasilkan kompleksitas waktu O(n) untuk kedua algoritma.
    •	Average case terjadi ketika array tidak terurut secara terbalik tetapi juga tidak terurut secara terurut, yang menghasilkan kompleksitas waktu O(n^2) untuk kedua algoritma.
    Dalam analisis ini, perlu diperhatikan bahwa kedua algoritma ini bukanlah algoritma yang efisien untuk pengurutan dalam kasus umum. Jika Anda perlu mengurutkan array dengan jumlah elemen yang besar, ada algoritma pengurutan lain yang lebih efisien, seperti Merge Sort atau Quick Sort.

2. Analisa Algoritma TSP dan Dijkstra
   a. Worst Case:
    •	Algoritma TSP:
    •	Dalam kasus terburuk, semua kemungkinan rute harus dijelajahi untuk menemukan rute terpendek.
    •	Kompleksitas waktu algoritma TSP pada kasus terburuk adalah O(n!), di mana n adalah jumlah vertex dalam graf.
    •	Algoritma Dijkstra:
    •	Dalam kasus terburuk, semua vertex harus dikunjungi dan semua edge harus diperiksa.
    •	Kompleksitas waktu algoritma Dijkstra pada kasus terburuk adalah O((V + E) log V), di mana V adalah jumlah vertex dan E adalah jumlah edge dalam graf.
   b. Best Case:
    •	Algoritma TSP:
    •	Dalam kasus terbaik, ketika graf memiliki hanya dua vertex, algoritma langsung menghasilkan rute terpendek tanpa perlu memeriksa vertex lain.
    •	Kompleksitas waktu algoritma TSP pada kasus terbaik adalah O(1).
    •	Algoritma Dijkstra:
    •	Dalam kasus terbaik, ketika vertex awal adalah tujuan yang diinginkan, algoritma hanya memerlukan satu iterasi.
    •	Kompleksitas waktu algoritma Dijkstra pada kasus terbaik adalah O(V), di mana V adalah jumlah vertex dalam graf.
   c. Average Case:
    •	Algoritma TSP:
    •	Rata-rata kasus dalam algoritma TSP lebih sulit untuk dianalisis secara tepat karena melibatkan permutasi rute yang berbeda.
    •	Dalam kasus rata-rata, kompleksitas waktu algoritma TSP diperkirakan menjadi O(n^2 * 2^n), di mana n adalah jumlah vertex dalam graf.
    •	Algoritma Dijkstra:
    •	Rata-rata kasus dalam algoritma Dijkstra juga sulit untuk dianalisis secara tepat.
    •	Dalam kasus rata-rata, kompleksitas waktu algoritma Dijkstra diperkirakan menjadi O((V + E) log V), di mana V adalah jumlah vertex dan E adalah jumlah edge dalam graf.
   Kesimpulan:
    •	Algoritma TSP memiliki kompleksitas waktu yang sangat tinggi pada kasus terburuk dan rata-rata.
    •	Algoritma Dijkstra memiliki kompleksitas waktu yang lebih baik dibandingkan dengan TSP, tetapi tetap membutuhkan waktu yang signifikan terutama pada kasus terburuk.
    •	Dalam kedua algoritma, kasus terbaik terjadi ketika masukan memiliki karakteristik khusus yang menghasilkan waktu eksekusi yang lebih cepat.
    •	Untuk kasus terburuk dan rata-rata, diperlukan algoritma yang lebih efisien untuk menangani graf dengan ukuran yang lebih besar.

   
