from plotter import Plotter

def main():
    # Инициализация Plotter
    plotter = Plotter()

    # Путь к JSON файлу
    json_file = "deviation.json"

    # Построение и сохранение графиков
    plots_paths = plotter.draw_plots(json_file)

    # Отображение путей к графикам
    for path in plots_paths:
        print(f'График сохранен по пути: {path}')

if __name__ == "__main__":
    main()
