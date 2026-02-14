import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="BioTwin-Integrated", layout="wide")

st.title("🧬 BioTwin-Integrated")
st.subheader("30 Günlük Kronik Stres ve Uyku Azalması Simülasyonu")

# ---------------------------
# GİRİŞ PARAMETRELERİ
# ---------------------------

st.sidebar.header("Girdi Parametreleri")

stress = st.sidebar.slider("Stres Seviyesi (0-10)", 0, 10, 6)
sleep = st.sidebar.slider("Uyku Süresi (Saat)", 4, 8, 5)
days = st.sidebar.slider("Simülasyon Süresi (Gün)", 1, 30, 30)

# ---------------------------
# BAŞLANGIÇ DEĞERLERİ
# ---------------------------

C = 50  # Kortizol
results = []

for t in range(1, days + 1):
    
    # Kortizol (zamana bağlı birikimli)
    C = C + (stress * 0.8) - (sleep * 0.5)
    C = np.clip(C, 30, 100)
    
    # Kan Şekeri
    G = 50 + (C * 0.3)
    
    # İnsülin Duyarlılığı
    I = 100 - (G * 0.4) - (t * 0.5)
    I = np.clip(I, 0, 100)
    
    # Bağışıklık
    B = 100 - (C * 0.3) - ((8 - sleep) * 5) - (t * 0.7)
    B = np.clip(B, 0, 100)
    
    # Homeostaz
    H = (I + B) / 2
    
    results.append([t, C, G, I, B, H])

# ---------------------------
# DATAFRAME
# ---------------------------

df = pd.DataFrame(results, columns=["Gün", "Kortizol", "Kan Şekeri", "İnsülin", "Bağışıklık", "Homeostaz"])

# ---------------------------
# GRAFİKLER
# ---------------------------

st.subheader("📊 Fizyolojik Değişim Grafikleri")

fig, ax = plt.subplots()
ax.plot(df["Gün"], df["Kortizol"], label="Kortizol")
ax.plot(df["Gün"], df["Kan Şekeri"], label="Kan Şekeri")
ax.plot(df["Gün"], df["İnsülin"], label="İnsülin")
ax.plot(df["Gün"], df["Bağışıklık"], label="Bağışıklık")
ax.plot(df["Gün"], df["Homeostaz"], label="Homeostaz")

ax.set_xlabel("Gün")
ax.set_ylabel("İndeks Değeri")
ax.legend()

st.pyplot(fig)

# ---------------------------
# SON GÜN DURUMU
# ---------------------------

st.subheader("📌 Son Gün Fizyolojik Durum")

last = df.iloc[-1]

st.write(f"**Kortizol:** {round(last['Kortizol'],1)}")
st.write(f"**Kan Şekeri:** {round(last['Kan Şekeri'],1)}")
st.write(f"**İnsülin Duyarlılığı:** {round(last['İnsülin'],1)}")
st.write(f"**Bağışıklık İndeksi:** {round(last['Bağışıklık'],1)}")
st.write(f"**Homeostaz Skoru:** {round(last['Homeostaz'],1)}")



