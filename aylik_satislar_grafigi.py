import matplotlib.pyplot as plt

def aylik_satis_grafigi_olusturma(df,output_dir):
    plt.figure(figsize = (10,6))
    plt.plot(df['month'], df['total_sales'], marker = 'o')
    plt.title('Aylık Toplam Satışlar')
    plt.xlabel('Aylar')
    plt.ylabel('Toplam Satışlar')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig(output_dir /'aylik_satislar_grafigi.png')
    plt.close()