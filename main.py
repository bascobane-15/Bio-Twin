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
# ---------------------------
# AVATAR GÖRSELİ
# ---------------------------

st.subheader("🧍 Dijital İkiz Görsel Durum")

last = df.iloc[-1]

C_val = last["Kortizol"]
G_val = last["Kan Şekeri"]
B_val = last["Bağışıklık"]
H_val = last["Homeostaz"]

# Renk Mantığı
brain_color = "yellow" if C_val > 70 else "lightgray"
abdomen_color = "orange" if G_val > 70 else "lightgray"
body_color = "red" if H_val < 50 else "#cccccc"
opacity = 0.5 if B_val < 60 else 1

avatar_html = f"""
<svg width="300" height="500" viewBox="0 0 200 400">
    <!-- Body -->
    <ellipse cx="100" cy="200" rx="60" ry="120" fill="{body_color}" opacity="{opacity}" />
    
    <!-- Head -->
    <circle cx="100" cy="80" r="40" fill="{body_color}" opacity="{opacity}" />
    
    <!-- Brain (Stress Area) -->
    <circle cx="100" cy="70" r="15" fill="{brain_color}" />
    
    <!-- Abdomen (Metabolic Area) -->
    <ellipse cx="100" cy="220" rx="30" ry="40" fill="{abdomen_color}" />
</svg>
"""


# Renk hesaplama
if homeostasis > 70:
    body_color = "#00FFFF"
elif homeostasis > 40:
    body_color = "#FFD700"
else:
    body_color = "#FF3B3B"

brain_glow = min(1, stress / 10)

svg_code = f"""
<svg width="300" height="500" viewBox="0 0 300 500">
<style>
@keyframes pulse {{
  0% {{ opacity: 0.7; }}
  50% {{ opacity: 1; }}
  100% {{ opacity: 0.7; }}
}}

.hologram {{
  fill: {body_color};
  opacity: 0.6;
  animation: pulse 2s infinite;
}}

.brain {{
  fill: yellow;
  opacity: {brain_glow};
}}
</style>

<ellipse cx="150" cy="250" rx="90" ry="200" fill="{body_color}" opacity="0.2"/>
<ellipse cx="150" cy="250" rx="70" ry="180" class="hologram"/>
<circle cx="150" cy="80" r="50" class="hologram"/>
<circle cx="150" cy="70" r="20" class="brain"/>
</svg>
"""

st.markdown(svg_code, unsafe_allow_html=True)





