from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_form import Ui_Widget
import pandas as pd
import matplotlib.pyplot as plt

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btn_file.clicked.connect(self.Read)
        self.ui.btn_calc.clicked.connect(self.Calc_statistics)
        self.ui.btn_bubble.clicked.connect(self.Draw_bubble)
        self.ui.btn_scatter_matrix.clicked.connect(self.Scatter_plot)
        self.ui.btn_par_coord.clicked.connect(self.Par_coord)
        self.columns = [[]]

    def Read(self):
        file, checked = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        
        if file:
            with open(file, 'r') as file1:
                lines = file1.readlines()

            columns = [[] for _ in range(len(lines[0].split()))]

            for line in lines:
                line = line.strip()
                values = line.split()

                for i, value in enumerate(values):
                 columns[i].append(float(value))
            self.columns = columns
            

          
        table_view = self.ui.tableView
        if table_view.model() is not None:
            table_view.setModel(None)

        model = QStandardItemModel()

        num_rows = len(self.columns[0])
        num_cols = len(self.columns)
        model.setRowCount(num_rows)
        model.setColumnCount(num_cols)

        for i, row in enumerate(self.columns):
            for j, item in enumerate(row):
                model.setData(model.index(j, i), str(item))

        self.columns = list(zip(*self.columns))

        table_view.setModel(model)
        table_view.show()
    
    def Calc_statistics(self):
        df = pd.DataFrame(self.columns)
        description = df.describe()
        table_view = self.ui.tableView_2
        if table_view.model() is not None:
            table_view.setModel(None)

        model = QStandardItemModel()
        model.setColumnCount(len(description.columns))
        model.setRowCount(len(description.index))
        for i, (index, row) in enumerate(description.iterrows()):
            model.setVerticalHeaderItem(i, QStandardItem(index))
            for j, value in enumerate(row):
                item = QStandardItem(str(round(value,4)))
                model.setItem(i, j, item)
        
        table_view.setModel(model)
        table_view.show()

    def Draw_bubble(self):
        self.columns = list(zip(*self.columns))
        if len(self.columns) == 3:
            plt.scatter(self.columns[0], self.columns[1], s=self.columns[2])
            plt.show()
        self.columns = list(zip(*self.columns))

    def Scatter_plot(self):
        df = pd.DataFrame(self.columns)
        pd.plotting.scatter_matrix(df)
        plt.show()

    def Par_coord(self):
        fig, ax = plt.subplots()
        for i, col in enumerate(self.columns):
            ax.plot(range(len(col)), col, color='#FF5733')
        ax.set_xticks(range(len(col)))
        ax.set_xticklabels(['Column{}'.format(i+1) for i in range(len(col))])
        plt.show()


