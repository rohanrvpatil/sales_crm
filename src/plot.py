import matplotlib.pyplot as plt
import streamlit as st


class Plot:
    def __init__(self, data):
        self.data = data
        plt.rcParams.update({"font.size": 14})

    def show(self):
        plt.tight_layout()
        st.pyplot(plt)


class PieChart(Plot):
    def __init__(self, data, title):
        super().__init__(data)
        self.title = title

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.pie(self.data.values, labels=self.data.index, autopct="%1.1f%%")
        plt.title(self.title)
        self.show()


class BarChart(Plot):
    def __init__(self, data, title, xlabel, ylabel):
        super().__init__(data)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self):
        colors = plt.cm.tab10(range(len(self.data)))
        plt.figure(figsize=(10, 8))
        plt.grid(True)
        plt.bar(self.data.index, self.data.values, color=colors)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xticks(rotation=45)
        self.show()


class LineChart(Plot):
    def __init__(self, data, title, xlabel, ylabel):
        super().__init__(data)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(
            self.data.index, self.data.values, linestyle="-", color="g", linewidth=2.5
        )
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(True)
        self.show()
