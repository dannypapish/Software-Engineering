from polygons import Polygons
import math
import tkinter as tk


class TkinterGUI(Polygons):  # Something is missing here
    # TODO 11: Fix this class so that it inherits from the Polygons class

    def __init__(self, num_sides, side_length):
        super().__init__(num_sides, side_length)

        self.root = tk.Tk()
        self.root.title("Tkinter Polygon Visualizer")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.rotation = 2
        self.root.bind("<Up>", self.increase_sides)
        self.root.bind("<Down>", self.decrease_sides)
        self.root.after(0, self.main_scene)
        self.root.mainloop()
        self.warning = False

    def draw_polygon(self, color, center, rotation):
        points = []

        for i in range(self.num_sides):
            angle = math.radians(360 / self.num_sides * i + rotation)
            x = center[0] + self.radius * math.cos(angle)
            y = center[1] + self.radius * math.sin(angle)
            points.append((x, y))

        self.radius = math.sqrt(self.area / math.pi)
        self.area = self.polygon_area()
        self.canvas.create_polygon(points, fill=color)

    def main_scene(self):

        self.canvas.delete("all")
        self.draw_polygon("purple", (400, 300), self.rotation)

        self.canvas.create_text(400, 10, text=f"Area: {self.area:.2f}")
        self.canvas.create_text(400, 30, text=f"Sides: {self.num_sides}")
        self.canvas.create_text(800, 590, text="Up/Down Arrows to change num_sides",
                                anchor="se")
        self.rotation += 1
        self.root.after(1000 // 60, self.main_scene)

    def increase_sides(self, event):
        self.num_sides += 1

    def decrease_sides(self, event):
        # display a warning if the user tries to decrease the number of sides when it is already 3
        if self.num_sides == 3:
            # show a warning message in huge red text
            self.canvas.create_text(
                400, 300, text="Can't decrease sides below 3!", fill="red", font=("Helvetica", 32))

        else:
            self.num_sides -= 1


def run_tkinter(num_sides, side_length):
    TkinterGUI(num_sides, side_length)


if __name__ == "__main__":
    run_tkinter(3, 100)
