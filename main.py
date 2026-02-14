import streamlit as st

st.set_page_config(page_title="BioTwin-Systems", layout="centered")

st.title("🧠 BioTwin-Systems")
st.subheader("Sinir ve Endokrin Sistem Dijital İkizi")
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
    st.header("Kortizol Hormonu (Stres Hormonu)")

    stress = st.slider("Stres Düzeyi", 0, 100, 50)
    kortizol = stress  # basit ilişki

    st.metric("Kortizol Düzeyi", kortizol)

    if kortizol > 70:
        st.error("⚠️ Kortizol Fazlalığı")
        st.markdown("""
        **Olası Sonuçlar:**
        - Bağışıklık sisteminin baskılanması  
        - Kan şekerinde artış  
        - Uyku bozuklukları  

        **İlişkili Hastalıklar:**
        - Cushing Sendromu  
        - Kronik stres kaynaklı bağışıklık zayıflığı
        """)
    elif kortizol < 30:
        st.warning("⚠️ Kortizol Eksikliği")
        st.markdown("""
        **Olası Sonuçlar:**
        - Düşük stres toleransı  
        - Halsizlik  
        - Düşük tansiyon  

        **İlişkili Hastalık:**
        - Addison Hastalığı
        """)
    else:
        st.success("✅ Kortizol dengede. Homeostaz korunuyor.")
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

    # FİZYOLOJİK GİRDİ
    calcium = st.slider("Kandaki Kalsiyum Düzeyi", 0, 100, 50)

    # HORMON DÜZEYLERİ (basitleştirilmiş model)
    parathormon = max(0, 70 - calcium)
    kalsitonin = max(0, calcium - 30)

    # HORMON DÜZEYLERİ GÖSTERİM
    col1, col2 = st.columns(2)
    col1.metric("Parathormon (PTH)", parathormon)
    col2.metric("Kalsitonin", kalsitonin)

    # ANTİAGONİST HORMON GRAFİĞİ
    df = pd.DataFrame({
        "Hormon": ["Parathormon (PTH)", "Kalsitonin"],
        "Düzey": [parathormon, kalsitonin]
    })

    st.subheader("Antagonist Hormonlar – Aynı Grafikte")
    st.bar_chart(df.set_index("Hormon"))

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











