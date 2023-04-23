import os
from os.path import exists

if not (exists('tailwind.config.js')):
    os.system('tailwindcss.3.3.1.exe init')

if (exists('tailwindcss.3.3.1.exe')):
    os.system('tailwindcss.3.3.1.exe -i webapp/static/tailwind/3.3.1/main.css -o webapp/static/tailwind/3.3.1/main.min.css --watch --minify')
