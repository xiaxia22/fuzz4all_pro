# Class Applet

**Source:** `java.desktop\java\applet\Applet.html`

### Class Description

```java
@Deprecated
(
since
="9")
public class
Applet

extends
Panel
```

An applet is a small program that is intended not to be run on
its own, but rather to be embedded inside another application.

The

Applet

class must be the superclass of any
applet that is to be embedded in a Web page or viewed by the Java
Applet Viewer. The

Applet

class provides a standard
interface between applets and their environment.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

*No entries found.*

### Constructor Details

#### public Applet()
throws
HeadlessException

Constructs a new Applet.

Note: Many methods in

java.applet.Applet

may be invoked by the applet only after the applet is
fully constructed; applet should avoid calling methods
in

java.applet.Applet

in the constructor.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.4

---

### Method Details

#### public final void setStub​(
AppletStub
stub)

Sets this applet's stub. This is done automatically by the system.

If there is a security manager, its

checkPermission

method is called with the

AWTPermission("setAppletStub")

permission if a stub has already been set.

**Parameters:**
- stub

- the new stub.

**Throws:**
- SecurityException

- if the caller cannot set the stub

---

#### public boolean isActive()

Determines if this applet is active. An applet is marked active
just before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:**
- true

if the applet is active;

false

otherwise.

**See Also:**
- start()

,

stop()

---

#### public
URL
getDocumentBase()

Gets the URL of the document in which this applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:**
- the

URL

of the document that contains this
applet.

**See Also:**
- getCodeBase()

---

#### public
URL
getCodeBase()

Gets the base URL. This is the URL of the directory which contains this applet.

**Returns:**
- the base

URL

of
the directory which contains this applet.

**See Also:**
- getDocumentBase()

---

#### public
String
getParameter​(
String
name)

Returns the value of the named parameter in the HTML tag. For
example, if this applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

The

name

argument is case insensitive.

**Parameters:**
- name

- a parameter name.

**Returns:**
- the value of the named parameter,
or

null

if not set.

---

#### public
AppletContext
getAppletContext()

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

This environment of an applet represents the document that
contains the applet.

**Returns:**
- the applet's context.

---

#### public void resize​(int width,
int height)

Requests that this applet be resized.

**Overrides:**
- resize

in class

Component

**Parameters:**
- width

- the new requested width for the applet.
- height

- the new requested height for the applet.

---

#### public void resize​(
Dimension
d)

Requests that this applet be resized.

**Overrides:**
- resize

in class

Component

**Parameters:**
- d

- an object giving the new width and height.

---

#### public boolean isValidateRoot()

Indicates if this container is a validate root.

Applet

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:**
- isValidateRoot

in class

Container

**Returns:**
- true

**See Also:**
- Container.isValidateRoot()

**Since:**
- 1.7

---

#### public void showStatus​(
String
msg)

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:**
- msg

- a string to display in the status window.

---

#### public
Image
getImage​(
URL
url)

Returns an

Image

object that can then be painted on
the screen. The

url

that is passed as an argument
must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:**
- url

- an absolute URL giving the location of the image.

**Returns:**
- the image at the specified URL.

**See Also:**
- Image

---

#### public
Image
getImage​(
URL
url,

String
name)

Returns an

Image

object that can then be painted on
the screen. The

url

argument must specify an absolute
URL. The

name

argument is a specifier that is
relative to the

url

argument.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:**
- url

- an absolute URL giving the base location of the image.
- name

- the location of the image, relative to the

url

argument.

**Returns:**
- the image at the specified URL.

**See Also:**
- Image

---

#### public static final
AudioClip
newAudioClip​(
URL
url)

Get an audio clip from the given URL.

**Parameters:**
- url

- points to the audio clip

**Returns:**
- the audio clip at the specified URL.

**Since:**
- 1.2

---

#### public
AudioClip
getAudioClip​(
URL
url)

Returns the

AudioClip

object specified by the

URL

argument.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:**
- url

- an absolute URL giving the location of the audio clip.

**Returns:**
- the audio clip at the specified URL.

**See Also:**
- AudioClip

---

#### public
AudioClip
getAudioClip​(
URL
url,

String
name)

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:**
- url

- an absolute URL giving the base location of the
audio clip.
- name

- the location of the audio clip, relative to the

url

argument.

**Returns:**
- the audio clip at the specified URL.

**See Also:**
- AudioClip

---

#### public
String
getAppletInfo()

Returns information about this applet. An applet should override
this method to return a

String

containing information
about the author, version, and copyright of the applet.

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:**
- a string containing information about the author, version, and
copyright of the applet.

---

#### public
Locale
getLocale()

Gets the locale of the applet. It allows the applet
to maintain its own locale separated from the locale
of the browser or appletviewer.

**Overrides:**
- getLocale

in class

Component

**Returns:**
- the locale of the applet; if no locale has
been set, the default locale is returned.

**See Also:**
- Component.setLocale(java.util.Locale)

**Since:**
- 1.1

---

#### public
String
[][] getParameterInfo()

Returns information about the parameters that are understood by
this applet. An applet should override this method to return an
array of

Strings

describing these parameters.

Each element of the array should be a set of three

Strings

containing the name, the type, and a
description. For example:

```java
String pinfo[][] = {
{"fps", "1-10", "frames per second"},
{"repeat", "boolean", "repeat image loop"},
{"imgs", "url", "images directory"}
};
```

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:**
- an array describing the parameters this applet looks for.

---

#### public void play​(
URL
url)

Plays the audio clip at the specified absolute URL. Nothing
happens if the audio clip cannot be found.

**Parameters:**
- url

- an absolute URL giving the location of the audio clip.

---

#### public void play​(
URL
url,

String
name)

Plays the audio clip given the URL and a specifier that is
relative to it. Nothing happens if the audio clip cannot be found.

**Parameters:**
- url

- an absolute URL giving the base location of the
audio clip.
- name

- the location of the audio clip, relative to the

url

argument.

---

#### public void init()

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system. It is always
called before the first time that the

start

method is
called.

A subclass of

Applet

should override this method if
it has initialization to perform. For example, an applet with
threads would use the

init

method to create the
threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:**
- destroy()

,

start()

,

stop()

---

#### public void start()

Called by the browser or applet viewer to inform
this applet that it should start its execution. It is called after
the

init

method and each time the applet is revisited
in a Web page.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is visited. For example, an applet with
animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

Note: some methods, such as

getLocationOnScreen

, can only
provide meaningful results if the applet is showing. Because

isShowing

returns

false

when the applet's

start

is first called, methods requiring

isShowing

to return

true

should be called from
a

ComponentListener

.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:**
- destroy()

,

init()

,

stop()

,

Component.isShowing()

,

ComponentListener.componentShown(java.awt.event.ComponentEvent)

---

#### public void stop()

Called by the browser or applet viewer to inform
this applet that it should stop its execution. It is called when
the Web page that contains this applet has been replaced by
another page, and also just before the applet is to be destroyed.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is no longer visible. For example, an applet
with animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:**
- destroy()

,

init()

---

#### public void destroy()

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated. The

stop

method
will always be called before

destroy

.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform before it is
destroyed. For example, an applet with threads would use the

init

method to create the threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:**
- init()

,

start()

,

stop()

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this Applet.
For applets, the AccessibleContext takes the form of an
AccessibleApplet.
A new AccessibleApplet instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Panel

**Returns:**
- an AccessibleApplet that serves as the
AccessibleContext of this Applet

**Since:**
- 1.3

---

### Additional Sections

#### Class Applet

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Panel
- - java.applet.Applet

java.awt.Component

- java.awt.Container
- - java.awt.Panel
- - java.applet.Applet

java.awt.Container

- java.awt.Panel
- - java.applet.Applet

java.awt.Panel

- java.applet.Applet

java.applet.Applet

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

**Direct Known Subclasses:** JApplet

```java
@Deprecated
(
since
="9")
public class
Applet

extends
Panel
```

Deprecated.

The Applet API is deprecated, no replacement.

An applet is a small program that is intended not to be run on
its own, but rather to be embedded inside another application.

The

Applet

class must be the superclass of any
applet that is to be embedded in a Web page or viewed by the Java
Applet Viewer. The

Applet

class provides a standard
interface between applets and their environment.

**Since:** 1.0
**See Also:** Serialized Form

@Deprecated

(

since

="9")
public class

Applet

extends

Panel

An applet is a small program that is intended not to be run on
its own, but rather to be embedded inside another application.

The

Applet

class must be the superclass of any
applet that is to be embedded in a Web page or viewed by the Java
Applet Viewer. The

Applet

class provides a standard
interface between applets and their environment.

The

Applet

class must be the superclass of any
applet that is to be embedded in a Web page or viewed by the Java
Applet Viewer. The

Applet

class provides a standard
interface between applets and their environment.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Applet.AccessibleApplet

Deprecated.

This class implements accessibility support for the

Applet

class.

- Nested classes/interfaces declared in class java.awt.

Panel

Panel.AccessibleAWTPanel

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.

Component

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Applet

()

Deprecated.

Constructs a new Applet.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

destroy

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated.

AccessibleContext

getAccessibleContext

()

Deprecated.

Gets the AccessibleContext associated with this Applet.

AppletContext

getAppletContext

()

Deprecated.

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

String

getAppletInfo

()

Deprecated.

Returns information about this applet.

AudioClip

getAudioClip

​(

URL

url)

Deprecated.

Returns the

AudioClip

object specified by the

URL

argument.

AudioClip

getAudioClip

​(

URL

url,

String

name)

Deprecated.

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

URL

getCodeBase

()

Deprecated.

Gets the base URL.

URL

getDocumentBase

()

Deprecated.

Gets the URL of the document in which this applet is embedded.

Image

getImage

​(

URL

url)

Deprecated.

Returns an

Image

object that can then be painted on
the screen.

Image

getImage

​(

URL

url,

String

name)

Deprecated.

Returns an

Image

object that can then be painted on
the screen.

Locale

getLocale

()

Deprecated.

Gets the locale of the applet.

String

getParameter

​(

String

name)

Deprecated.

Returns the value of the named parameter in the HTML tag.

String

[][]

getParameterInfo

()

Deprecated.

Returns information about the parameters that are understood by
this applet.

void

init

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system.

boolean

isActive

()

Deprecated.

Determines if this applet is active.

boolean

isValidateRoot

()

Deprecated.

Indicates if this container is a validate root.

static

AudioClip

newAudioClip

​(

URL

url)

Deprecated.

Get an audio clip from the given URL.

void

play

​(

URL

url)

Deprecated.

Plays the audio clip at the specified absolute URL.

void

play

​(

URL

url,

String

name)

Deprecated.

Plays the audio clip given the URL and a specifier that is
relative to it.

void

resize

​(int width,
int height)

Deprecated.

Requests that this applet be resized.

void

resize

​(

Dimension

d)

Deprecated.

Requests that this applet be resized.

void

setStub

​(

AppletStub

stub)

Deprecated.

Sets this applet's stub.

void

showStatus

​(

String

msg)

Deprecated.

Requests that the argument string be displayed in the
"status window".

void

start

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should start its execution.

void

stop

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should stop its execution.

- Methods declared in class java.awt.

Panel

addNotify

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getAlignmentX

,

getAlignmentY

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getListeners

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paint

,

paintComponents

,

paramString

,

preferredSize

,

print

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disable

,

disableEvents

,

dispatchEvent

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Applet.AccessibleApplet

Deprecated.

This class implements accessibility support for the

Applet

class.

- Nested classes/interfaces declared in class java.awt.

Panel

Panel.AccessibleAWTPanel

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

Deprecated.

This class implements accessibility support for the

Applet

class.

Nested classes/interfaces declared in class java.awt.

Panel

Panel.AccessibleAWTPanel

---

#### Nested classes/interfaces declared in class java.awt. Panel

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

- Fields declared in class java.awt.

Component

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Fields declared in class java.awt.

Component

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

Applet

()

Deprecated.

Constructs a new Applet.

---

#### Constructor Summary

Deprecated.

Constructs a new Applet.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

destroy

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated.

AccessibleContext

getAccessibleContext

()

Deprecated.

Gets the AccessibleContext associated with this Applet.

AppletContext

getAppletContext

()

Deprecated.

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

String

getAppletInfo

()

Deprecated.

Returns information about this applet.

AudioClip

getAudioClip

​(

URL

url)

Deprecated.

Returns the

AudioClip

object specified by the

URL

argument.

AudioClip

getAudioClip

​(

URL

url,

String

name)

Deprecated.

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

URL

getCodeBase

()

Deprecated.

Gets the base URL.

URL

getDocumentBase

()

Deprecated.

Gets the URL of the document in which this applet is embedded.

Image

getImage

​(

URL

url)

Deprecated.

Returns an

Image

object that can then be painted on
the screen.

Image

getImage

​(

URL

url,

String

name)

Deprecated.

Returns an

Image

object that can then be painted on
the screen.

Locale

getLocale

()

Deprecated.

Gets the locale of the applet.

String

getParameter

​(

String

name)

Deprecated.

Returns the value of the named parameter in the HTML tag.

String

[][]

getParameterInfo

()

Deprecated.

Returns information about the parameters that are understood by
this applet.

void

init

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system.

boolean

isActive

()

Deprecated.

Determines if this applet is active.

boolean

isValidateRoot

()

Deprecated.

Indicates if this container is a validate root.

static

AudioClip

newAudioClip

​(

URL

url)

Deprecated.

Get an audio clip from the given URL.

void

play

​(

URL

url)

Deprecated.

Plays the audio clip at the specified absolute URL.

void

play

​(

URL

url,

String

name)

Deprecated.

Plays the audio clip given the URL and a specifier that is
relative to it.

void

resize

​(int width,
int height)

Deprecated.

Requests that this applet be resized.

void

resize

​(

Dimension

d)

Deprecated.

Requests that this applet be resized.

void

setStub

​(

AppletStub

stub)

Deprecated.

Sets this applet's stub.

void

showStatus

​(

String

msg)

Deprecated.

Requests that the argument string be displayed in the
"status window".

void

start

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should start its execution.

void

stop

()

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should stop its execution.

- Methods declared in class java.awt.

Panel

addNotify

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getAlignmentX

,

getAlignmentY

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getListeners

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paint

,

paintComponents

,

paramString

,

preferredSize

,

print

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disable

,

disableEvents

,

dispatchEvent

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Deprecated.

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated.

Gets the AccessibleContext associated with this Applet.

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

Returns information about this applet.

Returns the

AudioClip

object specified by the

URL

argument.

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

Gets the base URL.

Gets the URL of the document in which this applet is embedded.

Returns an

Image

object that can then be painted on
the screen.

Gets the locale of the applet.

Returns the value of the named parameter in the HTML tag.

Returns information about the parameters that are understood by
this applet.

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system.

Determines if this applet is active.

Indicates if this container is a validate root.

Get an audio clip from the given URL.

Plays the audio clip at the specified absolute URL.

Plays the audio clip given the URL and a specifier that is
relative to it.

Requests that this applet be resized.

Sets this applet's stub.

Requests that the argument string be displayed in the
"status window".

Called by the browser or applet viewer to inform
this applet that it should start its execution.

Called by the browser or applet viewer to inform
this applet that it should stop its execution.

Methods declared in class java.awt.

Panel

addNotify

---

#### Methods declared in class java.awt. Panel

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getAlignmentX

,

getAlignmentY

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getListeners

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paint

,

paintComponents

,

paramString

,

preferredSize

,

print

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disable

,

disableEvents

,

dispatchEvent

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Applet

```java
public Applet()
throws
HeadlessException
```

Deprecated.

Constructs a new Applet.

Note: Many methods in

java.applet.Applet

may be invoked by the applet only after the applet is
fully constructed; applet should avoid calling methods
in

java.applet.Applet

in the constructor.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- setStub

```java
public final void setStub​(
AppletStub
stub)
```

Deprecated.

Sets this applet's stub. This is done automatically by the system.

If there is a security manager, its

checkPermission

method is called with the

AWTPermission("setAppletStub")

permission if a stub has already been set.

**Parameters:** stub

- the new stub.
**Throws:** SecurityException

- if the caller cannot set the stub

- isActive

```java
public boolean isActive()
```

Deprecated.

Determines if this applet is active. An applet is marked active
just before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:** true

if the applet is active;

false

otherwise.
**See Also:** start()

,

stop()

- getDocumentBase

```java
public
URL
getDocumentBase()
```

Deprecated.

Gets the URL of the document in which this applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:** the

URL

of the document that contains this
applet.
**See Also:** getCodeBase()

- getCodeBase

```java
public
URL
getCodeBase()
```

Deprecated.

Gets the base URL. This is the URL of the directory which contains this applet.

**Returns:** the base

URL

of
the directory which contains this applet.
**See Also:** getDocumentBase()

- getParameter

```java
public
String
getParameter​(
String
name)
```

Deprecated.

Returns the value of the named parameter in the HTML tag. For
example, if this applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

The

name

argument is case insensitive.

**Parameters:** name

- a parameter name.
**Returns:** the value of the named parameter,
or

null

if not set.

- getAppletContext

```java
public
AppletContext
getAppletContext()
```

Deprecated.

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

This environment of an applet represents the document that
contains the applet.

**Returns:** the applet's context.

- resize

```java
public void resize​(int width,
int height)
```

Deprecated.

Requests that this applet be resized.

**Overrides:** resize

in class

Component
**Parameters:** width

- the new requested width for the applet.
**Parameters:** height

- the new requested height for the applet.

- resize

```java
public void resize​(
Dimension
d)
```

Deprecated.

Requests that this applet be resized.

**Overrides:** resize

in class

Component
**Parameters:** d

- an object giving the new width and height.

- isValidateRoot

```java
public boolean isValidateRoot()
```

Deprecated.

Indicates if this container is a validate root.

Applet

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:** isValidateRoot

in class

Container
**Returns:** true
**Since:** 1.7
**See Also:** Container.isValidateRoot()

- showStatus

```java
public void showStatus​(
String
msg)
```

Deprecated.

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:** msg

- a string to display in the status window.

- getImage

```java
public
Image
getImage​(
URL
url)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

that is passed as an argument
must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the location of the image.
**Returns:** the image at the specified URL.
**See Also:** Image

- getImage

```java
public
Image
getImage​(
URL
url,

String
name)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

argument must specify an absolute
URL. The

name

argument is a specifier that is
relative to the

url

argument.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the base location of the image.
**Parameters:** name

- the location of the image, relative to the

url

argument.
**Returns:** the image at the specified URL.
**See Also:** Image

- newAudioClip

```java
public static final
AudioClip
newAudioClip​(
URL
url)
```

Deprecated.

Get an audio clip from the given URL.

**Parameters:** url

- points to the audio clip
**Returns:** the audio clip at the specified URL.
**Since:** 1.2

- getAudioClip

```java
public
AudioClip
getAudioClip​(
URL
url)
```

Deprecated.

Returns the

AudioClip

object specified by the

URL

argument.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:** url

- an absolute URL giving the location of the audio clip.
**Returns:** the audio clip at the specified URL.
**See Also:** AudioClip

- getAudioClip

```java
public
AudioClip
getAudioClip​(
URL
url,

String
name)
```

Deprecated.

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:** url

- an absolute URL giving the base location of the
audio clip.
**Parameters:** name

- the location of the audio clip, relative to the

url

argument.
**Returns:** the audio clip at the specified URL.
**See Also:** AudioClip

- getAppletInfo

```java
public
String
getAppletInfo()
```

Deprecated.

Returns information about this applet. An applet should override
this method to return a

String

containing information
about the author, version, and copyright of the applet.

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:** a string containing information about the author, version, and
copyright of the applet.

- getLocale

```java
public
Locale
getLocale()
```

Deprecated.

Gets the locale of the applet. It allows the applet
to maintain its own locale separated from the locale
of the browser or appletviewer.

**Overrides:** getLocale

in class

Component
**Returns:** the locale of the applet; if no locale has
been set, the default locale is returned.
**Since:** 1.1
**See Also:** Component.setLocale(java.util.Locale)

- getParameterInfo

```java
public
String
[][] getParameterInfo()
```

Deprecated.

Returns information about the parameters that are understood by
this applet. An applet should override this method to return an
array of

Strings

describing these parameters.

Each element of the array should be a set of three

Strings

containing the name, the type, and a
description. For example:

```java
String pinfo[][] = {
{"fps", "1-10", "frames per second"},
{"repeat", "boolean", "repeat image loop"},
{"imgs", "url", "images directory"}
};
```

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:** an array describing the parameters this applet looks for.

- play

```java
public void play​(
URL
url)
```

Deprecated.

Plays the audio clip at the specified absolute URL. Nothing
happens if the audio clip cannot be found.

**Parameters:** url

- an absolute URL giving the location of the audio clip.

- play

```java
public void play​(
URL
url,

String
name)
```

Deprecated.

Plays the audio clip given the URL and a specifier that is
relative to it. Nothing happens if the audio clip cannot be found.

**Parameters:** url

- an absolute URL giving the base location of the
audio clip.
**Parameters:** name

- the location of the audio clip, relative to the

url

argument.

- init

```java
public void init()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system. It is always
called before the first time that the

start

method is
called.

A subclass of

Applet

should override this method if
it has initialization to perform. For example, an applet with
threads would use the

init

method to create the
threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

start()

,

stop()

- start

```java
public void start()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should start its execution. It is called after
the

init

method and each time the applet is revisited
in a Web page.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is visited. For example, an applet with
animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

Note: some methods, such as

getLocationOnScreen

, can only
provide meaningful results if the applet is showing. Because

isShowing

returns

false

when the applet's

start

is first called, methods requiring

isShowing

to return

true

should be called from
a

ComponentListener

.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

init()

,

stop()

,

Component.isShowing()

,

ComponentListener.componentShown(java.awt.event.ComponentEvent)

- stop

```java
public void stop()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should stop its execution. It is called when
the Web page that contains this applet has been replaced by
another page, and also just before the applet is to be destroyed.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is no longer visible. For example, an applet
with animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

init()

- destroy

```java
public void destroy()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated. The

stop

method
will always be called before

destroy

.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform before it is
destroyed. For example, an applet with threads would use the

init

method to create the threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** init()

,

start()

,

stop()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Deprecated.

Gets the AccessibleContext associated with this Applet.
For applets, the AccessibleContext takes the form of an
AccessibleApplet.
A new AccessibleApplet instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Panel
**Returns:** an AccessibleApplet that serves as the
AccessibleContext of this Applet
**Since:** 1.3

Constructor Detail

- Applet

```java
public Applet()
throws
HeadlessException
```

Deprecated.

Constructs a new Applet.

Note: Many methods in

java.applet.Applet

may be invoked by the applet only after the applet is
fully constructed; applet should avoid calling methods
in

java.applet.Applet

in the constructor.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

Applet

```java
public Applet()
throws
HeadlessException
```

Deprecated.

Constructs a new Applet.

Note: Many methods in

java.applet.Applet

may be invoked by the applet only after the applet is
fully constructed; applet should avoid calling methods
in

java.applet.Applet

in the constructor.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Applet

public Applet()
throws

HeadlessException

Constructs a new Applet.

Note: Many methods in

java.applet.Applet

may be invoked by the applet only after the applet is
fully constructed; applet should avoid calling methods
in

java.applet.Applet

in the constructor.

Note: Many methods in

java.applet.Applet

may be invoked by the applet only after the applet is
fully constructed; applet should avoid calling methods
in

java.applet.Applet

in the constructor.

Method Detail

- setStub

```java
public final void setStub​(
AppletStub
stub)
```

Deprecated.

Sets this applet's stub. This is done automatically by the system.

If there is a security manager, its

checkPermission

method is called with the

AWTPermission("setAppletStub")

permission if a stub has already been set.

**Parameters:** stub

- the new stub.
**Throws:** SecurityException

- if the caller cannot set the stub

- isActive

```java
public boolean isActive()
```

Deprecated.

Determines if this applet is active. An applet is marked active
just before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:** true

if the applet is active;

false

otherwise.
**See Also:** start()

,

stop()

- getDocumentBase

```java
public
URL
getDocumentBase()
```

Deprecated.

Gets the URL of the document in which this applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:** the

URL

of the document that contains this
applet.
**See Also:** getCodeBase()

- getCodeBase

```java
public
URL
getCodeBase()
```

Deprecated.

Gets the base URL. This is the URL of the directory which contains this applet.

**Returns:** the base

URL

of
the directory which contains this applet.
**See Also:** getDocumentBase()

- getParameter

```java
public
String
getParameter​(
String
name)
```

Deprecated.

Returns the value of the named parameter in the HTML tag. For
example, if this applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

The

name

argument is case insensitive.

**Parameters:** name

- a parameter name.
**Returns:** the value of the named parameter,
or

null

if not set.

- getAppletContext

```java
public
AppletContext
getAppletContext()
```

Deprecated.

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

This environment of an applet represents the document that
contains the applet.

**Returns:** the applet's context.

- resize

```java
public void resize​(int width,
int height)
```

Deprecated.

Requests that this applet be resized.

**Overrides:** resize

in class

Component
**Parameters:** width

- the new requested width for the applet.
**Parameters:** height

- the new requested height for the applet.

- resize

```java
public void resize​(
Dimension
d)
```

Deprecated.

Requests that this applet be resized.

**Overrides:** resize

in class

Component
**Parameters:** d

- an object giving the new width and height.

- isValidateRoot

```java
public boolean isValidateRoot()
```

Deprecated.

Indicates if this container is a validate root.

Applet

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:** isValidateRoot

in class

Container
**Returns:** true
**Since:** 1.7
**See Also:** Container.isValidateRoot()

- showStatus

```java
public void showStatus​(
String
msg)
```

Deprecated.

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:** msg

- a string to display in the status window.

- getImage

```java
public
Image
getImage​(
URL
url)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

that is passed as an argument
must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the location of the image.
**Returns:** the image at the specified URL.
**See Also:** Image

- getImage

```java
public
Image
getImage​(
URL
url,

String
name)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

argument must specify an absolute
URL. The

name

argument is a specifier that is
relative to the

url

argument.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the base location of the image.
**Parameters:** name

- the location of the image, relative to the

url

argument.
**Returns:** the image at the specified URL.
**See Also:** Image

- newAudioClip

```java
public static final
AudioClip
newAudioClip​(
URL
url)
```

Deprecated.

Get an audio clip from the given URL.

**Parameters:** url

- points to the audio clip
**Returns:** the audio clip at the specified URL.
**Since:** 1.2

- getAudioClip

```java
public
AudioClip
getAudioClip​(
URL
url)
```

Deprecated.

Returns the

AudioClip

object specified by the

URL

argument.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:** url

- an absolute URL giving the location of the audio clip.
**Returns:** the audio clip at the specified URL.
**See Also:** AudioClip

- getAudioClip

```java
public
AudioClip
getAudioClip​(
URL
url,

String
name)
```

Deprecated.

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:** url

- an absolute URL giving the base location of the
audio clip.
**Parameters:** name

- the location of the audio clip, relative to the

url

argument.
**Returns:** the audio clip at the specified URL.
**See Also:** AudioClip

- getAppletInfo

```java
public
String
getAppletInfo()
```

Deprecated.

Returns information about this applet. An applet should override
this method to return a

String

containing information
about the author, version, and copyright of the applet.

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:** a string containing information about the author, version, and
copyright of the applet.

- getLocale

```java
public
Locale
getLocale()
```

Deprecated.

Gets the locale of the applet. It allows the applet
to maintain its own locale separated from the locale
of the browser or appletviewer.

**Overrides:** getLocale

in class

Component
**Returns:** the locale of the applet; if no locale has
been set, the default locale is returned.
**Since:** 1.1
**See Also:** Component.setLocale(java.util.Locale)

- getParameterInfo

```java
public
String
[][] getParameterInfo()
```

Deprecated.

Returns information about the parameters that are understood by
this applet. An applet should override this method to return an
array of

Strings

describing these parameters.

Each element of the array should be a set of three

Strings

containing the name, the type, and a
description. For example:

```java
String pinfo[][] = {
{"fps", "1-10", "frames per second"},
{"repeat", "boolean", "repeat image loop"},
{"imgs", "url", "images directory"}
};
```

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:** an array describing the parameters this applet looks for.

- play

```java
public void play​(
URL
url)
```

Deprecated.

Plays the audio clip at the specified absolute URL. Nothing
happens if the audio clip cannot be found.

**Parameters:** url

- an absolute URL giving the location of the audio clip.

- play

```java
public void play​(
URL
url,

String
name)
```

Deprecated.

Plays the audio clip given the URL and a specifier that is
relative to it. Nothing happens if the audio clip cannot be found.

**Parameters:** url

- an absolute URL giving the base location of the
audio clip.
**Parameters:** name

- the location of the audio clip, relative to the

url

argument.

- init

```java
public void init()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system. It is always
called before the first time that the

start

method is
called.

A subclass of

Applet

should override this method if
it has initialization to perform. For example, an applet with
threads would use the

init

method to create the
threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

start()

,

stop()

- start

```java
public void start()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should start its execution. It is called after
the

init

method and each time the applet is revisited
in a Web page.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is visited. For example, an applet with
animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

Note: some methods, such as

getLocationOnScreen

, can only
provide meaningful results if the applet is showing. Because

isShowing

returns

false

when the applet's

start

is first called, methods requiring

isShowing

to return

true

should be called from
a

ComponentListener

.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

init()

,

stop()

,

Component.isShowing()

,

ComponentListener.componentShown(java.awt.event.ComponentEvent)

- stop

```java
public void stop()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should stop its execution. It is called when
the Web page that contains this applet has been replaced by
another page, and also just before the applet is to be destroyed.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is no longer visible. For example, an applet
with animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

init()

- destroy

```java
public void destroy()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated. The

stop

method
will always be called before

destroy

.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform before it is
destroyed. For example, an applet with threads would use the

init

method to create the threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** init()

,

start()

,

stop()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Deprecated.

Gets the AccessibleContext associated with this Applet.
For applets, the AccessibleContext takes the form of an
AccessibleApplet.
A new AccessibleApplet instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Panel
**Returns:** an AccessibleApplet that serves as the
AccessibleContext of this Applet
**Since:** 1.3

---

#### Method Detail

setStub

```java
public final void setStub​(
AppletStub
stub)
```

Deprecated.

Sets this applet's stub. This is done automatically by the system.

If there is a security manager, its

checkPermission

method is called with the

AWTPermission("setAppletStub")

permission if a stub has already been set.

**Parameters:** stub

- the new stub.
**Throws:** SecurityException

- if the caller cannot set the stub

---

#### setStub

public final void setStub​(

AppletStub

stub)

Sets this applet's stub. This is done automatically by the system.

If there is a security manager, its

checkPermission

method is called with the

AWTPermission("setAppletStub")

permission if a stub has already been set.

If there is a security manager, its

checkPermission

method is called with the

AWTPermission("setAppletStub")

permission if a stub has already been set.

isActive

```java
public boolean isActive()
```

Deprecated.

Determines if this applet is active. An applet is marked active
just before its

start

method is called. It becomes
inactive just before its

stop

method is called.

**Returns:** true

if the applet is active;

false

otherwise.
**See Also:** start()

,

stop()

---

#### isActive

public boolean isActive()

Determines if this applet is active. An applet is marked active
just before its

start

method is called. It becomes
inactive just before its

stop

method is called.

getDocumentBase

```java
public
URL
getDocumentBase()
```

Deprecated.

Gets the URL of the document in which this applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

**Returns:** the

URL

of the document that contains this
applet.
**See Also:** getCodeBase()

---

#### getDocumentBase

public

URL

getDocumentBase()

Gets the URL of the document in which this applet is embedded.
For example, suppose an applet is contained
within the document:

```java
http://www.oracle.com/technetwork/java/index.html
```

The document base is:

```java
http://www.oracle.com/technetwork/java/index.html
```

http://www.oracle.com/technetwork/java/index.html

getCodeBase

```java
public
URL
getCodeBase()
```

Deprecated.

Gets the base URL. This is the URL of the directory which contains this applet.

**Returns:** the base

URL

of
the directory which contains this applet.
**See Also:** getDocumentBase()

---

#### getCodeBase

public

URL

getCodeBase()

Gets the base URL. This is the URL of the directory which contains this applet.

getParameter

```java
public
String
getParameter​(
String
name)
```

Deprecated.

Returns the value of the named parameter in the HTML tag. For
example, if this applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

The

name

argument is case insensitive.

**Parameters:** name

- a parameter name.
**Returns:** the value of the named parameter,
or

null

if not set.

---

#### getParameter

public

String

getParameter​(

String

name)

Returns the value of the named parameter in the HTML tag. For
example, if this applet is specified as

```java
<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>
```

then a call to

getParameter("Color")

returns the
value

"blue"

.

The

name

argument is case insensitive.

<applet code="Clock" width=50 height=50>
<param name=Color value="blue">
</applet>

then a call to

getParameter("Color")

returns the
value

"blue"

.

The

name

argument is case insensitive.

The

name

argument is case insensitive.

getAppletContext

```java
public
AppletContext
getAppletContext()
```

Deprecated.

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

This environment of an applet represents the document that
contains the applet.

**Returns:** the applet's context.

---

#### getAppletContext

public

AppletContext

getAppletContext()

Determines this applet's context, which allows the applet to
query and affect the environment in which it runs.

This environment of an applet represents the document that
contains the applet.

This environment of an applet represents the document that
contains the applet.

resize

```java
public void resize​(int width,
int height)
```

Deprecated.

Requests that this applet be resized.

**Overrides:** resize

in class

Component
**Parameters:** width

- the new requested width for the applet.
**Parameters:** height

- the new requested height for the applet.

---

#### resize

public void resize​(int width,
int height)

Requests that this applet be resized.

resize

```java
public void resize​(
Dimension
d)
```

Deprecated.

Requests that this applet be resized.

**Overrides:** resize

in class

Component
**Parameters:** d

- an object giving the new width and height.

---

#### resize

public void resize​(

Dimension

d)

Requests that this applet be resized.

isValidateRoot

```java
public boolean isValidateRoot()
```

Deprecated.

Indicates if this container is a validate root.

Applet

objects are the validate roots, and, therefore, they
override this method to return

true

.

**Overrides:** isValidateRoot

in class

Container
**Returns:** true
**Since:** 1.7
**See Also:** Container.isValidateRoot()

---

#### isValidateRoot

public boolean isValidateRoot()

Indicates if this container is a validate root.

Applet

objects are the validate roots, and, therefore, they
override this method to return

true

.

Applet

objects are the validate roots, and, therefore, they
override this method to return

true

.

showStatus

```java
public void showStatus​(
String
msg)
```

Deprecated.

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

**Parameters:** msg

- a string to display in the status window.

---

#### showStatus

public void showStatus​(

String

msg)

Requests that the argument string be displayed in the
"status window". Many browsers and applet viewers
provide such a window, where the application can inform users of
its current state.

getImage

```java
public
Image
getImage​(
URL
url)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

that is passed as an argument
must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the location of the image.
**Returns:** the image at the specified URL.
**See Also:** Image

---

#### getImage

public

Image

getImage​(

URL

url)

Returns an

Image

object that can then be painted on
the screen. The

url

that is passed as an argument
must specify an absolute URL.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

getImage

```java
public
Image
getImage​(
URL
url,

String
name)
```

Deprecated.

Returns an

Image

object that can then be painted on
the screen. The

url

argument must specify an absolute
URL. The

name

argument is a specifier that is
relative to the

url

argument.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

**Parameters:** url

- an absolute URL giving the base location of the image.
**Parameters:** name

- the location of the image, relative to the

url

argument.
**Returns:** the image at the specified URL.
**See Also:** Image

---

#### getImage

public

Image

getImage​(

URL

url,

String

name)

Returns an

Image

object that can then be painted on
the screen. The

url

argument must specify an absolute
URL. The

name

argument is a specifier that is
relative to the

url

argument.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

This method always returns immediately, whether or not the image
exists. When this applet attempts to draw the image on the screen,
the data will be loaded. The graphics primitives that draw the
image will incrementally paint on the screen.

newAudioClip

```java
public static final
AudioClip
newAudioClip​(
URL
url)
```

Deprecated.

Get an audio clip from the given URL.

**Parameters:** url

- points to the audio clip
**Returns:** the audio clip at the specified URL.
**Since:** 1.2

---

#### newAudioClip

public static final

AudioClip

newAudioClip​(

URL

url)

Get an audio clip from the given URL.

getAudioClip

```java
public
AudioClip
getAudioClip​(
URL
url)
```

Deprecated.

Returns the

AudioClip

object specified by the

URL

argument.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:** url

- an absolute URL giving the location of the audio clip.
**Returns:** the audio clip at the specified URL.
**See Also:** AudioClip

---

#### getAudioClip

public

AudioClip

getAudioClip​(

URL

url)

Returns the

AudioClip

object specified by the

URL

argument.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

getAudioClip

```java
public
AudioClip
getAudioClip​(
URL
url,

String
name)
```

Deprecated.

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

**Parameters:** url

- an absolute URL giving the base location of the
audio clip.
**Parameters:** name

- the location of the audio clip, relative to the

url

argument.
**Returns:** the audio clip at the specified URL.
**See Also:** AudioClip

---

#### getAudioClip

public

AudioClip

getAudioClip​(

URL

url,

String

name)

Returns the

AudioClip

object specified by the

URL

and

name

arguments.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

This method always returns immediately, whether or not the audio
clip exists. When this applet attempts to play the audio clip, the
data will be loaded.

getAppletInfo

```java
public
String
getAppletInfo()
```

Deprecated.

Returns information about this applet. An applet should override
this method to return a

String

containing information
about the author, version, and copyright of the applet.

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:** a string containing information about the author, version, and
copyright of the applet.

---

#### getAppletInfo

public

String

getAppletInfo()

Returns information about this applet. An applet should override
this method to return a

String

containing information
about the author, version, and copyright of the applet.

The implementation of this method provided by the

Applet

class returns

null

.

The implementation of this method provided by the

Applet

class returns

null

.

getLocale

```java
public
Locale
getLocale()
```

Deprecated.

Gets the locale of the applet. It allows the applet
to maintain its own locale separated from the locale
of the browser or appletviewer.

**Overrides:** getLocale

in class

Component
**Returns:** the locale of the applet; if no locale has
been set, the default locale is returned.
**Since:** 1.1
**See Also:** Component.setLocale(java.util.Locale)

---

#### getLocale

public

Locale

getLocale()

Gets the locale of the applet. It allows the applet
to maintain its own locale separated from the locale
of the browser or appletviewer.

getParameterInfo

```java
public
String
[][] getParameterInfo()
```

Deprecated.

Returns information about the parameters that are understood by
this applet. An applet should override this method to return an
array of

Strings

describing these parameters.

Each element of the array should be a set of three

Strings

containing the name, the type, and a
description. For example:

```java
String pinfo[][] = {
{"fps", "1-10", "frames per second"},
{"repeat", "boolean", "repeat image loop"},
{"imgs", "url", "images directory"}
};
```

The implementation of this method provided by the

Applet

class returns

null

.

**Returns:** an array describing the parameters this applet looks for.

---

#### getParameterInfo

public

String

[][] getParameterInfo()

Returns information about the parameters that are understood by
this applet. An applet should override this method to return an
array of

Strings

describing these parameters.

Each element of the array should be a set of three

Strings

containing the name, the type, and a
description. For example:

```java
String pinfo[][] = {
{"fps", "1-10", "frames per second"},
{"repeat", "boolean", "repeat image loop"},
{"imgs", "url", "images directory"}
};
```

The implementation of this method provided by the

Applet

class returns

null

.

Each element of the array should be a set of three

Strings

containing the name, the type, and a
description. For example:

```java
String pinfo[][] = {
{"fps", "1-10", "frames per second"},
{"repeat", "boolean", "repeat image loop"},
{"imgs", "url", "images directory"}
};
```

The implementation of this method provided by the

Applet

class returns

null

.

String pinfo[][] = {
{"fps", "1-10", "frames per second"},
{"repeat", "boolean", "repeat image loop"},
{"imgs", "url", "images directory"}
};

The implementation of this method provided by the

Applet

class returns

null

.

play

```java
public void play​(
URL
url)
```

Deprecated.

Plays the audio clip at the specified absolute URL. Nothing
happens if the audio clip cannot be found.

**Parameters:** url

- an absolute URL giving the location of the audio clip.

---

#### play

public void play​(

URL

url)

Plays the audio clip at the specified absolute URL. Nothing
happens if the audio clip cannot be found.

play

```java
public void play​(
URL
url,

String
name)
```

Deprecated.

Plays the audio clip given the URL and a specifier that is
relative to it. Nothing happens if the audio clip cannot be found.

**Parameters:** url

- an absolute URL giving the base location of the
audio clip.
**Parameters:** name

- the location of the audio clip, relative to the

url

argument.

---

#### play

public void play​(

URL

url,

String

name)

Plays the audio clip given the URL and a specifier that is
relative to it. Nothing happens if the audio clip cannot be found.

init

```java
public void init()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system. It is always
called before the first time that the

start

method is
called.

A subclass of

Applet

should override this method if
it has initialization to perform. For example, an applet with
threads would use the

init

method to create the
threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

start()

,

stop()

---

#### init

public void init()

Called by the browser or applet viewer to inform
this applet that it has been loaded into the system. It is always
called before the first time that the

start

method is
called.

A subclass of

Applet

should override this method if
it has initialization to perform. For example, an applet with
threads would use the

init

method to create the
threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

A subclass of

Applet

should override this method if
it has initialization to perform. For example, an applet with
threads would use the

init

method to create the
threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

The implementation of this method provided by the

Applet

class does nothing.

start

```java
public void start()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should start its execution. It is called after
the

init

method and each time the applet is revisited
in a Web page.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is visited. For example, an applet with
animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

Note: some methods, such as

getLocationOnScreen

, can only
provide meaningful results if the applet is showing. Because

isShowing

returns

false

when the applet's

start

is first called, methods requiring

isShowing

to return

true

should be called from
a

ComponentListener

.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

init()

,

stop()

,

Component.isShowing()

,

ComponentListener.componentShown(java.awt.event.ComponentEvent)

---

#### start

public void start()

Called by the browser or applet viewer to inform
this applet that it should start its execution. It is called after
the

init

method and each time the applet is revisited
in a Web page.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is visited. For example, an applet with
animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

Note: some methods, such as

getLocationOnScreen

, can only
provide meaningful results if the applet is showing. Because

isShowing

returns

false

when the applet's

start

is first called, methods requiring

isShowing

to return

true

should be called from
a

ComponentListener

.

The implementation of this method provided by the

Applet

class does nothing.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is visited. For example, an applet with
animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

Note: some methods, such as

getLocationOnScreen

, can only
provide meaningful results if the applet is showing. Because

isShowing

returns

false

when the applet's

start

is first called, methods requiring

isShowing

to return

true

should be called from
a

ComponentListener

.

The implementation of this method provided by the

Applet

class does nothing.

Note: some methods, such as

getLocationOnScreen

, can only
provide meaningful results if the applet is showing. Because

isShowing

returns

false

when the applet's

start

is first called, methods requiring

isShowing

to return

true

should be called from
a

ComponentListener

.

The implementation of this method provided by the

Applet

class does nothing.

The implementation of this method provided by the

Applet

class does nothing.

stop

```java
public void stop()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it should stop its execution. It is called when
the Web page that contains this applet has been replaced by
another page, and also just before the applet is to be destroyed.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is no longer visible. For example, an applet
with animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** destroy()

,

init()

---

#### stop

public void stop()

Called by the browser or applet viewer to inform
this applet that it should stop its execution. It is called when
the Web page that contains this applet has been replaced by
another page, and also just before the applet is to be destroyed.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is no longer visible. For example, an applet
with animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

The implementation of this method provided by the

Applet

class does nothing.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform each time the Web
page containing it is no longer visible. For example, an applet
with animation might want to use the

start

method to
resume animation, and the

stop

method to suspend the
animation.

The implementation of this method provided by the

Applet

class does nothing.

The implementation of this method provided by the

Applet

class does nothing.

destroy

```java
public void destroy()
```

Deprecated.

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated. The

stop

method
will always be called before

destroy

.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform before it is
destroyed. For example, an applet with threads would use the

init

method to create the threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

**See Also:** init()

,

start()

,

stop()

---

#### destroy

public void destroy()

Called by the browser or applet viewer to inform
this applet that it is being reclaimed and that it should destroy
any resources that it has allocated. The

stop

method
will always be called before

destroy

.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform before it is
destroyed. For example, an applet with threads would use the

init

method to create the threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

A subclass of

Applet

should override this method if
it has any operation that it wants to perform before it is
destroyed. For example, an applet with threads would use the

init

method to create the threads and the

destroy

method to kill them.

The implementation of this method provided by the

Applet

class does nothing.

The implementation of this method provided by the

Applet

class does nothing.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Deprecated.

Gets the AccessibleContext associated with this Applet.
For applets, the AccessibleContext takes the form of an
AccessibleApplet.
A new AccessibleApplet instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Panel
**Returns:** an AccessibleApplet that serves as the
AccessibleContext of this Applet
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this Applet.
For applets, the AccessibleContext takes the form of an
AccessibleApplet.
A new AccessibleApplet instance is created if necessary.

---

