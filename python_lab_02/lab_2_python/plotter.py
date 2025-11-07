# impoterar matplotlib föratt kunna plotta 
# impotera klasserna för att plotta 
import matplotlib.pyplot as plt
from circle import Circle
from rectangle import Rectangle

# skappar en plott klass 
class Shape2DPlotter:

# här skappar vi en matplotlib figur 
    @staticmethod
    def plot_shapes(shapes):
        fig, ax = plt.subplots()
        
        
    # se till att x- och y-axlarna skalas lika
        ax.set_aspect('equal')
    
    # display background för att kunna visualisera kordinaterna bätter 
        ax.grid(True)
        
        # plot titel 
        ax.set_title("2D Shape Plotter")

        # här kommer de ritade figurer förvaras 
        handles = []
        labels = []

        # här loopar den genom alla mönster  
        for shape in shapes:
            
            # om mönstret är cirkel rita den 
            if isinstance(shape, Circle):
                
                # skappa en cirkel tentread på (x, y) med den givna radius 
                circle = plt.Circle((shape.x, shape.y), shape.radius, fill=False)
                ax.add_patch(circle)  
                handles.append(circle)
                labels.append(f"Circle r={shape.radius}") # lägger till namn/label

            # om rektangle rita den
            elif isinstance(shape, Rectangle):
                # rekntangle förväntas var på nedre vänstra hörn, så vi skiftar mitt punkten
                rect = plt.Rectangle(
                    (shape.x - shape.width / 2, shape.y - shape.height / 2),
                    shape.width, shape.height,
                    fill=False
                )
                ax.add_patch(rect)      # lägger till rektanglen i plotten
                handles.append(rect)    
                labels.append(f"Rectangle {shape.width}x{shape.height}") # lägger till namn/label

        # tar allt från x och y cordinaterna för att atomatisk skalningvy
        all_x = [shape.x for s in shapes]
        all_y = [shape.y for s in shapes]
        
        # atomatisk skusterar plotens begrensning så att alla figurer passar in fint
        ax.set_xlim(min(all_x) - 5, max(all_x) + 5)
        ax.set_ylim(min(all_y) - 5, max(all_y) + 5)

        # lägger till legens så att det lenkar figurena och theras namn/lables 
        ax.legend(handles, labels)
        
        # vissar slutliga ploten på skärm 
        plt.show()
       
