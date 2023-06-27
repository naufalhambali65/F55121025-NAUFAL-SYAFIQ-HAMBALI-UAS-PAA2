Nama : Naufal Syafiq Hambali
NIM  : F55121035
UAS PAA 2 KELAS A

1. Analisa Algoritma bubble sort dan insertion sort<br />
    Untuk melakukan analisis algoritma, kita perlu memahami kompleksitas waktu dari masing-masing algoritma pengurutan (Bubble Sort dan Insertion Sort) terlebih dahulu.
    Kompleksitas waktu untuk Bubble Sort:<br />
    •	Worst Case: O(n^2)<br />
    •	Best Case: O(n) (jika array sudah terurut)<br />
    •	Average Case: O(n^2)<br />
    Kompleksitas waktu untuk Insertion Sort:<br />
    •	Worst Case: O(n^2)<br />
    •	Best Case: O(n) (jika array sudah terurut)<br />
    •	Average Case: O(n^2)<br />
    Analisis Algoritma:<br />
    1.	Worst Case:<br />
    •	Ketika array tidak terurut secara terbalik, baik Bubble Sort maupun Insertion Sort akan memerlukan jumlah iterasi yang maksimum.<br />
    •	Jumlah elemen yang harus dibandingkan dan digeser pada setiap iterasi adalah maksimum.<br />
    2.	Best Case:<br />
    •	Ketika array sudah terurut secara ascending, baik Bubble Sort maupun Insertion Sort akan memiliki kompleksitas waktu terbaik.<br />
    •	Dalam kasus terbaik, algoritma hanya perlu melakukan satu iterasi untuk memeriksa bahwa array sudah terurut.<br />
    3.	Average Case:<br />
    •	Average case terjadi ketika array tidak terurut secara terbalik tetapi juga tidak terurut secara terurut.<br />
    •	Pada average case, baik Bubble Sort maupun Insertion Sort memerlukan jumlah iterasi dan pergeseran yang sedang.<br />
    4.  Kesimpulan:<br />
    •	Dalam kedua algoritma, worst case terjadi ketika array terurut secara terbalik, yang menghasilkan kompleksitas waktu O(n^2).<br />
    •	Best case terjadi ketika array sudah terurut, menghasilkan kompleksitas waktu O(n) untuk kedua algoritma.<br />
    •	Average case terjadi ketika array tidak terurut secara terbalik tetapi juga tidak terurut secara terurut, yang menghasilkan kompleksitas waktu O(n^2) untuk kedua algoritma.<br />
    Dalam analisis ini, perlu diperhatikan bahwa kedua algoritma ini bukanlah algoritma yang efisien untuk pengurutan dalam kasus umum. Jika Anda perlu mengurutkan array dengan jumlah elemen yang besar, ada algoritma pengurutan lain yang lebih efisien, seperti Merge Sort atau Quick Sort.<br />

2. Analisa Algoritma TSP dan Dijkstra<br />
   1. Worst Case:<br />
        •	Algoritma TSP:<br />
        •	Dalam kasus terburuk, semua kemungkinan rute harus dijelajahi untuk menemukan rute terpendek.<br />
        •	Kompleksitas waktu algoritma TSP pada kasus terburuk adalah O(n!), di mana n adalah jumlah vertex dalam graf.<br />
        •	Algoritma Dijkstra:<br />
        •	Dalam kasus terburuk, semua vertex harus dikunjungi dan semua edge harus diperiksa.<br />
        •	Kompleksitas waktu algoritma Dijkstra pada kasus terburuk adalah O((V + E) log V), di mana V adalah jumlah vertex dan E adalah jumlah edge dalam graf.<br />
   2. Best Case:<br />
        •	Algoritma TSP:<br />
        •	Dalam kasus terbaik, ketika graf memiliki hanya dua vertex, algoritma langsung menghasilkan rute terpendek tanpa perlu memeriksa vertex lain.<br />
        •	Kompleksitas waktu algoritma TSP pada kasus terbaik adalah O(1).<br />
        •	Algoritma Dijkstra:<br />
        •	Dalam kasus terbaik, ketika vertex awal adalah tujuan yang diinginkan, algoritma hanya memerlukan satu iterasi.<br />
        •	Kompleksitas waktu algoritma Dijkstra pada kasus terbaik adalah O(V), di mana V adalah jumlah vertex dalam graf.<br />
   3. Average Case:<br />
        •	Algoritma TSP:<br />
        •	Rata-rata kasus dalam algoritma TSP lebih sulit untuk dianalisis secara tepat karena melibatkan permutasi rute yang berbeda.<br />
        •	Dalam kasus rata-rata, kompleksitas waktu algoritma TSP diperkirakan menjadi O(n^2 * 2^n), di mana n adalah jumlah vertex dalam graf.<br />
        •	Algoritma Dijkstra:<br />
        •	Rata-rata kasus dalam algoritma Dijkstra juga sulit untuk dianalisis secara tepat.<br />
        •	Dalam kasus rata-rata, kompleksitas waktu algoritma Dijkstra diperkirakan menjadi O((V + E) log V), di mana V adalah jumlah vertex dan E adalah jumlah edge dalam graf.<br />
   4. Kesimpulan:<br />
        •	Algoritma TSP memiliki kompleksitas waktu yang sangat tinggi pada kasus terburuk dan rata-rata.<br />
        •	Algoritma Dijkstra memiliki kompleksitas waktu yang lebih baik dibandingkan dengan TSP, tetapi tetap membutuhkan waktu yang signifikan terutama pada kasus terburuk.<br />
        •	Dalam kedua algoritma, kasus terbaik terjadi ketika masukan memiliki karakteristik khusus yang menghasilkan waktu eksekusi yang lebih cepat.<br />
        •	Untuk kasus terburuk dan rata-rata, diperlukan algoritma yang lebih efisien untuk menangani graf dengan ukuran yang lebih besar.<br />

   
