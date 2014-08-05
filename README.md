Blender NLE
=========

The Non-Linear Video Editor of [Blender] allows you to perform basic actions like video cuts and splicing, as well as more complex tasks like video masking. Check out the video tutorials (playlist) created by [Mikeycal Meyers] to learn how to use Blender as a video editor

I've created some preset settings for the Blender Video Editing UI and Keyboard Shortcuts which are mostly inspired from the commercial software Final Cut Pro.

Also I've included some addons to make life with Blender NLE easier

The files are located in the "import these" folder:

Presets
----
  
  - ##### NLEvideoInterface.blend : 
  the Video Editing interface
 
  - ##### NLE_KeyPreset.py :
  the keyboard shorcuts

Addons
----
  
  - ##### checkforupdates.py :
  Check for new version of Blender available on download page
  ( [Check for Updates Addon page] )
  
  - ##### sequencer_jumptocut.py
  tool collection to help speed up editting videos with blender in the VSE
  ( [Jump to Cut Addon page] )

Download
----
- latest :        [Download] [1]
- version :       2.0.1
- history :       [Cangelog] [3]
- old versions :  [View] [2]

Installation
--------------

The installation of the preset settings and addons is easy :

- For the *Video Editing interface* just open the NLEvideoInterface.blend file from the blender file menu

```
> File -> Open
```

- For the *keyboard shorcuts* just import the NLE_KeyPreset.py file from the User Preferences

```
> File -> User Preferences --> Input --> Import Key Configuration
```

- For the *Addons* just import the files file from the User Preferences

```
> File -> User Preferences --> Addons --> Install from file --> Add a tick to enable
```

Then you should click on "Save User Settings"


- If you want Blender to start up always in the Video Editing mode, just save the startup file

```
> File -> Save Startup File
```

License
----

The contents of this repository are licensed under:
[Artistic License v2.0]


**Free Software, Hell Yeah!**

[1]:https://github.com/cerebrux/Blender-NLE/archive/master.zip
[2]:https://github.com/cerebrux/Blender-NLE/releases
[3]:https://github.com/cerebrux/Blender-NLE/commits/master
[Artistic License v2.0]:https://github.com/cerebrux/Blender-NLE/blob/master/LICENSE
[Mikeycal Meyers]:https://www.youtube.com/playlist?list=PLjyuVPBuorqIZOWRDICIZ2WCFapHHYLPv
[Blender]:http://www.blender.org/
[Jump to Cut Addon page]:http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Jump_to_cut
[Check for Updates Addon page]:http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/System/Check_for_updates

