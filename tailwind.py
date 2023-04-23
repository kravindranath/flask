import os
from os.path import exists

if not (exists('tailwind.config.js')):
    os.system('tailwindcss.3.3.1.exe init')

if (exists('tailwindcss.3.3.1.exe')):
    os.system('tailwindcss.3.3.1.exe -i static/tailwind/3.3.1/input.css -o static/tailwind/3.3.1/output.css --watch --minify')
