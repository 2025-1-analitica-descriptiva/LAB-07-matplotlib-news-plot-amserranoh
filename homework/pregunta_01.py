"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    input_file = "files/input/news.csv"
    output_dir = "files/plots"

    df = pd.read_csv(input_file, index_col=0)

    plt.figure()
    
    colores = {
        'Television':'dimgray',
        'Newspaper':'grey',
        'Internet':'tab:blue',
        'Radio':'lightgrey'
    }

    orden = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    ancholinea = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        plt.plot(
            df[col], 
            color=colores[col], 
            label=col, 
            zorder=orden[col],
            linewidth=ancholinea[col]
        )

    for col in df.columns:
        first_year=df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colores[col], 
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) +"%",
            ha='right',
            va='center',
            color=colores[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colores[col], 
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha='left',
            va='center',
            color=colores[col],
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center'
    )
    plt.tight_layout()

    if os.path.exists(output_dir):
        for file in glob.glob(f"{output_dir}/*"):
            os.remove(file)

    os.makedirs(output_dir)

    plt.savefig(f"{output_dir}/news.png")
    

  