import streamlit as st

def main():
    st.title("Aplikasi Sistem Pendukung Keputusan dengan Metode SAW")

    st.write("### Data Input")
    # Input data kriteria
    st.write("#### Masukkan Data Kriteria")
    kriteria = st.text_input("Nama Kriteria (pisahkan dengan koma)", "Harga, Kualitas, Fitur, Garansi").split(', ')

    st.write("#### Masukkan Bobot Kriteria (jumlah harus 1)")
    bobot = st.text_input("Bobot Kriteria (pisahkan dengan koma)", "0.3, 0.35, 0.2, 0.15").split(',')
    bobot = list(map(float, bobot))

    st.write("#### Masukkan Jenis Kriteria (cost atau benefit)")
    costbenefit = st.text_input("Jenis Kriteria (cost/benefit, pisahkan dengan koma)", "cost, benefit, benefit, benefit").split(', ')

    # Input data alternatif
    st.write("#### Masukkan Data Alternatif")
    alternatif = st.text_area("Nama Alternatif (pisahkan dengan baris)", "Produk A\nProduk B\nProduk C\nProduk D").split('\n')

    st.write("#### Masukkan Nilai Kriteria untuk Setiap Alternatif")
    alternatifkriteria = []
    for alt in alternatif:
        nilai = st.text_input(f"Nilai Kriteria untuk {alt} (pisahkan dengan koma)", "5000, 70, 10, 36").split(',')
        nilai = list(map(int, nilai))
        alternatifkriteria.append(nilai)

    # Tombol untuk proses perhitungan SAW
    if st.button("Hitung Perangkingan"):
        st.write("### Hasil Perangkingan")
        
        # Proses perhitungan SAW
        pembagi = []
        for i in range(len(kriteria)):
            min_max = min if costbenefit[i] == 'cost' else max
            pembagi.append(min_max(alternatifkriteria[j][i] for j in range(len(alternatif))))

        normalisasi = []
        for i in range(len(alternatif)):
            normalisasi.append([])
            for j in range(len(kriteria)):
                if costbenefit[j] == 'cost':
                    normalisasi[i].append(pembagi[j] / alternatifkriteria[i][j])
                else:
                    normalisasi[i].append(alternatifkriteria[i][j] / pembagi[j])

        hasil = []
        for i in range(len(alternatif)):
            hasil.append(sum(normalisasi[i][j] * bobot[j] for j in range(len(kriteria))))

        # Mengurutkan hasil perangkingan
        alternatifrangking = [alt for _, alt in sorted(zip(hasil, alternatif), reverse=True)]
        hasilrangking = sorted(hasil, reverse=True)

        # Menampilkan hasil perangkingan
        st.write("#### Alternatif Berdasarkan Perangkingan:")
        for rank, (alt, nilai) in enumerate(zip(alternatifrangking, hasilrangking), start=1):
            st.write(f"Rank {rank}: {alt} - Nilai: {nilai}")

if __name__ == '__main__':
    main()
