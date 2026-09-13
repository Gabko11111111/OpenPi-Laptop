"""Generate a documented space-planning model, NOT a fabrication model."""
import os
import json
import FreeCAD as App
import Part

HERE = os.path.dirname(os.path.abspath(__file__))
doc = App.newDocument("OpenPiLayout")

def box(w, d, h, x=0, y=0, z=0):
    return Part.makeBox(w, d, h, App.Vector(x, y, z))

def add(name, label, shape):
    obj = doc.addObject("PartDesign::Feature", name)
    obj.Label = label
    obj.Shape = shape
    obj.addProperty("App::PropertyString", "DesignStatus")
    obj.DesignStatus = "PRELIMINARY ENVELOPE - NOT FOR FABRICATION"
    return obj

# Front is y=0. Component dimensions are conservative planning envelopes.
base = add("BaseEnvelope", "Base shell envelope 250 x 250 x 42", box(250,250,42).cut(box(244,244,40,3,3,3)))
keyboard = add("KeyboardReserve", "Keyboard reserve 230 x 160 x 26 (unverified)", box(230,160,26,10,10,13))
pi = add("PiReserve", "Pi assembly reserve 85 x 58 x 30 (unverified)", box(85,58,30,12,180,7))
cable = add("CableReserve", "USB cable and connector reserve (routing unverified)", box(125,58,30,110,180,7))

# Display lid shown beside the base in a flat layout.
lid = add("LidEnvelope", "Lid envelope, flat exploded view", box(250,250,22,280,0,0).cut(box(244,244,21,283,3,3)))
screen = add("DisplayReserve", "7 inch display reserve, depth unverified", box(189.32,120.24,16,310.34,64.88,3))

doc.recompute()
objects = [base, keyboard, pi, cable, lid, screen]
checks = {o.Name: {"valid": o.Shape.isValid(), "solids": len(o.Shape.Solids)} for o in objects}
assert all(c["valid"] and c["solids"] == 1 for c in checks.values())
# Envelope collision checks only; they do not validate detailed mechanical fit.
for first, second in [(base,keyboard),(base,pi),(base,cable),(keyboard,pi),(keyboard,cable),(pi,cable),(lid,screen)]:
    assert first.Shape.common(second.Shape).Volume < 0.001, (first.Name,second.Name)
doc.saveAs(os.path.join(HERE,"openpi-layout.FCStd"))
Part.export(objects, os.path.join(HERE,"openpi-layout.step"))
with open(os.path.join(HERE,"layout-checks.json"),"w",encoding="utf-8") as f:
    json.dump({"scope":"Preliminary envelopes only; physical fit unverified", "objects":checks},f,indent=2)
print("Saved FCStd and STEP; six valid solids; tested envelope pairs do not overlap.")
