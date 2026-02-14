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
    st.header("Kortizol: Stres ve Sistemik Etkiler")
    
    # 1. GİRDİ ALANI
    stress = st.slider("Stres Düzeyi (Psikolojik/Fiziksel)", 0, 100, 50)
    
    # Matematiksel Hesaplama
    kortizol_seviyesi = stress * 1.15
    
    # 2. GÖRSEL GÖSTERGE (Gauge)
    import plotly.graph_objects as go
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = kortizol_seviyesi,
        title = {'text': "Kortizol Konsantrasyonu"},
        gauge = {
            'axis': {'range': [None, 120]},
            'bar': {'color': "darkred"},
            'steps' : [
                {'range': [0, 40], 'color': "#d9f2d9"},
                {'range': [40, 80], 'color': "#ffebcc"},
                {'range': [80, 120], 'color': "#ffcccc"}],
            'threshold': {'line': {'color': "black", 'width': 4}, 'value': 100}}))
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # 3. AKADEMİK BİLGİ ALANI (Ders Materyali Bölümü)
    st.subheader("📚 Klinik Bilgi Paneli: Kortizol Artışının Etkileri")
    
    col_info1, col_info2 = st.columns(2)

    with col_info1:
        st.markdown("""
        **1. Metabolik Etkiler:**
        * **Glukoneojenez:** Karaciğerde glikoz üretimini artırarak kan şekerini yükseltir.
        * **Protein Katabolizması:** Kas dokusunda protein yıkımına neden olur (kas zayıflığı).
        * **Lipoliz:** Yağların parçalanıp kanda serbest yağ asitlerinin artmasına yol açar.
        
        **2. Bağışıklık Sistemi:**
        * **İmmünsupresyon:** Lökosit aktivitesini baskılayarak bağışıklığı zayıflatır.
        * **Anti-inflamatuar:** Enflamasyonu (yangıyı) azaltır (Bu yüzden ilaç olarak kullanılır).
        """)

    with col_info2:
        st.markdown("""
        **3. Kardiyovasküler Etkiler:**
        * **Hipertansiyon:** Kan damarlarının adrenalin gibi maddelere duyarlılığını artırarak tansiyonu yükseltir.
        
        **4. Uzun Vadeli (Kronik) Sonuçlar:**
        * **Cushing Sendromu:** Kronik yüksek kortizol sonucu oluşan klinik tablo.
        * **Obezite:** Özellikle gövde ve yüz bölgesinde (ay dede yüzü) yağlanma.
        * **Osteoporoz:** Kemik yapımını azaltıp yıkımını hızlandırır.
        """)

    # 4. DİNAMİK ÖĞRENCİ NOTU
    if stress > 80:
        st.info("💡 **Eğitim Notu:** Şu anki yüksek değerler, vücudun 'Savaş veya Kaç' (Fight or Flight) modunda takılı kaldığını simüle ediyor. Bu durumda protein yıkımı (kas erimesi) maksimumdadır.")
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






















