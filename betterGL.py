import glfw
import moderngl
import numpy as np
from pyrr import Matrix44

glfw.init()
window = glfw.create_window(800, 600, "Rotating Cube", None, None)
glfw.make_context_current(window)

ctx = moderngl.create_context()

vertex_shader = '''
#version 330
in vec3 in_vert;
in vec3 in_color;
out vec3 v_color;
uniform mat4 Mvp;
void main() {
    gl_Position = Mvp * vec4(in_vert, 1.0);
    v_color = in_color;
}
'''

fragment_shader = '''
#version 330
in vec3 v_color;
out vec4 f_color;
void main() {
    f_color = vec4(v_color, 1.0);
}
'''

prog = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

vertices = np.array([
    -1, -1, -1, 1, 0, 0,
     1, -1, -1, 0, 1, 0,
     1,  1, -1, 0, 0, 1,
    -1,  1, -1, 1, 1, 0,
    -1, -1,  1, 1, 0, 1,
     1, -1,  1, 0, 1, 1,
     1,  1,  1, 1, 1, 1,
    -1,  1,  1, 0, 0, 0,
], dtype='f4')

indices = np.array([
    0, 1, 2, 2, 3, 0,
    4, 5, 6, 6, 7, 4,
    0, 4, 7, 7, 3, 0,
    1, 5, 6, 6, 2, 1,
    3, 2, 6, 6, 7, 3,
    0, 1, 5, 5, 4, 0
], dtype='i4')

vbo = ctx.buffer(vertices.tobytes())
ibo = ctx.buffer(indices.tobytes())
vao = ctx.vertex_array(prog, [(vbo, '3f 3f', 'in_vert', 'in_color')], ibo)

while not glfw.window_should_close(window):
    glfw.poll_events()
    ctx.clear(0.1, 0.1, 0.1)

    angle = glfw.get_time()
    model = Matrix44.from_y_rotation(angle) * Matrix44.from_x_rotation(angle * 0.5)
    proj = Matrix44.perspective_projection(45.0, 800/600, 0.1, 100.0)
    lookat = Matrix44.look_at(
        eye=[3, 3, 3],
        target=[0, 0, 0],
        up=[0, 1, 0]
    )
    mvp = proj * lookat * model

    prog['Mvp'].write(mvp.astype('f4').tobytes())
    vao.render()

    glfw.swap_buffers(window)

glfw.terminate()
