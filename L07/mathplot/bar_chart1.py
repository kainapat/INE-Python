import matplotlib.pyplot as plt
def main():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    bar_witdth = 5
    plt.bar(left_edges, heights, bar_witdth)
    plt.show()
main()