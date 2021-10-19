from gl import *



def gourad(render, **kwargs):
  # barycentric
  w, v, u = kwargs['bar']
  # texture
  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)
  # normals
  nA, nB, nC = kwargs['varying_normals']

  # light intensity
  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC

  return color(
      int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
      int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
      int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
    )


import random




r = Render(800, 800)


t = Texture('./models/mueble.bmp')
r.light = V3(0, 1, 1)

r.active_texture = t

r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/mueble.obj', translate=(0.6, -0.8, 0), scale=(1, 1, 1), rotate=(0, 5, 0))
r.draw_arrays('TRIANGLES')

t = Texture('./models/normal.bmp')
r.light = V3(0, 1, 1)

r.active_texture = t

r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/lucas.obj', translate=(0, -0.8, 0), scale=(1, 1, 1), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')


t = Texture('./models/lampara.bmp')
r.light = V3(0, 1, 1)

r.active_texture = t

r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/lampara.obj', translate=(0, 1, 0), scale=(1, 1, 1), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')

t = Texture('./models/lupa.bmp')
r.light = V3(0, 1, 1)

r.active_texture = t

r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/lupa.obj', translate=(-0.1, -0.7, 0), scale=(1, 1, 1), rotate=(0, 1, 0.5))
r.draw_arrays('TRIANGLES')


t = Texture('./models/tv.bmp')
r.light = V3(0, 1, 1)

r.active_texture = t

r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/tv.obj', translate=(0.6, -0.25, 0), scale=(1, 1, 1), rotate=(0, -1.2, 0))
r.draw_arrays('TRIANGLES')

t = Texture('./models/sillon.bmp')
r.light = V3(0, 1, 1)

r.active_texture = t

r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/sillon.obj', translate=(-0.7, -0.8, 0), scale=(0.6, 0.6, 0.6), rotate=(0, 1.9, 0))
r.draw_arrays('TRIANGLES')


r.display('gabriel.bmp')
print('Se ha creado el archivo "gabriel.bmp"')

