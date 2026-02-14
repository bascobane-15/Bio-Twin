import streamlit as st
import pandas as pd


st.set_page_config(page_title="BioTwin-Systems", layout="centered")

st.title("🧠 BioTwin-Systems")
st.subheader("Endokrin Sistem Dijital İkizi")
st.markdown("Her hormon için ayrı senaryo üzerinden **neden–sonuç ilişkileri** gözlemlenir.")

st.divider()

tabs = st.tabs([
    "🟠 Kortizol",
    "🔵 İnsülin",
    "🟣 Tiroksin",
    "🟢 Parathormon–Kalsitonin"
])

# ------------------------------------------------
# KORTİZOL SEKME
# ------------------------------------------------
with tabs[0]:
    st.header("Kortizol Hormonu (Stres ve Yaşam Ritmi)")
    
    # İKİNCİL GİRDİ: GÜNÜN SAATİ (Sirkadiyen Ritim için)
    saat = st.select_slider(
        "Günün Hangi Saatindeyiz?",
        options=["06:00", "09:00", "12:00", "15:00", "18:00", "21:00", "00:00", "03:00"],
        value="09:00"
    )

    # ANA GİRDİ: STRES DÜZEYİ
    stress = st.slider("Psikolojik/Fiziksel Stres Düzeyi", 0, 100, 50)

    # DİJİTAL İKİZ HESAPLAMA MANTIĞI
    # Sirkadiyen baz puanları (Sabah yüksek, gece düşük)
    ritim_puanlari = {
        "06:00": 70, "09:00": 90, "12:00": 60, "15:00": 40, 
        "18:00": 30, "21:00": 20, "00:00": 10, "03:00": 30
    }
    baz_kortizol = ritim_puanlari[saat]
    
    # Toplam Kortizol = Biyolojik Ritim + Stres Etkisi (Normalize edilmiş)
    toplam_kortizol = min(100, baz_kortizol + (stress * 0.5))

    # GÖRSELLEŞTİRME: METRİK
    st.metric("Anlık Kortizol Seviyesi", f"{toplam_kortizol:.1f} µg/dL", delta=f"{stress/2:.1f} (Stres Kaynaklı)")

    # GÖRSELLEŞTİRME: PLOTLY ÇİZGİ GRAFİĞİ (Sirkadiyen Ritim)
    import plotly.express as px
    df_ritim = pd.DataFrame({
        "Saat": list(ritim_puanlari.keys()),
        "Normal Seviye": list(ritim_puanlari.values()),
        "Senin Seviyen": [min(100, v + (stress * 0.5)) for v in ritim_puanlari.values()]
    })
    
    fig_kortizol = px.line(df_ritim, x="Saat", y=["Normal Seviye", "Senin Seviyen"], 
                          title="24 Saatlik Kortizol Döngüsü ve Stres Etkisi",
                          color_discrete_map={"Normal Seviye": "gray", "Senin Seviyen": "orange"})
    st.plotly_chart(fig_kortizol, use_container_width=True)

    # KLİNİK YORUM
    if toplam_kortizol > 80:
        st.error("⚠️ Yüksek Kortizol: Uyku bozukluğu ve bağışıklık zayıflığı riski!")
    elif toplam_kortizol < 20:
        st.warning("⚠️ Düşük Kortizol: Yorgunluk ve düşük kan şekeri riski.")
    else:
        st.success("✅ Kortizol seviyesi şu anki saat dilimi için dengeli.")
# ------------------------------------------------
# İNSÜLİN SEKME
# ------------------------------------------------
with tabs[1]:
    st.header("İnsülin Hormonu (Kan Şekeri Düzenleyici)")

    st.markdown("""
    İnsülin ve glukagon hormonları **antagonist** etki göstererek
    kan şekeri dengesinin (homeostaz) sağlanmasında rol oynar.
    """)

    # ÇEVRESEL / FİZYOLOJİK GİRDİ
    glucose = st.slider("Kan Glikoz Alımı", 0, 100, 60)

    # HORMON DÜZEYLERİ (basitleştirilmiş model)
    insulin = max(0, glucose - 30)
    glucagon = max(0, 70 - glucose)

    # HORMON DÜZEYLERİ GÖSTERİM
    col1, col2 = st.columns(2)
    col1.metric("İnsülin Düzeyi", insulin)
    col2.metric("Glukagon Düzeyi", glucagon)

    # ANTİAGONİST HORMON GRAFİĞİ
    df = pd.DataFrame({
        "Hormon": ["İnsülin", "Glukagon"],
        "Düzey": [insulin, glucagon]
    })

    st.subheader("Antagonist Hormonlar – Aynı Grafikte")
    st.bar_chart(df.set_index("Hormon"))

    # FİZYOLOJİK YORUM
    if insulin > glucagon:
        st.success("""
        ✅ **İnsülin Baskın**
        - Hücrelere glikoz girişi artar  
        - Kan şekeri düşürülür  
        - Homeostaz korunur
        """)
    elif glucagon > insulin:
        st.warning("""
        ⚠️ **Glukagon Baskın**
        - Karaciğerde glikojen yıkımı artar  
        - Kana glikoz verilir  
        - Kan şekeri yükselir
        """)
    else:
        st.info("ℹ️ İnsülin ve glukagon dengede → Kan şekeri dengesi sağlanıyor")

    # HASTALIK SENARYOLARI
    st.subheader("Hormon Dengesizliğinde Oluşan Durumlar")

    if insulin < 20:
        st.error("""
        ❗ **İnsülin Eksikliği**
        - Hiperglisemi (kan şekeri yüksekliği)
        - Hücreler glikozu kullanamaz

        **İlişkili Hastalık:**  
        - Diyabet (Tip 1 benzeri tablo)
        """)

    if insulin > 80:
        st.warning("""
        ⚠️ **İnsülin Fazlalığı**
        - Hipoglisemi (kan şekeri düşüklüğü)
        - Baş dönmesi, bilinç bulanıklığı

        **İlişkili Durum:**  
        - Reaktif hipoglisemi
        """)

      
# ------------------------------------------------
# TİROKSİN SEKME
# ------------------------------------------------
with tabs[2]:
    st.header("Tiroksin (T4) Hormonu – Metabolizma Düzenleyici")

    tiroksin = st.slider("Tiroksin (T4) Düzeyi", 0, 100, 50)
    st.metric("Tiroksin Düzeyi", tiroksin)

    if tiroksin < 30:
        st.warning("⚠️ Tiroksin Eksikliği")
        st.markdown("""
        **Olası Sonuçlar:**
        - Metabolizma hızının yavaşlaması  
        - Kilo artışı  
        - Yorgunluk, soğuğa hassasiyet  

        **İlişkili Hastalık:**
        - Hipotiroidi
        """)
    elif tiroksin > 70:
        st.error("⚠️ Tiroksin Fazlalığı")
        st.markdown("""
        **Olası Sonuçlar:**
        - Metabolizma hızının artması  
        - Kilo kaybı  
        - Çarpıntı, sinirlilik  

        **İlişkili Hastalık:**
        - Hipertiroidi
        """)
    else:
        st.success("✅ Tiroksin dengede. Metabolik denge sağlanıyor.")

# ------------------------------------------------
# PARATHORMON – KALSİTONİN SEKME
# ------------------------------------------------

with tabs[3]:
    st.header("Parathormon – Kalsitonin (Kalsiyum Dengesi)")

    st.markdown("""
    Parathormon (PTH) ve kalsitonin hormonları **antagonist** etki göstererek
    kandaki kalsiyum düzeyinin düzenlenmesini sağlar.
    """)

   # FİZYOLOJİK GİRDİ (Kalsiyum değerini 8-12 arasına çektik, daha gerçekçi)
    calcium = st.slider("Kandaki Kalsiyum Düzeyi (mg/dL)", 8.0, 12.0, 10.0)

    # HORMON DÜZEYLERİ (Antagonist Model)
    # Kalsiyum düştükçe PTH tavan yapar, kalsiyum arttıkça PTH sıfıra yaklaşır.
    parathormon = max(0.0, (12.0 - calcium) * 25) 
    
    # Kalsiyum arttıkça Kalsitonin tavan yapar.
    kalsitonin = max(0.0, (calcium - 8.0) * 25)
    # HORMON DÜZEYLERİ GÖSTERİM
    col1, col2 = st.columns(2)
    col1.metric("Parathormon (PTH)", parathormon)
    col2.metric("Kalsitonin", kalsitonin)

    # ANTİAGONİST HORMON GRAFİĞİ
   # PLOTLY İLE ETKİLEŞİMLİ GRAFİK
    import plotly.graph_objects as go

    fig = go.Figure()

    # Parathormon Çubuğu
    fig.add_trace(go.Bar(
        x=['Parathormon (PTH)', 'Kalsitonin'],
        y=[parathormon, kalsitonin],
        marker_color=['#FFA500', '#00CED1'], # Turuncu ve Turkuaz renkler
        text=[f"%{parathormon:.1f}", f"%{kalsitonin:.1f}"],
        textposition='auto',
    ))

    fig.update_layout(
        title_text='Hormonların Dinamik Dengesi',
        yaxis_range=[0, 100],
        template='plotly_white',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # FİZYOLOJİK VE KLİNİK YORUM
    if parathormon > kalsitonin:
        st.warning("""
        ⚠️ **Parathormon Baskın**
        - Kemiklerden kana kalsiyum geçişi artar  
        - Kemik mineral yoğunluğu azalabilir  

        **İlişkili Durum:**  
        - Osteoporoz riski
        """)
    elif kalsitonin > parathormon:
        st.success("""
        ✅ **Kalsitonin Baskın**
        - Kalsiyum kemiklerde tutulur  
        - Kemik yapısı korunur
        """)
    else:
        st.info("ℹ️ Kalsiyum dengede → İskelet sistemi homeostazı sağlanıyor")



st.divider()
st.caption("BioTwin-Systems | Eğitim Amaçlı Dijital İkiz Modeli")



















