"""OpenPi enclosure v0.2: printable prototype geometry, not a tested product.
Run with FreeCAD's Python. All dimensions mm; fastener lengths exclude heads.
"""
from pathlib import Path
import math, json
import FreeCAD as App
import Part, MeshPart

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'v0.2'
(OUT/'STL').mkdir(parents=True,exist_ok=True)
W,D=262.,250.
AY,AZ=255.,44.5
HINGES=(20.,206.)
BASE_FIX=[(x,y) for x in (8.,254.) for y in (8.,181.,242.)]
LID_FIX=[(x,y) for x in (8.,254.) for y in (8.,125.,242.)]
CLAMP_FIX=[(x,y) for x in (9.,253.) for y in (45.,145.)]
V=App.Vector

def box(w,d,h,x=0,y=0,z=0): return Part.makeBox(w,d,h,V(x,y,z))
def cyl(r,h,x,y,z,axis=V(0,0,1)): return Part.makeCylinder(r,h,V(x,y,z),axis)
def join(shapes):
    result=shapes[0]
    for s in shapes[1:]: result=result.fuse(s)
    return result.removeSplitter()
def hexhole(af,h,x,y,z):
    r=af/math.sqrt(3)
    pts=[V(x+r*math.cos(math.radians(30+60*i)),y+r*math.sin(math.radians(30+60*i)),z) for i in range(6)]
    return Part.Face(Part.makePolygon(pts+[pts[0]])).extrude(V(0,0,h))
def sector(x,length,y,z,r0,r1,a0,a1):
    # 1-degree segmented arcs keep printable stops explicit and reproducible.
    count=max(2,int(abs(a1-a0)))
    angles=[math.radians(a0+(a1-a0)*i/count) for i in range(count+1)]
    pts=[V(x,y+r1*math.cos(a),z+r1*math.sin(a)) for a in angles]
    pts += [V(x,y+r0*math.cos(a),z+r0*math.sin(a)) for a in reversed(angles)]
    return Part.Face(Part.makePolygon(pts+[pts[0]])).extrude(V(length,0,0))
def lid_closed(s):
    s=s.copy();s.rotate(V(0,0,0),V(0,1,0),180);s.translate(V(W,0,73));return s
def opened(s,angle=110):
    s=lid_closed(s);s.rotate(V(0,AY,AZ),V(1,0,0),-angle);return s
def shell(w,d,h,wall=3): return box(w,d,h).cut(box(w-2*wall,d-2*wall,h,wall,wall,3))

# BASE: 3 mm floor, structural towers with underside driver wells.
base=shell(W,D,39)
for x,y in BASE_FIX:
    base=base.fuse(cyl(6,39,x,y,0))
    base=base.cut(cyl(4.1,31.5,x,y,-1)).cut(cyl(1.7,12.5,x,y,30.5))
for x,y in CLAMP_FIX: base=base.cut(cyl(4.1,5,x,y,-1))
# Pi 5, rotated 180 degrees: USB ports face left, USB-C toward rear.
# Board reference 85 x 56; 58 x 49 hole pitch. Recheck physical board.
PI_HOLES=[(106-u,244-v) for u in (3.5,61.5) for v in (3.5,52.5)]
for x,y in PI_HOLES: base=base.cut(cyl(1.45,5,x,y,-1))
# Broad service openings allow real plugs to be checked before refining.
base=base.cut(box(5,59,27,-1,183,6))
base=base.cut(box(54,5,22,55,246,5))
base=base.cut(box(34,5,20,114,246,23))
# Bottom ventilation in electronics bay, clear of screw mounting points.
for x in range(50,94,7): base=base.cut(box(3,27,5,x,205,-1))
for x in range(158,231,9): base=base.cut(box(3,33,5,x,199,-1))
# Integral fixed hinge forks and positive opening stops.
for hx in HINGES:
    for xx in (hx,hx+28):
        lug=join([box(8,11,13.5,xx,244,31),cyl(7,8,xx,AY,AZ,V(1,0,0))])
        lug=lug.cut(cyl(2.2,10,xx-1,AY,AZ,V(1,0,0)))
        base=base.fuse(lug)
    stop=sector(hx+13,10,AY,AZ,7.4,11.5,-135,-110)
    base=base.fuse(stop)
base=base.removeSplitter()

# DECK: two-millimetre lip over the keyboard's plastic perimeter.
deck=box(W,D,4,0,0,39).cut(box(226,156,6,18,16,38))
for hx in HINGES:
    for xx in (hx,hx+28): deck=deck.cut(box(8.6,7,6,xx-.3,243.7,38))
    deck=deck.cut(box(36.6,3.2,6,hx-.3,247.8,38))
deck=deck.cut(box(34,5,6,114,246,38))
for x,y in BASE_FIX:
    deck=deck.cut(hexhole(5.8,2.6,x,y,39)).cut(cyl(1.7,3.5,x,y,39))
for x,y in CLAMP_FIX:
    post=cyl(5.5,27,x,y,12)
    post=post.cut(hexhole(5.8,2.6,x,y,12)).cut(cyl(1.7,5.5,x,y,12))
    deck=deck.fuse(post)
for x in range(32,97,7): deck=deck.cut(box(3,22,6,x,208,38))
deck=deck.removeSplitter()

# Lower keyboard rails stop against posts at z=12; pads end at z=13.
rails=[]
for left in (True,False):
    x0=4 if left else 238
    sx=9 if left else 253
    rail=box(20,137,3,x0,25,9)
    for y in (45,145):rail=rail.cut(cyl(1.7,5,sx,y,8))
    rails.append(rail)

# LID: padded cradle avoids relying on unknown display screw engagement.
lid=shell(W,D,22)
for x,y in LID_FIX:
    lid=lid.fuse(cyl(6,22,x,y,0))
    lid=lid.cut(cyl(4.1,14.5,x,y,-1)).cut(cyl(1.7,10,x,y,13.5))
# Rounded-up official 7-inch envelope 189.5 x 120 x 15.
SX,SY=(W-189.5)/2,(D-120)/2
cradle=box(195.5,126,3,SX-3,SY-3,3).cut(box(190.5,121,5,SX-.5,SY-.5,2))
lid=lid.fuse(cradle)
lid=lid.cut(box(34,5,21,114,246,3))
for hx in HINGES:
    xx=hx+8.5
    lug=join([box(19,11,13.5,xx,244,15),cyl(7,19,xx,AY,28.5,V(1,0,0)),sector(hx+13,10,AY,28.5,6.5,11,-6,0)])
    lug=lug.cut(cyl(2.2,21,xx-1,AY,28.5,V(1,0,0)))
    lid=lid.fuse(lug)
lid=lid.removeSplitter()
bezel=box(W,D,5,0,0,22).cut(box(157.5,90,7,(W-157.5)/2,(D-90)/2,21))
for x,y in LID_FIX:
    bezel=bezel.cut(hexhole(5.8,2.6,x,y,22)).cut(cyl(1.7,4,x,y,22))
for hx in HINGES:
    bezel=bezel.cut(box(19.6,7,7,hx+8.2,243.7,21))
    bezel=bezel.cut(box(36.6,3.2,7,hx-.3,247.8,21))
bezel=bezel.cut(box(34,5,7,114,246,21)).removeSplitter()

parts={'base':base,'keyboard_deck':deck,'keyboard_rail_left':rails[0],'keyboard_rail_right':rails[1],'lid_back':lid,'display_bezel':bezel}
doc=App.newDocument('OpenPiEnclosureV02')
objs=[]
checks={}
for name,s in parts.items():
    assert s.isValid() and len(s.Solids)==1,(name,s.isValid(),len(s.Solids))
    obj=doc.addObject('PartDesign::Feature',name)
    obj.Label=name.replace('_',' ').title()+' [prototype v0.2]'
    obj.Shape=s
    obj.addProperty('App::PropertyString','Status');obj.Status='Designed; physical fit and strength NOT tested'
    objs.append(obj)
    printable=s.copy();b=printable.BoundBox;printable.translate(V(-b.XMin,-b.YMin,-b.ZMin))
    mesh=MeshPart.meshFromShape(Shape=printable,LinearDeflection=.10,AngularDeflection=.15,Relative=False)
    mesh.write(str(OUT/'STL'/f'{name}.stl'))
    checks[name]={'valid_solid':True,'size_mm':[round(b.XLength,3),round(b.YLength,3),round(b.ZLength,3)],'mesh_facets':mesh.CountFacets,'mesh_closed':mesh.isSolid()}
    assert mesh.isSolid(),name
    assert b.XLength<=270 and b.YLength<=270 and b.ZLength<=256,name

# Static manufactured-part interference checks (touching surfaces allowed).
static_pairs=[('base','keyboard_deck'),('base','keyboard_rail_left'),('base','keyboard_rail_right'),('keyboard_deck','keyboard_rail_left'),('keyboard_deck','keyboard_rail_right'),('lid_back','display_bezel')]
for a,b in static_pairs:
    vol=parts[a].common(parts[b]).Volume
    assert vol<.01,(a,b,vol)
# Electronics envelopes: keyboard nominal 26 maximum, Pi assembly envelope 28.
keyboard=box(230,160,26,16,14,13)
pi_board=box(85,56,1.6,21,188,9)
pi_clear=box(85,56,28,21,188,9)
for name in ('base','keyboard_deck','keyboard_rail_left','keyboard_rail_right'):
    assert parts[name].common(keyboard).Volume<.01,('keyboard collision',name)
for name in ('base','keyboard_deck'):
    assert parts[name].common(pi_clear).Volume<.01,('Pi collision',name)
# Sweep the moving printed lid; stop deliberately interferes beyond 110 deg.
fixed=join([base,deck]+rails)
moving=join([lid,bezel])
angles=[0,5,15,30,45,60,75,90,100,105,110]
sweep={str(a):round(fixed.common(opened(moving,a)).Volume,6) for a in angles}
if max(sweep.values())>=.02:
    for a in (0,110):
        for fn in ('base','keyboard_deck'):
            for mn in ('lid_back','display_bezel'):
                hit=parts[fn].common(opened(parts[mn],a))
                if hit.Volume>.01: print('COLLISION',a,fn,mn,hit.Volume,str(hit.BoundBox))
assert max(sweep.values())<.02,('hinge sweep',sweep)
overtravel=fixed.common(opened(moving,112)).Volume
assert overtravel>.1,('stop did not engage',overtravel)
checks['hinge_sweep']={'angles_degrees':angles,'interference_mm3':sweep,'stop_interference_at_112_deg_mm3':round(overtravel,3),'scope':'Rigid printed geometry only; cables and deformation not simulated'}

# Coupon geometry is cut from the actual hinge; same axis and washer gaps.
coupons={'hinge_fixed_coupon':base.common(box(44,28,28,16,240,27)),
         'hinge_moving_coupon':lid.common(box(32,28,26,22,240,12))}
for name,s in coupons.items():
    assert s.isValid() and len(s.Solids)==1,(name,len(s.Solids))
    b=s.BoundBox;s.translate(V(-b.XMin,-b.YMin,-b.ZMin))
    mesh=MeshPart.meshFromShape(Shape=s,LinearDeflection=.10,AngularDeflection=.15,Relative=False)
    mesh.write(str(OUT/'STL'/f'{name}.stl'))

# Assembly document uses the open position and includes reference envelopes.
assembly=App.newDocument('OpenPiAssemblyV02')
render=[]
for name,s in parts.items():
    shown=opened(s) if name in ('lid_back','display_bezel') else s
    ob=assembly.addObject('PartDesign::Feature',name);ob.Shape=shown
    render.append((name,shown,'#3c5066' if name in ('base','lid_back') else '#6b8096'))
display=box(189.5,120,15,SX,SY,6)
screen=box(154.5,87,.15,(W-154.5)/2,(D-87)/2,21)
references=[('Keyboard_reference',keyboard,'#202a35'),('Pi_reference',pi_board,'#319974'),('Display_reference',opened(display),'#192b40'),('Screen_reference',opened(screen),'#4dd1bd')]
for name,s,color in references:
    ob=assembly.addObject('PartDesign::Feature',name);ob.Label=name+' (not measured)';ob.Shape=s
    render.append((name,s,color))
# Smooth fastener visualizations are not thread models or manufacturing parts.
for hx in HINGES:
    screw=join([cyl(2,45,hx-.8,AY,AZ,V(1,0,0)),cyl(3.5,4,hx-4.8,AY,AZ,V(1,0,0))])
    ob=assembly.addObject('PartDesign::Feature','Hinge_axis');ob.Shape=screw
    render.append(('M4 hinge axis',screw,'#d3b56e'))
doc.recompute();assembly.recompute()
doc.saveAs(str(OUT/'openpi-parts.FCStd'))
assembly.saveAs(str(OUT/'openpi-assembly.FCStd'))
Part.export(list(assembly.Objects),str(OUT/'openpi-assembly.step'))
Part.export(objs,str(OUT/'openpi-parts.step'))
(OUT/'checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')

# Real CAD tessellation for deterministic previews, not an AI illustration.
scenes={}
for scene,items in [('open',render),('underside',[('base',base,'#607891')]),('hinge',[('fixed',base.common(box(46,32,34,15,239,24)),'#607891'),('moving',opened(lid).common(box(50,50,50,15,240,24)),'#d3b56e')])]:
    triangles=[]
    for name,s,color in items:
        verts,faces=s.tessellate(.35)
        for face in faces:triangles.append({'v':[[verts[i].x,verts[i].y,verts[i].z] for i in face],'color':color})
    scenes[scene]=triangles
(OUT/'preview-mesh.json').write_text(json.dumps(scenes),encoding='utf-8')
print(json.dumps({'printed_parts':len(parts),'checks':checks,'output':str(OUT)},indent=2))
