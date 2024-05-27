import pandas as pd
import matplotlib.pyplot as plt
import os

class Plotter:
    def __init__(self):
        self.plots_dir = "plots"
        if not os.path.exists(self.plots_dir):
            os.makedirs(self.plots_dir)

    def draw_plots(self, json_file):
        # Чтение JSON файла как pandas DataFrame
        df = pd.read_json(json_file)

        # Построение и сохранение графиков
        plots_paths = []

        # Распределение значений отклонений
        for column in df.columns:
            if column not in ['room_name', 'gt_corners', 'rb_corners']:
                plt.figure(figsize=(10, 6))
                plt.hist(df[column], bins=30, edgecolor='k', alpha=0.7)
                plt.title(f'Distribution of {column}')
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plot_path = os.path.join(self.plots_dir, f'{column}_distribution.png')
                plt.savefig(plot_path)
                plt.close()
                plots_paths.append(plot_path)

        # Сравнение реальных и предсказанных значений углов
        plt.figure(figsize=(10, 6))
        plt.scatter(df['gt_corners'], df['rb_corners'], alpha=0.6)
        plt.plot([df['gt_corners'].min(), df['gt_corners'].max()],
                 [df['gt_corners'].min(), df['gt_corners'].max()],
                 color='red', lw=2)
        plt.xlabel('Ground Truth Corners')
        plt.ylabel('Predicted Corners')
        plt.title('Ground Truth vs Predicted Corners')
        plot_path = os.path.join(self.plots_dir, 'gt_vs_predicted_corners.png')
        plt.savefig(plot_path)
        plt.close()
        plots_paths.append(plot_path)

        return plots_paths
