from OCC.Display.SimpleGui import init_display
from OCC.Core.gp import gp_Pln
from OCC.Core.gp import gp_Pnt, gp_Vec
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Core.BOPAlgo import BOPAlgo_MakerVolume, BOPAlgo_Builder
from OCC.Core.BRep import BRep_Builder

if __name__ == "__main__":
    display, start_display, add_menu, add_function_to_menu = init_display()

    display.DisplayShape(gp_Pnt())

    display.FitAll()
    start_display()
