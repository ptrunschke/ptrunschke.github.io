import os

html = ""
outputs_and_sizes = []

for size in [16, 32, 48, 64, 96, 128, 196, 228, 256]:
    output = "favicon-{size}x{size}.png".format(size=size)
    html += "<link rel=\"icon\" type=\"image/png\" sizes=\"{size}x{size}\" href=\"/{output}\">\n".format(size=size, output=output)
    outputs_and_sizes.append((output, size))

for size in [57, 60, 72, 76, 114, 120, 144, 152, 180]:
    output = "apple-touch-icon-{size}x{size}.png".format(size=size)
    html += "<link rel=\"apple-touch-icon\" sizes=\"{size}x{size}\" href=\"/{output}\">\n".format(size=size, output=output)
    outputs_and_sizes.append((output, size))

for output, size in outputs_and_sizes:
    os.system("inkscape --export-filename={output} -w {size} -h {size} icon.svg".format(size=size, output=output))

html += "<link rel=\"mask-icon\" href=\"/mask_icon.svg\" color=\"#ee4c2c\">\n"
html += "<meta name=\"theme-color\" content=\"#e8e8e8\">\n"

with open("_includes/head_custom.html", "a") as f:
    f.write(html)
