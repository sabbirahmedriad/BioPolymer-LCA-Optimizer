import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class BioPolymerLCAOptimizer:
    """
    Advanced Multi-Objective Optimization Framework for Sustainable Material Selection.
    Evaluates Tensile Strength, Biodegradability Rate, Water Consumption, and Carbon Footprint.
    """
    def __init__(self):
        # Database containing experimental/literature parameters of Bio-Polymers & Composites
        self.materials_db = {
            'Material_Name': [
                'Polylactic Acid (PLA)', 
                'Polyhydroxyalkanoates (PHA)', 
                'Chitosan-Starch Matrix', 
                'Jute-reinforced PLA Composite', 
                'Hemp-reinforced Epoxy Composite',
                'Petroleum-based Polyethylene (PE)'
            ],
            'Tensile_Strength_MPa': [60.0, 40.0, 25.0, 85.0, 110.0, 30.0],
            'Youngs_Modulus_GPa': [3.5, 2.0, 1.2, 6.5, 8.0, 0.8],
            'Water_Footprint_L_kg': [1200, 800, 300, 450, 2100, 150],
            'Carbon_Footprint_kgCO2_kg': [2.8, 1.9, 0.8, 1.2, 4.5, 3.1],
            'Biodegradation_HalfLife_Days': [180, 60, 30, 120, 3650, 18250]
        }
        self.df = pd.DataFrame(self.materials_db)

    def calculate_composite_rule_of_mixtures(self, fiber_modulus, matrix_modulus, fiber_volume_fraction):
        """
        Calculates the theoretical Elastic Modulus of fiber-reinforced bio-composites 
        using the Voigt Upper-Bound Rule of Mixtures.
        """
        Vf = fiber_volume_fraction
        Vm = 1.0 - Vf
        Ec = (fiber_modulus * Vf) + (matrix_modulus * Vm)
        return round(Ec, 3)

    def compute_sustainability_index(self, w_strength=0.3, w_water=0.2, w_carbon=0.3, w_degrad=0.2):
        """
        Computes a Normalized Polymer Sustainability Index (PSI) using Multi-Criteria Decision Analysis (MCDA).
        """
        # Feature Normalization (Min-Max Scaling)
        norm_strength = (self.df['Tensile_Strength_MPa'] - self.df['Tensile_Strength_MPa'].min()) / \
                        (self.df['Tensile_Strength_MPa'].max() - self.df['Tensile_Strength_MPa'].min())
        
        # Inverse Normalization for Environmental Penalties (Lower is better)
        norm_water = 1.0 - ((self.df['Water_Footprint_L_kg'] - self.df['Water_Footprint_L_kg'].min()) / \
                     (self.df['Water_Footprint_L_kg'].max() - self.df['Water_Footprint_L_kg'].min()))
        
        norm_carbon = 1.0 - ((self.df['Carbon_Footprint_kgCO2_kg'] - self.df['Carbon_Footprint_kgCO2_kg'].min()) / \
                      (self.df['Carbon_Footprint_kgCO2_kg'].max() - self.df['Carbon_Footprint_kgCO2_kg'].min()))
        
        norm_degrad = 1.0 - ((self.df['Biodegradation_HalfLife_Days'] - self.df['Biodegradation_HalfLife_Days'].min()) / \
                      (self.df['Biodegradation_HalfLife_Days'].max() - self.df['Biodegradation_HalfLife_Days'].min()))

        # Weighted composite score
        psi_scores = (w_strength * norm_strength) + (w_water * norm_water) + \
                     (w_carbon * norm_carbon) + (w_degrad * norm_degrad)
        
        self.df['PSI_Score'] = np.round(psi_scores * 100, 2)
        return self.df.sort_values(by='PSI_Score', ascending=False)

    def generate_pareto_plot(self):
        """
        Generates a publication-ready Pareto Optimization plot comparing mechanical performance 
        versus lifecycle carbon emissions.
        """
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(
            self.df['Carbon_Footprint_kgCO2_kg'], 
            self.df['Tensile_Strength_MPa'], 
            c=self.df['PSI_Score'], 
            cmap='viridis', 
            s=self.df['PSI_Score']*8, 
            edgecolors='black', 
            alpha=0.85
        )
        
        for i, name in enumerate(self.df['Material_Name']):
            plt.annotate(
                name, 
                (self.df['Carbon_Footprint_kgCO2_kg'][i] + 0.1, self.df['Tensile_Strength_MPa'][i] + 1.5),
                fontsize=9,
                fontweight='semibold'
            )

        cbar = plt.colorbar(scatter)
        cbar.set_label('Polymer Sustainability Index (PSI Score)', fontsize=10)

        plt.title('Multi-Objective Material Selection: Tensile Strength vs. Carbon Footprint', fontsize=12, fontweight='bold')
        plt.xlabel('Carbon Footprint (kg CO2-eq per kg material)', fontsize=11)
        plt.ylabel('Tensile Strength (MPa)', fontsize=11)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig('pareto_material_optimization.png', dpi=300)
        print("[SUCCESS] Optimization plot saved as 'pareto_material_optimization.png'")

if __name__ == "__main__":
    optimizer = BioPolymerLCAOptimizer()
    
    # 1. Theoretical Elastic Modulus Evaluation
    jute_modulus = 40.0  # GPa
    pla_modulus = 3.5    # GPa
    v_f = 0.35           # 35% Fiber Volume Fraction
    
    ec_est = optimizer.calculate_composite_rule_of_mixtures(jute_modulus, pla_modulus, v_f)
    print(f"[ANALYTICAL] Estimated Modulus for 35% Jute/PLA Composite: {ec_est} GPa\n")

    # 2. Multi-Objective Ranking
    ranked_materials = optimizer.compute_sustainability_index()
    print("=== MULTI-CRITERIA MATERIAL SUSTAINABILITY RANKING ===")
    print(ranked_materials[['Material_Name', 'Tensile_Strength_MPa', 'Carbon_Footprint_kgCO2_kg', 'PSI_Score']].to_string(index=False))

    # 3. Visualization
    optimizer.generate_pareto_plot()
