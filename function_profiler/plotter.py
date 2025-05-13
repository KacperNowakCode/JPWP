import matplotlib.pyplot as plt
import csv
import json


def plot_results(results, output_file=None):
    names, times = zip(*results.items())
    plt.figure()
    plt.bar(names, times)
    plt.xticks(rotation=45, ha='right')
    plt.title('Profiling Times (ms)')
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()


def export_results(results, csv_file=None, html_file=None):
    if csv_file:
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Function','Time_ms'])
            for k,v in results.items():
                writer.writerow([k, f"{v:.2f}"])
    if html_file:
        html = ['<table border="1"><tr><th>Function</th><th>Time (ms)</th></tr>']
        for k,v in results.items():
            html.append(f"<tr><td>{k}</td><td>{v:.2f}</td></tr>")
        html.append('</table>')
        with open(html_file,'w') as f:
            f.write(''.join(html))