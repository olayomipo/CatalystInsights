import os
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns

# Create directory for saving plots
plot_dir = "plots"
os.makedirs(plot_dir, exist_ok=True)

# Load data
df = pd.read_json('data/catalysis.json')

# Catalyst Performance Analysis
sns.set(style="whitegrid")

# --- Scatter Plot: TOF vs. Temperature ---
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df, x="Temperature (°C)", y="TOF (s⁻¹)", 
    hue="Catalyst Type", style="Catalyst Type", s=100, edgecolor="black"
)
plt.xlabel("Temperature (°C)")
plt.ylabel(r"Turnover Frequency (TOF) ($\mathregular{s^{-1}}$)")
plt.title("Turnover Frequency vs. Temperature")
plt.legend(title="Catalyst Type", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., ncol=2)
plt.savefig(os.path.join(plot_dir, "TOF_vs_Temperature.png"), dpi=300, bbox_inches="tight")
plt.show()

# --- Scatter Plot: Selectivity vs. Adsorption Energy ---
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df, x="Adsorption Energy (eV)", y="Selectivity (%)", 
    hue="Catalyst Type", style="Catalyst Type", s=100, edgecolor="black"
)
plt.xlabel("Adsorption Energy (eV)")
plt.ylabel("Selectivity (%)")
plt.title("Selectivity vs. Adsorption Energy")
plt.legend(title="Catalyst Type", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., ncol=2)
plt.savefig(os.path.join(plot_dir, "Selectivity_vs_Adsorption_Energy.png"), dpi=300, bbox_inches="tight")
plt.show()

# --- Scatter Plot: Stability vs. TOF ---
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df, x="TOF (s⁻¹)", y="Stability (h)", 
    hue="Catalyst Type", style="Catalyst Type", s=100, edgecolor="black"
)
plt.xlabel(r"Turnover Frequency (TOF) ($\mathregular{s^{-1}}$)")
plt.ylabel("Stability (h)")
plt.title("Stability vs. Turnover Frequency")
plt.legend(title="Catalyst Type", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., ncol=2)
plt.savefig(os.path.join(plot_dir, "Stability_vs_TOF.png"), dpi=300, bbox_inches="tight")
plt.show()

# Emissions Reduction & Sustainability

# --- Scatter Plot: CO₂ Conversion Efficiency vs. Stability ---
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df, x="Stability (h)", y="CO₂ Conversion Efficiency (%)", 
    hue="Catalyst Type", style="Catalyst Type", s=100, edgecolor="black"
)
plt.xlabel("Stability (h)")
plt.ylabel(r"CO$_2$ Conversion Efficiency (%)")
plt.title(r"CO$_2$ Conversion Efficiency vs. Stability")
plt.legend(title="Catalyst Type", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., ncol=2)
plt.savefig(os.path.join(plot_dir, "CO2_Conversion_vs_Stability.png"), dpi=300, bbox_inches="tight")
plt.show()

# --- Line Plot: CO₂ Conversion Efficiency vs. Temperature ---
plt.figure(figsize=(12, 8))
sns.lineplot(
    data=df, x="Temperature (°C)", y="CO₂ Conversion Efficiency (%)", 
    hue="Catalyst Type", marker="o"
)
plt.xlabel("Temperature (°C)")
plt.ylabel(r"CO$_2$ Conversion Efficiency (%)")
plt.title(r"CO$_2$ Conversion Efficiency vs. Temperature")
plt.legend(title="Catalyst Type", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., ncol=2)
plt.savefig(os.path.join(plot_dir, "CO2_Conversion_vs_Temperature.png"), dpi=300, bbox_inches="tight")
plt.show()

# --- Bar Chart: Emissions Reduction vs. Catalyst Type ---
plt.figure(figsize=(12, 8))
sns.barplot(
    data=df, x="Catalyst Type", y="Emissions Reduction (kg CO-eq)", 
    estimator=sum, ci=None, palette="viridis"
)
plt.xlabel("Catalyst Type")
plt.ylabel(r"Emissions Reduction (kg CO$_2$-eq)")
plt.title("Emissions Reduction by Catalyst Type")
plt.xticks(rotation=45, ha="right")
plt.savefig(os.path.join(plot_dir, "Emissions_Reduction_by_Catalyst.png"), dpi=300, bbox_inches="tight")
plt.show()

# Process Efficiency & Operating Conditions

# --- Scatter Plot: Activation Energy (kJ/mol) vs. TOF (s⁻¹) ---
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df, x="TOF (s⁻¹)", y="Activation Energy (kJ/mol)", 
    hue="Catalyst Type", style="Catalyst Type", s=100, edgecolor="black"
)
plt.xlabel(r"Turnover Frequency (TOF) ($\mathregular{s^{-1}}$)")
plt.ylabel("Activation Energy (kJ/mol)")
plt.title(r"Activation Energy vs. Turnover Frequency")
plt.legend(title="Catalyst Type", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., ncol=2)
plt.savefig(os.path.join(plot_dir, "Activation_Energy_vs_TOF.png"), dpi=300, bbox_inches="tight")
plt.show()

# --- Scatter Plot: Pressure (bar) vs. TOF (s⁻¹) ---
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df, x="TOF (s⁻¹)", y="Pressure (bar)", 
    hue="Catalyst Type", style="Catalyst Type", s=100, edgecolor="black"
)
plt.xlabel(r"Turnover Frequency (TOF) ($\mathregular{s^{-1}}$)")
plt.ylabel("Pressure (bar)")
plt.title(r"Pressure vs. Turnover Frequency")
plt.legend(title="Catalyst Type", bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0., ncol=2)
plt.savefig(os.path.join(plot_dir, "Pressure_vs_TOF.png"), dpi=300, bbox_inches="tight")
plt.show()

# Overall Correlation Analysis

# Ensure Catalyst Type is categorical
df["Catalyst Type"] = df["Catalyst Type"].astype("category")

# Drop non-numeric columns before correlation calculation
df_numeric = df.select_dtypes(include=["number"])

# Compute correlation matrix
corr_matrix = df_numeric.corr()

# Set up the figure
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

# Generate heatmap
sns.heatmap(
    corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5
)
plt.title("Correlation Heatmap of Catalyst Properties and Performance Metrics")
plt.savefig(os.path.join(plot_dir, "Correlation_Heatmap.png"), dpi=300, bbox_inches="tight")
plt.show()
