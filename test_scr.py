import imgkit
import subprocess

def main():
  subprocess.run(['wkhtmltoimage', 'preview.html', 'preview.png'])

if __name__ == '__main__':
    main()
