# Vanguard Toggler

![random photo](https://staticr1.blastingcdn.com/media/photogallery/2020/4/14/660x290/b_502x220/valorant-players-have-expressed-their-worries-about-the-games-vanguard-anti-cheat-image-source-in-game-screenshot_2440431.jpg)

Riot's new game, VALORANT, uses an anti-cheat that is always on unless you disable it. This tool provides an easy way to enable and disable Vanguard (vgc) services.

# F.A.Q.
## How do I install this?

Install [Python 3](https://www.python.org/download/releases/3.0/)

Python 3 should come with pip, you can check with command ```py -m pip``` and if it didn't you can get it [here](https://pip.pypa.io/en/stable/installing/)

Download the source files and extract them where you want. For example ```C:\path\to\source```

Open powershell/command prompt and navigate to the downloaded files by typing ```cd C:\path\to\source```

Run ```py -m pip install infi.systray pypiwin32```

Then run ```py app.py``` and you will see the new icons in your system tray.

## I'm not computer savvy, is there an easier way?

Eventually, you will be able to download it [here](https://github.com/reptoralabs/Vanguard-Toggler/releases). I am currently having trouble building an executable file.

## How do I use this?

Build it or run the .exe file and it will appear in your system tray(?) area. Right click the program to disable and enable Vanguard Services as well as quit the program.

Legend: 

![Off](https://www.iconfinder.com/icons/132716/download/png/16) Vanguard Services are OFF

![On](https://cdn4.iconfinder.com/data/icons/6x16-free-application-icons/16/OK.png) Vanguard Services are ON

![Warn](https://cdn4.iconfinder.com/data/icons/6x16-free-application-icons/16/Warning.png) Cannot detect Vanguard Services(Is it installed?)

## Why does your code look like ass?

I'm a beginner and copy-paste code from about a dozen different sites.

## How does this work?

If you open your command prompy (Windows Key + R) and enter ```services.msc```, you will see all the services available on your computer that you can enable\disable. This program\script basically provides a shortcut to doing this.

## Will you keep this update?

Probably not, someone will likely have to fork it. 
