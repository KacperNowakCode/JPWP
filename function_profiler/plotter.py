import matplotlib.pyplot as plt
import csv
import seaborn as sns

def plot_results(results, output_file=None):
    sns.set_theme(style="whitegrid")  
    names, times = zip(*results.items())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, times, color=sns.color_palette("pastel"))

    plt.yscale('log')
    plt.ylabel('Czas wykonania (ms, skala log)', fontsize=12)
    plt.title('Porównanie czasów wykonania operacji', fontsize=14, weight='bold')
    plt.xticks(rotation=35, ha='right', fontsize=10)
    plt.yticks(fontsize=10)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.1f}',
            ha='center',
            va='bottom',
            fontsize=9,
            rotation=0
        )

    plt.tight_layout()

    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
    else:
        plt.show()


def export_results(results, csv_file=None, html_file=None):
    if csv_file:
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Function','Time_ms'])
            for k,v in results.items():
                writer.writerow([k, f"{v:.2f}"])
