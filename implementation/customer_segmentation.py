import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

from kmodes.kmodes import KModes
from kmodes.kprototypes import KPrototypes

import pickle
from pathlib import Path


df = pd.read_csv("./datasets/customer_segments.txt", sep="\t")

# # menampilkan data
# print (df.head())

# # Menampilkan informasi data
# df.info()

sns.set(style='white')

# Fungsi untuk membuat plot
def observasi_num(features):
    fig, axs = plt.subplots(2, 2, figsize=(10, 9))
    for i, kol in enumerate(features):
        sns.boxplot(df[kol], ax = axs[i][0])
        sns.distplot(df[kol], ax = axs[i][1])
        axs[i][0].set_title('mean = %.2f\n median = %.2f\n std = %.2f'%(df[kol].mean(), df[kol].median(), df[kol].std()))
        plt.setp(axs)
        plt.tight_layout()
        # plt.show()

# Memanggil fungsi untuk membuat Plot untuk data numerik
kolom_numerik = ['Umur','NilaiBelanjaSetahun']
observasi_num(kolom_numerik)

# Menyiapkan kolom kategorikal
kolom_kategorikal = ['Jenis Kelamin','Profesi','Tipe Residen']

# Membuat canvas
fig, axs = plt.subplots(3,1,figsize=(7,10))

# Membuat plot untuk setiap kolom kategorikal
for i, kol in enumerate(kolom_kategorikal):
    # Membuat Plot
    sns.countplot(df[kol], order = df[kol].value_counts().index, ax = axs[i])
    axs[i].set_title('\nCount Plot %s\n'%(kol), fontsize=15)

# Memberikan anotasi
for p in axs[i].patches:
    axs[i].annotate(format(p.get_height(), '.0f'),
    (p.get_x() + p.get_width() / 2., p.get_height()),
    ha = 'center',
    va = 'center',
    xytext = (0, 10),
    textcoords = 'offset points')

    # Setting Plot
    sns.despine(right=True,top = True, left = True)
    axs[i].axes.yaxis.set_visible(False)
    plt.setp(axs)
    plt.tight_layout()

    # Tampilkan plot
    # plt.show()

# # Statistik sebelum Standardisasi
# print('Statistik Sebelum Standardisasi\n')
# print(df[kolom_numerik ].describe().round(1))

# Standardisasi
df_std = StandardScaler().fit_transform(df[kolom_numerik])

# Membuat DataFrame
df_std = pd.DataFrame(data=df_std, index=df.index, columns=df[kolom_numerik].columns)

# # Menampilkan contoh isi data dan summary statistic
# print('Contoh hasil standardisasi\n')
# print(df_std.head())

# print('Statistik hasil standardisasi\n')
# print(df_std.describe().round(0))

# Membuat salinan data frame
df_encode = df[kolom_kategorikal].copy()

# Menggabungkan data frame
df_model = df_encode.merge(df_std, left_index = True, right_index=True, how = 'left')
print (df_model.head())
