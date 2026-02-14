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
with tabs[1]:
    st.header("İnsülin Hormonu (Kan Şekeri Düzenleyici)")

    nutrition = st.slider("Beslenme / Glikoz Alımı", 0, 100, 60)
    insulin = nutrition

    st.metric("İnsülin Düzeyi", insulin)

    if insulin < 30:
        st.error("❗ İnsülin Eksikliği")
        st.markdown("""
        **Olası Sonuçlar:**
        - Kan şekerinin yükselmesi (hiperglisemi)  
        - Hücrelere glikoz girişi azalır  

        **İlişkili Hastalık:**
        - Diyabet (Tip 1 benzeri tablo)
        """)
    elif insulin > 70:
        st.warning("⚠️ İnsülin Fazlalığı")
        st.markdown("""
        **Olası Sonuçlar:**
        - Kan şekerinin aşırı düşmesi (hipoglisemi)  
        - Baş dönmesi, bilinç bulanıklığı  

        **İlişkili Durum:**
        - Reaktif hipoglisemi
        """)
    else:
        st.success("✅ İnsülin dengede. Kan şekeri kontrol altında.")

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

st.divider()
st.caption("BioTwin-Systems | Eğitim Amaçlı Dijital İkiz Modeli")











