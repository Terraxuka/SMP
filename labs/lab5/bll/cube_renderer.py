from math import sin, cos

class CubeRenderer:
    def __init__(self, display):
        self.display = display
        self.A = 3
        self.B = 7
        self.K2 = 400
        self.K1 = self.display.screen_height * self.K2 * 3 / (8 * self.display.screen_width)
        self.chars = ".,-~:;=!*#$@"
        self.cube_size = 3
        self.viewer_shift = [0, 0, 60]  # Shift for the viewer position (inside the cube)

    def calculate_frame(self):
        output = [' '] * self.display.screen_size
        zbuffer = [0] * self.display.screen_size

        vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1],
        ]

        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7),
        ]

        cosA, sinA = cos(self.A), sin(self.A)
        cosB, sinB = cos(self.B), sin(self.B)

        transformed_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            x *= self.cube_size
            y *= self.cube_size
            z *= self.cube_size

            # Rotate around X-axis
            x1 = x
            y1 = y * cosA - z * sinA
            z1 = y * sinA + z * cosA

            # Rotate around Y-axis
            x2 = x1 * cosB - z1 * sinB
            y2 = y1
            z2 = x1 * sinB + z1 * cosB

            # Apply viewer shift
            x2 += self.viewer_shift[0]
            y2 += self.viewer_shift[1]
            z2 += self.viewer_shift[2]

            transformed_vertices.append((x2, y2, z2))

        for edge in edges:
            start, end = transformed_vertices[edge[0]], transformed_vertices[edge[1]]
            x1, y1, z1 = start
            x2, y2, z2 = end

            for t in range(101):
                t /= 100
                x = x1 + t * (x2 - x1)
                y = y1 + t * (y2 - y1)
                z = z1 + t * (z2 - z1)

                if z <= 0:  # Skip points behind the viewer
                    continue

                ooz = 1 / z
                xp = int(self.display.width / 2 / self.display.pixel_width + self.K1 * ooz * x)
                yp = int(self.display.height / 2 / self.display.pixel_height - self.K1 * ooz * y)

                if 0 <= xp < self.display.screen_width and 0 <= yp < self.display.screen_height:
                    position = xp + self.display.screen_width * yp

                    if ooz > zbuffer[position]:
                        zbuffer[position] = ooz
                        luminance_index = int((ooz - 0.5) * 16)  # Scale luminance based on depth
                        output[position] = self.chars[max(0, min(len(self.chars) - 1, luminance_index))]

        return output

    def rotate(self, dA, dB):
        self.A += dA
        self.B += dB

    def set_viewer_shift(self, x, y, z):
        """
        Set the viewer's position shift (the direction and distance the cube is translated).
        """
        self.viewer_shift = [x, y, z]
