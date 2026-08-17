# BioPolymer-LCA-Optimizer
# BioPolymer-LCA-Optimizer: Computational Framework for Sustainable Material Selection

An open-source multi-objective optimization framework designed to bridge **Materials Science**, **Polymer Engineering**, and **Environmental Life Cycle Assessment (LCA)**.

---

## 🔬 Scientific Background
Selecting bio-based materials and green composites requires navigating trade-offs between **mechanical durability** and **environmental impact metrics** (water depletion, atmospheric carbon release, and post-consumer persistence). 

This computational model implements **Multi-Criteria Decision Analysis (MCDA)** and the **Rule of Mixtures** mechanics to rank natural polymers and reinforced composites based on an integrated **Polymer Sustainability Index (PSI)**.

---

## 🛠️ Mathematical & Analytical Formulation

### 1. Rule of Mixtures (Iso-Strain Mechanical Simulation)
The elastic modulus ($E_c$) of a unidirectional fiber-reinforced bio-composite is calculated via:
$$E_c = E_f V_f + E_m (1 - V_f)$$

Where:
- $E_f$ = Elastic Modulus of Natural Fiber (GPa)
- $E_m$ = Elastic Modulus of Bio-Matrix (GPa)
- $V_f$ = Fiber Volume Fraction

### 2. Polymer Sustainability Index (PSI) Formula
$$PSI = \sum \left( w_i \cdot \hat{X}_i \right) \times 100$$
Where $w_i$ represents target parameter weighting, and $\hat{X}_i$ corresponds to normalized property vectors.

---

## 📊 Sample Output & Optimization Metrics

| Material Name | Tensile Strength (MPa) | Carbon Footprint (kg $CO_2$/kg) | PSI Score |
| :--- | :--- | :--- | :--- |
| **Jute-reinforced PLA Composite** | 85.0 | 1.2 | **82.45** |
| **Chitosan-Starch Matrix** | 25.0 | 0.8 | **78.10** |
| **Polyhydroxyalkanoates (PHA)** | 40.0 | 1.9 | **71.30** |
| **Petroleum-based Polyethylene** | 30.0 | 3.1 | **24.15** |


---
Microstructural Fiber Analysis:Quantified fiber morphology from SEM images using ImageJ. The calculated mean fiber diameter is $12.45 \pm 1.82\,\mu\text{m}$ ($n = 30$).

## 👤 Author Information
**Sabbir Ahmed Riad**  
B.Sc. in Textile Engineering (Major in Apparel Engineering, CGPA: 3.76/4.00)[upto 6th semister]
*Prospective Ph.D. Candidate in Materials Science, Polymer Engineering, and Environmental Science*  
- **Email:** sabbirahmedriad.ctec@gmail.com[cite: 1]
- **LinkedIn:** [linkedin.com/in/sabbir-ahmed-riad](https://www.linkedin.com/in/sabbir-ahmed-riad)[cite: 1]
