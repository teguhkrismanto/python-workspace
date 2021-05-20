import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

resp = requests.get('https://data.covid19.go.id/public/api/update.json')

cov_id_raw = resp.json()
cov_id_update = cov_id_raw['update']
# print('Tanggal pembaharuan data penambahan kasus   :', cov_id_update['penambahan']['tanggal'])
# print('Jumlah penambahan kasus sembuh              :', cov_id_update['penambahan']['jumlah_sembuh'])
# print('Jumlah penambahan kasus meninggal           :', cov_id_update['penambahan']['jumlah_meninggal'])
# print('Jumlah total kasus positif hingga saat ini  :', cov_id_update['total']['jumlah_positif'])
# print('Jumlah total kasus meninggal hingga saat ini:', cov_id_update['total']['jumlah_meninggal'])

resp_jabar = requests.get('https://data.covid19.go.id/public/api/prov_detail_JAWA_BARAT.json')
cov_jabar_raw = resp_jabar.json()
# print('Nama-nama elemen utama:\n', cov_jabar_raw.keys())
# print('\nJumlah total kasus COVID-19 di Jawa Barat : %d' %cov_jabar_raw['kasus_total'])
# print('Persentase kematian akibat COVID-19 di Jawa Barat : %f.2%%' %cov_jabar_raw['meninggal_persen'])
# print('Persentase tingkat kesembuhan dari COVID-19 di Jawa Barat : %f.2%%' %cov_jabar_raw['sembuh_persen'])

cov_jabar = pd.DataFrame(cov_jabar_raw['list_perkembangan'])
# print('Info cov_jabar:\n', cov_jabar.info())
# print('\nLima data teratas cov_jabar:\n', cov_jabar.head())

cov_jabar_tidy = (cov_jabar.drop(columns=[item for item in cov_jabar.columns
                                if item.startswith('AKUMULASI') 
                                or item.startswith('DIRAWAT')])
                                .rename(columns=str.lower)
                                .rename(columns={'kasus': 'kasus_baru'})
)
cov_jabar_tidy['tanggal'] = pd.to_datetime(cov_jabar_tidy['tanggal'] * 1e6, unit='ns')
# print('Lima data teratas:\n', cov_jabar_tidy.head())

# # Grafik kasus harian
# fig, ax = plt.subplots(figsize=(10,5))
# ax.bar(data=cov_jabar_tidy, x = 'tanggal', height = 'kasus_baru', color = 'salmon')
# fig.suptitle('Kasus Harian Positif COVID-19 di Jawa Barat',
#             y = 1.00,
#             fontsize = 16,
#             fontweight = 'bold',
#             ha='center')
# ax.set_title('Terjadi pelonjakan kasus di awal bulan Juli akibat klaster Secapa AD Bandung', fontsize = 10)
# ax.set_xlabel('')
# ax.set_ylabel('Jumlah kasus')
# ax.text(1, -0.1, 'Sumber data: covid.19.go.id', color = 'blue',
#         ha = 'right',
#         transform = ax.transAxes)

# ax.xaxis.set_major_locator(mdates.MonthLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# plt.grid(axis = 'y')
# plt.tight_layout()
# plt.show()

# # Grafik untuk Kasus Sembuh
# fig, ax = plt.subplots(figsize=(10,5))
# ax.bar(data = cov_jabar_tidy, x = 'tanggal', height = 'sembuh', color = 'olivedrab')
# ax.set_title('Kasus Harian Sembuh Dari COVID-19 di Jawa Barat', fontsize = 22)
# ax.set_xlabel('')
# ax.set_ylabel('Jumlah kasus')
# ax.text(1, -0.1, 'Sumber data: covid.19.go.id', color = 'blue', ha = 'right', transform = ax.transAxes)

# ax.xaxis.set_major_locator(mdates.MonthLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# plt.grid(axis = 'y')
# plt.tight_layout()
# plt.show()

# # Grafik kasus meninggal
# fig, ax = plt.subplots(figsize=(10,5))
# ax.bar(data = cov_jabar_tidy, x = 'tanggal', height = 'meninggal', color = 'slategrey')
# ax.set_title('Kasus Harian Meninggal Dari COVID-19 di Jawa Barat', fontsize = 22)
# ax.set_xlabel('')
# ax.set_ylabel('Jumlah kasus')
# ax.text(1, -0.1, 'Sumber data: covid.19.go.id', color = 'blue', ha = 'right', transform = ax.transAxes)

# ax.xaxis.set_major_locator(mdates.MonthLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# plt.grid(axis = 'y')
# plt.tight_layout()
# plt.show()

# Kasus per pekan
cov_jabar_pekanan = (cov_jabar_tidy.set_index('tanggal')['kasus_baru']
                    .resample('W')
                    .sum()
                    .reset_index()
                    .rename(columns={'kasus_baru': 'jumlah'})
)
cov_jabar_pekanan['tahun'] = cov_jabar_pekanan['tanggal'].apply(lambda x: x.year)
cov_jabar_pekanan['pekan_ke'] = cov_jabar_pekanan['tanggal'].apply(lambda x: x.weekofyear)
cov_jabar_pekanan = cov_jabar_pekanan[['tahun', 'pekan_ke', 'jumlah']]
# print('Info cov_jabar_pekanan:')
# print(cov_jabar_pekanan.info())
# print('\nLima data teratas cov_jabar_pekanan:\n', cov_jabar_pekanan.head())

cov_jabar_pekanan['jumlah_pekanlalu'] = cov_jabar_pekanan['jumlah'].shift().replace(np.nan, 0).astype(int)
cov_jabar_pekanan['lebih_baik'] = cov_jabar_pekanan['jumlah'] < cov_jabar_pekanan['jumlah_pekanlalu']
# print('Sepuluh data teratas:\n', cov_jabar_pekanan.head(10))

# fig, ax = plt.subplots(figsize = (10,5))
# ax.bar(data = cov_jabar_pekanan,
#         x = 'pekan_ke',
#         height='jumlah',
#         color=['mediumseagreen'
#             if x is True else 'salmon'
#             for x in cov_jabar_pekanan['lebih_baik']
#         ]
# )
# fig.suptitle('Kasus Pekanan Positif COVID-19 di Jawa Barat',
#             y=1.00,
#             fontsize=16,
#             fontweight='bold',
#             ha='center'
# )
# ax.set_title('Kolom hijau menunjukan penambahan kasus baru lebih sedikit dibandingkan satu pekan sebelumnya', fontsize = 12)
# ax.set_xlabel('')
# ax.set_ylabel('Jumlah kasus')
# ax.text(1, -0.1, 'Sumber data: covid.19.go.id',
#         color = 'blue',
#         ha = 'right',
#         transform = ax.transAxes
# )

# plt.grid(axis='y')
# plt.tight_layout()
# plt.show()

cov_jabar_akumulasi = cov_jabar_tidy[['tanggal']].copy()
cov_jabar_akumulasi['akumulasi_aktif'] = (cov_jabar_tidy['kasus_baru'] - cov_jabar_tidy['sembuh'] - cov_jabar_tidy['meninggal']).cumsum()
cov_jabar_akumulasi['akumulasi_sembuh'] = cov_jabar_tidy['sembuh'].cumsum()
cov_jabar_akumulasi['akumulasi_meninggal'] = cov_jabar_tidy['meninggal'].cumsum()
cov_jabar_akumulasi.tail()

# fig, ax = plt.subplots(figsize=(10,5))
# ax.plot('tanggal', 'akumulasi_aktif', data=cov_jabar_akumulasi, lw=2)

# ax.set_title('Akumulasi aktif COVID-19 di Jawa Barat',
#             fontsize = 22)
# ax.set_xlabel('')
# ax.set_ylabel('Akumulasi aktif')
# ax.text(1, -0.1, 'Sumber data: covid.19.go.id',
#         color = 'blue',
#         ha = 'right',
#         transform = ax.transAxes)

# ax.xaxis.set_major_locator(mdates.MonthLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# plt.grid()
# plt.tight_layout()
# plt.show()

fig, ax = plt.subplots(figsize=(10,5))
cov_jabar_akumulasi.plot(x = 'tanggal', kind = 'line', ax = ax, lw = 3,
color=['salmon', 'slategrey', 'olivedrab'])

ax.set_title('Dinamika Kasus COVID-19 di Jawa Barat', fontsize = 22)
ax.set_xlabel('')
ax.set_ylabel('Akumulasi aktif')
ax.text(1, -0.1, 'Sumber data: covid.19.go.id',
        color = 'blue',
        ha = 'right',
        transform = ax.transAxes)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.grid()
plt.tight_layout()
plt.show()