import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_palette("colorblind")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

revenue = [12000, 13500, 15000, 17000, 18500, 20000,
           22000, 25000, 27000, 30000, 32000, 35000]

df = pd.DataFrame({
    "Month": months,
    "Revenue": revenue
})

plt.figure(figsize=(10,6))
plt.plot(df["Month"], df["Revenue"], marker='o')

plt.title("Revenue Grew Consistently Across the Year in Amman Digital Market")
plt.xlabel("Month")
plt.ylabel("Revenue (JOD)")

max_value = df["Revenue"].max()
max_month = df.loc[df["Revenue"].idxmax(), "Month"]

plt.annotate(f"Peak: {max_value}",
             (max_month, max_value),
             textcoords="offset points",
             xytext=(0,10),
             ha='center')

plt.tight_layout()


output_path = Path(__file__).resolve().parent / "chart.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight')

plt.show()