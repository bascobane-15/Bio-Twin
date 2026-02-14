import streamlit as st

st.set_page_config(page_title="BioTwin-Systems", layout="centered")

st.title("🧠 BioTwin-Systems")
st.subheader("Sinir ve Endokrin Sistem Dijital İkizi")
st.markdown("Her hormon için ayrı senaryo üzerinden **neden–sonuç ilişkileri** gözlemlenir.")

st.divider()

# SEKME YAPISI
tabs = st.tabs(["🟠 Kortizol", "🔵 İnsülin", "🟣 Tiroksin"])

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
    st.subheader("İnsülin – Glukagon Antagonizması")

    glucose = st.slider("Kan Glikoz Alımı", 0, 100, 60)

    insulin = max(0, glucose - 30)
    glucagon = max(0, 70 - glucose)

    df = pd.DataFrame({
        "Hormon": ["İnsülin", "Glukagon"],
        "Düzey": [insulin, glucagon]
    })

    st.bar_chart(df.set_index("Hormon"))

    if insulin > glucagon:
        st.success("✅ İnsülin baskın → Kan şekeri düşürülüyor")
    elif glucagon > insulin:
        st.warning("⚠️ Glukagon baskın → Kan şekeri yükseltiliyor")
    else:
        st.info("ℹ️ Hormonlar dengede → Homeostaz sağlanıyor")

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
    st.subheader("Parathormon – Kalsitonin Antagonizması (Kalsiyum Dengesi)")

    calcium = st.slider("Kandaki Kalsiyum Düzeyi", 0, 100, 50)

    parathormon = max(0, 70 - calcium)
    kalsitonin = max(0, calcium - 30)

    df2 = pd.DataFrame({
        "Hormon": ["Parathormon (PTH)", "Kalsitonin"],
        "Düzey": [parathormon, kalsitonin]
    })

    st.bar_chart(df2.set_index("Hormon"))

    if parathormon > kalsitonin:
        st.warning("⚠️ Parathormon baskın → Kemikten kana kalsiyum geçişi artar")
    elif kalsitonin > parathormon:
        st.success("✅ Kalsitonin baskın → Kalsiyum kemikte tutulur")
    else:
        st.info("ℹ️ Kalsiyum dengede → İskelet sistemi homeostazı")

st.divider()
st.caption("BioTwin-Systems | Eğitim Amaçlı Dijital İkiz Modeli")

