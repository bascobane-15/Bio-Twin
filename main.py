import streamlit as st
import pandas as pd


st.set_page_config(page_title="BioTwin-Systems", layout="wide")
# SOL PANEL (SIDEBAR) EKLEYELİM
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2865/2865914.png", width=80)
    st.title("BioTwin Dashboard")
    st.markdown("---")
    st.info("""
    **Proje Vizyonu:**
    Bu platform, insan fizyolojisini dijital dünyada modellemek amacıyla başlatılan **BioTwin-Systems** serisinin ilk modülüdür. 
    
    Şu an yayında olan **Endokrin Sistem** modülüdür. 
    
    **Gelecek Planları:**
    * 🫀 Dolaşım ve Solunum Sistemi Simülasyonları
           
    Çalışmamız, eğitimde dijital ikiz kullanımını yaygınlaştırmak için geliştirilmeye devam etmektedir.
    """)
    
    st.subheader("Simülasyon Durumu")
    st.success("🟢 Sistem Aktif")
    
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
    st.header("İnsülin ve Glukagon: Kan Şekeri Homeostazı")
    
    # 1. GİRDİ ALANI: Kan Glikoz Düzeyi
    # Tıbbi olarak normal açlık şekeri 70-100 mg/dL arasıdır.
    glikoz = st.slider("Kan Glikoz Seviyesi (mg/dL)", 40, 200, 90)
    
    # 2. HESAPLAMA MANTIĞI (Antagonist Model)
    # Glikoz arttıkça İnsülin artar, Glukagon azalır.
    insulin = max(0.0, (glikoz - 70) * 1.5) if glikoz > 70 else 0
    glukagon = max(0.0, (110 - glikoz) * 1.5) if glikoz < 110 else 0

    # 3. GÖRSELLEŞTİRME: Karşılaştırmalı Bar Grafik
    import plotly.graph_objects as go
    fig_kan_sekeri = go.Figure()
    fig_kan_sekeri.add_trace(go.Bar(
        x=['İnsülin (Anabolik)', 'Glukagon (Katabolik)'],
        y=[insulin, glukagon],
        marker_color=['#1f77b4', '#d62728'], # Mavi ve Kırmızı
        text=[f"Seviye: {insulin:.1f}", f"Seviye: {glukagon:.1f}"],
        textposition='auto'
    ))
    fig_kan_sekeri.update_layout(title="Hormonların Glikoz Seviyesine Yanıtı", yaxis_range=[0, 150])
    st.plotly_chart(fig_kan_sekeri, use_container_width=True)

    st.divider()

    # 4. AKADEMİK BİLGİ ALANI (Ders Materyali)
    st.subheader("📚 Klinik Bilgi Paneli: Glikoz Regülasyonu")
    
    col_ins1, col_ins2 = st.columns(2)

    with col_ins1:
        st.markdown("""
        **🔵 İnsülin (Beta Hücreleri):**
        * **Görevi:** Kan şekerini düşürmek.
        * **Mekanizma:** Glikozun hücre içine girişini sağlar (GLUT4 kapılarını açar).
        * **Depolama:** Glikozun fazlasını karaciğer ve kasta **Glikojen** olarak depolar.
        * **Sentez:** Protein ve yağ sentezini uyarır (Anabolik hormon).
        """)

    with col_ins2:
        st.markdown("""
        **🔴 Glukagon (Alfa Hücreleri):**
        * **Görevi:** Kan şekerini yükseltmek.
        * **Mekanizma:** Karaciğerdeki glikojenin parçalanmasını sağlar (**Glikojenoliz**).
        * **Üretim:** Karbonhidrat olmayan kaynaklardan (protein/yağ) glikoz üretir (**Glukoneojenez**).
        * **Yıkım:** Enerji açığı durumunda devreye girer (Katabolik hormon).
        """)

    # 5. KLİNİK DURUM ÖZETİ
    if glikoz > 140:
        st.error(f"⚠️ **Hiperglisemi:** Kan şekeri yüksek ({glikoz} mg/dL). İnsülin salgısı maksimumda, glikoz hücrelere taşınmaya çalışılıyor.")
    elif glikoz < 70:
        st.warning(f"⚠️ **Hipoglisemi:** Kan şekeri düşük ({glikoz} mg/dL). Glukagon devreye girerek karaciğerden kana şeker salınmasını uyarıyor.")
    else:
        st.success("✅ **Normoglisemi:** Kan şekeri ideal aralıkta. Homeostaz korunuyor.")
      
# ------------------------------------------------
# TİROKSİN SEKME
# ------------------------------------------------
with tabs[2]:
    st.header("Tiroksin ve HPT Aksı: Negatif Feedback Mekanizması")
    
    # 1. GİRDİ ALANI: Tiroit Bezi Aktivitesi
    tiroit_aktivite = st.slider("Tiroit Bezi Çalışma Kapasitesi (%)", 0, 200, 100)
    
    # 2. FEEDBACK MANTIĞI (Dijital İkiz Hesaplaması)
    # Tiroksin (T4), tiroit bezinin aktivitesine bağlı üretilir.
    tiroksin = tiroit_aktivite * 0.5
    
    # Negatif Feedback: Tiroksin arttıkça Hipofiz'den salgılanan TSH azalır (Gaz-Fren ilişkisi).
    tsh = max(0.1, 100 - (tiroksin * 1.5))

    # 3. GÖRSEL METRİKLER
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.metric("Tiroksin (T4) Seviyesi", f"{tiroksin:.1f}", 
                  delta="Yüksek (Hiper)" if tiroksin > 65 else ("Düşük (Hipo)" if tiroksin < 35 else "Normal"))
    with col_t2:
        st.metric("TSH (Hipofiz Yanıtı)", f"{tsh:.1f}", 
                  delta="Baskılanmış" if tsh < 20 else ("Uyarıcı" if tsh > 80 else "Dengeli"), 
                  delta_color="inverse")

    # 4. GÖRSELLEŞTİRME: Bar Grafik
    import plotly.graph_objects as go
    fig_tiroit = go.Figure()
    fig_tiroit.add_trace(go.Bar(
        x=['TSH (Hipofiz Uyarıcı)', 'Tiroksin (Tiroit Yanıtı)'],
        y=[tsh, tiroksin],
        marker_color=['#9b59b6', '#3498db'], # Mor ve Mavi
        text=[f"TSH: {tsh:.1f}", f"T4: {tiroksin:.1f}"],
        textposition='auto'
    ))
    fig_tiroit.update_layout(title="HPT Aksı: Dinamik Geri Bildirim Dengesi", yaxis_range=[0, 150])
    st.plotly_chart(fig_tiroit, use_container_width=True)

    st.divider()

    # 5. AKADEMİK BİLGİ ALANI (Ders Materyali)
    st.subheader("📚 Klinik Bilgi Paneli: Tiroit Fizyopatolojisi")
    
    st.info("💡 **Negatif Feedback Mekanizması:** Kanda Tiroksin (T4) yükseldiğinde, Hipofiz bezi bunu algılar ve tiroit bezini daha fazla uyarmamak için TSH salgısını azaltır. Bu bir öz-denetim sistemidir.")

    col_symp1, col_symp2 = st.columns(2)

    with col_symp1:
        st.error("🔥 Hipertiroidi (Zehirli Guatr)")
        st.markdown("""
        **Kanda T4 Yüksek, TSH Düşüktür.**
        * **Metabolizma:** Aşırı hızlanır, bazal enerji tüketimi artar.
        * **Kardiyovasküler:** Çarpıntı (Taşikardi) ve yüksek tansiyon.
        * **Sinir Sistemi:** Titreme (tremor), huzursuzluk ve uykusuzluk.
        * **Fiziksel:** Sıcağa tahammülsüzlük, aşırı terleme ve hızlı kilo kaybı.
        """)

    with col_symp2:
        st.warning("❄️ Hipotiroidi")
        st.markdown("""
        **Kanda T4 Düşük, TSH Yüksektir.**
        * **Metabolizma:** Yavaşlar, vücut ısısı düşer.
        * **Kilo:** İştahsızlığa rağmen kilo alma ve vücutta ödem.
        * **Zihinsel:** Unutkanlık, yavaş düşünme ve depresyon eğilimi.
        * **Fiziksel:** Soğuğa tahammülsüzlük, halsizlik ve cilt kuruluğu.
        """)

    # 6. ÖĞRENCİLER İÇİN ÖZET
    st.info("""
    **HPT Aksı Akış Şeması:** Hipotalamus (TRH) ➡️ Ön Hipofiz (TSH) ➡️ Tiroit Bezi (T4) ➡️ Hedef Dokular.
    """)
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
   # HORMON DÜZEYLERİ (Yuvarlama eklendi)
    parathormon = round(max(0.0, (12.0 - calcium) * 25), 1) 
    kalsitonin = round(max(0.0, (calcium - 8.0) * 25), 1)

    # GÖSTERİM (Metriklerin içinde de formatlama yapıyoruz)
    col1, col2 = st.columns(2)
    col1.metric("Parathormon (PTH)", f"{parathormon}")
    col2.metric("Kalsitonin", f"{kalsitonin}")

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








































