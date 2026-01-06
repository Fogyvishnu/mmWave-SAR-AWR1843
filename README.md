# Synthetic Aperture Radar (SAR) using AWR1843BOOST

This repository presents a complete implementation of **Synthetic Aperture Radar (SAR)**
using the **TI AWR1843BOOST mmWave FMCW radar**. The project focuses on **raw ADC data
capture**, coherent SAR processing, and high-resolution 2D imaging.

---

## 🚀 Key Features
- FMCW-based SAR implementation at **77 GHz**
- Raw ADC data capture using **DCA1000EVM**
- Phase-preserving SAR signal processing
- MATLAB & Python based processing pipeline
- Linear rail based synthetic aperture formation

---

## 🧠 System Overview


::contentReference[oaicite:0]{index=0}


The radar is translated along a linear path while capturing FMCW chirps at discrete
positions. The collected phase history is processed using **Back Projection Algorithm**
to form a high-resolution SAR image.

---

## 🧩 Hardware Used
- **:contentReference[oaicite:1]{index=1}**
- **:contentReference[oaicite:2]{index=2}**
- Linear rail with stepper motor
- PC for data acquisition and processing

---

## 📡 Radar Configuration (Typical)
| Parameter | Value |
|--------|------|
| Start Frequency | 77 GHz |
| Bandwidth | 4 GHz |
| ADC Samples | 256 |
| Chirps / Frame | 64 |
| TX | 1 |
| RX | 4 |

Range Resolution ≈ **3.75 cm**

---

## 📥 Data Acquisition
- Raw ADC data captured using **mmWave Studio**
- LVDS streaming enabled
- Each radar position stored as a separate `.bin` file

---

## 🧮 Signal Processing Pipeline
1. Raw ADC data parsing
2. Range FFT
3. Phase history extraction
4. SAR Back Projection
5. Image visualization

---

## 📊 Results
Sample outputs include:
- Range profiles
- 2D SAR reflectivity images

---

## 📌 Applications
- Indoor imaging
- Object profiling
- Educational SAR demonstrations
- Radar signal processing research

---

## 📚 References
- TI mmWave SDK Documentation
- Skolnik, *Introduction to Radar Systems*
- Richards, *Principles of Modern Radar*

---

## 👤 Author
**Vishnu Prashanth**  
Electronics & Radar Systems Enthusiast  


