{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOYYIizIZEcdgxsZiC13elE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LuchoValr/Pruebas-codigos/blob/main/plot_decision_regions_script_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "k5ZJkwNAvx3Q"
      },
      "outputs": [],
      "source": [
        "from matplotlib.colors import ListedColormap\n",
        "def plot_decision_regions(X, y, classifier, resolution=0.02):\n",
        "  # setup marker generator and color map\n",
        "  markers = ('o', 's', '^', 'v', '<')\n",
        "  colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')\n",
        "  cmap = ListedColormap(colors[:len(np.unique(y))])\n",
        "  # plot the decision surface\n",
        "  x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1\n",
        "  x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1\n",
        "  xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),\n",
        "                         np.arange(x2_min, x2_max, resolution))\n",
        "  lab = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)\n",
        "  lab = lab.reshape(xx1.shape)\n",
        "  plt.contourf(xx1, xx2, lab, alpha=0.3, cmap=cmap)\n",
        "  plt.xlim(xx1.min(), xx1.max())\n",
        "  plt.ylim(xx2.min(), xx2.max())\n",
        "  # plot class examples\n",
        "  for idx, cl in enumerate(np.unique(y)):\n",
        "    plt.scatter(x=X[y == cl, 0],\n",
        "    y=X[y == cl, 1],\n",
        "    alpha=0.8,\n",
        "    c=colors[idx],\n",
        "    marker=markers[idx],\n",
        "    label=f'Class {cl}',\n",
        "    edgecolor='black')"
      ]
    }
  ]
}