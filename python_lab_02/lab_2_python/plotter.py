import matplotlib.pyplot as plt 
from circle import Circle
from rectangle import Rectangle


class Shape2DPlotter:
    """Plotterklass som visualiserar 2D-former genom matplotlib,
    skapar figur och axlar med lika skalning,
    ritar cirklar och rektanglar baserat på deras koordinater och mått,
    justerar visningsområdet efter alla formers positioner 
    samt visar en legend och den slutliga plotten."""
    
    @staticmethod
    def plot_shapes(shapes):
        fig, ax = plt.subplots()
        ax.set_aspect('equal') 
        ax.grid(True)

        ax.set_title("2D Shape Plotter")
        handles = []
        labels = []

        for shape in shapes:
            if isinstance(shape, Circle):
                circle = plt.Circle((shape.x, shape.y), shape.radius, fill=False)
                ax.add_patch(circle)  
                handles.append(circle)
                labels.append(f"Circle r={shape.radius}") 

            elif isinstance(shape, Rectangle):
                rect = plt.Rectangle(
                    (shape.x - shape.width / 2, shape.y - shape.height / 2),
                    shape.width, shape.height,
                    fill=False
                )
                ax.add_patch(rect)      
                handles.append(rect)    
                labels.append(f"Rectangle {shape.width}x{shape.height}") 

        all_x = [shape.x for shape in shapes]
        all_y = [shape.y for shape in shapes]
        ax.set_xlim(min(all_x) - 5, max(all_x) + 5)
        ax.set_ylim(min(all_y) - 5, max(all_y) + 5)
        ax.legend(handles, labels)
        plt.show()
       
