# Class Component

**Source:** `java.desktop\java\awt\Component.html`

### Class Description

```java
public abstract class
Component

extends
Object

implements
ImageObserver
,
MenuContainer
,
Serializable
```

A

component

is an object having a graphical representation
that can be displayed on the screen and that can interact with the
user. Examples of components are the buttons, checkboxes, and scrollbars
of a typical graphical user interface.

The

Component

class is the abstract superclass of
the nonmenu-related Abstract Window Toolkit components. Class

Component

can also be extended directly to create a
lightweight component. A lightweight component is a component that is
not associated with a native window. On the contrary, a heavyweight
component is associated with a native window. The

isLightweight()

method may be used to distinguish between the two kinds of the components.

Lightweight and heavyweight components may be mixed in a single component
hierarchy. However, for correct operating of such a mixed hierarchy of
components, the whole hierarchy must be valid. When the hierarchy gets
invalidated, like after changing the bounds of components, or
adding/removing components to/from containers, the whole hierarchy must be
validated afterwards by means of the

Container.validate()

method
invoked on the top-most invalid container of the hierarchy.

Serialization

It is important to note that only AWT listeners which conform
to the

Serializable

protocol will be saved when
the object is stored. If an AWT object has listeners that
aren't marked serializable, they will be dropped at

writeObject

time. Developers will need, as always,
to consider the implications of making an object serializable.
One situation to watch out for is this:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements ActionListener, Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

MyApp()
{
// Oops, now aButton has a listener with a reference
// to bigOne!
aButton.addActionListener(this);
}

public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}
```

In this example, serializing

aButton

by itself
will cause

MyApp

and everything it refers to
to be serialized as well. The problem is that the listener
is serializable by coincidence, not by design. To separate
the decisions about

MyApp

and the

ActionListener

being serializable one can use a
nested class, as in the following example:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements java.io.Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

static class MyActionListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}

MyApp()
{
aButton.addActionListener(new MyActionListener());
}
}
```

Note

: For more information on the paint mechanisms utilized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

---

### Field Details

#### public static final float TOP_ALIGNMENT

Ease-of-use constant for

getAlignmentY()

.
Specifies an alignment to the top of the component.

**See Also:**
- getAlignmentY()

,

Constant Field Values

---

#### public static final float CENTER_ALIGNMENT

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

. Specifies an alignment to
the center of the component

**See Also:**
- getAlignmentX()

,

getAlignmentY()

,

Constant Field Values

---

#### public static final float BOTTOM_ALIGNMENT

Ease-of-use constant for

getAlignmentY

.
Specifies an alignment to the bottom of the component.

**See Also:**
- getAlignmentY()

,

Constant Field Values

---

#### public static final float LEFT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the left side of the component.

**See Also:**
- getAlignmentX()

,

Constant Field Values

---

#### public static final float RIGHT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the right side of the component.

**See Also:**
- getAlignmentX()

,

Constant Field Values

---

#### protected
AccessibleContext
accessibleContext

The

AccessibleContext

associated with this

Component

.

---

### Constructor Details

#### protected Component()

Constructs a new component. Class

Component

can be
extended directly to create a lightweight component that does not
utilize an opaque native window. A lightweight component must be
hosted by a native container somewhere higher up in the component
tree (for example, by a

Frame

object).

---

### Method Details

#### public
String
getName()

Gets the name of the component.

**Returns:**
- this component's name

**See Also:**
- setName(java.lang.String)

**Since:**
- 1.1

---

#### public void setName​(
String
name)

Sets the name of the component to the specified string.

**Parameters:**
- name

- the string that is to be this
component's name

**See Also:**
- getName()

**Since:**
- 1.1

---

#### public
Container
getParent()

Gets the parent of this component.

**Returns:**
- the parent container of this component

**Since:**
- 1.0

---

#### public void setDropTarget​(
DropTarget
dt)

Associate a

DropTarget

with this component.
The

Component

will receive drops only if it
is enabled.

**Parameters:**
- dt

- The DropTarget

**See Also:**
- isEnabled()

---

#### public
DropTarget
getDropTarget()

Gets the

DropTarget

associated with this

Component

.

**Returns:**
- the drop target

---

#### public
GraphicsConfiguration
getGraphicsConfiguration()

Gets the

GraphicsConfiguration

associated with this

Component

.
If the

Component

has not been assigned a specific

GraphicsConfiguration

,
the

GraphicsConfiguration

of the

Component

object's top-level container is
returned.
If the

Component

has been created, but not yet added
to a

Container

, this method returns

null

.

**Returns:**
- the

GraphicsConfiguration

used by this

Component

or

null

**Since:**
- 1.3

---

#### public final
Object
getTreeLock()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:**
- this component's locking object

---

#### public
Toolkit
getToolkit()

Gets the toolkit of this component. Note that
the frame that contains a component controls which
toolkit is used by that component. Therefore if the component
is moved from one frame to another, the toolkit it uses may change.

**Returns:**
- the toolkit of this component

**Since:**
- 1.0

---

#### public boolean isValid()

Determines whether this component is valid. A component is valid
when it is correctly sized and positioned within its parent
container and all its children are also valid.
In order to account for peers' size requirements, components are invalidated
before they are first shown on the screen. By the time the parent container
is fully realized, all its components will be valid.

**Returns:**
- true

if the component is valid,

false

otherwise

**See Also:**
- validate()

,

invalidate()

**Since:**
- 1.0

---

#### public boolean isDisplayable()

Determines whether this component is displayable. A component is
displayable when it is connected to a native screen resource.

A component is made displayable either when it is added to
a displayable containment hierarchy or when its containment
hierarchy is made displayable.
A containment hierarchy is made displayable when its ancestor
window is either packed or made visible.

A component is made undisplayable either when it is removed from
a displayable containment hierarchy or when its containment hierarchy
is made undisplayable. A containment hierarchy is made
undisplayable when its ancestor window is disposed.

**Returns:**
- true

if the component is displayable,

false

otherwise

**See Also:**
- Container.add(Component)

,

Window.pack()

,

Window.show()

,

Container.remove(Component)

,

Window.dispose()

**Since:**
- 1.2

---

#### public boolean isVisible()

Determines whether this component should be visible when its
parent is visible. Components are
initially visible, with the exception of top level components such
as

Frame

objects.

**Returns:**
- true

if the component is visible,

false

otherwise

**See Also:**
- setVisible(boolean)

**Since:**
- 1.0

---

#### public
Point
getMousePosition()
throws
HeadlessException

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.
If the

Component

is not showing on the screen, this method
returns

null

even if the mouse pointer is above the area
where the

Component

would be displayed.
If the

Component

is partially or fully obscured by other

Component

s or native windows, this method returns a non-null
value only if the mouse pointer is located above the unobscured part of the

Component

.

For

Container

s it returns a non-null value if the mouse is
above the

Container

itself or above any of its descendants.
Use

Container.getMousePosition(boolean)

if you need to exclude children.

Sometimes the exact mouse coordinates are not important, and the only thing
that matters is whether a specific

Component

is under the mouse
pointer. If the return value of this method is

null

, mouse
pointer is not directly above the

Component

.

**Returns:**
- mouse coordinates relative to this

Component

, or null

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless() returns true

**See Also:**
- isShowing()

,

Container.getMousePosition(boolean)

**Since:**
- 1.5

---

#### public boolean isShowing()

Determines whether this component is showing on screen. This means
that the component must be visible, and it must be in a container
that is visible and showing.

Note:

sometimes there is no way to detect whether the

Component

is actually visible to the user. This can happen when:

- the component has been added to a visible

ScrollPane

but
the

Component

is not currently in the scroll pane's view port.

the

Component

is obscured by another

Component

or

Container

.

**Returns:**
- true

if the component is showing,

false

otherwise

**See Also:**
- setVisible(boolean)

**Since:**
- 1.0

---

#### public boolean isEnabled()

Determines whether this component is enabled. An enabled component
can respond to user input and generate events. Components are
enabled initially by default. A component may be enabled or disabled by
calling its

setEnabled

method.

**Returns:**
- true

if the component is enabled,

false

otherwise

**See Also:**
- setEnabled(boolean)

**Since:**
- 1.0

---

#### public void setEnabled​(boolean b)

Enables or disables this component, depending on the value of the
parameter

b

. An enabled component can respond to user
input and generate events. Components are enabled initially by default.

Note: Disabling a lightweight component does not prevent it from
receiving MouseEvents.

Note: Disabling a heavyweight container prevents all components
in this container from receiving any input events. But disabling a
lightweight container affects only this container.

**Parameters:**
- b

- If

true

, this component is
enabled; otherwise this component is disabled

**See Also:**
- isEnabled()

,

isLightweight()

**Since:**
- 1.1

---

#### @Deprecated

public void enable()

*No description found.*

---

#### @Deprecated

public void enable​(boolean b)

Enables or disables this component.

**Parameters:**
- b

-

true

to enable this component;
otherwise

false

---

#### @Deprecated

public void disable()

*No description found.*

---

#### public boolean isDoubleBuffered()

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later. Component
subclasses that support double buffering should override this
method to return true if double buffering is enabled.

**Returns:**
- false by default

---

#### public void enableInputMethods​(boolean enable)

Enables or disables input method support for this component. If input
method support is enabled and the component also processes key events,
incoming events are offered to
the current input method and will only be processed by the component or
dispatched to its listeners if the input method does not consume them.
By default, input method support is enabled.

**Parameters:**
- enable

- true to enable, false to disable

**See Also:**
- processKeyEvent(java.awt.event.KeyEvent)

**Since:**
- 1.2

---

#### public void setVisible​(boolean b)

Shows or hides this component depending on the value of parameter

b

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- b

- if

true

, shows this component;
otherwise, hides this component

**See Also:**
- isVisible()

,

invalidate()

**Since:**
- 1.1

---

#### @Deprecated

public void show()

*No description found.*

---

#### @Deprecated

public void show​(boolean b)

Makes this component visible or invisible.

**Parameters:**
- b

-

true

to make this component visible;
otherwise

false

---

#### @Deprecated

public void hide()

*No description found.*

---

#### public
Color
getForeground()

Gets the foreground color of this component.

**Returns:**
- this component's foreground color; if this component does
not have a foreground color, the foreground color of its parent
is returned

**See Also:**
- setForeground(java.awt.Color)

**Since:**
- 1.0

---

#### public void setForeground​(
Color
c)

Sets the foreground color of this component.

**Parameters:**
- c

- the color to become this component's
foreground color; if this parameter is

null

then this component will inherit
the foreground color of its parent

**See Also:**
- getForeground()

**Since:**
- 1.0

---

#### public boolean isForegroundSet()

Returns whether the foreground color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its foreground color from an ancestor.

**Returns:**
- true

if the foreground color has been explicitly
set for this Component;

false

otherwise.

**Since:**
- 1.4

---

#### public
Color
getBackground()

Gets the background color of this component.

**Returns:**
- this component's background color; if this component does
not have a background color,
the background color of its parent is returned

**See Also:**
- setBackground(java.awt.Color)

**Since:**
- 1.0

---

#### public void setBackground​(
Color
c)

Sets the background color of this component.

The background color affects each component differently and the
parts of the component that are affected by the background color
may differ between operating systems.

**Parameters:**
- c

- the color to become this component's color;
if this parameter is

null

, then this
component will inherit the background color of its parent

**See Also:**
- getBackground()

**Since:**
- 1.0

---

#### public boolean isBackgroundSet()

Returns whether the background color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its background color from an ancestor.

**Returns:**
- true

if the background color has been explicitly
set for this Component;

false

otherwise.

**Since:**
- 1.4

---

#### public
Font
getFont()

Gets the font of this component.

**Specified by:**
- getFont

in interface

MenuContainer

**Returns:**
- this component's font; if a font has not been set
for this component, the font of its parent is returned

**See Also:**
- setFont(java.awt.Font)

**Since:**
- 1.0

---

#### public void setFont​(
Font
f)

Sets the font of this component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- f

- the font to become this component's font;
if this parameter is

null

then this
component will inherit the font of its parent

**See Also:**
- getFont()

,

invalidate()

**Since:**
- 1.0

---

#### public boolean isFontSet()

Returns whether the font has been explicitly set for this Component. If
this method returns

false

, this Component is inheriting its
font from an ancestor.

**Returns:**
- true

if the font has been explicitly set for this
Component;

false

otherwise.

**Since:**
- 1.4

---

#### public
Locale
getLocale()

Gets the locale of this component.

**Returns:**
- this component's locale; if this component does not
have a locale, the locale of its parent is returned

**Throws:**
- IllegalComponentStateException

- if the

Component

does not have its own locale and has not yet been added to
a containment hierarchy such that the locale can be determined
from the containing parent

**See Also:**
- setLocale(java.util.Locale)

**Since:**
- 1.1

---

#### public void setLocale​(
Locale
l)

Sets the locale of this component. This is a bound property.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- l

- the locale to become this component's locale

**See Also:**
- getLocale()

,

invalidate()

**Since:**
- 1.1

---

#### public
ColorModel
getColorModel()

Gets the instance of

ColorModel

used to display
the component on the output device.

**Returns:**
- the color model used by this component

**See Also:**
- ColorModel

,

ComponentPeer.getColorModel()

,

Toolkit.getColorModel()

**Since:**
- 1.0

---

#### public
Point
getLocation()

Gets the location of this component in the form of a
point specifying the component's top-left corner.
The location will be relative to the parent's coordinate space.

Due to the asynchronous nature of native event handling, this
method can return outdated values (for instance, after several calls
of

setLocation()

in rapid succession). For this
reason, the recommended method of obtaining a component's position is
within

java.awt.event.ComponentListener.componentMoved()

,
which is called after the operating system has finished moving the
component.

**Returns:**
- an instance of

Point

representing
the top-left corner of the component's bounds in
the coordinate space of the component's parent

**See Also:**
- setLocation(int, int)

,

getLocationOnScreen()

**Since:**
- 1.1

---

#### public
Point
getLocationOnScreen()

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

**Returns:**
- an instance of

Point

representing
the top-left corner of the component's bounds in the
coordinate space of the screen

**Throws:**
- IllegalComponentStateException

- if the
component is not showing on the screen

**See Also:**
- setLocation(int, int)

,

getLocation()

---

#### @Deprecated

public
Point
location()

Returns the location of this component's top left corner.

**Returns:**
- the location of this component's top left corner

---

#### public void setLocation​(int x,
int y)

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
- y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space

**See Also:**
- getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

**Since:**
- 1.1

---

#### @Deprecated

public void move​(int x,
int y)

Moves this component to a new location.

**Parameters:**
- x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
- y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space

---

#### public void setLocation​(
Point
p)

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent

**See Also:**
- getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

**Since:**
- 1.1

---

#### public
Dimension
getSize()

Returns the size of this component in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this component's height, and the

width

field of the

Dimension

object contains
this component's width.

**Returns:**
- a

Dimension

object that indicates the
size of this component

**See Also:**
- setSize(int, int)

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
size()

Returns the size of this component in the form of a

Dimension

object.

**Returns:**
- the

Dimension

object that indicates the
size of this component

---

#### public void setSize​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- width

- the new width of this component in pixels
- height

- the new height of this component in pixels

**See Also:**
- getSize()

,

setBounds(int, int, int, int)

,

invalidate()

**Since:**
- 1.1

---

#### @Deprecated

public void resize​(int width,
int height)

Resizes this component.

**Parameters:**
- width

- the new width of the component
- height

- the new height of the component

---

#### public void setSize​(
Dimension
d)

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- d

- the dimension specifying the new size
of this component

**Throws:**
- NullPointerException

- if

d

is

null

**See Also:**
- setSize(int, int)

,

setBounds(int, int, int, int)

,

invalidate()

**Since:**
- 1.1

---

#### @Deprecated

public void resize​(
Dimension
d)

Resizes this component so that it has width

d.width

and height

d.height

.

**Parameters:**
- d

- the new size of this component

---

#### public
Rectangle
getBounds()

Gets the bounds of this component in the form of a

Rectangle

object. The bounds specify this
component's width, height, and location relative to
its parent.

**Returns:**
- a rectangle indicating this component's bounds

**See Also:**
- setBounds(int, int, int, int)

,

getLocation()

,

getSize()

---

#### @Deprecated

public
Rectangle
bounds()

Returns the bounding rectangle of this component.

**Returns:**
- the bounding rectangle for this component

---

#### public void setBounds​(int x,
int y,
int width,
int height)

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- x

- the new

x

-coordinate of this component
- y

- the new

y

-coordinate of this component
- width

- the new

width

of this component
- height

- the new

height

of this
component

**See Also:**
- getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

**Since:**
- 1.1

---

#### @Deprecated

public void reshape​(int x,
int y,
int width,
int height)

Reshapes the bounding rectangle for this component.

**Parameters:**
- x

- the

x

coordinate of the upper left corner of the rectangle
- y

- the

y

coordinate of the upper left corner of the rectangle
- width

- the width of the rectangle
- height

- the height of the rectangle

---

#### public void setBounds​(
Rectangle
r)

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- r

- the new bounding rectangle for this component

**Throws:**
- NullPointerException

- if

r

is

null

**See Also:**
- getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

**Since:**
- 1.1

---

#### public int getX()

Returns the current x coordinate of the components origin.
This method is preferable to writing

component.getBounds().x

,
or

component.getLocation().x

because it doesn't
cause any heap allocations.

**Returns:**
- the current x coordinate of the components origin

**Since:**
- 1.2

---

#### public int getY()

Returns the current y coordinate of the components origin.
This method is preferable to writing

component.getBounds().y

,
or

component.getLocation().y

because it
doesn't cause any heap allocations.

**Returns:**
- the current y coordinate of the components origin

**Since:**
- 1.2

---

#### public int getWidth()

Returns the current width of this component.
This method is preferable to writing

component.getBounds().width

,
or

component.getSize().width

because it
doesn't cause any heap allocations.

**Returns:**
- the current width of this component

**Since:**
- 1.2

---

#### public int getHeight()

Returns the current height of this component.
This method is preferable to writing

component.getBounds().height

,
or

component.getSize().height

because it
doesn't cause any heap allocations.

**Returns:**
- the current height of this component

**Since:**
- 1.2

---

#### public
Rectangle
getBounds​(
Rectangle
rv)

Stores the bounds of this component into "return value"

rv

and
return

rv

. If rv is

null

a new

Rectangle

is allocated.
This version of

getBounds

is useful if the caller
wants to avoid allocating a new

Rectangle

object
on the heap.

**Parameters:**
- rv

- the return value, modified to the components bounds

**Returns:**
- rv

---

#### public
Dimension
getSize​(
Dimension
rv)

Stores the width/height of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Dimension

object is allocated. This version of

getSize

is useful if the caller wants to avoid
allocating a new

Dimension

object on the heap.

**Parameters:**
- rv

- the return value, modified to the components size

**Returns:**
- rv

---

#### public
Point
getLocation​(
Point
rv)

Stores the x,y origin of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Point

is allocated.
This version of

getLocation

is useful if the
caller wants to avoid allocating a new

Point

object on the heap.

**Parameters:**
- rv

- the return value, modified to the components location

**Returns:**
- rv

---

#### public boolean isOpaque()

Returns true if this component is completely opaque, returns
false by default.

An opaque component paints every pixel within its
rectangular region. A non-opaque component paints only some of
its pixels, allowing the pixels underneath it to "show through".
A component that does not fully paint its pixels therefore
provides a degree of transparency.

Subclasses that guarantee to always completely paint their
contents should override this method and return true.

**Returns:**
- true if this component is completely opaque

**See Also:**
- isLightweight()

**Since:**
- 1.2

---

#### public boolean isLightweight()

A lightweight component doesn't have a native toolkit peer.
Subclasses of

Component

and

Container

,
other than the ones defined in this package like

Button

or

Scrollbar

, are lightweight.
All of the Swing components are lightweights.

This method will always return

false

if this component
is not displayable because it is impossible to determine the
weight of an undisplayable component.

**Returns:**
- true if this component has a lightweight peer; false if
it has a native peer or no peer

**See Also:**
- isDisplayable()

**Since:**
- 1.2

---

#### public void setPreferredSize​(
Dimension
preferredSize)

Sets the preferred size of this component to a constant
value. Subsequent calls to

getPreferredSize

will always
return this value. Setting the preferred size to

null

restores the default behavior.

**Parameters:**
- preferredSize

- The new preferred size, or null

**See Also:**
- getPreferredSize()

,

isPreferredSizeSet()

**Since:**
- 1.5

---

#### public boolean isPreferredSizeSet()

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

**Returns:**
- true if

setPreferredSize

has been invoked
with a non-null value.

**Since:**
- 1.5

---

#### public
Dimension
getPreferredSize()

Gets the preferred size of this component.

**Returns:**
- a dimension object indicating this component's preferred size

**See Also:**
- getMinimumSize()

,

LayoutManager

---

#### @Deprecated

public
Dimension
preferredSize()

Returns the component's preferred size.

**Returns:**
- the component's preferred size

---

#### public void setMinimumSize​(
Dimension
minimumSize)

Sets the minimum size of this component to a constant
value. Subsequent calls to

getMinimumSize

will always
return this value. Setting the minimum size to

null

restores the default behavior.

**Parameters:**
- minimumSize

- the new minimum size of this component

**See Also:**
- getMinimumSize()

,

isMinimumSizeSet()

**Since:**
- 1.5

---

#### public boolean isMinimumSizeSet()

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

**Returns:**
- true if

setMinimumSize

has been invoked with a
non-null value.

**Since:**
- 1.5

---

#### public
Dimension
getMinimumSize()

Gets the minimum size of this component.

**Returns:**
- a dimension object indicating this component's minimum size

**See Also:**
- getPreferredSize()

,

LayoutManager

---

#### @Deprecated

public
Dimension
minimumSize()

Returns the minimum size of this component.

**Returns:**
- the minimum size of this component

---

#### public void setMaximumSize​(
Dimension
maximumSize)

Sets the maximum size of this component to a constant
value. Subsequent calls to

getMaximumSize

will always
return this value. Setting the maximum size to

null

restores the default behavior.

**Parameters:**
- maximumSize

- a

Dimension

containing the
desired maximum allowable size

**See Also:**
- getMaximumSize()

,

isMaximumSizeSet()

**Since:**
- 1.5

---

#### public boolean isMaximumSizeSet()

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

**Returns:**
- true if

maximumSize

is non-

null

,
false otherwise

**Since:**
- 1.5

---

#### public
Dimension
getMaximumSize()

Gets the maximum size of this component.

**Returns:**
- a dimension object indicating this component's maximum size

**See Also:**
- getMinimumSize()

,

getPreferredSize()

,

LayoutManager

---

#### public float getAlignmentX()

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:**
- the horizontal alignment of this component

---

#### public float getAlignmentY()

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:**
- the vertical alignment of this component

---

#### public int getBaseline​(int width,
int height)

Returns the baseline. The baseline is measured from the top of
the component. This method is primarily meant for

LayoutManager

s to align components along their
baseline. A return value less than 0 indicates this component
does not have a reasonable baseline and that

LayoutManager

s should not align this component on
its baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:**
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- the baseline or < 0 indicating there is no reasonable
baseline

**Throws:**
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- getBaselineResizeBehavior()

,

FontMetrics

**Since:**
- 1.6

---

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior()

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

. Subclasses that have a
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Returns:**
- an enum indicating how the baseline changes as the component
size changes

**See Also:**
- getBaseline(int, int)

**Since:**
- 1.6

---

#### public void doLayout()

Prompts the layout manager to lay out this component. This is
usually called when the component (more specifically, container)
is validated.

**See Also:**
- validate()

,

LayoutManager

---

#### @Deprecated

public void layout()

*No description found.*

---

#### public void validate()

Validates this component.

The meaning of the term

validating

is defined by the ancestors of
this class. See

Container.validate()

for more details.

**See Also:**
- invalidate()

,

doLayout()

,

LayoutManager

,

Container.validate()

**Since:**
- 1.0

---

#### public void invalidate()

Invalidates this component and its ancestors.

By default, all the ancestors of the component up to the top-most
container of the hierarchy are marked invalid. If the

java.awt.smartInvalidate

system property is set to

true

,
invalidation stops on the nearest validate root of this component.
Marking a container

invalid

indicates that the container needs to
be laid out.

This method is called automatically when any layout-related information
changes (e.g. setting the bounds of the component, or adding the
component to a container).

This method might be called often, so it should work fast.

**See Also:**
- validate()

,

doLayout()

,

LayoutManager

,

Container.isValidateRoot()

**Since:**
- 1.0

---

#### public void revalidate()

Revalidates the component hierarchy up to the nearest validate root.

This method first invalidates the component hierarchy starting from this
component up to the nearest validate root. Afterwards, the component
hierarchy is validated starting from the nearest validate root.

This is a convenience method supposed to help application developers
avoid looking for validate roots manually. Basically, it's equivalent to
first calling the

invalidate()

method on this component, and
then calling the

validate()

method on the nearest validate
root.

**See Also:**
- Container.isValidateRoot()

**Since:**
- 1.7

---

#### public
Graphics
getGraphics()

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Returns:**
- a graphics context for this component, or

null

if it has none

**See Also:**
- paint(java.awt.Graphics)

**Since:**
- 1.0

---

#### public
FontMetrics
getFontMetrics​(
Font
font)

Gets the font metrics for the specified font.
Warning: Since Font metrics are affected by the

FontRenderContext

and
this method does not provide one, it can return only metrics for
the default render context which may not match that used when
rendering on the Component if

Graphics2D

functionality is being
used. Instead metrics can be obtained at rendering time by calling

Graphics.getFontMetrics()

or text measurement APIs on the

Font

class.

**Parameters:**
- font

- the font for which font metrics is to be
obtained

**Returns:**
- the font metrics for

font

**See Also:**
- getFont()

,

ComponentPeer.getFontMetrics(Font)

,

Toolkit.getFontMetrics(Font)

**Since:**
- 1.0

---

#### public void setCursor​(
Cursor
cursor)

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Parameters:**
- cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent

**See Also:**
- isEnabled()

,

isShowing()

,

getCursor()

,

contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

**Since:**
- 1.1

---

#### public
Cursor
getCursor()

Gets the cursor set in the component. If the component does
not have a cursor set, the cursor of its parent is returned.
If no cursor is set in the entire hierarchy,

Cursor.DEFAULT_CURSOR

is returned.

**Returns:**
- the cursor for this component

**See Also:**
- setCursor(java.awt.Cursor)

**Since:**
- 1.1

---

#### public boolean isCursorSet()

Returns whether the cursor has been explicitly set for this Component.
If this method returns

false

, this Component is inheriting
its cursor from an ancestor.

**Returns:**
- true

if the cursor has been explicitly set for this
Component;

false

otherwise.

**Since:**
- 1.4

---

#### public void paint​(
Graphics
g)

Paints this component.

This method is called when the contents of the component should
be painted; such as when the component is first being shown or
is damaged and in need of repair. The clip rectangle in the

Graphics

parameter is set to the area
which needs to be painted.
Subclasses of

Component

that override this
method need not call

super.paint(g)

.

For performance reasons,

Component

s with zero width
or height aren't considered to need painting when they are first shown,
and also aren't considered to need repair.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:**
- g

- the graphics context to use for painting

**See Also:**
- update(java.awt.Graphics)

**Since:**
- 1.0

---

#### public void update​(
Graphics
g)

Updates this component.

If this component is not a lightweight component, the
AWT calls the

update

method in response to
a call to

repaint

. You can assume that
the background is not cleared.

The

update

method of

Component

calls this component's

paint

method to redraw
this component. This method is commonly overridden by subclasses
which need to do additional work in response to a call to

repaint

.
Subclasses of Component that override this method should either
call

super.update(g)

, or call

paint(g)

directly from their

update

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:**
- g

- the specified context to use for updating

**See Also:**
- paint(java.awt.Graphics)

,

repaint()

**Since:**
- 1.0

---

#### public void paintAll​(
Graphics
g)

Paints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:**
- g

- the graphics context to use for painting

**See Also:**
- paint(java.awt.Graphics)

**Since:**
- 1.0

---

#### public void repaint()

Repaints this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method as soon as possible. Otherwise, this method causes
a call to this component's

update

method as soon
as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**See Also:**
- update(Graphics)

**Since:**
- 1.0

---

#### public void repaint​(long tm)

Repaints the component. If this component is a lightweight
component, this results in a call to

paint

within

tm

milliseconds.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:**
- tm

- maximum time in milliseconds before update

**See Also:**
- paint(java.awt.Graphics)

,

update(Graphics)

**Since:**
- 1.0

---

#### public void repaint​(int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method
as soon as possible. Otherwise, this method causes a call to
this component's

update

method as soon as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:**
- x

- the

x

coordinate
- y

- the

y

coordinate
- width

- the width
- height

- the height

**See Also:**
- update(Graphics)

**Since:**
- 1.0

---

#### public void repaint​(long tm,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

tm

milliseconds.

If this component is a lightweight component, this method causes
a call to this component's

paint

method.
Otherwise, this method causes a call to this component's

update

method.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:**
- tm

- maximum time in milliseconds before update
- x

- the

x

coordinate
- y

- the

y

coordinate
- width

- the width
- height

- the height

**See Also:**
- update(Graphics)

**Since:**
- 1.0

---

#### public void print​(
Graphics
g)

Prints this component. Applications should override this method
for components that must do special processing before being
printed or should be printed differently than they are painted.

The default implementation of this method calls the

paint

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:**
- g

- the graphics context to use for printing

**See Also:**
- paint(Graphics)

**Since:**
- 1.0

---

#### public void printAll​(
Graphics
g)

Prints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:**
- g

- the graphics context to use for printing

**See Also:**
- print(Graphics)

**Since:**
- 1.0

---

#### public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:**
- imageUpdate

in interface

ImageObserver

**Parameters:**
- img

- the image being observed
- infoflags

- see

imageUpdate

for more information
- x

- the

x

coordinate
- y

- the

y

coordinate
- w

- the width
- h

- the height

**Returns:**
- false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.

**See Also:**
- ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

**Since:**
- 1.0

---

#### public
Image
createImage​(
ImageProducer
producer)

Creates an image from the specified image producer.

**Parameters:**
- producer

- the image producer

**Returns:**
- the image produced

**Since:**
- 1.0

---

#### public
Image
createImage​(int width,
int height)

Creates an off-screen drawable image to be used for double buffering.

**Parameters:**
- width

- the specified width
- height

- the specified height

**Returns:**
- an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- isDisplayable()

,

GraphicsEnvironment.isHeadless()

**Since:**
- 1.0

---

#### public
VolatileImage
createVolatileImage​(int width,
int height)

Creates a volatile off-screen drawable image to be used for double
buffering.

**Parameters:**
- width

- the specified width
- height

- the specified height

**Returns:**
- an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- VolatileImage

,

isDisplayable()

,

GraphicsEnvironment.isHeadless()

**Since:**
- 1.4

---

#### public
VolatileImage
createVolatileImage​(int width,
int height,

ImageCapabilities
caps)
throws
AWTException

Creates a volatile off-screen drawable image, with the given
capabilities. The contents of this image may be lost at any time due to
operating system issues, so the image must be managed via the

VolatileImage

interface.

**Parameters:**
- width

- the specified width
- height

- the specified height
- caps

- the image capabilities

**Returns:**
- a VolatileImage object, which can be used to manage surface
contents loss and capabilities. The

null

value if the
component is not displayable or

GraphicsEnvironment.isHeadless()

returns

true

.

**Throws:**
- AWTException

- if an image with the specified capabilities cannot
be created

**See Also:**
- VolatileImage

**Since:**
- 1.4

---

#### public boolean prepareImage​(
Image
image,

ImageObserver
observer)

Prepares an image for rendering on this component. The image
data is downloaded asynchronously in another thread and the
appropriate screen representation of the image is generated.

**Parameters:**
- image

- the

Image

for which to
prepare a screen representation
- observer

- the

ImageObserver

object
to be notified as the image is being prepared

**Returns:**
- true

if the image has already been fully
prepared;

false

otherwise

**Since:**
- 1.0

---

#### public boolean prepareImage​(
Image
image,
int width,
int height,

ImageObserver
observer)

Prepares an image for rendering on this component at the
specified width and height.

The image data is downloaded asynchronously in another thread,
and an appropriately scaled screen representation of the image is
generated.

**Parameters:**
- image

- the instance of

Image

for which to prepare a screen representation
- width

- the width of the desired screen representation
- height

- the height of the desired screen representation
- observer

- the

ImageObserver

object
to be notified as the image is being prepared

**Returns:**
- true

if the image has already been fully
prepared;

false

otherwise

**See Also:**
- ImageObserver

**Since:**
- 1.0

---

#### public int checkImage​(
Image
image,

ImageObserver
observer)

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:**
- image

- the

Image

object whose status
is being checked
- observer

- the

ImageObserver

object to be notified as the image is being prepared

**Returns:**
- the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available

**See Also:**
- prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

**Since:**
- 1.0

---

#### public int checkImage​(
Image
image,
int width,
int height,

ImageObserver
observer)

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

The

checkImage

method of

Component

calls its peer's

checkImage

method to calculate
the flags. If this component does not yet have a peer, the
component's toolkit's

checkImage

method is called
instead.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:**
- image

- the

Image

object whose status
is being checked
- width

- the width of the scaled version
whose status is to be checked
- height

- the height of the scaled version
whose status is to be checked
- observer

- the

ImageObserver

object
to be notified as the image is being prepared

**Returns:**
- the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available

**See Also:**
- prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

**Since:**
- 1.0

---

#### public void setIgnoreRepaint​(boolean ignoreRepaint)

Sets whether or not paint messages received from the operating system
should be ignored. This does not affect paint events generated in
software by the AWT, unless they are an immediate response to an
OS-level paint message.

This is useful, for example, if running under full-screen mode and
better performance is desired, or if page-flipping is used as the
buffer strategy.

**Parameters:**
- ignoreRepaint

-

true

if the paint messages from the OS
should be ignored; otherwise

false

**See Also:**
- getIgnoreRepaint()

,

Canvas.createBufferStrategy(int)

,

Window.createBufferStrategy(int)

,

BufferStrategy

,

GraphicsDevice.setFullScreenWindow(java.awt.Window)

**Since:**
- 1.4

---

#### public boolean getIgnoreRepaint()

**Returns:**
- whether or not paint messages received from the operating system
should be ignored.

**See Also:**
- setIgnoreRepaint(boolean)

**Since:**
- 1.4

---

#### public boolean contains​(int x,
int y)

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

**Parameters:**
- x

- the

x

coordinate of the point
- y

- the

y

coordinate of the point

**Returns:**
- true

if the point is within the component;
otherwise

false

**See Also:**
- getComponentAt(int, int)

**Since:**
- 1.1

---

#### @Deprecated

public boolean inside​(int x,
int y)

Checks whether the point is inside of this component.

**Parameters:**
- x

- the

x

coordinate of the point
- y

- the

y

coordinate of the point

**Returns:**
- true

if the point is within the component;
otherwise

false

---

#### public boolean contains​(
Point
p)

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

**Parameters:**
- p

- the point

**Returns:**
- true

if the point is within the component;
otherwise

false

**Throws:**
- NullPointerException

- if

p

is

null

**See Also:**
- getComponentAt(Point)

**Since:**
- 1.1

---

#### public
Component
getComponentAt​(int x,
int y)

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component. This method only
looks one level deep. If the point (

x

,

y

) is
inside a subcomponent that itself has subcomponents, it does not
go looking down the subcomponent tree.

The

locate

method of

Component

simply
returns the component itself if the (

x

,

y

)
coordinate location is inside its bounding box, and

null

otherwise.

**Parameters:**
- x

- the

x

coordinate
- y

- the

y

coordinate

**Returns:**
- the component or subcomponent that contains the
(

x

,

y

) location;

null

if the location
is outside this component

**See Also:**
- contains(int, int)

**Since:**
- 1.0

---

#### @Deprecated

public
Component
locate​(int x,
int y)

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

**Parameters:**
- x

- the

x

coordinate to search for components at
- y

- the

y

coordinate to search for components at

**Returns:**
- the component at the specified location or

null

---

#### public
Component
getComponentAt​(
Point
p)

Returns the component or subcomponent that contains the
specified point.

**Parameters:**
- p

- the point

**Returns:**
- the component at the specified location or

null

**See Also:**
- contains(int, int)

**Since:**
- 1.1

---

#### @Deprecated

public void deliverEvent​(
Event
e)

**Parameters:**
- e

- the event to deliver

---

#### public final void dispatchEvent​(
AWTEvent
e)

Dispatches an event to this component or one of its sub components.
Calls

processEvent

before returning for 1.1-style
events which have been enabled for the

Component

.

**Parameters:**
- e

- the event

---

#### @Deprecated

public boolean postEvent​(
Event
e)

Description copied from interface:

MenuContainer

**Specified by:**
- postEvent

in interface

MenuContainer

**Parameters:**
- e

- the event to dispatch

**Returns:**
- the results of posting the event

---

#### public void addComponentListener​(
ComponentListener
l)

Adds the specified component listener to receive component events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the component listener

**See Also:**
- ComponentEvent

,

ComponentListener

,

removeComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

**Since:**
- 1.1

---

#### public void removeComponentListener​(
ComponentListener
l)

Removes the specified component listener so that it no longer
receives component events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the component listener

**See Also:**
- ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

**Since:**
- 1.1

---

#### public
ComponentListener
[] getComponentListeners()

Returns an array of all the component listeners
registered on this component.

**Returns:**
- all

ComponentListener

s of this component
or an empty array if no component
listeners are currently registered

**See Also:**
- addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

**Since:**
- 1.4

---

#### public void addFocusListener​(
FocusListener
l)

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the focus listener

**See Also:**
- FocusEvent

,

FocusListener

,

removeFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

**Since:**
- 1.1

---

#### public void removeFocusListener​(
FocusListener
l)

Removes the specified focus listener so that it no longer
receives focus events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the focus listener

**See Also:**
- FocusEvent

,

FocusListener

,

addFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

**Since:**
- 1.1

---

#### public
FocusListener
[] getFocusListeners()

Returns an array of all the focus listeners
registered on this component.

**Returns:**
- all of this component's

FocusListener

s
or an empty array if no component
listeners are currently registered

**See Also:**
- addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

**Since:**
- 1.4

---

#### public void addHierarchyListener​(
HierarchyListener
l)

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the hierarchy listener

**See Also:**
- HierarchyEvent

,

HierarchyListener

,

removeHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

**Since:**
- 1.3

---

#### public void removeHierarchyListener​(
HierarchyListener
l)

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the hierarchy listener

**See Also:**
- HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

**Since:**
- 1.3

---

#### public
HierarchyListener
[] getHierarchyListeners()

Returns an array of all the hierarchy listeners
registered on this component.

**Returns:**
- all of this component's

HierarchyListener

s
or an empty array if no hierarchy
listeners are currently registered

**See Also:**
- addHierarchyListener(java.awt.event.HierarchyListener)

,

removeHierarchyListener(java.awt.event.HierarchyListener)

**Since:**
- 1.4

---

#### public void addHierarchyBoundsListener​(
HierarchyBoundsListener
l)

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the hierarchy bounds listener

**See Also:**
- HierarchyEvent

,

HierarchyBoundsListener

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

**Since:**
- 1.3

---

#### public void removeHierarchyBoundsListener​(
HierarchyBoundsListener
l)

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the hierarchy bounds listener

**See Also:**
- HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

**Since:**
- 1.3

---

#### public
HierarchyBoundsListener
[] getHierarchyBoundsListeners()

Returns an array of all the hierarchy bounds listeners
registered on this component.

**Returns:**
- all of this component's

HierarchyBoundsListener

s
or an empty array if no hierarchy bounds
listeners are currently registered

**See Also:**
- addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

**Since:**
- 1.4

---

#### public void addKeyListener​(
KeyListener
l)

Adds the specified key listener to receive key events from
this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the key listener.

**See Also:**
- KeyEvent

,

KeyListener

,

removeKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

**Since:**
- 1.1

---

#### public void removeKeyListener​(
KeyListener
l)

Removes the specified key listener so that it no longer
receives key events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the key listener

**See Also:**
- KeyEvent

,

KeyListener

,

addKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

**Since:**
- 1.1

---

#### public
KeyListener
[] getKeyListeners()

Returns an array of all the key listeners
registered on this component.

**Returns:**
- all of this component's

KeyListener

s
or an empty array if no key
listeners are currently registered

**See Also:**
- addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

**Since:**
- 1.4

---

#### public void addMouseListener​(
MouseListener
l)

Adds the specified mouse listener to receive mouse events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the mouse listener

**See Also:**
- MouseEvent

,

MouseListener

,

removeMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

**Since:**
- 1.1

---

#### public void removeMouseListener​(
MouseListener
l)

Removes the specified mouse listener so that it no longer
receives mouse events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the mouse listener

**See Also:**
- MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

**Since:**
- 1.1

---

#### public
MouseListener
[] getMouseListeners()

Returns an array of all the mouse listeners
registered on this component.

**Returns:**
- all of this component's

MouseListener

s
or an empty array if no mouse
listeners are currently registered

**See Also:**
- addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

**Since:**
- 1.4

---

#### public void addMouseMotionListener​(
MouseMotionListener
l)

Adds the specified mouse motion listener to receive mouse motion
events from this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the mouse motion listener

**See Also:**
- MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

**Since:**
- 1.1

---

#### public void removeMouseMotionListener​(
MouseMotionListener
l)

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the mouse motion listener

**See Also:**
- MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

**Since:**
- 1.1

---

#### public
MouseMotionListener
[] getMouseMotionListeners()

Returns an array of all the mouse motion listeners
registered on this component.

**Returns:**
- all of this component's

MouseMotionListener

s
or an empty array if no mouse motion
listeners are currently registered

**See Also:**
- addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

**Since:**
- 1.4

---

#### public void addMouseWheelListener​(
MouseWheelListener
l)

Adds the specified mouse wheel listener to receive mouse wheel events
from this component. Containers also receive mouse wheel events from
sub-components.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the mouse wheel listener

**See Also:**
- MouseWheelEvent

,

MouseWheelListener

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

**Since:**
- 1.4

---

#### public void removeMouseWheelListener​(
MouseWheelListener
l)

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the mouse wheel listener.

**See Also:**
- MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

**Since:**
- 1.4

---

#### public
MouseWheelListener
[] getMouseWheelListeners()

Returns an array of all the mouse wheel listeners
registered on this component.

**Returns:**
- all of this component's

MouseWheelListener

s
or an empty array if no mouse wheel
listeners are currently registered

**See Also:**
- addMouseWheelListener(java.awt.event.MouseWheelListener)

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

**Since:**
- 1.4

---

#### public void addInputMethodListener​(
InputMethodListener
l)

Adds the specified input method listener to receive
input method events from this component. A component will
only receive input method events from input methods
if it also overrides

getInputMethodRequests

to return an

InputMethodRequests

instance.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the input method listener

**See Also:**
- InputMethodEvent

,

InputMethodListener

,

removeInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

,

getInputMethodRequests()

**Since:**
- 1.2

---

#### public void removeInputMethodListener​(
InputMethodListener
l)

Removes the specified input method listener so that it no longer
receives input method events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the input method listener

**See Also:**
- InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

**Since:**
- 1.2

---

#### public
InputMethodListener
[] getInputMethodListeners()

Returns an array of all the input method listeners
registered on this component.

**Returns:**
- all of this component's

InputMethodListener

s
or an empty array if no input method
listeners are currently registered

**See Also:**
- addInputMethodListener(java.awt.event.InputMethodListener)

,

removeInputMethodListener(java.awt.event.InputMethodListener)

**Since:**
- 1.4

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Component c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
- NullPointerException

- if

listenerType

is

null

**See Also:**
- getComponentListeners()

,

getFocusListeners()

,

getHierarchyListeners()

,

getHierarchyBoundsListeners()

,

getKeyListeners()

,

getMouseListeners()

,

getMouseMotionListeners()

,

getMouseWheelListeners()

,

getInputMethodListeners()

,

getPropertyChangeListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of the listeners

---

#### public
InputMethodRequests
getInputMethodRequests()

Gets the input method request handler which supports
requests from input methods for this component. A component
that supports on-the-spot text input must override this
method to return an

InputMethodRequests

instance.
At the same time, it also has to handle input method events.

**Returns:**
- the input method request handler for this component,

null

by default

**See Also:**
- addInputMethodListener(java.awt.event.InputMethodListener)

**Since:**
- 1.2

---

#### public
InputContext
getInputContext()

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component. By default, the input context used for
the parent component is returned. Components may
override this to return a private input context.

**Returns:**
- the input context used by this component;

null

if no context can be determined

**Since:**
- 1.2

---

#### protected final void enableEvents​(long eventsToEnable)

Enables the events defined by the specified event mask parameter
to be delivered to this component.

Event types are automatically enabled when a listener for
that event type is added to the component.

This method only needs to be invoked by subclasses of

Component

which desire to have the specified event
types delivered to

processEvent

regardless of whether
or not a listener is registered.

**Parameters:**
- eventsToEnable

- the event mask defining the event types

**See Also:**
- processEvent(java.awt.AWTEvent)

,

disableEvents(long)

,

AWTEvent

**Since:**
- 1.1

---

#### protected final void disableEvents​(long eventsToDisable)

Disables the events defined by the specified event mask parameter
from being delivered to this component.

**Parameters:**
- eventsToDisable

- the event mask defining the event types

**See Also:**
- enableEvents(long)

**Since:**
- 1.1

---

#### protected
AWTEvent
coalesceEvents​(
AWTEvent
existingEvent,

AWTEvent
newEvent)

Potentially coalesce an event being posted with an existing
event. This method is called by

EventQueue.postEvent

if an event with the same ID as the event to be posted is found in
the queue (both events must have this component as their source).
This method either returns a coalesced event which replaces
the existing event (and the new event is then discarded), or

null

to indicate that no combining should be done
(add the second event to the end of the queue). Either event
parameter may be modified and returned, as the other one is discarded
unless

null

is returned.

This implementation of

coalesceEvents

coalesces
two event types: mouse move (and drag) events,
and paint (and update) events.
For mouse move events the last event is always returned, causing
intermediate moves to be discarded. For paint events, the new
event is coalesced into a complex

RepaintArea

in the peer.
The new

AWTEvent

is always returned.

**Parameters:**
- existingEvent

- the event already on the

EventQueue
- newEvent

- the event being posted to the

EventQueue

**Returns:**
- a coalesced event, or

null

indicating that no
coalescing was done

---

#### protected void processEvent​(
AWTEvent
e)

Processes events occurring on this component. By default this
method calls the appropriate

process<event type>Event

method for the given class of event.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the event

**See Also:**
- processComponentEvent(java.awt.event.ComponentEvent)

,

processFocusEvent(java.awt.event.FocusEvent)

,

processKeyEvent(java.awt.event.KeyEvent)

,

processMouseEvent(java.awt.event.MouseEvent)

,

processMouseMotionEvent(java.awt.event.MouseEvent)

,

processInputMethodEvent(java.awt.event.InputMethodEvent)

,

processHierarchyEvent(java.awt.event.HierarchyEvent)

,

processMouseWheelEvent(java.awt.event.MouseWheelEvent)

**Since:**
- 1.1

---

#### protected void processComponentEvent​(
ComponentEvent
e)

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

This method is not called unless component events are
enabled for this component. Component events are enabled
when one of the following occurs:

- A

ComponentListener

object is registered
via

addComponentListener

.

Component events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the component event

**See Also:**
- ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

enableEvents(long)

**Since:**
- 1.1

---

#### protected void processFocusEvent​(
FocusEvent
e)

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

This method is not called unless focus events are
enabled for this component. Focus events are enabled
when one of the following occurs:

- A

FocusListener

object is registered
via

addFocusListener

.

Focus events are enabled via

enableEvents

.

If focus events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a focus event should be dispatched to
registered

FocusListener

objects. If the
events are to be dispatched, the

KeyboardFocusManager

calls the

Component

's

dispatchEvent

method, which results in a call to the

Component

's

processFocusEvent

method.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the focus event

**See Also:**
- FocusEvent

,

FocusListener

,

KeyboardFocusManager

,

addFocusListener(java.awt.event.FocusListener)

,

enableEvents(long)

,

dispatchEvent(java.awt.AWTEvent)

**Since:**
- 1.1

---

#### protected void processKeyEvent​(
KeyEvent
e)

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

This method is not called unless key events are
enabled for this component. Key events are enabled
when one of the following occurs:

- A

KeyListener

object is registered
via

addKeyListener

.

Key events are enabled via

enableEvents

.

If key events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a key event should be dispatched to
registered

KeyListener

objects. The

DefaultKeyboardFocusManager

will not dispatch
key events to a

Component

that is not the focus
owner or is not showing.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the key event

**See Also:**
- KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

processEvent(java.awt.AWTEvent)

,

dispatchEvent(java.awt.AWTEvent)

,

addKeyListener(java.awt.event.KeyListener)

,

enableEvents(long)

,

isShowing()

**Since:**
- 1.1

---

#### protected void processMouseEvent​(
MouseEvent
e)

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

This method is not called unless mouse events are
enabled for this component. Mouse events are enabled
when one of the following occurs:

- A

MouseListener

object is registered
via

addMouseListener

.

Mouse events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

enableEvents(long)

**Since:**
- 1.1

---

#### protected void processMouseMotionEvent​(
MouseEvent
e)

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

This method is not called unless mouse motion events are
enabled for this component. Mouse motion events are enabled
when one of the following occurs:

- A

MouseMotionListener

object is registered
via

addMouseMotionListener

.

Mouse motion events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the mouse motion event

**See Also:**
- MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

enableEvents(long)

**Since:**
- 1.1

---

#### protected void processMouseWheelEvent​(
MouseWheelEvent
e)

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

This method is not called unless mouse wheel events are
enabled for this component. Mouse wheel events are enabled
when one of the following occurs:

- A

MouseWheelListener

object is registered
via

addMouseWheelListener

.

Mouse wheel events are enabled via

enableEvents

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the mouse wheel event

**See Also:**
- MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

enableEvents(long)

**Since:**
- 1.4

---

#### protected void processInputMethodEvent​(
InputMethodEvent
e)

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

This method is not called unless input method events
are enabled for this component. Input method events are enabled
when one of the following occurs:

- An

InputMethodListener

object is registered
via

addInputMethodListener

.

Input method events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the input method event

**See Also:**
- InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

enableEvents(long)

**Since:**
- 1.2

---

#### protected void processHierarchyEvent​(
HierarchyEvent
e)

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

This method is not called unless hierarchy events
are enabled for this component. Hierarchy events are enabled
when one of the following occurs:

- An

HierarchyListener

object is registered
via

addHierarchyListener

.

Hierarchy events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the hierarchy event

**See Also:**
- HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

enableEvents(long)

**Since:**
- 1.3

---

#### protected void processHierarchyBoundsEvent​(
HierarchyEvent
e)

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

This method is not called unless hierarchy bounds events
are enabled for this component. Hierarchy bounds events are enabled
when one of the following occurs:

- An

HierarchyBoundsListener

object is registered
via

addHierarchyBoundsListener

.

Hierarchy bounds events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the hierarchy event

**See Also:**
- HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

enableEvents(long)

**Since:**
- 1.3

---

#### @Deprecated

public boolean handleEvent​(
Event
evt)

**Parameters:**
- evt

- the event to handle

**Returns:**
- true

if the event was handled,

false

otherwise

---

#### @Deprecated

public boolean mouseDown​(
Event
evt,
int x,
int y)

**Parameters:**
- evt

- the event to handle
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- false

---

#### @Deprecated

public boolean mouseDrag​(
Event
evt,
int x,
int y)

**Parameters:**
- evt

- the event to handle
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- false

---

#### @Deprecated

public boolean mouseUp​(
Event
evt,
int x,
int y)

**Parameters:**
- evt

- the event to handle
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- false

---

#### @Deprecated

public boolean mouseMove​(
Event
evt,
int x,
int y)

**Parameters:**
- evt

- the event to handle
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- false

---

#### @Deprecated

public boolean mouseEnter​(
Event
evt,
int x,
int y)

**Parameters:**
- evt

- the event to handle
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- false

---

#### @Deprecated

public boolean mouseExit​(
Event
evt,
int x,
int y)

**Parameters:**
- evt

- the event to handle
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- false

---

#### @Deprecated

public boolean keyDown​(
Event
evt,
int key)

**Parameters:**
- evt

- the event to handle
- key

- the key pressed

**Returns:**
- false

---

#### @Deprecated

public boolean keyUp​(
Event
evt,
int key)

**Parameters:**
- evt

- the event to handle
- key

- the key pressed

**Returns:**
- false

---

#### @Deprecated

public boolean action​(
Event
evt,

Object
what)

**Parameters:**
- evt

- the event to handle
- what

- the object acted on

**Returns:**
- false

---

#### public void addNotify()

Makes this

Component

displayable by connecting it to a
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**See Also:**
- isDisplayable()

,

removeNotify()

,

invalidate()

**Since:**
- 1.0

---

#### public void removeNotify()

Makes this

Component

undisplayable by destroying it native
screen resource.

This method is called by the toolkit internally and should
not be called directly by programs. Code overriding
this method should call

super.removeNotify

as
the first line of the overriding method.

**See Also:**
- isDisplayable()

,

addNotify()

**Since:**
- 1.0

---

#### @Deprecated

public boolean gotFocus​(
Event
evt,

Object
what)

**Parameters:**
- evt

- the event to handle
- what

- the object focused

**Returns:**
- false

---

#### @Deprecated

public boolean lostFocus​(
Event
evt,

Object
what)

**Parameters:**
- evt

- the event to handle
- what

- the object focused

**Returns:**
- false

---

#### @Deprecated

public boolean isFocusTraversable()

Returns whether this

Component

can become the focus
owner.

**Returns:**
- true

if this

Component

is
focusable;

false

otherwise

**See Also:**
- setFocusable(boolean)

**Since:**
- 1.1

---

#### public boolean isFocusable()

Returns whether this Component can be focused.

**Returns:**
- true

if this Component is focusable;

false

otherwise.

**See Also:**
- setFocusable(boolean)

**Since:**
- 1.4

---

#### public void setFocusable​(boolean focusable)

Sets the focusable state of this Component to the specified value. This
value overrides the Component's default focusability.

**Parameters:**
- focusable

- indicates whether this Component is focusable

**See Also:**
- isFocusable()

**Since:**
- 1.4

---

#### public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Component.

The default values for a Component's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Component's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Component. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Parameters:**
- id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
- keystrokes

- the Set of AWTKeyStroke for the specified operation

**Throws:**
- IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Component

**See Also:**
- getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

**Since:**
- 1.4

---

#### public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Component. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Component, then this Component's parent's Set is returned. If no Set
has been explicitly defined for any of this Component's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Parameters:**
- id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

**Returns:**
- the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.

**Throws:**
- IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

**See Also:**
- setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

**Since:**
- 1.4

---

#### public boolean areFocusTraversalKeysSet​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component. If
this method returns

false

, this Component is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Parameters:**
- id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

**Returns:**
- true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.

**Throws:**
- IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

**Since:**
- 1.4

---

#### public void setFocusTraversalKeysEnabled​(boolean focusTraversalKeysEnabled)

Sets whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Parameters:**
- focusTraversalKeysEnabled

- whether focus traversal keys are
enabled for this Component

**See Also:**
- getFocusTraversalKeysEnabled()

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

**Since:**
- 1.4

---

#### public boolean getFocusTraversalKeysEnabled()

Returns whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Returns:**
- whether focus traversal keys are enabled for this Component

**See Also:**
- setFocusTraversalKeysEnabled(boolean)

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

**Since:**
- 1.4

---

#### public void requestFocus()

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window. This
component must be displayable, focusable, visible and all of
its ancestors (with the exception of the top-level Window) must
be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event. If this request is denied because this
Component's top-level Window cannot become the focused Window,
the request will be remembered and will be granted when the
Window is later focused by the user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**See Also:**
- requestFocusInWindow()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

**Since:**
- 1.0

---

#### public void requestFocus​(
FocusEvent.Cause
cause)

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level Window)
must be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of method. If this request is denied because this Component's
top-level Window cannot become the focused Window, the request will be
remembered and will be granted when the Window is later focused by the
user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:**
- cause

- the cause why the focus is requested

**See Also:**
- FocusEvent

,

FocusEvent.Cause

,

requestFocusInWindow(FocusEvent.Cause)

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

**Since:**
- 9

---

#### protected boolean requestFocus​(boolean temporary)

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:**
- temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification

**Returns:**
- false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed

**See Also:**
- FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

**Since:**
- 1.4

---

#### protected boolean requestFocus​(boolean temporary,

FocusEvent.Cause
cause)

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the {FocusEvent}
generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:**
- temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
- cause

- the cause why the focus is requested

**Returns:**
- false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed

**See Also:**
- FocusEvent

,

FocusEvent.Cause

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

**Since:**
- 9

---

#### public boolean requestFocusInWindow()

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Returns:**
- false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed

**See Also:**
- requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

**Since:**
- 1.4

---

#### public boolean requestFocusInWindow​(
FocusEvent.Cause
cause)

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:**
- cause

- the cause why the focus is requested

**Returns:**
- false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed

**See Also:**
- requestFocus(FocusEvent.Cause)

,

FocusEvent

,

FocusEvent.Cause

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

**Since:**
- 9

---

#### protected boolean requestFocusInWindow​(boolean temporary)

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:**
- temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification

**Returns:**
- false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed

**See Also:**
- requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

**Since:**
- 1.4

---

#### public
Container
getFocusCycleRootAncestor()

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle. Each focus traversal cycle has only a single
focus cycle root and each Component which is not a Container belongs to
only a single focus traversal cycle. Containers which are focus cycle
roots belong to two cycles: one rooted at the Container itself, and one
rooted at the Container's nearest focus-cycle-root ancestor. For such
Containers, this method will return the Container's nearest focus-cycle-
root ancestor.

**Returns:**
- this Component's nearest focus-cycle-root ancestor

**See Also:**
- Container.isFocusCycleRoot()

**Since:**
- 1.4

---

#### public boolean isFocusCycleRoot​(
Container
container)

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Component which is not a Container
belongs to only a single focus traversal cycle.

**Parameters:**
- container

- the Container to be tested

**Returns:**
- true

if the specified Container is a focus-cycle-
root of this Component;

false

otherwise

**See Also:**
- Container.isFocusCycleRoot()

**Since:**
- 1.4

---

#### public void transferFocus()

Transfers the focus to the next component, as though this Component were
the focus owner.

**See Also:**
- requestFocus()

**Since:**
- 1.1

---

#### @Deprecated

public void nextFocus()

*No description found.*

---

#### public void transferFocusBackward()

Transfers the focus to the previous component, as though this Component
were the focus owner.

**See Also:**
- requestFocus()

**Since:**
- 1.4

---

#### public void transferFocusUpCycle()

Transfers the focus up one focus traversal cycle. Typically, the focus
owner is set to this Component's focus cycle root, and the current focus
cycle root is set to the new focus owner's focus cycle root. If,
however, this Component's focus cycle root is a Window, then the focus
owner is set to the focus cycle root's default Component to focus, and
the current focus cycle root is unchanged.

**See Also:**
- requestFocus()

,

Container.isFocusCycleRoot()

,

Container.setFocusCycleRoot(boolean)

**Since:**
- 1.4

---

#### public boolean hasFocus()

Returns

true

if this

Component

is the
focus owner. This method is obsolete, and has been replaced by

isFocusOwner()

.

**Returns:**
- true

if this

Component

is the
focus owner;

false

otherwise

**Since:**
- 1.2

---

#### public boolean isFocusOwner()

Returns

true

if this

Component

is the
focus owner.

**Returns:**
- true

if this

Component

is the
focus owner;

false

otherwise

**Since:**
- 1.4

---

#### public void add​(
PopupMenu
popup)

Adds the specified popup menu to the component.

**Parameters:**
- popup

- the popup menu to be added to the component.

**Throws:**
- NullPointerException

- if

popup

is

null

**See Also:**
- remove(MenuComponent)

**Since:**
- 1.1

---

#### public void remove​(
MenuComponent
popup)

Removes the specified popup menu from the component.

**Specified by:**
- remove

in interface

MenuContainer

**Parameters:**
- popup

- the popup menu to be removed

**See Also:**
- add(PopupMenu)

**Since:**
- 1.1

---

#### protected
String
paramString()

Returns a string representing the state of this component. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:**
- a string representation of this component's state

**Since:**
- 1.0

---

#### public
String
toString()

Returns a string representation of this component and its values.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this component

**Since:**
- 1.0

---

#### public void list()

Prints a listing of this component to the standard system output
stream

System.out

.

**See Also:**
- System.out

**Since:**
- 1.0

---

#### public void list​(
PrintStream
out)

Prints a listing of this component to the specified output
stream.

**Parameters:**
- out

- a print stream

**Throws:**
- NullPointerException

- if

out

is

null

**Since:**
- 1.0

---

#### public void list​(
PrintStream
out,
int indent)

Prints out a list, starting at the specified indentation, to the
specified print stream.

**Parameters:**
- out

- a print stream
- indent

- number of spaces to indent

**Throws:**
- NullPointerException

- if

out

is

null

**See Also:**
- PrintStream.println(java.lang.Object)

**Since:**
- 1.0

---

#### public void list​(
PrintWriter
out)

Prints a listing to the specified print writer.

**Parameters:**
- out

- the print writer to print to

**Throws:**
- NullPointerException

- if

out

is

null

**Since:**
- 1.1

---

#### public void list​(
PrintWriter
out,
int indent)

Prints out a list, starting at the specified indentation, to
the specified print writer.

**Parameters:**
- out

- the print writer to print to
- indent

- the number of spaces to indent

**Throws:**
- NullPointerException

- if

out

is

null

**See Also:**
- PrintStream.println(java.lang.Object)

**Since:**
- 1.1

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Component's preferred size ("preferredSize")
- this Component's minimum size ("minimumSize")
- this Component's maximum size ("maximumSize")
- this Component's name ("name")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:**
- listener

- the property change listener to be added

**See Also:**
- removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a PropertyChangeListener from the listener list. This method
should be used to remove PropertyChangeListeners that were registered
for all bound properties of this class.

If listener is null, no exception is thrown and no action is performed.

**Parameters:**
- listener

- the PropertyChangeListener to be removed

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

---

#### public
PropertyChangeListener
[] getPropertyChangeListeners()

Returns an array of all the property change listeners
registered on this component.

**Returns:**
- all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

PropertyChangeSupport.getPropertyChangeListeners()

**Since:**
- 1.4

---

#### public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:**
- propertyName

- one of the property names listed above
- listener

- the property change listener to be added

**See Also:**
- removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

---

#### public void removePropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)

Removes a

PropertyChangeListener

from the listener
list for a specific property. This method should be used to remove

PropertyChangeListener

s
that were registered for a specific bound property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:**
- propertyName

- a valid property name
- listener

- the PropertyChangeListener to be removed

**See Also:**
- addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public
PropertyChangeListener
[] getPropertyChangeListeners​(
String
propertyName)

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:**
- propertyName

- the property name

**Returns:**
- all of the

PropertyChangeListener

s associated with
the named property; if no such listeners have been added or
if

propertyName

is

null

, an empty
array is returned

**See Also:**
- addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

**Since:**
- 1.4

---

#### protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Support for reporting bound property changes for Object properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

#### protected void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

**Since:**
- 1.4

---

#### protected void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)

Support for reporting bound property changes for integer properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

**Since:**
- 1.4

---

#### public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)

Reports a bound property change.

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a byte)
- newValue

- the new value of the property (as a byte)

**See Also:**
- firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

**Since:**
- 1.5

---

#### public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)

Reports a bound property change.

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a char)
- newValue

- the new value of the property (as a char)

**See Also:**
- firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

**Since:**
- 1.5

---

#### public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)

Reports a bound property change.

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a short)
- newValue

- the new value of the property (as a short)

**See Also:**
- firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

**Since:**
- 1.5

---

#### public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)

Reports a bound property change.

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a long)
- newValue

- the new value of the property (as a long)

**See Also:**
- firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

**Since:**
- 1.5

---

#### public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)

Reports a bound property change.

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a float)
- newValue

- the new value of the property (as a float)

**See Also:**
- firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

**Since:**
- 1.5

---

#### public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)

Reports a bound property change.

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a double)
- newValue

- the new value of the property (as a double)

**See Also:**
- firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

**Since:**
- 1.5

---

#### public void setComponentOrientation​(
ComponentOrientation
o)

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component. Language-sensitive

LayoutManager

and

Component

subclasses will use this property to
determine how to lay out and draw components.

At construction time, a component's orientation is set to

ComponentOrientation.UNKNOWN

,
indicating that it has not been specified
explicitly. The UNKNOWN orientation behaves the same as

ComponentOrientation.LEFT_TO_RIGHT

.

To set the orientation of a single component, use this method.
To set the orientation of an entire component
hierarchy, use

applyComponentOrientation

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- o

- the orientation to be set

**See Also:**
- ComponentOrientation

,

invalidate()

---

#### public
ComponentOrientation
getComponentOrientation()

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

LayoutManager

and

Component

subclasses that wish to respect orientation should call this method to
get the component's orientation before performing layout or drawing.

**Returns:**
- the orientation to order the elements or text

**See Also:**
- ComponentOrientation

---

#### public void applyComponentOrientation​(
ComponentOrientation
orientation)

Sets the

ComponentOrientation

property of this component
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- orientation

- the new component orientation of this component and
the components contained within it.

**Throws:**
- NullPointerException

- if

orientation

is null.

**See Also:**
- setComponentOrientation(java.awt.ComponentOrientation)

,

getComponentOrientation()

,

invalidate()

**Since:**
- 1.4

---

#### public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated
with this

Component

.
The method implemented by this base
class returns null. Classes that extend

Component

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:**
- the

AccessibleContext

of this

Component

**Since:**
- 1.3

---

#### public void setMixingCutoutShape​(
Shape
shape)

Sets a 'mixing-cutout' shape for this lightweight component.

This method is used exclusively for the purposes of the
Heavyweight/Lightweight Components Mixing feature and will
have no effect if applied to a heavyweight component.

By default a lightweight component is treated as an opaque rectangle for
the purposes of the Heavyweight/Lightweight Components Mixing feature.
This method enables developers to set an arbitrary shape to be cut out
from heavyweight components positioned underneath the lightweight
component in the z-order.

The

shape

argument may have the following values:

- null

- reverts the default cutout shape (the rectangle equal
to the component's

getBounds()

)

empty-shape

- does not cut out anything from heavyweight
components. This makes this lightweight component effectively
transparent. Note that descendants of the lightweight component still
affect the shapes of heavyweight components. An example of an

empty-shape

is

new Rectangle()

.

non-empty-shape

- the given shape will be cut out from
heavyweight components.

The most common example when the 'mixing-cutout' shape is needed is a
glass pane component. The

JRootPane.setGlassPane(java.awt.Component)

method
automatically sets the

empty-shape

as the 'mixing-cutout' shape
for the given glass pane component. If a developer needs some other
'mixing-cutout' shape for the glass pane (which is rare), this must be
changed manually after installing the glass pane to the root pane.

**Parameters:**
- shape

- the new 'mixing-cutout' shape

**Since:**
- 9

---

### Additional Sections

#### Class Component

java.lang.Object

- java.awt.Component

java.awt.Component

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

**Direct Known Subclasses:** Button

,

Canvas

,

Checkbox

,

Choice

,

Container

,

Label

,

List

,

Scrollbar

,

TextComponent

```java
public abstract class
Component

extends
Object

implements
ImageObserver
,
MenuContainer
,
Serializable
```

A

component

is an object having a graphical representation
that can be displayed on the screen and that can interact with the
user. Examples of components are the buttons, checkboxes, and scrollbars
of a typical graphical user interface.

The

Component

class is the abstract superclass of
the nonmenu-related Abstract Window Toolkit components. Class

Component

can also be extended directly to create a
lightweight component. A lightweight component is a component that is
not associated with a native window. On the contrary, a heavyweight
component is associated with a native window. The

isLightweight()

method may be used to distinguish between the two kinds of the components.

Lightweight and heavyweight components may be mixed in a single component
hierarchy. However, for correct operating of such a mixed hierarchy of
components, the whole hierarchy must be valid. When the hierarchy gets
invalidated, like after changing the bounds of components, or
adding/removing components to/from containers, the whole hierarchy must be
validated afterwards by means of the

Container.validate()

method
invoked on the top-most invalid container of the hierarchy.

Serialization

It is important to note that only AWT listeners which conform
to the

Serializable

protocol will be saved when
the object is stored. If an AWT object has listeners that
aren't marked serializable, they will be dropped at

writeObject

time. Developers will need, as always,
to consider the implications of making an object serializable.
One situation to watch out for is this:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements ActionListener, Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

MyApp()
{
// Oops, now aButton has a listener with a reference
// to bigOne!
aButton.addActionListener(this);
}

public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}
```

In this example, serializing

aButton

by itself
will cause

MyApp

and everything it refers to
to be serialized as well. The problem is that the listener
is serializable by coincidence, not by design. To separate
the decisions about

MyApp

and the

ActionListener

being serializable one can use a
nested class, as in the following example:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements java.io.Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

static class MyActionListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}

MyApp()
{
aButton.addActionListener(new MyActionListener());
}
}
```

Note

: For more information on the paint mechanisms utilized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**See Also:** Serialized Form

public abstract class

Component

extends

Object

implements

ImageObserver

,

MenuContainer

,

Serializable

A

component

is an object having a graphical representation
that can be displayed on the screen and that can interact with the
user. Examples of components are the buttons, checkboxes, and scrollbars
of a typical graphical user interface.

The

Component

class is the abstract superclass of
the nonmenu-related Abstract Window Toolkit components. Class

Component

can also be extended directly to create a
lightweight component. A lightweight component is a component that is
not associated with a native window. On the contrary, a heavyweight
component is associated with a native window. The

isLightweight()

method may be used to distinguish between the two kinds of the components.

Lightweight and heavyweight components may be mixed in a single component
hierarchy. However, for correct operating of such a mixed hierarchy of
components, the whole hierarchy must be valid. When the hierarchy gets
invalidated, like after changing the bounds of components, or
adding/removing components to/from containers, the whole hierarchy must be
validated afterwards by means of the

Container.validate()

method
invoked on the top-most invalid container of the hierarchy.

Serialization

It is important to note that only AWT listeners which conform
to the

Serializable

protocol will be saved when
the object is stored. If an AWT object has listeners that
aren't marked serializable, they will be dropped at

writeObject

time. Developers will need, as always,
to consider the implications of making an object serializable.
One situation to watch out for is this:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements ActionListener, Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

MyApp()
{
// Oops, now aButton has a listener with a reference
// to bigOne!
aButton.addActionListener(this);
}

public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}
```

In this example, serializing

aButton

by itself
will cause

MyApp

and everything it refers to
to be serialized as well. The problem is that the listener
is serializable by coincidence, not by design. To separate
the decisions about

MyApp

and the

ActionListener

being serializable one can use a
nested class, as in the following example:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements java.io.Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

static class MyActionListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}

MyApp()
{
aButton.addActionListener(new MyActionListener());
}
}
```

Note

: For more information on the paint mechanisms utilized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

The

Component

class is the abstract superclass of
the nonmenu-related Abstract Window Toolkit components. Class

Component

can also be extended directly to create a
lightweight component. A lightweight component is a component that is
not associated with a native window. On the contrary, a heavyweight
component is associated with a native window. The

isLightweight()

method may be used to distinguish between the two kinds of the components.

Lightweight and heavyweight components may be mixed in a single component
hierarchy. However, for correct operating of such a mixed hierarchy of
components, the whole hierarchy must be valid. When the hierarchy gets
invalidated, like after changing the bounds of components, or
adding/removing components to/from containers, the whole hierarchy must be
validated afterwards by means of the

Container.validate()

method
invoked on the top-most invalid container of the hierarchy.

Serialization

It is important to note that only AWT listeners which conform
to the

Serializable

protocol will be saved when
the object is stored. If an AWT object has listeners that
aren't marked serializable, they will be dropped at

writeObject

time. Developers will need, as always,
to consider the implications of making an object serializable.
One situation to watch out for is this:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements ActionListener, Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

MyApp()
{
// Oops, now aButton has a listener with a reference
// to bigOne!
aButton.addActionListener(this);
}

public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}
```

In this example, serializing

aButton

by itself
will cause

MyApp

and everything it refers to
to be serialized as well. The problem is that the listener
is serializable by coincidence, not by design. To separate
the decisions about

MyApp

and the

ActionListener

being serializable one can use a
nested class, as in the following example:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements java.io.Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

static class MyActionListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}

MyApp()
{
aButton.addActionListener(new MyActionListener());
}
}
```

Note

: For more information on the paint mechanisms utilized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

Lightweight and heavyweight components may be mixed in a single component
hierarchy. However, for correct operating of such a mixed hierarchy of
components, the whole hierarchy must be valid. When the hierarchy gets
invalidated, like after changing the bounds of components, or
adding/removing components to/from containers, the whole hierarchy must be
validated afterwards by means of the

Container.validate()

method
invoked on the top-most invalid container of the hierarchy.

Serialization

It is important to note that only AWT listeners which conform
to the

Serializable

protocol will be saved when
the object is stored. If an AWT object has listeners that
aren't marked serializable, they will be dropped at

writeObject

time. Developers will need, as always,
to consider the implications of making an object serializable.
One situation to watch out for is this:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements ActionListener, Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

MyApp()
{
// Oops, now aButton has a listener with a reference
// to bigOne!
aButton.addActionListener(this);
}

public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}
```

In this example, serializing

aButton

by itself
will cause

MyApp

and everything it refers to
to be serialized as well. The problem is that the listener
is serializable by coincidence, not by design. To separate
the decisions about

MyApp

and the

ActionListener

being serializable one can use a
nested class, as in the following example:

```java
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements java.io.Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

static class MyActionListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}

MyApp()
{
aButton.addActionListener(new MyActionListener());
}
}
```

Note

: For more information on the paint mechanisms utilized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

---

#### Serialization

import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements ActionListener, Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

MyApp()
{
// Oops, now aButton has a listener with a reference
// to bigOne!
aButton.addActionListener(this);
}

public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}

import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;

class MyApp implements java.io.Serializable
{
BigObjectThatShouldNotBeSerializedWithAButton bigOne;
Button aButton = new Button();

static class MyActionListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
System.out.println("Hello There");
}
}

MyApp()
{
aButton.addActionListener(new MyActionListener());
}
}

Note

: For more information on the paint mechanisms utilized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Component.AccessibleAWTComponent

Inner class of Component used to provide default support for
accessibility.

static class

Component.BaselineResizeBehavior

Enumeration of the common ways the baseline of a component can
change as the size changes.

protected class

Component.BltBufferStrategy

Inner class for blitting offscreen surfaces to a component.

protected class

Component.FlipBufferStrategy

Inner class for flipping buffers on a component.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

AccessibleContext

accessibleContext

The

AccessibleContext

associated with this

Component

.

static float

BOTTOM_ALIGNMENT

Ease-of-use constant for

getAlignmentY

.

static float

CENTER_ALIGNMENT

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

.

static float

LEFT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.

static float

RIGHT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.

static float

TOP_ALIGNMENT

Ease-of-use constant for

getAlignmentY()

.

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

Modifier

Constructor

Description

protected

Component

()

Constructs a new component.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

action

​(

Event

evt,

Object

what)

Deprecated.

As of JDK version 1.1,
should register this component as ActionListener on component
which fires action events.

void

add

​(

PopupMenu

popup)

Adds the specified popup menu to the component.

void

addComponentListener

​(

ComponentListener

l)

Adds the specified component listener to receive component events from
this component.

void

addFocusListener

​(

FocusListener

l)

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.

void

addHierarchyBoundsListener

​(

HierarchyBoundsListener

l)

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.

void

addHierarchyListener

​(

HierarchyListener

l)

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.

void

addInputMethodListener

​(

InputMethodListener

l)

Adds the specified input method listener to receive
input method events from this component.

void

addKeyListener

​(

KeyListener

l)

Adds the specified key listener to receive key events from
this component.

void

addMouseListener

​(

MouseListener

l)

Adds the specified mouse listener to receive mouse events from
this component.

void

addMouseMotionListener

​(

MouseMotionListener

l)

Adds the specified mouse motion listener to receive mouse motion
events from this component.

void

addMouseWheelListener

​(

MouseWheelListener

l)

Adds the specified mouse wheel listener to receive mouse wheel events
from this component.

void

addNotify

()

Makes this

Component

displayable by connecting it to a
native screen resource.

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addPropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property.

void

applyComponentOrientation

​(

ComponentOrientation

orientation)

Sets the

ComponentOrientation

property of this component
and all components contained within it.

boolean

areFocusTraversalKeysSet

​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component.

Rectangle

bounds

()

Deprecated.

As of JDK version 1.1,
replaced by

getBounds()

.

int

checkImage

​(

Image

image,
int width,
int height,

ImageObserver

observer)

Returns the status of the construction of a screen representation
of the specified image.

int

checkImage

​(

Image

image,

ImageObserver

observer)

Returns the status of the construction of a screen representation
of the specified image.

protected

AWTEvent

coalesceEvents

​(

AWTEvent

existingEvent,

AWTEvent

newEvent)

Potentially coalesce an event being posted with an existing
event.

boolean

contains

​(int x,
int y)

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

boolean

contains

​(

Point

p)

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

Image

createImage

​(int width,
int height)

Creates an off-screen drawable image to be used for double buffering.

Image

createImage

​(

ImageProducer

producer)

Creates an image from the specified image producer.

VolatileImage

createVolatileImage

​(int width,
int height)

Creates a volatile off-screen drawable image to be used for double
buffering.

VolatileImage

createVolatileImage

​(int width,
int height,

ImageCapabilities

caps)

Creates a volatile off-screen drawable image, with the given
capabilities.

void

deliverEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

.

void

disable

()

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

protected void

disableEvents

​(long eventsToDisable)

Disables the events defined by the specified event mask parameter
from being delivered to this component.

void

dispatchEvent

​(

AWTEvent

e)

Dispatches an event to this component or one of its sub components.

void

doLayout

()

Prompts the layout manager to lay out this component.

void

enable

()

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

void

enable

​(boolean b)

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

protected void

enableEvents

​(long eventsToEnable)

Enables the events defined by the specified event mask parameter
to be delivered to this component.

void

enableInputMethods

​(boolean enable)

Enables or disables input method support for this component.

protected void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Support for reporting bound property changes for boolean properties.

void

firePropertyChange

​(

String

propertyName,
byte oldValue,
byte newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
char oldValue,
char newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
double oldValue,
double newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
float oldValue,
float newValue)

Reports a bound property change.

protected void

firePropertyChange

​(

String

propertyName,
int oldValue,
int newValue)

Support for reporting bound property changes for integer properties.

void

firePropertyChange

​(

String

propertyName,
long oldValue,
long newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
short oldValue,
short newValue)

Reports a bound property change.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes for Object properties.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated
with this

Component

.

float

getAlignmentX

()

Returns the alignment along the x axis.

float

getAlignmentY

()

Returns the alignment along the y axis.

Color

getBackground

()

Gets the background color of this component.

int

getBaseline

​(int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

()

Returns an enum indicating how the baseline of the component
changes as the size changes.

Rectangle

getBounds

()

Gets the bounds of this component in the form of a

Rectangle

object.

Rectangle

getBounds

​(

Rectangle

rv)

Stores the bounds of this component into "return value"

rv

and
return

rv

.

ColorModel

getColorModel

()

Gets the instance of

ColorModel

used to display
the component on the output device.

Component

getComponentAt

​(int x,
int y)

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component.

Component

getComponentAt

​(

Point

p)

Returns the component or subcomponent that contains the
specified point.

ComponentListener

[]

getComponentListeners

()

Returns an array of all the component listeners
registered on this component.

ComponentOrientation

getComponentOrientation

()

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

Cursor

getCursor

()

Gets the cursor set in the component.

DropTarget

getDropTarget

()

Gets the

DropTarget

associated with this

Component

.

Container

getFocusCycleRootAncestor

()

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle.

FocusListener

[]

getFocusListeners

()

Returns an array of all the focus listeners
registered on this component.

Set

<

AWTKeyStroke

>

getFocusTraversalKeys

​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Component.

boolean

getFocusTraversalKeysEnabled

()

Returns whether focus traversal keys are enabled for this Component.

Font

getFont

()

Gets the font of this component.

FontMetrics

getFontMetrics

​(

Font

font)

Gets the font metrics for the specified font.

Color

getForeground

()

Gets the foreground color of this component.

Graphics

getGraphics

()

Creates a graphics context for this component.

GraphicsConfiguration

getGraphicsConfiguration

()

Gets the

GraphicsConfiguration

associated with this

Component

.

int

getHeight

()

Returns the current height of this component.

HierarchyBoundsListener

[]

getHierarchyBoundsListeners

()

Returns an array of all the hierarchy bounds listeners
registered on this component.

HierarchyListener

[]

getHierarchyListeners

()

Returns an array of all the hierarchy listeners
registered on this component.

boolean

getIgnoreRepaint

()

InputContext

getInputContext

()

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component.

InputMethodListener

[]

getInputMethodListeners

()

Returns an array of all the input method listeners
registered on this component.

InputMethodRequests

getInputMethodRequests

()

Gets the input method request handler which supports
requests from input methods for this component.

KeyListener

[]

getKeyListeners

()

Returns an array of all the key listeners
registered on this component.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Locale

getLocale

()

Gets the locale of this component.

Point

getLocation

()

Gets the location of this component in the form of a
point specifying the component's top-left corner.

Point

getLocation

​(

Point

rv)

Stores the x,y origin of this component into "return value"

rv

and return

rv

.

Point

getLocationOnScreen

()

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

Dimension

getMaximumSize

()

Gets the maximum size of this component.

Dimension

getMinimumSize

()

Gets the minimum size of this component.

MouseListener

[]

getMouseListeners

()

Returns an array of all the mouse listeners
registered on this component.

MouseMotionListener

[]

getMouseMotionListeners

()

Returns an array of all the mouse motion listeners
registered on this component.

Point

getMousePosition

()

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.

MouseWheelListener

[]

getMouseWheelListeners

()

Returns an array of all the mouse wheel listeners
registered on this component.

String

getName

()

Gets the name of the component.

Container

getParent

()

Gets the parent of this component.

Dimension

getPreferredSize

()

Gets the preferred size of this component.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the property change listeners
registered on this component.

PropertyChangeListener

[]

getPropertyChangeListeners

​(

String

propertyName)

Returns an array of all the listeners which have been associated
with the named property.

Dimension

getSize

()

Returns the size of this component in the form of a

Dimension

object.

Dimension

getSize

​(

Dimension

rv)

Stores the width/height of this component into "return value"

rv

and return

rv

.

Toolkit

getToolkit

()

Gets the toolkit of this component.

Object

getTreeLock

()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

int

getWidth

()

Returns the current width of this component.

int

getX

()

Returns the current x coordinate of the components origin.

int

getY

()

Returns the current y coordinate of the components origin.

boolean

gotFocus

​(

Event

evt,

Object

what)

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

boolean

handleEvent

​(

Event

evt)

Deprecated.

As of JDK version 1.1
replaced by processEvent(AWTEvent).

boolean

hasFocus

()

Returns

true

if this

Component

is the
focus owner.

void

hide

()

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.

boolean

inside

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by contains(int, int).

void

invalidate

()

Invalidates this component and its ancestors.

boolean

isBackgroundSet

()

Returns whether the background color has been explicitly set for this
Component.

boolean

isCursorSet

()

Returns whether the cursor has been explicitly set for this Component.

boolean

isDisplayable

()

Determines whether this component is displayable.

boolean

isDoubleBuffered

()

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later.

boolean

isEnabled

()

Determines whether this component is enabled.

boolean

isFocusable

()

Returns whether this Component can be focused.

boolean

isFocusCycleRoot

​(

Container

container)

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle.

boolean

isFocusOwner

()

Returns

true

if this

Component

is the
focus owner.

boolean

isFocusTraversable

()

Deprecated.

As of 1.4, replaced by

isFocusable()

.

boolean

isFontSet

()

Returns whether the font has been explicitly set for this Component.

boolean

isForegroundSet

()

Returns whether the foreground color has been explicitly set for this
Component.

boolean

isLightweight

()

A lightweight component doesn't have a native toolkit peer.

boolean

isMaximumSizeSet

()

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

boolean

isMinimumSizeSet

()

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

boolean

isOpaque

()

Returns true if this component is completely opaque, returns
false by default.

boolean

isPreferredSizeSet

()

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

boolean

isShowing

()

Determines whether this component is showing on screen.

boolean

isValid

()

Determines whether this component is valid.

boolean

isVisible

()

Determines whether this component should be visible when its
parent is visible.

boolean

keyDown

​(

Event

evt,
int key)

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

boolean

keyUp

​(

Event

evt,
int key)

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

void

layout

()

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

void

list

()

Prints a listing of this component to the standard system output
stream

System.out

.

void

list

​(

PrintStream

out)

Prints a listing of this component to the specified output
stream.

void

list

​(

PrintStream

out,
int indent)

Prints out a list, starting at the specified indentation, to the
specified print stream.

void

list

​(

PrintWriter

out)

Prints a listing to the specified print writer.

void

list

​(

PrintWriter

out,
int indent)

Prints out a list, starting at the specified indentation, to
the specified print writer.

Component

locate

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by getComponentAt(int, int).

Point

location

()

Deprecated.

As of JDK version 1.1,
replaced by

getLocation()

.

boolean

lostFocus

​(

Event

evt,

Object

what)

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

boolean

mouseDown

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

boolean

mouseDrag

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

boolean

mouseEnter

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

boolean

mouseExit

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

boolean

mouseMove

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

boolean

mouseUp

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

void

move

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by

setLocation(int, int)

.

void

nextFocus

()

Deprecated.

As of JDK version 1.1,
replaced by transferFocus().

void

paint

​(

Graphics

g)

Paints this component.

void

paintAll

​(

Graphics

g)

Paints this component and all of its subcomponents.

protected

String

paramString

()

Returns a string representing the state of this component.

boolean

postEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1,
replaced by dispatchEvent(AWTEvent).

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

boolean

prepareImage

​(

Image

image,
int width,
int height,

ImageObserver

observer)

Prepares an image for rendering on this component at the
specified width and height.

boolean

prepareImage

​(

Image

image,

ImageObserver

observer)

Prepares an image for rendering on this component.

void

print

​(

Graphics

g)

Prints this component.

void

printAll

​(

Graphics

g)

Prints this component and all of its subcomponents.

protected void

processComponentEvent

​(

ComponentEvent

e)

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events occurring on this component.

protected void

processFocusEvent

​(

FocusEvent

e)

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

protected void

processHierarchyBoundsEvent

​(

HierarchyEvent

e)

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

protected void

processHierarchyEvent

​(

HierarchyEvent

e)

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

protected void

processInputMethodEvent

​(

InputMethodEvent

e)

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

protected void

processKeyEvent

​(

KeyEvent

e)

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

protected void

processMouseEvent

​(

MouseEvent

e)

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

protected void

processMouseMotionEvent

​(

MouseEvent

e)

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

protected void

processMouseWheelEvent

​(

MouseWheelEvent

e)

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

void

remove

​(

MenuComponent

popup)

Removes the specified popup menu from the component.

void

removeComponentListener

​(

ComponentListener

l)

Removes the specified component listener so that it no longer
receives component events from this component.

void

removeFocusListener

​(

FocusListener

l)

Removes the specified focus listener so that it no longer
receives focus events from this component.

void

removeHierarchyBoundsListener

​(

HierarchyBoundsListener

l)

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component.

void

removeHierarchyListener

​(

HierarchyListener

l)

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component.

void

removeInputMethodListener

​(

InputMethodListener

l)

Removes the specified input method listener so that it no longer
receives input method events from this component.

void

removeKeyListener

​(

KeyListener

l)

Removes the specified key listener so that it no longer
receives key events from this component.

void

removeMouseListener

​(

MouseListener

l)

Removes the specified mouse listener so that it no longer
receives mouse events from this component.

void

removeMouseMotionListener

​(

MouseMotionListener

l)

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component.

void

removeMouseWheelListener

​(

MouseWheelListener

l)

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component.

void

removeNotify

()

Makes this

Component

undisplayable by destroying it native
screen resource.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.

void

removePropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener
list for a specific property.

void

repaint

()

Repaints this component.

void

repaint

​(int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component.

void

repaint

​(long tm)

Repaints the component.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

tm

milliseconds.

void

requestFocus

()

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window.

protected boolean

requestFocus

​(boolean temporary)

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

.

protected boolean

requestFocus

​(boolean temporary,

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

.

void

requestFocus

​(

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window.

boolean

requestFocusInWindow

()

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window.

protected boolean

requestFocusInWindow

​(boolean temporary)

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

.

boolean

requestFocusInWindow

​(

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window.

void

reshape

​(int x,
int y,
int width,
int height)

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

void

resize

​(int width,
int height)

Deprecated.

As of JDK version 1.1,
replaced by

setSize(int, int)

.

void

resize

​(

Dimension

d)

Deprecated.

As of JDK version 1.1,
replaced by

setSize(Dimension)

.

void

revalidate

()

Revalidates the component hierarchy up to the nearest validate root.

void

setBackground

​(

Color

c)

Sets the background color of this component.

void

setBounds

​(int x,
int y,
int width,
int height)

Moves and resizes this component.

void

setBounds

​(

Rectangle

r)

Moves and resizes this component to conform to the new
bounding rectangle

r

.

void

setComponentOrientation

​(

ComponentOrientation

o)

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component.

void

setCursor

​(

Cursor

cursor)

Sets the cursor image to the specified cursor.

void

setDropTarget

​(

DropTarget

dt)

Associate a

DropTarget

with this component.

void

setEnabled

​(boolean b)

Enables or disables this component, depending on the value of the
parameter

b

.

void

setFocusable

​(boolean focusable)

Sets the focusable state of this Component to the specified value.

void

setFocusTraversalKeys

​(int id,

Set

<? extends

AWTKeyStroke

> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Component.

void

setFocusTraversalKeysEnabled

​(boolean focusTraversalKeysEnabled)

Sets whether focus traversal keys are enabled for this Component.

void

setFont

​(

Font

f)

Sets the font of this component.

void

setForeground

​(

Color

c)

Sets the foreground color of this component.

void

setIgnoreRepaint

​(boolean ignoreRepaint)

Sets whether or not paint messages received from the operating system
should be ignored.

void

setLocale

​(

Locale

l)

Sets the locale of this component.

void

setLocation

​(int x,
int y)

Moves this component to a new location.

void

setLocation

​(

Point

p)

Moves this component to a new location.

void

setMaximumSize

​(

Dimension

maximumSize)

Sets the maximum size of this component to a constant
value.

void

setMinimumSize

​(

Dimension

minimumSize)

Sets the minimum size of this component to a constant
value.

void

setMixingCutoutShape

​(

Shape

shape)

Sets a 'mixing-cutout' shape for this lightweight component.

void

setName

​(

String

name)

Sets the name of the component to the specified string.

void

setPreferredSize

​(

Dimension

preferredSize)

Sets the preferred size of this component to a constant
value.

void

setSize

​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

void

setSize

​(

Dimension

d)

Resizes this component so that it has width

d.width

and height

d.height

.

void

setVisible

​(boolean b)

Shows or hides this component depending on the value of parameter

b

.

void

show

()

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

void

show

​(boolean b)

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

Dimension

size

()

Deprecated.

As of JDK version 1.1,
replaced by

getSize()

.

String

toString

()

Returns a string representation of this component and its values.

void

transferFocus

()

Transfers the focus to the next component, as though this Component were
the focus owner.

void

transferFocusBackward

()

Transfers the focus to the previous component, as though this Component
were the focus owner.

void

transferFocusUpCycle

()

Transfers the focus up one focus traversal cycle.

void

update

​(

Graphics

g)

Updates this component.

void

validate

()

Validates this component.

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

Component.AccessibleAWTComponent

Inner class of Component used to provide default support for
accessibility.

static class

Component.BaselineResizeBehavior

Enumeration of the common ways the baseline of a component can
change as the size changes.

protected class

Component.BltBufferStrategy

Inner class for blitting offscreen surfaces to a component.

protected class

Component.FlipBufferStrategy

Inner class for flipping buffers on a component.

---

#### Nested Class Summary

Inner class of Component used to provide default support for
accessibility.

Enumeration of the common ways the baseline of a component can
change as the size changes.

Inner class for blitting offscreen surfaces to a component.

Inner class for flipping buffers on a component.

Field Summary

Fields

Modifier and Type

Field

Description

protected

AccessibleContext

accessibleContext

The

AccessibleContext

associated with this

Component

.

static float

BOTTOM_ALIGNMENT

Ease-of-use constant for

getAlignmentY

.

static float

CENTER_ALIGNMENT

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

.

static float

LEFT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.

static float

RIGHT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.

static float

TOP_ALIGNMENT

Ease-of-use constant for

getAlignmentY()

.

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

The

AccessibleContext

associated with this

Component

.

Ease-of-use constant for

getAlignmentY

.

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

.

Ease-of-use constant for

getAlignmentX

.

Ease-of-use constant for

getAlignmentY()

.

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

Modifier

Constructor

Description

protected

Component

()

Constructs a new component.

---

#### Constructor Summary

Constructs a new component.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

action

​(

Event

evt,

Object

what)

Deprecated.

As of JDK version 1.1,
should register this component as ActionListener on component
which fires action events.

void

add

​(

PopupMenu

popup)

Adds the specified popup menu to the component.

void

addComponentListener

​(

ComponentListener

l)

Adds the specified component listener to receive component events from
this component.

void

addFocusListener

​(

FocusListener

l)

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.

void

addHierarchyBoundsListener

​(

HierarchyBoundsListener

l)

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.

void

addHierarchyListener

​(

HierarchyListener

l)

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.

void

addInputMethodListener

​(

InputMethodListener

l)

Adds the specified input method listener to receive
input method events from this component.

void

addKeyListener

​(

KeyListener

l)

Adds the specified key listener to receive key events from
this component.

void

addMouseListener

​(

MouseListener

l)

Adds the specified mouse listener to receive mouse events from
this component.

void

addMouseMotionListener

​(

MouseMotionListener

l)

Adds the specified mouse motion listener to receive mouse motion
events from this component.

void

addMouseWheelListener

​(

MouseWheelListener

l)

Adds the specified mouse wheel listener to receive mouse wheel events
from this component.

void

addNotify

()

Makes this

Component

displayable by connecting it to a
native screen resource.

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addPropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property.

void

applyComponentOrientation

​(

ComponentOrientation

orientation)

Sets the

ComponentOrientation

property of this component
and all components contained within it.

boolean

areFocusTraversalKeysSet

​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component.

Rectangle

bounds

()

Deprecated.

As of JDK version 1.1,
replaced by

getBounds()

.

int

checkImage

​(

Image

image,
int width,
int height,

ImageObserver

observer)

Returns the status of the construction of a screen representation
of the specified image.

int

checkImage

​(

Image

image,

ImageObserver

observer)

Returns the status of the construction of a screen representation
of the specified image.

protected

AWTEvent

coalesceEvents

​(

AWTEvent

existingEvent,

AWTEvent

newEvent)

Potentially coalesce an event being posted with an existing
event.

boolean

contains

​(int x,
int y)

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

boolean

contains

​(

Point

p)

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

Image

createImage

​(int width,
int height)

Creates an off-screen drawable image to be used for double buffering.

Image

createImage

​(

ImageProducer

producer)

Creates an image from the specified image producer.

VolatileImage

createVolatileImage

​(int width,
int height)

Creates a volatile off-screen drawable image to be used for double
buffering.

VolatileImage

createVolatileImage

​(int width,
int height,

ImageCapabilities

caps)

Creates a volatile off-screen drawable image, with the given
capabilities.

void

deliverEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

.

void

disable

()

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

protected void

disableEvents

​(long eventsToDisable)

Disables the events defined by the specified event mask parameter
from being delivered to this component.

void

dispatchEvent

​(

AWTEvent

e)

Dispatches an event to this component or one of its sub components.

void

doLayout

()

Prompts the layout manager to lay out this component.

void

enable

()

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

void

enable

​(boolean b)

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

protected void

enableEvents

​(long eventsToEnable)

Enables the events defined by the specified event mask parameter
to be delivered to this component.

void

enableInputMethods

​(boolean enable)

Enables or disables input method support for this component.

protected void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Support for reporting bound property changes for boolean properties.

void

firePropertyChange

​(

String

propertyName,
byte oldValue,
byte newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
char oldValue,
char newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
double oldValue,
double newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
float oldValue,
float newValue)

Reports a bound property change.

protected void

firePropertyChange

​(

String

propertyName,
int oldValue,
int newValue)

Support for reporting bound property changes for integer properties.

void

firePropertyChange

​(

String

propertyName,
long oldValue,
long newValue)

Reports a bound property change.

void

firePropertyChange

​(

String

propertyName,
short oldValue,
short newValue)

Reports a bound property change.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes for Object properties.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated
with this

Component

.

float

getAlignmentX

()

Returns the alignment along the x axis.

float

getAlignmentY

()

Returns the alignment along the y axis.

Color

getBackground

()

Gets the background color of this component.

int

getBaseline

​(int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

()

Returns an enum indicating how the baseline of the component
changes as the size changes.

Rectangle

getBounds

()

Gets the bounds of this component in the form of a

Rectangle

object.

Rectangle

getBounds

​(

Rectangle

rv)

Stores the bounds of this component into "return value"

rv

and
return

rv

.

ColorModel

getColorModel

()

Gets the instance of

ColorModel

used to display
the component on the output device.

Component

getComponentAt

​(int x,
int y)

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component.

Component

getComponentAt

​(

Point

p)

Returns the component or subcomponent that contains the
specified point.

ComponentListener

[]

getComponentListeners

()

Returns an array of all the component listeners
registered on this component.

ComponentOrientation

getComponentOrientation

()

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

Cursor

getCursor

()

Gets the cursor set in the component.

DropTarget

getDropTarget

()

Gets the

DropTarget

associated with this

Component

.

Container

getFocusCycleRootAncestor

()

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle.

FocusListener

[]

getFocusListeners

()

Returns an array of all the focus listeners
registered on this component.

Set

<

AWTKeyStroke

>

getFocusTraversalKeys

​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Component.

boolean

getFocusTraversalKeysEnabled

()

Returns whether focus traversal keys are enabled for this Component.

Font

getFont

()

Gets the font of this component.

FontMetrics

getFontMetrics

​(

Font

font)

Gets the font metrics for the specified font.

Color

getForeground

()

Gets the foreground color of this component.

Graphics

getGraphics

()

Creates a graphics context for this component.

GraphicsConfiguration

getGraphicsConfiguration

()

Gets the

GraphicsConfiguration

associated with this

Component

.

int

getHeight

()

Returns the current height of this component.

HierarchyBoundsListener

[]

getHierarchyBoundsListeners

()

Returns an array of all the hierarchy bounds listeners
registered on this component.

HierarchyListener

[]

getHierarchyListeners

()

Returns an array of all the hierarchy listeners
registered on this component.

boolean

getIgnoreRepaint

()

InputContext

getInputContext

()

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component.

InputMethodListener

[]

getInputMethodListeners

()

Returns an array of all the input method listeners
registered on this component.

InputMethodRequests

getInputMethodRequests

()

Gets the input method request handler which supports
requests from input methods for this component.

KeyListener

[]

getKeyListeners

()

Returns an array of all the key listeners
registered on this component.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Locale

getLocale

()

Gets the locale of this component.

Point

getLocation

()

Gets the location of this component in the form of a
point specifying the component's top-left corner.

Point

getLocation

​(

Point

rv)

Stores the x,y origin of this component into "return value"

rv

and return

rv

.

Point

getLocationOnScreen

()

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

Dimension

getMaximumSize

()

Gets the maximum size of this component.

Dimension

getMinimumSize

()

Gets the minimum size of this component.

MouseListener

[]

getMouseListeners

()

Returns an array of all the mouse listeners
registered on this component.

MouseMotionListener

[]

getMouseMotionListeners

()

Returns an array of all the mouse motion listeners
registered on this component.

Point

getMousePosition

()

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.

MouseWheelListener

[]

getMouseWheelListeners

()

Returns an array of all the mouse wheel listeners
registered on this component.

String

getName

()

Gets the name of the component.

Container

getParent

()

Gets the parent of this component.

Dimension

getPreferredSize

()

Gets the preferred size of this component.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the property change listeners
registered on this component.

PropertyChangeListener

[]

getPropertyChangeListeners

​(

String

propertyName)

Returns an array of all the listeners which have been associated
with the named property.

Dimension

getSize

()

Returns the size of this component in the form of a

Dimension

object.

Dimension

getSize

​(

Dimension

rv)

Stores the width/height of this component into "return value"

rv

and return

rv

.

Toolkit

getToolkit

()

Gets the toolkit of this component.

Object

getTreeLock

()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

int

getWidth

()

Returns the current width of this component.

int

getX

()

Returns the current x coordinate of the components origin.

int

getY

()

Returns the current y coordinate of the components origin.

boolean

gotFocus

​(

Event

evt,

Object

what)

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

boolean

handleEvent

​(

Event

evt)

Deprecated.

As of JDK version 1.1
replaced by processEvent(AWTEvent).

boolean

hasFocus

()

Returns

true

if this

Component

is the
focus owner.

void

hide

()

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.

boolean

inside

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by contains(int, int).

void

invalidate

()

Invalidates this component and its ancestors.

boolean

isBackgroundSet

()

Returns whether the background color has been explicitly set for this
Component.

boolean

isCursorSet

()

Returns whether the cursor has been explicitly set for this Component.

boolean

isDisplayable

()

Determines whether this component is displayable.

boolean

isDoubleBuffered

()

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later.

boolean

isEnabled

()

Determines whether this component is enabled.

boolean

isFocusable

()

Returns whether this Component can be focused.

boolean

isFocusCycleRoot

​(

Container

container)

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle.

boolean

isFocusOwner

()

Returns

true

if this

Component

is the
focus owner.

boolean

isFocusTraversable

()

Deprecated.

As of 1.4, replaced by

isFocusable()

.

boolean

isFontSet

()

Returns whether the font has been explicitly set for this Component.

boolean

isForegroundSet

()

Returns whether the foreground color has been explicitly set for this
Component.

boolean

isLightweight

()

A lightweight component doesn't have a native toolkit peer.

boolean

isMaximumSizeSet

()

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

boolean

isMinimumSizeSet

()

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

boolean

isOpaque

()

Returns true if this component is completely opaque, returns
false by default.

boolean

isPreferredSizeSet

()

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

boolean

isShowing

()

Determines whether this component is showing on screen.

boolean

isValid

()

Determines whether this component is valid.

boolean

isVisible

()

Determines whether this component should be visible when its
parent is visible.

boolean

keyDown

​(

Event

evt,
int key)

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

boolean

keyUp

​(

Event

evt,
int key)

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

void

layout

()

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

void

list

()

Prints a listing of this component to the standard system output
stream

System.out

.

void

list

​(

PrintStream

out)

Prints a listing of this component to the specified output
stream.

void

list

​(

PrintStream

out,
int indent)

Prints out a list, starting at the specified indentation, to the
specified print stream.

void

list

​(

PrintWriter

out)

Prints a listing to the specified print writer.

void

list

​(

PrintWriter

out,
int indent)

Prints out a list, starting at the specified indentation, to
the specified print writer.

Component

locate

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by getComponentAt(int, int).

Point

location

()

Deprecated.

As of JDK version 1.1,
replaced by

getLocation()

.

boolean

lostFocus

​(

Event

evt,

Object

what)

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

boolean

mouseDown

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

boolean

mouseDrag

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

boolean

mouseEnter

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

boolean

mouseExit

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

boolean

mouseMove

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

boolean

mouseUp

​(

Event

evt,
int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

void

move

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by

setLocation(int, int)

.

void

nextFocus

()

Deprecated.

As of JDK version 1.1,
replaced by transferFocus().

void

paint

​(

Graphics

g)

Paints this component.

void

paintAll

​(

Graphics

g)

Paints this component and all of its subcomponents.

protected

String

paramString

()

Returns a string representing the state of this component.

boolean

postEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1,
replaced by dispatchEvent(AWTEvent).

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

boolean

prepareImage

​(

Image

image,
int width,
int height,

ImageObserver

observer)

Prepares an image for rendering on this component at the
specified width and height.

boolean

prepareImage

​(

Image

image,

ImageObserver

observer)

Prepares an image for rendering on this component.

void

print

​(

Graphics

g)

Prints this component.

void

printAll

​(

Graphics

g)

Prints this component and all of its subcomponents.

protected void

processComponentEvent

​(

ComponentEvent

e)

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events occurring on this component.

protected void

processFocusEvent

​(

FocusEvent

e)

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

protected void

processHierarchyBoundsEvent

​(

HierarchyEvent

e)

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

protected void

processHierarchyEvent

​(

HierarchyEvent

e)

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

protected void

processInputMethodEvent

​(

InputMethodEvent

e)

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

protected void

processKeyEvent

​(

KeyEvent

e)

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

protected void

processMouseEvent

​(

MouseEvent

e)

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

protected void

processMouseMotionEvent

​(

MouseEvent

e)

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

protected void

processMouseWheelEvent

​(

MouseWheelEvent

e)

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

void

remove

​(

MenuComponent

popup)

Removes the specified popup menu from the component.

void

removeComponentListener

​(

ComponentListener

l)

Removes the specified component listener so that it no longer
receives component events from this component.

void

removeFocusListener

​(

FocusListener

l)

Removes the specified focus listener so that it no longer
receives focus events from this component.

void

removeHierarchyBoundsListener

​(

HierarchyBoundsListener

l)

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component.

void

removeHierarchyListener

​(

HierarchyListener

l)

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component.

void

removeInputMethodListener

​(

InputMethodListener

l)

Removes the specified input method listener so that it no longer
receives input method events from this component.

void

removeKeyListener

​(

KeyListener

l)

Removes the specified key listener so that it no longer
receives key events from this component.

void

removeMouseListener

​(

MouseListener

l)

Removes the specified mouse listener so that it no longer
receives mouse events from this component.

void

removeMouseMotionListener

​(

MouseMotionListener

l)

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component.

void

removeMouseWheelListener

​(

MouseWheelListener

l)

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component.

void

removeNotify

()

Makes this

Component

undisplayable by destroying it native
screen resource.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.

void

removePropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener
list for a specific property.

void

repaint

()

Repaints this component.

void

repaint

​(int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component.

void

repaint

​(long tm)

Repaints the component.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

tm

milliseconds.

void

requestFocus

()

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window.

protected boolean

requestFocus

​(boolean temporary)

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

.

protected boolean

requestFocus

​(boolean temporary,

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

.

void

requestFocus

​(

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window.

boolean

requestFocusInWindow

()

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window.

protected boolean

requestFocusInWindow

​(boolean temporary)

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

.

boolean

requestFocusInWindow

​(

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window.

void

reshape

​(int x,
int y,
int width,
int height)

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

void

resize

​(int width,
int height)

Deprecated.

As of JDK version 1.1,
replaced by

setSize(int, int)

.

void

resize

​(

Dimension

d)

Deprecated.

As of JDK version 1.1,
replaced by

setSize(Dimension)

.

void

revalidate

()

Revalidates the component hierarchy up to the nearest validate root.

void

setBackground

​(

Color

c)

Sets the background color of this component.

void

setBounds

​(int x,
int y,
int width,
int height)

Moves and resizes this component.

void

setBounds

​(

Rectangle

r)

Moves and resizes this component to conform to the new
bounding rectangle

r

.

void

setComponentOrientation

​(

ComponentOrientation

o)

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component.

void

setCursor

​(

Cursor

cursor)

Sets the cursor image to the specified cursor.

void

setDropTarget

​(

DropTarget

dt)

Associate a

DropTarget

with this component.

void

setEnabled

​(boolean b)

Enables or disables this component, depending on the value of the
parameter

b

.

void

setFocusable

​(boolean focusable)

Sets the focusable state of this Component to the specified value.

void

setFocusTraversalKeys

​(int id,

Set

<? extends

AWTKeyStroke

> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Component.

void

setFocusTraversalKeysEnabled

​(boolean focusTraversalKeysEnabled)

Sets whether focus traversal keys are enabled for this Component.

void

setFont

​(

Font

f)

Sets the font of this component.

void

setForeground

​(

Color

c)

Sets the foreground color of this component.

void

setIgnoreRepaint

​(boolean ignoreRepaint)

Sets whether or not paint messages received from the operating system
should be ignored.

void

setLocale

​(

Locale

l)

Sets the locale of this component.

void

setLocation

​(int x,
int y)

Moves this component to a new location.

void

setLocation

​(

Point

p)

Moves this component to a new location.

void

setMaximumSize

​(

Dimension

maximumSize)

Sets the maximum size of this component to a constant
value.

void

setMinimumSize

​(

Dimension

minimumSize)

Sets the minimum size of this component to a constant
value.

void

setMixingCutoutShape

​(

Shape

shape)

Sets a 'mixing-cutout' shape for this lightweight component.

void

setName

​(

String

name)

Sets the name of the component to the specified string.

void

setPreferredSize

​(

Dimension

preferredSize)

Sets the preferred size of this component to a constant
value.

void

setSize

​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

void

setSize

​(

Dimension

d)

Resizes this component so that it has width

d.width

and height

d.height

.

void

setVisible

​(boolean b)

Shows or hides this component depending on the value of parameter

b

.

void

show

()

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

void

show

​(boolean b)

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

Dimension

size

()

Deprecated.

As of JDK version 1.1,
replaced by

getSize()

.

String

toString

()

Returns a string representation of this component and its values.

void

transferFocus

()

Transfers the focus to the next component, as though this Component were
the focus owner.

void

transferFocusBackward

()

Transfers the focus to the previous component, as though this Component
were the focus owner.

void

transferFocusUpCycle

()

Transfers the focus up one focus traversal cycle.

void

update

​(

Graphics

g)

Updates this component.

void

validate

()

Validates this component.

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

As of JDK version 1.1,
should register this component as ActionListener on component
which fires action events.

Adds the specified popup menu to the component.

Adds the specified component listener to receive component events from
this component.

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.

Adds the specified input method listener to receive
input method events from this component.

Adds the specified key listener to receive key events from
this component.

Adds the specified mouse listener to receive mouse events from
this component.

Adds the specified mouse motion listener to receive mouse motion
events from this component.

Adds the specified mouse wheel listener to receive mouse wheel events
from this component.

Makes this

Component

displayable by connecting it to a
native screen resource.

Adds a PropertyChangeListener to the listener list.

Adds a PropertyChangeListener to the listener list for a specific
property.

Sets the

ComponentOrientation

property of this component
and all components contained within it.

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component.

Deprecated.

As of JDK version 1.1,
replaced by

getBounds()

.

Returns the status of the construction of a screen representation
of the specified image.

Potentially coalesce an event being posted with an existing
event.

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

Creates an off-screen drawable image to be used for double buffering.

Creates an image from the specified image producer.

Creates a volatile off-screen drawable image to be used for double
buffering.

Creates a volatile off-screen drawable image, with the given
capabilities.

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

.

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

Disables the events defined by the specified event mask parameter
from being delivered to this component.

Dispatches an event to this component or one of its sub components.

Prompts the layout manager to lay out this component.

Enables the events defined by the specified event mask parameter
to be delivered to this component.

Enables or disables input method support for this component.

Support for reporting bound property changes for boolean properties.

Reports a bound property change.

Support for reporting bound property changes for integer properties.

Support for reporting bound property changes for Object properties.

Gets the

AccessibleContext

associated
with this

Component

.

Returns the alignment along the x axis.

Returns the alignment along the y axis.

Gets the background color of this component.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Gets the bounds of this component in the form of a

Rectangle

object.

Stores the bounds of this component into "return value"

rv

and
return

rv

.

Gets the instance of

ColorModel

used to display
the component on the output device.

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component.

Returns the component or subcomponent that contains the
specified point.

Returns an array of all the component listeners
registered on this component.

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

Gets the cursor set in the component.

Gets the

DropTarget

associated with this

Component

.

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle.

Returns an array of all the focus listeners
registered on this component.

Returns the Set of focus traversal keys for a given traversal operation
for this Component.

Returns whether focus traversal keys are enabled for this Component.

Gets the font of this component.

Gets the font metrics for the specified font.

Gets the foreground color of this component.

Creates a graphics context for this component.

Gets the

GraphicsConfiguration

associated with this

Component

.

Returns the current height of this component.

Returns an array of all the hierarchy bounds listeners
registered on this component.

Returns an array of all the hierarchy listeners
registered on this component.

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component.

Returns an array of all the input method listeners
registered on this component.

Gets the input method request handler which supports
requests from input methods for this component.

Returns an array of all the key listeners
registered on this component.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Gets the locale of this component.

Gets the location of this component in the form of a
point specifying the component's top-left corner.

Stores the x,y origin of this component into "return value"

rv

and return

rv

.

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

Gets the maximum size of this component.

Gets the minimum size of this component.

Returns an array of all the mouse listeners
registered on this component.

Returns an array of all the mouse motion listeners
registered on this component.

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.

Returns an array of all the mouse wheel listeners
registered on this component.

Gets the name of the component.

Gets the parent of this component.

Gets the preferred size of this component.

Returns an array of all the property change listeners
registered on this component.

Returns an array of all the listeners which have been associated
with the named property.

Returns the size of this component in the form of a

Dimension

object.

Stores the width/height of this component into "return value"

rv

and return

rv

.

Gets the toolkit of this component.

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

Returns the current width of this component.

Returns the current x coordinate of the components origin.

Returns the current y coordinate of the components origin.

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

Deprecated.

As of JDK version 1.1
replaced by processEvent(AWTEvent).

Returns

true

if this

Component

is the
focus owner.

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

Repaints the component when the image has changed.

Deprecated.

As of JDK version 1.1,
replaced by contains(int, int).

Invalidates this component and its ancestors.

Returns whether the background color has been explicitly set for this
Component.

Returns whether the cursor has been explicitly set for this Component.

Determines whether this component is displayable.

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later.

Determines whether this component is enabled.

Returns whether this Component can be focused.

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle.

Deprecated.

As of 1.4, replaced by

isFocusable()

.

Returns whether the font has been explicitly set for this Component.

Returns whether the foreground color has been explicitly set for this
Component.

A lightweight component doesn't have a native toolkit peer.

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

Returns true if this component is completely opaque, returns
false by default.

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

Determines whether this component is showing on screen.

Determines whether this component is valid.

Determines whether this component should be visible when its
parent is visible.

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

Prints a listing of this component to the standard system output
stream

System.out

.

Prints a listing of this component to the specified output
stream.

Prints out a list, starting at the specified indentation, to the
specified print stream.

Prints a listing to the specified print writer.

Prints out a list, starting at the specified indentation, to
the specified print writer.

Deprecated.

As of JDK version 1.1,
replaced by getComponentAt(int, int).

Deprecated.

As of JDK version 1.1,
replaced by

getLocation()

.

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

Deprecated.

As of JDK version 1.1,
replaced by

setLocation(int, int)

.

Deprecated.

As of JDK version 1.1,
replaced by transferFocus().

Paints this component.

Paints this component and all of its subcomponents.

Returns a string representing the state of this component.

Deprecated.

As of JDK version 1.1,
replaced by dispatchEvent(AWTEvent).

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Prepares an image for rendering on this component at the
specified width and height.

Prepares an image for rendering on this component.

Prints this component.

Prints this component and all of its subcomponents.

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

Processes events occurring on this component.

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

Removes the specified popup menu from the component.

Removes the specified component listener so that it no longer
receives component events from this component.

Removes the specified focus listener so that it no longer
receives focus events from this component.

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component.

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component.

Removes the specified input method listener so that it no longer
receives input method events from this component.

Removes the specified key listener so that it no longer
receives key events from this component.

Removes the specified mouse listener so that it no longer
receives mouse events from this component.

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component.

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component.

Makes this

Component

undisplayable by destroying it native
screen resource.

Removes a PropertyChangeListener from the listener list.

Removes a

PropertyChangeListener

from the listener
list for a specific property.

Repaints this component.

Repaints the specified rectangle of this component.

Repaints the component.

Repaints the specified rectangle of this component within

tm

milliseconds.

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window.

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

.

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

.

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window.

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window.

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

.

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window.

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Deprecated.

As of JDK version 1.1,
replaced by

setSize(int, int)

.

Deprecated.

As of JDK version 1.1,
replaced by

setSize(Dimension)

.

Revalidates the component hierarchy up to the nearest validate root.

Sets the background color of this component.

Moves and resizes this component.

Moves and resizes this component to conform to the new
bounding rectangle

r

.

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component.

Sets the cursor image to the specified cursor.

Associate a

DropTarget

with this component.

Enables or disables this component, depending on the value of the
parameter

b

.

Sets the focusable state of this Component to the specified value.

Sets the focus traversal keys for a given traversal operation for this
Component.

Sets whether focus traversal keys are enabled for this Component.

Sets the font of this component.

Sets the foreground color of this component.

Sets whether or not paint messages received from the operating system
should be ignored.

Sets the locale of this component.

Moves this component to a new location.

Sets the maximum size of this component to a constant
value.

Sets the minimum size of this component to a constant
value.

Sets a 'mixing-cutout' shape for this lightweight component.

Sets the name of the component to the specified string.

Sets the preferred size of this component to a constant
value.

Resizes this component so that it has width

width

and height

height

.

Resizes this component so that it has width

d.width

and height

d.height

.

Shows or hides this component depending on the value of parameter

b

.

Deprecated.

As of JDK version 1.1,
replaced by

getSize()

.

Returns a string representation of this component and its values.

Transfers the focus to the next component, as though this Component were
the focus owner.

Transfers the focus to the previous component, as though this Component
were the focus owner.

Transfers the focus up one focus traversal cycle.

Updates this component.

Validates this component.

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

============ FIELD DETAIL ===========

- Field Detail

- TOP_ALIGNMENT

```java
public static final float TOP_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY()

.
Specifies an alignment to the top of the component.

**See Also:** getAlignmentY()

,

Constant Field Values

- CENTER_ALIGNMENT

```java
public static final float CENTER_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

. Specifies an alignment to
the center of the component

**See Also:** getAlignmentX()

,

getAlignmentY()

,

Constant Field Values

- BOTTOM_ALIGNMENT

```java
public static final float BOTTOM_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY

.
Specifies an alignment to the bottom of the component.

**See Also:** getAlignmentY()

,

Constant Field Values

- LEFT_ALIGNMENT

```java
public static final float LEFT_ALIGNMENT
```

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the left side of the component.

**See Also:** getAlignmentX()

,

Constant Field Values

- RIGHT_ALIGNMENT

```java
public static final float RIGHT_ALIGNMENT
```

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the right side of the component.

**See Also:** getAlignmentX()

,

Constant Field Values

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The

AccessibleContext

associated with this

Component

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Component

```java
protected Component()
```

Constructs a new component. Class

Component

can be
extended directly to create a lightweight component that does not
utilize an opaque native window. A lightweight component must be
hosted by a native container somewhere higher up in the component
tree (for example, by a

Frame

object).

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the component.

**Returns:** this component's name
**Since:** 1.1
**See Also:** setName(java.lang.String)

- setName

```java
public void setName​(
String
name)
```

Sets the name of the component to the specified string.

**Parameters:** name

- the string that is to be this
component's name
**Since:** 1.1
**See Also:** getName()

- getParent

```java
public
Container
getParent()
```

Gets the parent of this component.

**Returns:** the parent container of this component
**Since:** 1.0

- setDropTarget

```java
public void setDropTarget​(
DropTarget
dt)
```

Associate a

DropTarget

with this component.
The

Component

will receive drops only if it
is enabled.

**Parameters:** dt

- The DropTarget
**See Also:** isEnabled()

- getDropTarget

```java
public
DropTarget
getDropTarget()
```

Gets the

DropTarget

associated with this

Component

.

**Returns:** the drop target

- getGraphicsConfiguration

```java
public
GraphicsConfiguration
getGraphicsConfiguration()
```

Gets the

GraphicsConfiguration

associated with this

Component

.
If the

Component

has not been assigned a specific

GraphicsConfiguration

,
the

GraphicsConfiguration

of the

Component

object's top-level container is
returned.
If the

Component

has been created, but not yet added
to a

Container

, this method returns

null

.

**Returns:** the

GraphicsConfiguration

used by this

Component

or

null
**Since:** 1.3

- getTreeLock

```java
public final
Object
getTreeLock()
```

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:** this component's locking object

- getToolkit

```java
public
Toolkit
getToolkit()
```

Gets the toolkit of this component. Note that
the frame that contains a component controls which
toolkit is used by that component. Therefore if the component
is moved from one frame to another, the toolkit it uses may change.

**Returns:** the toolkit of this component
**Since:** 1.0

- isValid

```java
public boolean isValid()
```

Determines whether this component is valid. A component is valid
when it is correctly sized and positioned within its parent
container and all its children are also valid.
In order to account for peers' size requirements, components are invalidated
before they are first shown on the screen. By the time the parent container
is fully realized, all its components will be valid.

**Returns:** true

if the component is valid,

false

otherwise
**Since:** 1.0
**See Also:** validate()

,

invalidate()

- isDisplayable

```java
public boolean isDisplayable()
```

Determines whether this component is displayable. A component is
displayable when it is connected to a native screen resource.

A component is made displayable either when it is added to
a displayable containment hierarchy or when its containment
hierarchy is made displayable.
A containment hierarchy is made displayable when its ancestor
window is either packed or made visible.

A component is made undisplayable either when it is removed from
a displayable containment hierarchy or when its containment hierarchy
is made undisplayable. A containment hierarchy is made
undisplayable when its ancestor window is disposed.

**Returns:** true

if the component is displayable,

false

otherwise
**Since:** 1.2
**See Also:** Container.add(Component)

,

Window.pack()

,

Window.show()

,

Container.remove(Component)

,

Window.dispose()

- isVisible

```java
public boolean isVisible()
```

Determines whether this component should be visible when its
parent is visible. Components are
initially visible, with the exception of top level components such
as

Frame

objects.

**Returns:** true

if the component is visible,

false

otherwise
**Since:** 1.0
**See Also:** setVisible(boolean)

- getMousePosition

```java
public
Point
getMousePosition()
throws
HeadlessException
```

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.
If the

Component

is not showing on the screen, this method
returns

null

even if the mouse pointer is above the area
where the

Component

would be displayed.
If the

Component

is partially or fully obscured by other

Component

s or native windows, this method returns a non-null
value only if the mouse pointer is located above the unobscured part of the

Component

.

For

Container

s it returns a non-null value if the mouse is
above the

Container

itself or above any of its descendants.
Use

Container.getMousePosition(boolean)

if you need to exclude children.

Sometimes the exact mouse coordinates are not important, and the only thing
that matters is whether a specific

Component

is under the mouse
pointer. If the return value of this method is

null

, mouse
pointer is not directly above the

Component

.

**Returns:** mouse coordinates relative to this

Component

, or null
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** isShowing()

,

Container.getMousePosition(boolean)

- isShowing

```java
public boolean isShowing()
```

Determines whether this component is showing on screen. This means
that the component must be visible, and it must be in a container
that is visible and showing.

Note:

sometimes there is no way to detect whether the

Component

is actually visible to the user. This can happen when:

- the component has been added to a visible

ScrollPane

but
the

Component

is not currently in the scroll pane's view port.

the

Component

is obscured by another

Component

or

Container

.

**Returns:** true

if the component is showing,

false

otherwise
**Since:** 1.0
**See Also:** setVisible(boolean)

- isEnabled

```java
public boolean isEnabled()
```

Determines whether this component is enabled. An enabled component
can respond to user input and generate events. Components are
enabled initially by default. A component may be enabled or disabled by
calling its

setEnabled

method.

**Returns:** true

if the component is enabled,

false

otherwise
**Since:** 1.0
**See Also:** setEnabled(boolean)

- setEnabled

```java
public void setEnabled​(boolean b)
```

Enables or disables this component, depending on the value of the
parameter

b

. An enabled component can respond to user
input and generate events. Components are enabled initially by default.

Note: Disabling a lightweight component does not prevent it from
receiving MouseEvents.

Note: Disabling a heavyweight container prevents all components
in this container from receiving any input events. But disabling a
lightweight container affects only this container.

**Parameters:** b

- If

true

, this component is
enabled; otherwise this component is disabled
**Since:** 1.1
**See Also:** isEnabled()

,

isLightweight()

- enable

```java
@Deprecated

public void enable()
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

- enable

```java
@Deprecated

public void enable​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

Enables or disables this component.

**Parameters:** b

-

true

to enable this component;
otherwise

false

- disable

```java
@Deprecated

public void disable()
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

- isDoubleBuffered

```java
public boolean isDoubleBuffered()
```

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later. Component
subclasses that support double buffering should override this
method to return true if double buffering is enabled.

**Returns:** false by default

- enableInputMethods

```java
public void enableInputMethods​(boolean enable)
```

Enables or disables input method support for this component. If input
method support is enabled and the component also processes key events,
incoming events are offered to
the current input method and will only be processed by the component or
dispatched to its listeners if the input method does not consume them.
By default, input method support is enabled.

**Parameters:** enable

- true to enable, false to disable
**Since:** 1.2
**See Also:** processKeyEvent(java.awt.event.KeyEvent)

- setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this component depending on the value of parameter

b

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** b

- if

true

, shows this component;
otherwise, hides this component
**Since:** 1.1
**See Also:** isVisible()

,

invalidate()

- show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

- show

```java
@Deprecated

public void show​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

Makes this component visible or invisible.

**Parameters:** b

-

true

to make this component visible;
otherwise

false

- hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

- getForeground

```java
public
Color
getForeground()
```

Gets the foreground color of this component.

**Returns:** this component's foreground color; if this component does
not have a foreground color, the foreground color of its parent
is returned
**Since:** 1.0
**See Also:** setForeground(java.awt.Color)

- setForeground

```java
public void setForeground​(
Color
c)
```

Sets the foreground color of this component.

**Parameters:** c

- the color to become this component's
foreground color; if this parameter is

null

then this component will inherit
the foreground color of its parent
**Since:** 1.0
**See Also:** getForeground()

- isForegroundSet

```java
public boolean isForegroundSet()
```

Returns whether the foreground color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its foreground color from an ancestor.

**Returns:** true

if the foreground color has been explicitly
set for this Component;

false

otherwise.
**Since:** 1.4

- getBackground

```java
public
Color
getBackground()
```

Gets the background color of this component.

**Returns:** this component's background color; if this component does
not have a background color,
the background color of its parent is returned
**Since:** 1.0
**See Also:** setBackground(java.awt.Color)

- setBackground

```java
public void setBackground​(
Color
c)
```

Sets the background color of this component.

The background color affects each component differently and the
parts of the component that are affected by the background color
may differ between operating systems.

**Parameters:** c

- the color to become this component's color;
if this parameter is

null

, then this
component will inherit the background color of its parent
**Since:** 1.0
**See Also:** getBackground()

- isBackgroundSet

```java
public boolean isBackgroundSet()
```

Returns whether the background color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its background color from an ancestor.

**Returns:** true

if the background color has been explicitly
set for this Component;

false

otherwise.
**Since:** 1.4

- getFont

```java
public
Font
getFont()
```

Gets the font of this component.

**Specified by:** getFont

in interface

MenuContainer
**Returns:** this component's font; if a font has not been set
for this component, the font of its parent is returned
**Since:** 1.0
**See Also:** setFont(java.awt.Font)

- setFont

```java
public void setFont​(
Font
f)
```

Sets the font of this component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** f

- the font to become this component's font;
if this parameter is

null

then this
component will inherit the font of its parent
**Since:** 1.0
**See Also:** getFont()

,

invalidate()

- isFontSet

```java
public boolean isFontSet()
```

Returns whether the font has been explicitly set for this Component. If
this method returns

false

, this Component is inheriting its
font from an ancestor.

**Returns:** true

if the font has been explicitly set for this
Component;

false

otherwise.
**Since:** 1.4

- getLocale

```java
public
Locale
getLocale()
```

Gets the locale of this component.

**Returns:** this component's locale; if this component does not
have a locale, the locale of its parent is returned
**Throws:** IllegalComponentStateException

- if the

Component

does not have its own locale and has not yet been added to
a containment hierarchy such that the locale can be determined
from the containing parent
**Since:** 1.1
**See Also:** setLocale(java.util.Locale)

- setLocale

```java
public void setLocale​(
Locale
l)
```

Sets the locale of this component. This is a bound property.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** l

- the locale to become this component's locale
**Since:** 1.1
**See Also:** getLocale()

,

invalidate()

- getColorModel

```java
public
ColorModel
getColorModel()
```

Gets the instance of

ColorModel

used to display
the component on the output device.

**Returns:** the color model used by this component
**Since:** 1.0
**See Also:** ColorModel

,

ComponentPeer.getColorModel()

,

Toolkit.getColorModel()

- getLocation

```java
public
Point
getLocation()
```

Gets the location of this component in the form of a
point specifying the component's top-left corner.
The location will be relative to the parent's coordinate space.

Due to the asynchronous nature of native event handling, this
method can return outdated values (for instance, after several calls
of

setLocation()

in rapid succession). For this
reason, the recommended method of obtaining a component's position is
within

java.awt.event.ComponentListener.componentMoved()

,
which is called after the operating system has finished moving the
component.

**Returns:** an instance of

Point

representing
the top-left corner of the component's bounds in
the coordinate space of the component's parent
**Since:** 1.1
**See Also:** setLocation(int, int)

,

getLocationOnScreen()

- getLocationOnScreen

```java
public
Point
getLocationOnScreen()
```

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

**Returns:** an instance of

Point

representing
the top-left corner of the component's bounds in the
coordinate space of the screen
**Throws:** IllegalComponentStateException

- if the
component is not showing on the screen
**See Also:** setLocation(int, int)

,

getLocation()

- location

```java
@Deprecated

public
Point
location()
```

Deprecated.

As of JDK version 1.1,
replaced by

getLocation()

.

Returns the location of this component's top left corner.

**Returns:** the location of this component's top left corner

- setLocation

```java
public void setLocation​(int x,
int y)
```

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Since:** 1.1
**See Also:** getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

- move

```java
@Deprecated

public void move​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by

setLocation(int, int)

.

Moves this component to a new location.

**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space

- setLocation

```java
public void setLocation​(
Point
p)
```

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent
**Since:** 1.1
**See Also:** getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

- getSize

```java
public
Dimension
getSize()
```

Returns the size of this component in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this component's height, and the

width

field of the

Dimension

object contains
this component's width.

**Returns:** a

Dimension

object that indicates the
size of this component
**Since:** 1.1
**See Also:** setSize(int, int)

- size

```java
@Deprecated

public
Dimension
size()
```

Deprecated.

As of JDK version 1.1,
replaced by

getSize()

.

Returns the size of this component in the form of a

Dimension

object.

**Returns:** the

Dimension

object that indicates the
size of this component

- setSize

```java
public void setSize​(int width,
int height)
```

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** width

- the new width of this component in pixels
**Parameters:** height

- the new height of this component in pixels
**Since:** 1.1
**See Also:** getSize()

,

setBounds(int, int, int, int)

,

invalidate()

- resize

```java
@Deprecated

public void resize​(int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setSize(int, int)

.

Resizes this component.

**Parameters:** width

- the new width of the component
**Parameters:** height

- the new height of the component

- setSize

```java
public void setSize​(
Dimension
d)
```

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** d

- the dimension specifying the new size
of this component
**Throws:** NullPointerException

- if

d

is

null
**Since:** 1.1
**See Also:** setSize(int, int)

,

setBounds(int, int, int, int)

,

invalidate()

- resize

```java
@Deprecated

public void resize​(
Dimension
d)
```

Deprecated.

As of JDK version 1.1,
replaced by

setSize(Dimension)

.

Resizes this component so that it has width

d.width

and height

d.height

.

**Parameters:** d

- the new size of this component

- getBounds

```java
public
Rectangle
getBounds()
```

Gets the bounds of this component in the form of a

Rectangle

object. The bounds specify this
component's width, height, and location relative to
its parent.

**Returns:** a rectangle indicating this component's bounds
**See Also:** setBounds(int, int, int, int)

,

getLocation()

,

getSize()

- bounds

```java
@Deprecated

public
Rectangle
bounds()
```

Deprecated.

As of JDK version 1.1,
replaced by

getBounds()

.

Returns the bounding rectangle of this component.

**Returns:** the bounding rectangle for this component

- setBounds

```java
public void setBounds​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** x

- the new

x

-coordinate of this component
**Parameters:** y

- the new

y

-coordinate of this component
**Parameters:** width

- the new

width

of this component
**Parameters:** height

- the new

height

of this
component
**Since:** 1.1
**See Also:** getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

- reshape

```java
@Deprecated

public void reshape​(int x,
int y,
int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Reshapes the bounding rectangle for this component.

**Parameters:** x

- the

x

coordinate of the upper left corner of the rectangle
**Parameters:** y

- the

y

coordinate of the upper left corner of the rectangle
**Parameters:** width

- the width of the rectangle
**Parameters:** height

- the height of the rectangle

- setBounds

```java
public void setBounds​(
Rectangle
r)
```

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** r

- the new bounding rectangle for this component
**Throws:** NullPointerException

- if

r

is

null
**Since:** 1.1
**See Also:** getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

- getX

```java
public int getX()
```

Returns the current x coordinate of the components origin.
This method is preferable to writing

component.getBounds().x

,
or

component.getLocation().x

because it doesn't
cause any heap allocations.

**Returns:** the current x coordinate of the components origin
**Since:** 1.2

- getY

```java
public int getY()
```

Returns the current y coordinate of the components origin.
This method is preferable to writing

component.getBounds().y

,
or

component.getLocation().y

because it
doesn't cause any heap allocations.

**Returns:** the current y coordinate of the components origin
**Since:** 1.2

- getWidth

```java
public int getWidth()
```

Returns the current width of this component.
This method is preferable to writing

component.getBounds().width

,
or

component.getSize().width

because it
doesn't cause any heap allocations.

**Returns:** the current width of this component
**Since:** 1.2

- getHeight

```java
public int getHeight()
```

Returns the current height of this component.
This method is preferable to writing

component.getBounds().height

,
or

component.getSize().height

because it
doesn't cause any heap allocations.

**Returns:** the current height of this component
**Since:** 1.2

- getBounds

```java
public
Rectangle
getBounds​(
Rectangle
rv)
```

Stores the bounds of this component into "return value"

rv

and
return

rv

. If rv is

null

a new

Rectangle

is allocated.
This version of

getBounds

is useful if the caller
wants to avoid allocating a new

Rectangle

object
on the heap.

**Parameters:** rv

- the return value, modified to the components bounds
**Returns:** rv

- getSize

```java
public
Dimension
getSize​(
Dimension
rv)
```

Stores the width/height of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Dimension

object is allocated. This version of

getSize

is useful if the caller wants to avoid
allocating a new

Dimension

object on the heap.

**Parameters:** rv

- the return value, modified to the components size
**Returns:** rv

- getLocation

```java
public
Point
getLocation​(
Point
rv)
```

Stores the x,y origin of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Point

is allocated.
This version of

getLocation

is useful if the
caller wants to avoid allocating a new

Point

object on the heap.

**Parameters:** rv

- the return value, modified to the components location
**Returns:** rv

- isOpaque

```java
public boolean isOpaque()
```

Returns true if this component is completely opaque, returns
false by default.

An opaque component paints every pixel within its
rectangular region. A non-opaque component paints only some of
its pixels, allowing the pixels underneath it to "show through".
A component that does not fully paint its pixels therefore
provides a degree of transparency.

Subclasses that guarantee to always completely paint their
contents should override this method and return true.

**Returns:** true if this component is completely opaque
**Since:** 1.2
**See Also:** isLightweight()

- isLightweight

```java
public boolean isLightweight()
```

A lightweight component doesn't have a native toolkit peer.
Subclasses of

Component

and

Container

,
other than the ones defined in this package like

Button

or

Scrollbar

, are lightweight.
All of the Swing components are lightweights.

This method will always return

false

if this component
is not displayable because it is impossible to determine the
weight of an undisplayable component.

**Returns:** true if this component has a lightweight peer; false if
it has a native peer or no peer
**Since:** 1.2
**See Also:** isDisplayable()

- setPreferredSize

```java
public void setPreferredSize​(
Dimension
preferredSize)
```

Sets the preferred size of this component to a constant
value. Subsequent calls to

getPreferredSize

will always
return this value. Setting the preferred size to

null

restores the default behavior.

**Parameters:** preferredSize

- The new preferred size, or null
**Since:** 1.5
**See Also:** getPreferredSize()

,

isPreferredSizeSet()

- isPreferredSizeSet

```java
public boolean isPreferredSizeSet()
```

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

**Returns:** true if

setPreferredSize

has been invoked
with a non-null value.
**Since:** 1.5

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Gets the preferred size of this component.

**Returns:** a dimension object indicating this component's preferred size
**See Also:** getMinimumSize()

,

LayoutManager

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Returns the component's preferred size.

**Returns:** the component's preferred size

- setMinimumSize

```java
public void setMinimumSize​(
Dimension
minimumSize)
```

Sets the minimum size of this component to a constant
value. Subsequent calls to

getMinimumSize

will always
return this value. Setting the minimum size to

null

restores the default behavior.

**Parameters:** minimumSize

- the new minimum size of this component
**Since:** 1.5
**See Also:** getMinimumSize()

,

isMinimumSizeSet()

- isMinimumSizeSet

```java
public boolean isMinimumSizeSet()
```

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

**Returns:** true if

setMinimumSize

has been invoked with a
non-null value.
**Since:** 1.5

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Gets the minimum size of this component.

**Returns:** a dimension object indicating this component's minimum size
**See Also:** getPreferredSize()

,

LayoutManager

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Returns the minimum size of this component.

**Returns:** the minimum size of this component

- setMaximumSize

```java
public void setMaximumSize​(
Dimension
maximumSize)
```

Sets the maximum size of this component to a constant
value. Subsequent calls to

getMaximumSize

will always
return this value. Setting the maximum size to

null

restores the default behavior.

**Parameters:** maximumSize

- a

Dimension

containing the
desired maximum allowable size
**Since:** 1.5
**See Also:** getMaximumSize()

,

isMaximumSizeSet()

- isMaximumSizeSet

```java
public boolean isMaximumSizeSet()
```

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

**Returns:** true if

maximumSize

is non-

null

,
false otherwise
**Since:** 1.5

- getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Gets the maximum size of this component.

**Returns:** a dimension object indicating this component's maximum size
**See Also:** getMinimumSize()

,

getPreferredSize()

,

LayoutManager

- getAlignmentX

```java
public float getAlignmentX()
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:** the horizontal alignment of this component

- getAlignmentY

```java
public float getAlignmentY()
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:** the vertical alignment of this component

- getBaseline

```java
public int getBaseline​(int width,
int height)
```

Returns the baseline. The baseline is measured from the top of
the component. This method is primarily meant for

LayoutManager

s to align components along their
baseline. A return value less than 0 indicates this component
does not have a reasonable baseline and that

LayoutManager

s should not align this component on
its baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** getBaselineResizeBehavior()

,

FontMetrics

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior()
```

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

. Subclasses that have a
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Returns:** an enum indicating how the baseline changes as the component
size changes
**Since:** 1.6
**See Also:** getBaseline(int, int)

- doLayout

```java
public void doLayout()
```

Prompts the layout manager to lay out this component. This is
usually called when the component (more specifically, container)
is validated.

**See Also:** validate()

,

LayoutManager

- layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

- validate

```java
public void validate()
```

Validates this component.

The meaning of the term

validating

is defined by the ancestors of
this class. See

Container.validate()

for more details.

**Since:** 1.0
**See Also:** invalidate()

,

doLayout()

,

LayoutManager

,

Container.validate()

- invalidate

```java
public void invalidate()
```

Invalidates this component and its ancestors.

By default, all the ancestors of the component up to the top-most
container of the hierarchy are marked invalid. If the

java.awt.smartInvalidate

system property is set to

true

,
invalidation stops on the nearest validate root of this component.
Marking a container

invalid

indicates that the container needs to
be laid out.

This method is called automatically when any layout-related information
changes (e.g. setting the bounds of the component, or adding the
component to a container).

This method might be called often, so it should work fast.

**Since:** 1.0
**See Also:** validate()

,

doLayout()

,

LayoutManager

,

Container.isValidateRoot()

- revalidate

```java
public void revalidate()
```

Revalidates the component hierarchy up to the nearest validate root.

This method first invalidates the component hierarchy starting from this
component up to the nearest validate root. Afterwards, the component
hierarchy is validated starting from the nearest validate root.

This is a convenience method supposed to help application developers
avoid looking for validate roots manually. Basically, it's equivalent to
first calling the

invalidate()

method on this component, and
then calling the

validate()

method on the nearest validate
root.

**Since:** 1.7
**See Also:** Container.isValidateRoot()

- getGraphics

```java
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
font)
```

Gets the font metrics for the specified font.
Warning: Since Font metrics are affected by the

FontRenderContext

and
this method does not provide one, it can return only metrics for
the default render context which may not match that used when
rendering on the Component if

Graphics2D

functionality is being
used. Instead metrics can be obtained at rendering time by calling

Graphics.getFontMetrics()

or text measurement APIs on the

Font

class.

**Parameters:** font

- the font for which font metrics is to be
obtained
**Returns:** the font metrics for

font
**Since:** 1.0
**See Also:** getFont()

,

ComponentPeer.getFontMetrics(Font)

,

Toolkit.getFontMetrics(Font)

- setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Parameters:** cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent
**Since:** 1.1
**See Also:** isEnabled()

,

isShowing()

,

getCursor()

,

contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

- getCursor

```java
public
Cursor
getCursor()
```

Gets the cursor set in the component. If the component does
not have a cursor set, the cursor of its parent is returned.
If no cursor is set in the entire hierarchy,

Cursor.DEFAULT_CURSOR

is returned.

**Returns:** the cursor for this component
**Since:** 1.1
**See Also:** setCursor(java.awt.Cursor)

- isCursorSet

```java
public boolean isCursorSet()
```

Returns whether the cursor has been explicitly set for this Component.
If this method returns

false

, this Component is inheriting
its cursor from an ancestor.

**Returns:** true

if the cursor has been explicitly set for this
Component;

false

otherwise.
**Since:** 1.4

- paint

```java
public void paint​(
Graphics
g)
```

Paints this component.

This method is called when the contents of the component should
be painted; such as when the component is first being shown or
is damaged and in need of repair. The clip rectangle in the

Graphics

parameter is set to the area
which needs to be painted.
Subclasses of

Component

that override this
method need not call

super.paint(g)

.

For performance reasons,

Component

s with zero width
or height aren't considered to need painting when they are first shown,
and also aren't considered to need repair.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** g

- the graphics context to use for painting
**Since:** 1.0
**See Also:** update(java.awt.Graphics)

- update

```java
public void update​(
Graphics
g)
```

Updates this component.

If this component is not a lightweight component, the
AWT calls the

update

method in response to
a call to

repaint

. You can assume that
the background is not cleared.

The

update

method of

Component

calls this component's

paint

method to redraw
this component. This method is commonly overridden by subclasses
which need to do additional work in response to a call to

repaint

.
Subclasses of Component that override this method should either
call

super.update(g)

, or call

paint(g)

directly from their

update

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** g

- the specified context to use for updating
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

,

repaint()

- paintAll

```java
public void paintAll​(
Graphics
g)
```

Paints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for painting
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

- repaint

```java
public void repaint()
```

Repaints this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method as soon as possible. Otherwise, this method causes
a call to this component's

update

method as soon
as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Since:** 1.0
**See Also:** update(Graphics)

- repaint

```java
public void repaint​(long tm)
```

Repaints the component. If this component is a lightweight
component, this results in a call to

paint

within

tm

milliseconds.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** tm

- maximum time in milliseconds before update
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

,

update(Graphics)

- repaint

```java
public void repaint​(int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method
as soon as possible. Otherwise, this method causes a call to
this component's

update

method as soon as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.0
**See Also:** update(Graphics)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

tm

milliseconds.

If this component is a lightweight component, this method causes
a call to this component's

paint

method.
Otherwise, this method causes a call to this component's

update

method.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** tm

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.0
**See Also:** update(Graphics)

- print

```java
public void print​(
Graphics
g)
```

Prints this component. Applications should override this method
for components that must do special processing before being
printed or should be printed differently than they are painted.

The default implementation of this method calls the

paint

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for printing
**Since:** 1.0
**See Also:** paint(Graphics)

- printAll

```java
public void printAll​(
Graphics
g)
```

Prints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for printing
**Since:** 1.0
**See Also:** print(Graphics)

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:** imageUpdate

in interface

ImageObserver
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**Since:** 1.0
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- createImage

```java
public
Image
createImage​(
ImageProducer
producer)
```

Creates an image from the specified image producer.

**Parameters:** producer

- the image producer
**Returns:** the image produced
**Since:** 1.0

- createImage

```java
public
Image
createImage​(int width,
int height)
```

Creates an off-screen drawable image to be used for double buffering.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Returns:** an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.0
**See Also:** isDisplayable()

,

GraphicsEnvironment.isHeadless()

- createVolatileImage

```java
public
VolatileImage
createVolatileImage​(int width,
int height)
```

Creates a volatile off-screen drawable image to be used for double
buffering.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Returns:** an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** VolatileImage

,

isDisplayable()

,

GraphicsEnvironment.isHeadless()

- createVolatileImage

```java
public
VolatileImage
createVolatileImage​(int width,
int height,

ImageCapabilities
caps)
throws
AWTException
```

Creates a volatile off-screen drawable image, with the given
capabilities. The contents of this image may be lost at any time due to
operating system issues, so the image must be managed via the

VolatileImage

interface.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Parameters:** caps

- the image capabilities
**Returns:** a VolatileImage object, which can be used to manage surface
contents loss and capabilities. The

null

value if the
component is not displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Throws:** AWTException

- if an image with the specified capabilities cannot
be created
**Since:** 1.4
**See Also:** VolatileImage

- prepareImage

```java
public boolean prepareImage​(
Image
image,

ImageObserver
observer)
```

Prepares an image for rendering on this component. The image
data is downloaded asynchronously in another thread and the
appropriate screen representation of the image is generated.

**Parameters:** image

- the

Image

for which to
prepare a screen representation
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** true

if the image has already been fully
prepared;

false

otherwise
**Since:** 1.0

- prepareImage

```java
public boolean prepareImage​(
Image
image,
int width,
int height,

ImageObserver
observer)
```

Prepares an image for rendering on this component at the
specified width and height.

The image data is downloaded asynchronously in another thread,
and an appropriately scaled screen representation of the image is
generated.

**Parameters:** image

- the instance of

Image

for which to prepare a screen representation
**Parameters:** width

- the width of the desired screen representation
**Parameters:** height

- the height of the desired screen representation
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** true

if the image has already been fully
prepared;

false

otherwise
**Since:** 1.0
**See Also:** ImageObserver

- checkImage

```java
public int checkImage​(
Image
image,

ImageObserver
observer)
```

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:** image

- the

Image

object whose status
is being checked
**Parameters:** observer

- the

ImageObserver

object to be notified as the image is being prepared
**Returns:** the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available
**Since:** 1.0
**See Also:** prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

- checkImage

```java
public int checkImage​(
Image
image,
int width,
int height,

ImageObserver
observer)
```

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

The

checkImage

method of

Component

calls its peer's

checkImage

method to calculate
the flags. If this component does not yet have a peer, the
component's toolkit's

checkImage

method is called
instead.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:** image

- the

Image

object whose status
is being checked
**Parameters:** width

- the width of the scaled version
whose status is to be checked
**Parameters:** height

- the height of the scaled version
whose status is to be checked
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available
**Since:** 1.0
**See Also:** prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

- setIgnoreRepaint

```java
public void setIgnoreRepaint​(boolean ignoreRepaint)
```

Sets whether or not paint messages received from the operating system
should be ignored. This does not affect paint events generated in
software by the AWT, unless they are an immediate response to an
OS-level paint message.

This is useful, for example, if running under full-screen mode and
better performance is desired, or if page-flipping is used as the
buffer strategy.

**Parameters:** ignoreRepaint

-

true

if the paint messages from the OS
should be ignored; otherwise

false
**Since:** 1.4
**See Also:** getIgnoreRepaint()

,

Canvas.createBufferStrategy(int)

,

Window.createBufferStrategy(int)

,

BufferStrategy

,

GraphicsDevice.setFullScreenWindow(java.awt.Window)

- getIgnoreRepaint

```java
public boolean getIgnoreRepaint()
```

**Returns:** whether or not paint messages received from the operating system
should be ignored.
**Since:** 1.4
**See Also:** setIgnoreRepaint(boolean)

- contains

```java
public boolean contains​(int x,
int y)
```

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the point is within the component;
otherwise

false
**Since:** 1.1
**See Also:** getComponentAt(int, int)

- inside

```java
@Deprecated

public boolean inside​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by contains(int, int).

Checks whether the point is inside of this component.

**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the point is within the component;
otherwise

false

- contains

```java
public boolean contains​(
Point
p)
```

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

**Parameters:** p

- the point
**Returns:** true

if the point is within the component;
otherwise

false
**Throws:** NullPointerException

- if

p

is

null
**Since:** 1.1
**See Also:** getComponentAt(Point)

- getComponentAt

```java
public
Component
getComponentAt​(int x,
int y)
```

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component. This method only
looks one level deep. If the point (

x

,

y

) is
inside a subcomponent that itself has subcomponents, it does not
go looking down the subcomponent tree.

The

locate

method of

Component

simply
returns the component itself if the (

x

,

y

)
coordinate location is inside its bounding box, and

null

otherwise.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** the component or subcomponent that contains the
(

x

,

y

) location;

null

if the location
is outside this component
**Since:** 1.0
**See Also:** contains(int, int)

- locate

```java
@Deprecated

public
Component
locate​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by getComponentAt(int, int).

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

**Parameters:** x

- the

x

coordinate to search for components at
**Parameters:** y

- the

y

coordinate to search for components at
**Returns:** the component at the specified location or

null

- getComponentAt

```java
public
Component
getComponentAt​(
Point
p)
```

Returns the component or subcomponent that contains the
specified point.

**Parameters:** p

- the point
**Returns:** the component at the specified location or

null
**Since:** 1.1
**See Also:** contains(int, int)

- deliverEvent

```java
@Deprecated

public void deliverEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

.

**Parameters:** e

- the event to deliver

- dispatchEvent

```java
public final void dispatchEvent​(
AWTEvent
e)
```

Dispatches an event to this component or one of its sub components.
Calls

processEvent

before returning for 1.1-style
events which have been enabled for the

Component

.

**Parameters:** e

- the event

- postEvent

```java
@Deprecated

public boolean postEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by dispatchEvent(AWTEvent).

Description copied from interface:

MenuContainer

Posts an event to the listeners.

**Specified by:** postEvent

in interface

MenuContainer
**Parameters:** e

- the event to dispatch
**Returns:** the results of posting the event

- addComponentListener

```java
public void addComponentListener​(
ComponentListener
l)
```

Adds the specified component listener to receive component events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the component listener
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

removeComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

- removeComponentListener

```java
public void removeComponentListener​(
ComponentListener
l)
```

Removes the specified component listener so that it no longer
receives component events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the component listener
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

- getComponentListeners

```java
public
ComponentListener
[] getComponentListeners()
```

Returns an array of all the component listeners
registered on this component.

**Returns:** all

ComponentListener

s of this component
or an empty array if no component
listeners are currently registered
**Since:** 1.4
**See Also:** addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

- addFocusListener

```java
public void addFocusListener​(
FocusListener
l)
```

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the focus listener
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

removeFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

- removeFocusListener

```java
public void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so that it no longer
receives focus events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the focus listener
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

addFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

- getFocusListeners

```java
public
FocusListener
[] getFocusListeners()
```

Returns an array of all the focus listeners
registered on this component.

**Returns:** all of this component's

FocusListener

s
or an empty array if no component
listeners are currently registered
**Since:** 1.4
**See Also:** addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

- addHierarchyListener

```java
public void addHierarchyListener​(
HierarchyListener
l)
```

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

removeHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

- removeHierarchyListener

```java
public void removeHierarchyListener​(
HierarchyListener
l)
```

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

- getHierarchyListeners

```java
public
HierarchyListener
[] getHierarchyListeners()
```

Returns an array of all the hierarchy listeners
registered on this component.

**Returns:** all of this component's

HierarchyListener

s
or an empty array if no hierarchy
listeners are currently registered
**Since:** 1.4
**See Also:** addHierarchyListener(java.awt.event.HierarchyListener)

,

removeHierarchyListener(java.awt.event.HierarchyListener)

- addHierarchyBoundsListener

```java
public void addHierarchyBoundsListener​(
HierarchyBoundsListener
l)
```

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy bounds listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

- removeHierarchyBoundsListener

```java
public void removeHierarchyBoundsListener​(
HierarchyBoundsListener
l)
```

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy bounds listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

- getHierarchyBoundsListeners

```java
public
HierarchyBoundsListener
[] getHierarchyBoundsListeners()
```

Returns an array of all the hierarchy bounds listeners
registered on this component.

**Returns:** all of this component's

HierarchyBoundsListener

s
or an empty array if no hierarchy bounds
listeners are currently registered
**Since:** 1.4
**See Also:** addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

- addKeyListener

```java
public void addKeyListener​(
KeyListener
l)
```

Adds the specified key listener to receive key events from
this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the key listener.
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

removeKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

- removeKeyListener

```java
public void removeKeyListener​(
KeyListener
l)
```

Removes the specified key listener so that it no longer
receives key events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the key listener
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

addKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

- getKeyListeners

```java
public
KeyListener
[] getKeyListeners()
```

Returns an array of all the key listeners
registered on this component.

**Returns:** all of this component's

KeyListener

s
or an empty array if no key
listeners are currently registered
**Since:** 1.4
**See Also:** addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

- addMouseListener

```java
public void addMouseListener​(
MouseListener
l)
```

Adds the specified mouse listener to receive mouse events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

removeMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

- removeMouseListener

```java
public void removeMouseListener​(
MouseListener
l)
```

Removes the specified mouse listener so that it no longer
receives mouse events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

- getMouseListeners

```java
public
MouseListener
[] getMouseListeners()
```

Returns an array of all the mouse listeners
registered on this component.

**Returns:** all of this component's

MouseListener

s
or an empty array if no mouse
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

- addMouseMotionListener

```java
public void addMouseMotionListener​(
MouseMotionListener
l)
```

Adds the specified mouse motion listener to receive mouse motion
events from this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse motion listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

- removeMouseMotionListener

```java
public void removeMouseMotionListener​(
MouseMotionListener
l)
```

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse motion listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

- getMouseMotionListeners

```java
public
MouseMotionListener
[] getMouseMotionListeners()
```

Returns an array of all the mouse motion listeners
registered on this component.

**Returns:** all of this component's

MouseMotionListener

s
or an empty array if no mouse motion
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

- addMouseWheelListener

```java
public void addMouseWheelListener​(
MouseWheelListener
l)
```

Adds the specified mouse wheel listener to receive mouse wheel events
from this component. Containers also receive mouse wheel events from
sub-components.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse wheel listener
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

- removeMouseWheelListener

```java
public void removeMouseWheelListener​(
MouseWheelListener
l)
```

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse wheel listener.
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

- getMouseWheelListeners

```java
public
MouseWheelListener
[] getMouseWheelListeners()
```

Returns an array of all the mouse wheel listeners
registered on this component.

**Returns:** all of this component's

MouseWheelListener

s
or an empty array if no mouse wheel
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseWheelListener(java.awt.event.MouseWheelListener)

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

- addInputMethodListener

```java
public void addInputMethodListener​(
InputMethodListener
l)
```

Adds the specified input method listener to receive
input method events from this component. A component will
only receive input method events from input methods
if it also overrides

getInputMethodRequests

to return an

InputMethodRequests

instance.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the input method listener
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

removeInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

,

getInputMethodRequests()

- removeInputMethodListener

```java
public void removeInputMethodListener​(
InputMethodListener
l)
```

Removes the specified input method listener so that it no longer
receives input method events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the input method listener
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

- getInputMethodListeners

```java
public
InputMethodListener
[] getInputMethodListeners()
```

Returns an array of all the input method listeners
registered on this component.

**Returns:** all of this component's

InputMethodListener

s
or an empty array if no input method
listeners are currently registered
**Since:** 1.4
**See Also:** addInputMethodListener(java.awt.event.InputMethodListener)

,

removeInputMethodListener(java.awt.event.InputMethodListener)

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Component c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getComponentListeners()

,

getFocusListeners()

,

getHierarchyListeners()

,

getHierarchyBoundsListeners()

,

getKeyListeners()

,

getMouseListeners()

,

getMouseMotionListeners()

,

getMouseWheelListeners()

,

getInputMethodListeners()

,

getPropertyChangeListeners()

- getInputMethodRequests

```java
public
InputMethodRequests
getInputMethodRequests()
```

Gets the input method request handler which supports
requests from input methods for this component. A component
that supports on-the-spot text input must override this
method to return an

InputMethodRequests

instance.
At the same time, it also has to handle input method events.

**Returns:** the input method request handler for this component,

null

by default
**Since:** 1.2
**See Also:** addInputMethodListener(java.awt.event.InputMethodListener)

- getInputContext

```java
public
InputContext
getInputContext()
```

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component. By default, the input context used for
the parent component is returned. Components may
override this to return a private input context.

**Returns:** the input context used by this component;

null

if no context can be determined
**Since:** 1.2

- enableEvents

```java
protected final void enableEvents​(long eventsToEnable)
```

Enables the events defined by the specified event mask parameter
to be delivered to this component.

Event types are automatically enabled when a listener for
that event type is added to the component.

This method only needs to be invoked by subclasses of

Component

which desire to have the specified event
types delivered to

processEvent

regardless of whether
or not a listener is registered.

**Parameters:** eventsToEnable

- the event mask defining the event types
**Since:** 1.1
**See Also:** processEvent(java.awt.AWTEvent)

,

disableEvents(long)

,

AWTEvent

- disableEvents

```java
protected final void disableEvents​(long eventsToDisable)
```

Disables the events defined by the specified event mask parameter
from being delivered to this component.

**Parameters:** eventsToDisable

- the event mask defining the event types
**Since:** 1.1
**See Also:** enableEvents(long)

- coalesceEvents

```java
protected
AWTEvent
coalesceEvents​(
AWTEvent
existingEvent,

AWTEvent
newEvent)
```

Potentially coalesce an event being posted with an existing
event. This method is called by

EventQueue.postEvent

if an event with the same ID as the event to be posted is found in
the queue (both events must have this component as their source).
This method either returns a coalesced event which replaces
the existing event (and the new event is then discarded), or

null

to indicate that no combining should be done
(add the second event to the end of the queue). Either event
parameter may be modified and returned, as the other one is discarded
unless

null

is returned.

This implementation of

coalesceEvents

coalesces
two event types: mouse move (and drag) events,
and paint (and update) events.
For mouse move events the last event is always returned, causing
intermediate moves to be discarded. For paint events, the new
event is coalesced into a complex

RepaintArea

in the peer.
The new

AWTEvent

is always returned.

**Parameters:** existingEvent

- the event already on the

EventQueue
**Parameters:** newEvent

- the event being posted to the

EventQueue
**Returns:** a coalesced event, or

null

indicating that no
coalescing was done

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events occurring on this component. By default this
method calls the appropriate

process<event type>Event

method for the given class of event.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the event
**Since:** 1.1
**See Also:** processComponentEvent(java.awt.event.ComponentEvent)

,

processFocusEvent(java.awt.event.FocusEvent)

,

processKeyEvent(java.awt.event.KeyEvent)

,

processMouseEvent(java.awt.event.MouseEvent)

,

processMouseMotionEvent(java.awt.event.MouseEvent)

,

processInputMethodEvent(java.awt.event.InputMethodEvent)

,

processHierarchyEvent(java.awt.event.HierarchyEvent)

,

processMouseWheelEvent(java.awt.event.MouseWheelEvent)

- processComponentEvent

```java
protected void processComponentEvent​(
ComponentEvent
e)
```

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

This method is not called unless component events are
enabled for this component. Component events are enabled
when one of the following occurs:

- A

ComponentListener

object is registered
via

addComponentListener

.

Component events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the component event
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

enableEvents(long)

- processFocusEvent

```java
protected void processFocusEvent​(
FocusEvent
e)
```

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

This method is not called unless focus events are
enabled for this component. Focus events are enabled
when one of the following occurs:

- A

FocusListener

object is registered
via

addFocusListener

.

Focus events are enabled via

enableEvents

.

If focus events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a focus event should be dispatched to
registered

FocusListener

objects. If the
events are to be dispatched, the

KeyboardFocusManager

calls the

Component

's

dispatchEvent

method, which results in a call to the

Component

's

processFocusEvent

method.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the focus event
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

KeyboardFocusManager

,

addFocusListener(java.awt.event.FocusListener)

,

enableEvents(long)

,

dispatchEvent(java.awt.AWTEvent)

- processKeyEvent

```java
protected void processKeyEvent​(
KeyEvent
e)
```

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

This method is not called unless key events are
enabled for this component. Key events are enabled
when one of the following occurs:

- A

KeyListener

object is registered
via

addKeyListener

.

Key events are enabled via

enableEvents

.

If key events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a key event should be dispatched to
registered

KeyListener

objects. The

DefaultKeyboardFocusManager

will not dispatch
key events to a

Component

that is not the focus
owner or is not showing.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the key event
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

processEvent(java.awt.AWTEvent)

,

dispatchEvent(java.awt.AWTEvent)

,

addKeyListener(java.awt.event.KeyListener)

,

enableEvents(long)

,

isShowing()

- processMouseEvent

```java
protected void processMouseEvent​(
MouseEvent
e)
```

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

This method is not called unless mouse events are
enabled for this component. Mouse events are enabled
when one of the following occurs:

- A

MouseListener

object is registered
via

addMouseListener

.

Mouse events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse event
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

enableEvents(long)

- processMouseMotionEvent

```java
protected void processMouseMotionEvent​(
MouseEvent
e)
```

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

This method is not called unless mouse motion events are
enabled for this component. Mouse motion events are enabled
when one of the following occurs:

- A

MouseMotionListener

object is registered
via

addMouseMotionListener

.

Mouse motion events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse motion event
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

enableEvents(long)

- processMouseWheelEvent

```java
protected void processMouseWheelEvent​(
MouseWheelEvent
e)
```

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

This method is not called unless mouse wheel events are
enabled for this component. Mouse wheel events are enabled
when one of the following occurs:

- A

MouseWheelListener

object is registered
via

addMouseWheelListener

.

Mouse wheel events are enabled via

enableEvents

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse wheel event
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

enableEvents(long)

- processInputMethodEvent

```java
protected void processInputMethodEvent​(
InputMethodEvent
e)
```

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

This method is not called unless input method events
are enabled for this component. Input method events are enabled
when one of the following occurs:

- An

InputMethodListener

object is registered
via

addInputMethodListener

.

Input method events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the input method event
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

enableEvents(long)

- processHierarchyEvent

```java
protected void processHierarchyEvent​(
HierarchyEvent
e)
```

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

This method is not called unless hierarchy events
are enabled for this component. Hierarchy events are enabled
when one of the following occurs:

- An

HierarchyListener

object is registered
via

addHierarchyListener

.

Hierarchy events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the hierarchy event
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

enableEvents(long)

- processHierarchyBoundsEvent

```java
protected void processHierarchyBoundsEvent​(
HierarchyEvent
e)
```

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

This method is not called unless hierarchy bounds events
are enabled for this component. Hierarchy bounds events are enabled
when one of the following occurs:

- An

HierarchyBoundsListener

object is registered
via

addHierarchyBoundsListener

.

Hierarchy bounds events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the hierarchy event
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

enableEvents(long)

- handleEvent

```java
@Deprecated

public boolean handleEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1
replaced by processEvent(AWTEvent).

**Parameters:** evt

- the event to handle
**Returns:** true

if the event was handled,

false

otherwise

- mouseDown

```java
@Deprecated

public boolean mouseDown​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseDrag

```java
@Deprecated

public boolean mouseDrag​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseUp

```java
@Deprecated

public boolean mouseUp​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseMove

```java
@Deprecated

public boolean mouseMove​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseEnter

```java
@Deprecated

public boolean mouseEnter​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseExit

```java
@Deprecated

public boolean mouseExit​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- keyDown

```java
@Deprecated

public boolean keyDown​(
Event
evt,
int key)
```

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

**Parameters:** evt

- the event to handle
**Parameters:** key

- the key pressed
**Returns:** false

- keyUp

```java
@Deprecated

public boolean keyUp​(
Event
evt,
int key)
```

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

**Parameters:** evt

- the event to handle
**Parameters:** key

- the key pressed
**Returns:** false

- action

```java
@Deprecated

public boolean action​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
should register this component as ActionListener on component
which fires action events.

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object acted on
**Returns:** false

- addNotify

```java
public void addNotify()
```

Makes this

Component

displayable by connecting it to a
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Since:** 1.0
**See Also:** isDisplayable()

,

removeNotify()

,

invalidate()

- removeNotify

```java
public void removeNotify()
```

Makes this

Component

undisplayable by destroying it native
screen resource.

This method is called by the toolkit internally and should
not be called directly by programs. Code overriding
this method should call

super.removeNotify

as
the first line of the overriding method.

**Since:** 1.0
**See Also:** isDisplayable()

,

addNotify()

- gotFocus

```java
@Deprecated

public boolean gotFocus​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object focused
**Returns:** false

- lostFocus

```java
@Deprecated

public boolean lostFocus​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object focused
**Returns:** false

- isFocusTraversable

```java
@Deprecated

public boolean isFocusTraversable()
```

Deprecated.

As of 1.4, replaced by

isFocusable()

.

Returns whether this

Component

can become the focus
owner.

**Returns:** true

if this

Component

is
focusable;

false

otherwise
**Since:** 1.1
**See Also:** setFocusable(boolean)

- isFocusable

```java
public boolean isFocusable()
```

Returns whether this Component can be focused.

**Returns:** true

if this Component is focusable;

false

otherwise.
**Since:** 1.4
**See Also:** setFocusable(boolean)

- setFocusable

```java
public void setFocusable​(boolean focusable)
```

Sets the focusable state of this Component to the specified value. This
value overrides the Component's default focusability.

**Parameters:** focusable

- indicates whether this Component is focusable
**Since:** 1.4
**See Also:** isFocusable()

- setFocusTraversalKeys

```java
public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)
```

Sets the focus traversal keys for a given traversal operation for this
Component.

The default values for a Component's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Component's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Component. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Parameters:** keystrokes

- the Set of AWTKeyStroke for the specified operation
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Component
**Since:** 1.4
**See Also:** getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

- getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Returns the Set of focus traversal keys for a given traversal operation
for this Component. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Component, then this Component's parent's Set is returned. If no Set
has been explicitly defined for any of this Component's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Returns:** the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

- areFocusTraversalKeysSet

```java
public boolean areFocusTraversalKeysSet​(int id)
```

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component. If
this method returns

false

, this Component is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Returns:** true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4

- setFocusTraversalKeysEnabled

```java
public void setFocusTraversalKeysEnabled​(boolean focusTraversalKeysEnabled)
```

Sets whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Parameters:** focusTraversalKeysEnabled

- whether focus traversal keys are
enabled for this Component
**Since:** 1.4
**See Also:** getFocusTraversalKeysEnabled()

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

- getFocusTraversalKeysEnabled

```java
public boolean getFocusTraversalKeysEnabled()
```

Returns whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Returns:** whether focus traversal keys are enabled for this Component
**Since:** 1.4
**See Also:** setFocusTraversalKeysEnabled(boolean)

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

- requestFocus

```java
public void requestFocus()
```

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window. This
component must be displayable, focusable, visible and all of
its ancestors (with the exception of the top-level Window) must
be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event. If this request is denied because this
Component's top-level Window cannot become the focused Window,
the request will be remembered and will be granted when the
Window is later focused by the user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Since:** 1.0
**See Also:** requestFocusInWindow()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocus

```java
public void requestFocus​(
FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level Window)
must be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of method. If this request is denied because this Component's
top-level Window cannot become the focused Window, the request will be
remembered and will be granted when the Window is later focused by the
user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** cause

- the cause why the focus is requested
**Since:** 9
**See Also:** FocusEvent

,

FocusEvent.Cause

,

requestFocusInWindow(FocusEvent.Cause)

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocus

```java
protected boolean requestFocus​(boolean temporary)
```

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocus

```java
protected boolean requestFocus​(boolean temporary,

FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the {FocusEvent}
generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Parameters:** cause

- the cause why the focus is requested
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 9
**See Also:** FocusEvent

,

FocusEvent.Cause

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocusInWindow

```java
public boolean requestFocusInWindow()
```

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocusInWindow

```java
public boolean requestFocusInWindow​(
FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** cause

- the cause why the focus is requested
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 9
**See Also:** requestFocus(FocusEvent.Cause)

,

FocusEvent

,

FocusEvent.Cause

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocusInWindow

```java
protected boolean requestFocusInWindow​(boolean temporary)
```

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- getFocusCycleRootAncestor

```java
public
Container
getFocusCycleRootAncestor()
```

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle. Each focus traversal cycle has only a single
focus cycle root and each Component which is not a Container belongs to
only a single focus traversal cycle. Containers which are focus cycle
roots belong to two cycles: one rooted at the Container itself, and one
rooted at the Container's nearest focus-cycle-root ancestor. For such
Containers, this method will return the Container's nearest focus-cycle-
root ancestor.

**Returns:** this Component's nearest focus-cycle-root ancestor
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- isFocusCycleRoot

```java
public boolean isFocusCycleRoot​(
Container
container)
```

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Component which is not a Container
belongs to only a single focus traversal cycle.

**Parameters:** container

- the Container to be tested
**Returns:** true

if the specified Container is a focus-cycle-
root of this Component;

false

otherwise
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- transferFocus

```java
public void transferFocus()
```

Transfers the focus to the next component, as though this Component were
the focus owner.

**Since:** 1.1
**See Also:** requestFocus()

- nextFocus

```java
@Deprecated

public void nextFocus()
```

Deprecated.

As of JDK version 1.1,
replaced by transferFocus().

- transferFocusBackward

```java
public void transferFocusBackward()
```

Transfers the focus to the previous component, as though this Component
were the focus owner.

**Since:** 1.4
**See Also:** requestFocus()

- transferFocusUpCycle

```java
public void transferFocusUpCycle()
```

Transfers the focus up one focus traversal cycle. Typically, the focus
owner is set to this Component's focus cycle root, and the current focus
cycle root is set to the new focus owner's focus cycle root. If,
however, this Component's focus cycle root is a Window, then the focus
owner is set to the focus cycle root's default Component to focus, and
the current focus cycle root is unchanged.

**Since:** 1.4
**See Also:** requestFocus()

,

Container.isFocusCycleRoot()

,

Container.setFocusCycleRoot(boolean)

- hasFocus

```java
public boolean hasFocus()
```

Returns

true

if this

Component

is the
focus owner. This method is obsolete, and has been replaced by

isFocusOwner()

.

**Returns:** true

if this

Component

is the
focus owner;

false

otherwise
**Since:** 1.2

- isFocusOwner

```java
public boolean isFocusOwner()
```

Returns

true

if this

Component

is the
focus owner.

**Returns:** true

if this

Component

is the
focus owner;

false

otherwise
**Since:** 1.4

- add

```java
public void add​(
PopupMenu
popup)
```

Adds the specified popup menu to the component.

**Parameters:** popup

- the popup menu to be added to the component.
**Throws:** NullPointerException

- if

popup

is

null
**Since:** 1.1
**See Also:** remove(MenuComponent)

- remove

```java
public void remove​(
MenuComponent
popup)
```

Removes the specified popup menu from the component.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** popup

- the popup menu to be removed
**Since:** 1.1
**See Also:** add(PopupMenu)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this component. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:** a string representation of this component's state
**Since:** 1.0

- toString

```java
public
String
toString()
```

Returns a string representation of this component and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this component
**Since:** 1.0

- list

```java
public void list()
```

Prints a listing of this component to the standard system output
stream

System.out

.

**Since:** 1.0
**See Also:** System.out

- list

```java
public void list​(
PrintStream
out)
```

Prints a listing of this component to the specified output
stream.

**Parameters:** out

- a print stream
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0

- list

```java
public void list​(
PrintStream
out,
int indent)
```

Prints out a list, starting at the specified indentation, to the
specified print stream.

**Parameters:** out

- a print stream
**Parameters:** indent

- number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0
**See Also:** PrintStream.println(java.lang.Object)

- list

```java
public void list​(
PrintWriter
out)
```

Prints a listing to the specified print writer.

**Parameters:** out

- the print writer to print to
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1

- list

```java
public void list​(
PrintWriter
out,
int indent)
```

Prints out a list, starting at the specified indentation, to
the specified print writer.

**Parameters:** out

- the print writer to print to
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1
**See Also:** PrintStream.println(java.lang.Object)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Component's preferred size ("preferredSize")
- this Component's minimum size ("minimumSize")
- this Component's maximum size ("maximumSize")
- this Component's name ("name")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:** listener

- the property change listener to be added
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list. This method
should be used to remove PropertyChangeListeners that were registered
for all bound properties of this class.

If listener is null, no exception is thrown and no action is performed.

**Parameters:** listener

- the PropertyChangeListener to be removed
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this component.

**Returns:** all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

PropertyChangeSupport.getPropertyChangeListeners()

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the property change listener to be added
**See Also:** removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener
list for a specific property. This method should be used to remove

PropertyChangeListener

s
that were registered for a specific bound property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:** propertyName

- a valid property name
**Parameters:** listener

- the PropertyChangeListener to be removed
**See Also:** addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners​(
String
propertyName)
```

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:** propertyName

- the property name
**Returns:** all of the

PropertyChangeListener

s associated with
the named property; if no such listeners have been added or
if

propertyName

is

null

, an empty
array is returned
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes for Object properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.4

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Support for reporting bound property changes for integer properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.4

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- setComponentOrientation

```java
public void setComponentOrientation​(
ComponentOrientation
o)
```

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component. Language-sensitive

LayoutManager

and

Component

subclasses will use this property to
determine how to lay out and draw components.

At construction time, a component's orientation is set to

ComponentOrientation.UNKNOWN

,
indicating that it has not been specified
explicitly. The UNKNOWN orientation behaves the same as

ComponentOrientation.LEFT_TO_RIGHT

.

To set the orientation of a single component, use this method.
To set the orientation of an entire component
hierarchy, use

applyComponentOrientation

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** o

- the orientation to be set
**See Also:** ComponentOrientation

,

invalidate()

- getComponentOrientation

```java
public
ComponentOrientation
getComponentOrientation()
```

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

LayoutManager

and

Component

subclasses that wish to respect orientation should call this method to
get the component's orientation before performing layout or drawing.

**Returns:** the orientation to order the elements or text
**See Also:** ComponentOrientation

- applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
orientation)
```

Sets the

ComponentOrientation

property of this component
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** orientation

- the new component orientation of this component and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** setComponentOrientation(java.awt.ComponentOrientation)

,

getComponentOrientation()

,

invalidate()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated
with this

Component

.
The method implemented by this base
class returns null. Classes that extend

Component

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:** the

AccessibleContext

of this

Component
**Since:** 1.3

- setMixingCutoutShape

```java
public void setMixingCutoutShape​(
Shape
shape)
```

Sets a 'mixing-cutout' shape for this lightweight component.

This method is used exclusively for the purposes of the
Heavyweight/Lightweight Components Mixing feature and will
have no effect if applied to a heavyweight component.

By default a lightweight component is treated as an opaque rectangle for
the purposes of the Heavyweight/Lightweight Components Mixing feature.
This method enables developers to set an arbitrary shape to be cut out
from heavyweight components positioned underneath the lightweight
component in the z-order.

The

shape

argument may have the following values:

- null

- reverts the default cutout shape (the rectangle equal
to the component's

getBounds()

)

empty-shape

- does not cut out anything from heavyweight
components. This makes this lightweight component effectively
transparent. Note that descendants of the lightweight component still
affect the shapes of heavyweight components. An example of an

empty-shape

is

new Rectangle()

.

non-empty-shape

- the given shape will be cut out from
heavyweight components.

The most common example when the 'mixing-cutout' shape is needed is a
glass pane component. The

JRootPane.setGlassPane(java.awt.Component)

method
automatically sets the

empty-shape

as the 'mixing-cutout' shape
for the given glass pane component. If a developer needs some other
'mixing-cutout' shape for the glass pane (which is rare), this must be
changed manually after installing the glass pane to the root pane.

**Parameters:** shape

- the new 'mixing-cutout' shape
**Since:** 9

Field Detail

- TOP_ALIGNMENT

```java
public static final float TOP_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY()

.
Specifies an alignment to the top of the component.

**See Also:** getAlignmentY()

,

Constant Field Values

- CENTER_ALIGNMENT

```java
public static final float CENTER_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

. Specifies an alignment to
the center of the component

**See Also:** getAlignmentX()

,

getAlignmentY()

,

Constant Field Values

- BOTTOM_ALIGNMENT

```java
public static final float BOTTOM_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY

.
Specifies an alignment to the bottom of the component.

**See Also:** getAlignmentY()

,

Constant Field Values

- LEFT_ALIGNMENT

```java
public static final float LEFT_ALIGNMENT
```

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the left side of the component.

**See Also:** getAlignmentX()

,

Constant Field Values

- RIGHT_ALIGNMENT

```java
public static final float RIGHT_ALIGNMENT
```

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the right side of the component.

**See Also:** getAlignmentX()

,

Constant Field Values

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The

AccessibleContext

associated with this

Component

.

---

#### Field Detail

TOP_ALIGNMENT

```java
public static final float TOP_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY()

.
Specifies an alignment to the top of the component.

**See Also:** getAlignmentY()

,

Constant Field Values

---

#### TOP_ALIGNMENT

public static final float TOP_ALIGNMENT

Ease-of-use constant for

getAlignmentY()

.
Specifies an alignment to the top of the component.

CENTER_ALIGNMENT

```java
public static final float CENTER_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

. Specifies an alignment to
the center of the component

**See Also:** getAlignmentX()

,

getAlignmentY()

,

Constant Field Values

---

#### CENTER_ALIGNMENT

public static final float CENTER_ALIGNMENT

Ease-of-use constant for

getAlignmentY

and

getAlignmentX

. Specifies an alignment to
the center of the component

BOTTOM_ALIGNMENT

```java
public static final float BOTTOM_ALIGNMENT
```

Ease-of-use constant for

getAlignmentY

.
Specifies an alignment to the bottom of the component.

**See Also:** getAlignmentY()

,

Constant Field Values

---

#### BOTTOM_ALIGNMENT

public static final float BOTTOM_ALIGNMENT

Ease-of-use constant for

getAlignmentY

.
Specifies an alignment to the bottom of the component.

LEFT_ALIGNMENT

```java
public static final float LEFT_ALIGNMENT
```

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the left side of the component.

**See Also:** getAlignmentX()

,

Constant Field Values

---

#### LEFT_ALIGNMENT

public static final float LEFT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the left side of the component.

RIGHT_ALIGNMENT

```java
public static final float RIGHT_ALIGNMENT
```

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the right side of the component.

**See Also:** getAlignmentX()

,

Constant Field Values

---

#### RIGHT_ALIGNMENT

public static final float RIGHT_ALIGNMENT

Ease-of-use constant for

getAlignmentX

.
Specifies an alignment to the right side of the component.

accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The

AccessibleContext

associated with this

Component

.

---

#### accessibleContext

protected

AccessibleContext

accessibleContext

The

AccessibleContext

associated with this

Component

.

Constructor Detail

- Component

```java
protected Component()
```

Constructs a new component. Class

Component

can be
extended directly to create a lightweight component that does not
utilize an opaque native window. A lightweight component must be
hosted by a native container somewhere higher up in the component
tree (for example, by a

Frame

object).

---

#### Constructor Detail

Component

```java
protected Component()
```

Constructs a new component. Class

Component

can be
extended directly to create a lightweight component that does not
utilize an opaque native window. A lightweight component must be
hosted by a native container somewhere higher up in the component
tree (for example, by a

Frame

object).

---

#### Component

protected Component()

Constructs a new component. Class

Component

can be
extended directly to create a lightweight component that does not
utilize an opaque native window. A lightweight component must be
hosted by a native container somewhere higher up in the component
tree (for example, by a

Frame

object).

Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the component.

**Returns:** this component's name
**Since:** 1.1
**See Also:** setName(java.lang.String)

- setName

```java
public void setName​(
String
name)
```

Sets the name of the component to the specified string.

**Parameters:** name

- the string that is to be this
component's name
**Since:** 1.1
**See Also:** getName()

- getParent

```java
public
Container
getParent()
```

Gets the parent of this component.

**Returns:** the parent container of this component
**Since:** 1.0

- setDropTarget

```java
public void setDropTarget​(
DropTarget
dt)
```

Associate a

DropTarget

with this component.
The

Component

will receive drops only if it
is enabled.

**Parameters:** dt

- The DropTarget
**See Also:** isEnabled()

- getDropTarget

```java
public
DropTarget
getDropTarget()
```

Gets the

DropTarget

associated with this

Component

.

**Returns:** the drop target

- getGraphicsConfiguration

```java
public
GraphicsConfiguration
getGraphicsConfiguration()
```

Gets the

GraphicsConfiguration

associated with this

Component

.
If the

Component

has not been assigned a specific

GraphicsConfiguration

,
the

GraphicsConfiguration

of the

Component

object's top-level container is
returned.
If the

Component

has been created, but not yet added
to a

Container

, this method returns

null

.

**Returns:** the

GraphicsConfiguration

used by this

Component

or

null
**Since:** 1.3

- getTreeLock

```java
public final
Object
getTreeLock()
```

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:** this component's locking object

- getToolkit

```java
public
Toolkit
getToolkit()
```

Gets the toolkit of this component. Note that
the frame that contains a component controls which
toolkit is used by that component. Therefore if the component
is moved from one frame to another, the toolkit it uses may change.

**Returns:** the toolkit of this component
**Since:** 1.0

- isValid

```java
public boolean isValid()
```

Determines whether this component is valid. A component is valid
when it is correctly sized and positioned within its parent
container and all its children are also valid.
In order to account for peers' size requirements, components are invalidated
before they are first shown on the screen. By the time the parent container
is fully realized, all its components will be valid.

**Returns:** true

if the component is valid,

false

otherwise
**Since:** 1.0
**See Also:** validate()

,

invalidate()

- isDisplayable

```java
public boolean isDisplayable()
```

Determines whether this component is displayable. A component is
displayable when it is connected to a native screen resource.

A component is made displayable either when it is added to
a displayable containment hierarchy or when its containment
hierarchy is made displayable.
A containment hierarchy is made displayable when its ancestor
window is either packed or made visible.

A component is made undisplayable either when it is removed from
a displayable containment hierarchy or when its containment hierarchy
is made undisplayable. A containment hierarchy is made
undisplayable when its ancestor window is disposed.

**Returns:** true

if the component is displayable,

false

otherwise
**Since:** 1.2
**See Also:** Container.add(Component)

,

Window.pack()

,

Window.show()

,

Container.remove(Component)

,

Window.dispose()

- isVisible

```java
public boolean isVisible()
```

Determines whether this component should be visible when its
parent is visible. Components are
initially visible, with the exception of top level components such
as

Frame

objects.

**Returns:** true

if the component is visible,

false

otherwise
**Since:** 1.0
**See Also:** setVisible(boolean)

- getMousePosition

```java
public
Point
getMousePosition()
throws
HeadlessException
```

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.
If the

Component

is not showing on the screen, this method
returns

null

even if the mouse pointer is above the area
where the

Component

would be displayed.
If the

Component

is partially or fully obscured by other

Component

s or native windows, this method returns a non-null
value only if the mouse pointer is located above the unobscured part of the

Component

.

For

Container

s it returns a non-null value if the mouse is
above the

Container

itself or above any of its descendants.
Use

Container.getMousePosition(boolean)

if you need to exclude children.

Sometimes the exact mouse coordinates are not important, and the only thing
that matters is whether a specific

Component

is under the mouse
pointer. If the return value of this method is

null

, mouse
pointer is not directly above the

Component

.

**Returns:** mouse coordinates relative to this

Component

, or null
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** isShowing()

,

Container.getMousePosition(boolean)

- isShowing

```java
public boolean isShowing()
```

Determines whether this component is showing on screen. This means
that the component must be visible, and it must be in a container
that is visible and showing.

Note:

sometimes there is no way to detect whether the

Component

is actually visible to the user. This can happen when:

- the component has been added to a visible

ScrollPane

but
the

Component

is not currently in the scroll pane's view port.

the

Component

is obscured by another

Component

or

Container

.

**Returns:** true

if the component is showing,

false

otherwise
**Since:** 1.0
**See Also:** setVisible(boolean)

- isEnabled

```java
public boolean isEnabled()
```

Determines whether this component is enabled. An enabled component
can respond to user input and generate events. Components are
enabled initially by default. A component may be enabled or disabled by
calling its

setEnabled

method.

**Returns:** true

if the component is enabled,

false

otherwise
**Since:** 1.0
**See Also:** setEnabled(boolean)

- setEnabled

```java
public void setEnabled​(boolean b)
```

Enables or disables this component, depending on the value of the
parameter

b

. An enabled component can respond to user
input and generate events. Components are enabled initially by default.

Note: Disabling a lightweight component does not prevent it from
receiving MouseEvents.

Note: Disabling a heavyweight container prevents all components
in this container from receiving any input events. But disabling a
lightweight container affects only this container.

**Parameters:** b

- If

true

, this component is
enabled; otherwise this component is disabled
**Since:** 1.1
**See Also:** isEnabled()

,

isLightweight()

- enable

```java
@Deprecated

public void enable()
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

- enable

```java
@Deprecated

public void enable​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

Enables or disables this component.

**Parameters:** b

-

true

to enable this component;
otherwise

false

- disable

```java
@Deprecated

public void disable()
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

- isDoubleBuffered

```java
public boolean isDoubleBuffered()
```

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later. Component
subclasses that support double buffering should override this
method to return true if double buffering is enabled.

**Returns:** false by default

- enableInputMethods

```java
public void enableInputMethods​(boolean enable)
```

Enables or disables input method support for this component. If input
method support is enabled and the component also processes key events,
incoming events are offered to
the current input method and will only be processed by the component or
dispatched to its listeners if the input method does not consume them.
By default, input method support is enabled.

**Parameters:** enable

- true to enable, false to disable
**Since:** 1.2
**See Also:** processKeyEvent(java.awt.event.KeyEvent)

- setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this component depending on the value of parameter

b

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** b

- if

true

, shows this component;
otherwise, hides this component
**Since:** 1.1
**See Also:** isVisible()

,

invalidate()

- show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

- show

```java
@Deprecated

public void show​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

Makes this component visible or invisible.

**Parameters:** b

-

true

to make this component visible;
otherwise

false

- hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

- getForeground

```java
public
Color
getForeground()
```

Gets the foreground color of this component.

**Returns:** this component's foreground color; if this component does
not have a foreground color, the foreground color of its parent
is returned
**Since:** 1.0
**See Also:** setForeground(java.awt.Color)

- setForeground

```java
public void setForeground​(
Color
c)
```

Sets the foreground color of this component.

**Parameters:** c

- the color to become this component's
foreground color; if this parameter is

null

then this component will inherit
the foreground color of its parent
**Since:** 1.0
**See Also:** getForeground()

- isForegroundSet

```java
public boolean isForegroundSet()
```

Returns whether the foreground color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its foreground color from an ancestor.

**Returns:** true

if the foreground color has been explicitly
set for this Component;

false

otherwise.
**Since:** 1.4

- getBackground

```java
public
Color
getBackground()
```

Gets the background color of this component.

**Returns:** this component's background color; if this component does
not have a background color,
the background color of its parent is returned
**Since:** 1.0
**See Also:** setBackground(java.awt.Color)

- setBackground

```java
public void setBackground​(
Color
c)
```

Sets the background color of this component.

The background color affects each component differently and the
parts of the component that are affected by the background color
may differ between operating systems.

**Parameters:** c

- the color to become this component's color;
if this parameter is

null

, then this
component will inherit the background color of its parent
**Since:** 1.0
**See Also:** getBackground()

- isBackgroundSet

```java
public boolean isBackgroundSet()
```

Returns whether the background color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its background color from an ancestor.

**Returns:** true

if the background color has been explicitly
set for this Component;

false

otherwise.
**Since:** 1.4

- getFont

```java
public
Font
getFont()
```

Gets the font of this component.

**Specified by:** getFont

in interface

MenuContainer
**Returns:** this component's font; if a font has not been set
for this component, the font of its parent is returned
**Since:** 1.0
**See Also:** setFont(java.awt.Font)

- setFont

```java
public void setFont​(
Font
f)
```

Sets the font of this component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** f

- the font to become this component's font;
if this parameter is

null

then this
component will inherit the font of its parent
**Since:** 1.0
**See Also:** getFont()

,

invalidate()

- isFontSet

```java
public boolean isFontSet()
```

Returns whether the font has been explicitly set for this Component. If
this method returns

false

, this Component is inheriting its
font from an ancestor.

**Returns:** true

if the font has been explicitly set for this
Component;

false

otherwise.
**Since:** 1.4

- getLocale

```java
public
Locale
getLocale()
```

Gets the locale of this component.

**Returns:** this component's locale; if this component does not
have a locale, the locale of its parent is returned
**Throws:** IllegalComponentStateException

- if the

Component

does not have its own locale and has not yet been added to
a containment hierarchy such that the locale can be determined
from the containing parent
**Since:** 1.1
**See Also:** setLocale(java.util.Locale)

- setLocale

```java
public void setLocale​(
Locale
l)
```

Sets the locale of this component. This is a bound property.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** l

- the locale to become this component's locale
**Since:** 1.1
**See Also:** getLocale()

,

invalidate()

- getColorModel

```java
public
ColorModel
getColorModel()
```

Gets the instance of

ColorModel

used to display
the component on the output device.

**Returns:** the color model used by this component
**Since:** 1.0
**See Also:** ColorModel

,

ComponentPeer.getColorModel()

,

Toolkit.getColorModel()

- getLocation

```java
public
Point
getLocation()
```

Gets the location of this component in the form of a
point specifying the component's top-left corner.
The location will be relative to the parent's coordinate space.

Due to the asynchronous nature of native event handling, this
method can return outdated values (for instance, after several calls
of

setLocation()

in rapid succession). For this
reason, the recommended method of obtaining a component's position is
within

java.awt.event.ComponentListener.componentMoved()

,
which is called after the operating system has finished moving the
component.

**Returns:** an instance of

Point

representing
the top-left corner of the component's bounds in
the coordinate space of the component's parent
**Since:** 1.1
**See Also:** setLocation(int, int)

,

getLocationOnScreen()

- getLocationOnScreen

```java
public
Point
getLocationOnScreen()
```

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

**Returns:** an instance of

Point

representing
the top-left corner of the component's bounds in the
coordinate space of the screen
**Throws:** IllegalComponentStateException

- if the
component is not showing on the screen
**See Also:** setLocation(int, int)

,

getLocation()

- location

```java
@Deprecated

public
Point
location()
```

Deprecated.

As of JDK version 1.1,
replaced by

getLocation()

.

Returns the location of this component's top left corner.

**Returns:** the location of this component's top left corner

- setLocation

```java
public void setLocation​(int x,
int y)
```

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Since:** 1.1
**See Also:** getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

- move

```java
@Deprecated

public void move​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by

setLocation(int, int)

.

Moves this component to a new location.

**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space

- setLocation

```java
public void setLocation​(
Point
p)
```

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent
**Since:** 1.1
**See Also:** getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

- getSize

```java
public
Dimension
getSize()
```

Returns the size of this component in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this component's height, and the

width

field of the

Dimension

object contains
this component's width.

**Returns:** a

Dimension

object that indicates the
size of this component
**Since:** 1.1
**See Also:** setSize(int, int)

- size

```java
@Deprecated

public
Dimension
size()
```

Deprecated.

As of JDK version 1.1,
replaced by

getSize()

.

Returns the size of this component in the form of a

Dimension

object.

**Returns:** the

Dimension

object that indicates the
size of this component

- setSize

```java
public void setSize​(int width,
int height)
```

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** width

- the new width of this component in pixels
**Parameters:** height

- the new height of this component in pixels
**Since:** 1.1
**See Also:** getSize()

,

setBounds(int, int, int, int)

,

invalidate()

- resize

```java
@Deprecated

public void resize​(int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setSize(int, int)

.

Resizes this component.

**Parameters:** width

- the new width of the component
**Parameters:** height

- the new height of the component

- setSize

```java
public void setSize​(
Dimension
d)
```

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** d

- the dimension specifying the new size
of this component
**Throws:** NullPointerException

- if

d

is

null
**Since:** 1.1
**See Also:** setSize(int, int)

,

setBounds(int, int, int, int)

,

invalidate()

- resize

```java
@Deprecated

public void resize​(
Dimension
d)
```

Deprecated.

As of JDK version 1.1,
replaced by

setSize(Dimension)

.

Resizes this component so that it has width

d.width

and height

d.height

.

**Parameters:** d

- the new size of this component

- getBounds

```java
public
Rectangle
getBounds()
```

Gets the bounds of this component in the form of a

Rectangle

object. The bounds specify this
component's width, height, and location relative to
its parent.

**Returns:** a rectangle indicating this component's bounds
**See Also:** setBounds(int, int, int, int)

,

getLocation()

,

getSize()

- bounds

```java
@Deprecated

public
Rectangle
bounds()
```

Deprecated.

As of JDK version 1.1,
replaced by

getBounds()

.

Returns the bounding rectangle of this component.

**Returns:** the bounding rectangle for this component

- setBounds

```java
public void setBounds​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** x

- the new

x

-coordinate of this component
**Parameters:** y

- the new

y

-coordinate of this component
**Parameters:** width

- the new

width

of this component
**Parameters:** height

- the new

height

of this
component
**Since:** 1.1
**See Also:** getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

- reshape

```java
@Deprecated

public void reshape​(int x,
int y,
int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Reshapes the bounding rectangle for this component.

**Parameters:** x

- the

x

coordinate of the upper left corner of the rectangle
**Parameters:** y

- the

y

coordinate of the upper left corner of the rectangle
**Parameters:** width

- the width of the rectangle
**Parameters:** height

- the height of the rectangle

- setBounds

```java
public void setBounds​(
Rectangle
r)
```

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** r

- the new bounding rectangle for this component
**Throws:** NullPointerException

- if

r

is

null
**Since:** 1.1
**See Also:** getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

- getX

```java
public int getX()
```

Returns the current x coordinate of the components origin.
This method is preferable to writing

component.getBounds().x

,
or

component.getLocation().x

because it doesn't
cause any heap allocations.

**Returns:** the current x coordinate of the components origin
**Since:** 1.2

- getY

```java
public int getY()
```

Returns the current y coordinate of the components origin.
This method is preferable to writing

component.getBounds().y

,
or

component.getLocation().y

because it
doesn't cause any heap allocations.

**Returns:** the current y coordinate of the components origin
**Since:** 1.2

- getWidth

```java
public int getWidth()
```

Returns the current width of this component.
This method is preferable to writing

component.getBounds().width

,
or

component.getSize().width

because it
doesn't cause any heap allocations.

**Returns:** the current width of this component
**Since:** 1.2

- getHeight

```java
public int getHeight()
```

Returns the current height of this component.
This method is preferable to writing

component.getBounds().height

,
or

component.getSize().height

because it
doesn't cause any heap allocations.

**Returns:** the current height of this component
**Since:** 1.2

- getBounds

```java
public
Rectangle
getBounds​(
Rectangle
rv)
```

Stores the bounds of this component into "return value"

rv

and
return

rv

. If rv is

null

a new

Rectangle

is allocated.
This version of

getBounds

is useful if the caller
wants to avoid allocating a new

Rectangle

object
on the heap.

**Parameters:** rv

- the return value, modified to the components bounds
**Returns:** rv

- getSize

```java
public
Dimension
getSize​(
Dimension
rv)
```

Stores the width/height of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Dimension

object is allocated. This version of

getSize

is useful if the caller wants to avoid
allocating a new

Dimension

object on the heap.

**Parameters:** rv

- the return value, modified to the components size
**Returns:** rv

- getLocation

```java
public
Point
getLocation​(
Point
rv)
```

Stores the x,y origin of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Point

is allocated.
This version of

getLocation

is useful if the
caller wants to avoid allocating a new

Point

object on the heap.

**Parameters:** rv

- the return value, modified to the components location
**Returns:** rv

- isOpaque

```java
public boolean isOpaque()
```

Returns true if this component is completely opaque, returns
false by default.

An opaque component paints every pixel within its
rectangular region. A non-opaque component paints only some of
its pixels, allowing the pixels underneath it to "show through".
A component that does not fully paint its pixels therefore
provides a degree of transparency.

Subclasses that guarantee to always completely paint their
contents should override this method and return true.

**Returns:** true if this component is completely opaque
**Since:** 1.2
**See Also:** isLightweight()

- isLightweight

```java
public boolean isLightweight()
```

A lightweight component doesn't have a native toolkit peer.
Subclasses of

Component

and

Container

,
other than the ones defined in this package like

Button

or

Scrollbar

, are lightweight.
All of the Swing components are lightweights.

This method will always return

false

if this component
is not displayable because it is impossible to determine the
weight of an undisplayable component.

**Returns:** true if this component has a lightweight peer; false if
it has a native peer or no peer
**Since:** 1.2
**See Also:** isDisplayable()

- setPreferredSize

```java
public void setPreferredSize​(
Dimension
preferredSize)
```

Sets the preferred size of this component to a constant
value. Subsequent calls to

getPreferredSize

will always
return this value. Setting the preferred size to

null

restores the default behavior.

**Parameters:** preferredSize

- The new preferred size, or null
**Since:** 1.5
**See Also:** getPreferredSize()

,

isPreferredSizeSet()

- isPreferredSizeSet

```java
public boolean isPreferredSizeSet()
```

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

**Returns:** true if

setPreferredSize

has been invoked
with a non-null value.
**Since:** 1.5

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Gets the preferred size of this component.

**Returns:** a dimension object indicating this component's preferred size
**See Also:** getMinimumSize()

,

LayoutManager

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Returns the component's preferred size.

**Returns:** the component's preferred size

- setMinimumSize

```java
public void setMinimumSize​(
Dimension
minimumSize)
```

Sets the minimum size of this component to a constant
value. Subsequent calls to

getMinimumSize

will always
return this value. Setting the minimum size to

null

restores the default behavior.

**Parameters:** minimumSize

- the new minimum size of this component
**Since:** 1.5
**See Also:** getMinimumSize()

,

isMinimumSizeSet()

- isMinimumSizeSet

```java
public boolean isMinimumSizeSet()
```

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

**Returns:** true if

setMinimumSize

has been invoked with a
non-null value.
**Since:** 1.5

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Gets the minimum size of this component.

**Returns:** a dimension object indicating this component's minimum size
**See Also:** getPreferredSize()

,

LayoutManager

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Returns the minimum size of this component.

**Returns:** the minimum size of this component

- setMaximumSize

```java
public void setMaximumSize​(
Dimension
maximumSize)
```

Sets the maximum size of this component to a constant
value. Subsequent calls to

getMaximumSize

will always
return this value. Setting the maximum size to

null

restores the default behavior.

**Parameters:** maximumSize

- a

Dimension

containing the
desired maximum allowable size
**Since:** 1.5
**See Also:** getMaximumSize()

,

isMaximumSizeSet()

- isMaximumSizeSet

```java
public boolean isMaximumSizeSet()
```

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

**Returns:** true if

maximumSize

is non-

null

,
false otherwise
**Since:** 1.5

- getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Gets the maximum size of this component.

**Returns:** a dimension object indicating this component's maximum size
**See Also:** getMinimumSize()

,

getPreferredSize()

,

LayoutManager

- getAlignmentX

```java
public float getAlignmentX()
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:** the horizontal alignment of this component

- getAlignmentY

```java
public float getAlignmentY()
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:** the vertical alignment of this component

- getBaseline

```java
public int getBaseline​(int width,
int height)
```

Returns the baseline. The baseline is measured from the top of
the component. This method is primarily meant for

LayoutManager

s to align components along their
baseline. A return value less than 0 indicates this component
does not have a reasonable baseline and that

LayoutManager

s should not align this component on
its baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** getBaselineResizeBehavior()

,

FontMetrics

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior()
```

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

. Subclasses that have a
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Returns:** an enum indicating how the baseline changes as the component
size changes
**Since:** 1.6
**See Also:** getBaseline(int, int)

- doLayout

```java
public void doLayout()
```

Prompts the layout manager to lay out this component. This is
usually called when the component (more specifically, container)
is validated.

**See Also:** validate()

,

LayoutManager

- layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

- validate

```java
public void validate()
```

Validates this component.

The meaning of the term

validating

is defined by the ancestors of
this class. See

Container.validate()

for more details.

**Since:** 1.0
**See Also:** invalidate()

,

doLayout()

,

LayoutManager

,

Container.validate()

- invalidate

```java
public void invalidate()
```

Invalidates this component and its ancestors.

By default, all the ancestors of the component up to the top-most
container of the hierarchy are marked invalid. If the

java.awt.smartInvalidate

system property is set to

true

,
invalidation stops on the nearest validate root of this component.
Marking a container

invalid

indicates that the container needs to
be laid out.

This method is called automatically when any layout-related information
changes (e.g. setting the bounds of the component, or adding the
component to a container).

This method might be called often, so it should work fast.

**Since:** 1.0
**See Also:** validate()

,

doLayout()

,

LayoutManager

,

Container.isValidateRoot()

- revalidate

```java
public void revalidate()
```

Revalidates the component hierarchy up to the nearest validate root.

This method first invalidates the component hierarchy starting from this
component up to the nearest validate root. Afterwards, the component
hierarchy is validated starting from the nearest validate root.

This is a convenience method supposed to help application developers
avoid looking for validate roots manually. Basically, it's equivalent to
first calling the

invalidate()

method on this component, and
then calling the

validate()

method on the nearest validate
root.

**Since:** 1.7
**See Also:** Container.isValidateRoot()

- getGraphics

```java
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
font)
```

Gets the font metrics for the specified font.
Warning: Since Font metrics are affected by the

FontRenderContext

and
this method does not provide one, it can return only metrics for
the default render context which may not match that used when
rendering on the Component if

Graphics2D

functionality is being
used. Instead metrics can be obtained at rendering time by calling

Graphics.getFontMetrics()

or text measurement APIs on the

Font

class.

**Parameters:** font

- the font for which font metrics is to be
obtained
**Returns:** the font metrics for

font
**Since:** 1.0
**See Also:** getFont()

,

ComponentPeer.getFontMetrics(Font)

,

Toolkit.getFontMetrics(Font)

- setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Parameters:** cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent
**Since:** 1.1
**See Also:** isEnabled()

,

isShowing()

,

getCursor()

,

contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

- getCursor

```java
public
Cursor
getCursor()
```

Gets the cursor set in the component. If the component does
not have a cursor set, the cursor of its parent is returned.
If no cursor is set in the entire hierarchy,

Cursor.DEFAULT_CURSOR

is returned.

**Returns:** the cursor for this component
**Since:** 1.1
**See Also:** setCursor(java.awt.Cursor)

- isCursorSet

```java
public boolean isCursorSet()
```

Returns whether the cursor has been explicitly set for this Component.
If this method returns

false

, this Component is inheriting
its cursor from an ancestor.

**Returns:** true

if the cursor has been explicitly set for this
Component;

false

otherwise.
**Since:** 1.4

- paint

```java
public void paint​(
Graphics
g)
```

Paints this component.

This method is called when the contents of the component should
be painted; such as when the component is first being shown or
is damaged and in need of repair. The clip rectangle in the

Graphics

parameter is set to the area
which needs to be painted.
Subclasses of

Component

that override this
method need not call

super.paint(g)

.

For performance reasons,

Component

s with zero width
or height aren't considered to need painting when they are first shown,
and also aren't considered to need repair.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** g

- the graphics context to use for painting
**Since:** 1.0
**See Also:** update(java.awt.Graphics)

- update

```java
public void update​(
Graphics
g)
```

Updates this component.

If this component is not a lightweight component, the
AWT calls the

update

method in response to
a call to

repaint

. You can assume that
the background is not cleared.

The

update

method of

Component

calls this component's

paint

method to redraw
this component. This method is commonly overridden by subclasses
which need to do additional work in response to a call to

repaint

.
Subclasses of Component that override this method should either
call

super.update(g)

, or call

paint(g)

directly from their

update

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** g

- the specified context to use for updating
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

,

repaint()

- paintAll

```java
public void paintAll​(
Graphics
g)
```

Paints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for painting
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

- repaint

```java
public void repaint()
```

Repaints this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method as soon as possible. Otherwise, this method causes
a call to this component's

update

method as soon
as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Since:** 1.0
**See Also:** update(Graphics)

- repaint

```java
public void repaint​(long tm)
```

Repaints the component. If this component is a lightweight
component, this results in a call to

paint

within

tm

milliseconds.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** tm

- maximum time in milliseconds before update
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

,

update(Graphics)

- repaint

```java
public void repaint​(int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method
as soon as possible. Otherwise, this method causes a call to
this component's

update

method as soon as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.0
**See Also:** update(Graphics)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

tm

milliseconds.

If this component is a lightweight component, this method causes
a call to this component's

paint

method.
Otherwise, this method causes a call to this component's

update

method.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** tm

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.0
**See Also:** update(Graphics)

- print

```java
public void print​(
Graphics
g)
```

Prints this component. Applications should override this method
for components that must do special processing before being
printed or should be printed differently than they are painted.

The default implementation of this method calls the

paint

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for printing
**Since:** 1.0
**See Also:** paint(Graphics)

- printAll

```java
public void printAll​(
Graphics
g)
```

Prints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for printing
**Since:** 1.0
**See Also:** print(Graphics)

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:** imageUpdate

in interface

ImageObserver
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**Since:** 1.0
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- createImage

```java
public
Image
createImage​(
ImageProducer
producer)
```

Creates an image from the specified image producer.

**Parameters:** producer

- the image producer
**Returns:** the image produced
**Since:** 1.0

- createImage

```java
public
Image
createImage​(int width,
int height)
```

Creates an off-screen drawable image to be used for double buffering.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Returns:** an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.0
**See Also:** isDisplayable()

,

GraphicsEnvironment.isHeadless()

- createVolatileImage

```java
public
VolatileImage
createVolatileImage​(int width,
int height)
```

Creates a volatile off-screen drawable image to be used for double
buffering.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Returns:** an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** VolatileImage

,

isDisplayable()

,

GraphicsEnvironment.isHeadless()

- createVolatileImage

```java
public
VolatileImage
createVolatileImage​(int width,
int height,

ImageCapabilities
caps)
throws
AWTException
```

Creates a volatile off-screen drawable image, with the given
capabilities. The contents of this image may be lost at any time due to
operating system issues, so the image must be managed via the

VolatileImage

interface.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Parameters:** caps

- the image capabilities
**Returns:** a VolatileImage object, which can be used to manage surface
contents loss and capabilities. The

null

value if the
component is not displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Throws:** AWTException

- if an image with the specified capabilities cannot
be created
**Since:** 1.4
**See Also:** VolatileImage

- prepareImage

```java
public boolean prepareImage​(
Image
image,

ImageObserver
observer)
```

Prepares an image for rendering on this component. The image
data is downloaded asynchronously in another thread and the
appropriate screen representation of the image is generated.

**Parameters:** image

- the

Image

for which to
prepare a screen representation
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** true

if the image has already been fully
prepared;

false

otherwise
**Since:** 1.0

- prepareImage

```java
public boolean prepareImage​(
Image
image,
int width,
int height,

ImageObserver
observer)
```

Prepares an image for rendering on this component at the
specified width and height.

The image data is downloaded asynchronously in another thread,
and an appropriately scaled screen representation of the image is
generated.

**Parameters:** image

- the instance of

Image

for which to prepare a screen representation
**Parameters:** width

- the width of the desired screen representation
**Parameters:** height

- the height of the desired screen representation
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** true

if the image has already been fully
prepared;

false

otherwise
**Since:** 1.0
**See Also:** ImageObserver

- checkImage

```java
public int checkImage​(
Image
image,

ImageObserver
observer)
```

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:** image

- the

Image

object whose status
is being checked
**Parameters:** observer

- the

ImageObserver

object to be notified as the image is being prepared
**Returns:** the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available
**Since:** 1.0
**See Also:** prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

- checkImage

```java
public int checkImage​(
Image
image,
int width,
int height,

ImageObserver
observer)
```

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

The

checkImage

method of

Component

calls its peer's

checkImage

method to calculate
the flags. If this component does not yet have a peer, the
component's toolkit's

checkImage

method is called
instead.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:** image

- the

Image

object whose status
is being checked
**Parameters:** width

- the width of the scaled version
whose status is to be checked
**Parameters:** height

- the height of the scaled version
whose status is to be checked
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available
**Since:** 1.0
**See Also:** prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

- setIgnoreRepaint

```java
public void setIgnoreRepaint​(boolean ignoreRepaint)
```

Sets whether or not paint messages received from the operating system
should be ignored. This does not affect paint events generated in
software by the AWT, unless they are an immediate response to an
OS-level paint message.

This is useful, for example, if running under full-screen mode and
better performance is desired, or if page-flipping is used as the
buffer strategy.

**Parameters:** ignoreRepaint

-

true

if the paint messages from the OS
should be ignored; otherwise

false
**Since:** 1.4
**See Also:** getIgnoreRepaint()

,

Canvas.createBufferStrategy(int)

,

Window.createBufferStrategy(int)

,

BufferStrategy

,

GraphicsDevice.setFullScreenWindow(java.awt.Window)

- getIgnoreRepaint

```java
public boolean getIgnoreRepaint()
```

**Returns:** whether or not paint messages received from the operating system
should be ignored.
**Since:** 1.4
**See Also:** setIgnoreRepaint(boolean)

- contains

```java
public boolean contains​(int x,
int y)
```

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the point is within the component;
otherwise

false
**Since:** 1.1
**See Also:** getComponentAt(int, int)

- inside

```java
@Deprecated

public boolean inside​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by contains(int, int).

Checks whether the point is inside of this component.

**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the point is within the component;
otherwise

false

- contains

```java
public boolean contains​(
Point
p)
```

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

**Parameters:** p

- the point
**Returns:** true

if the point is within the component;
otherwise

false
**Throws:** NullPointerException

- if

p

is

null
**Since:** 1.1
**See Also:** getComponentAt(Point)

- getComponentAt

```java
public
Component
getComponentAt​(int x,
int y)
```

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component. This method only
looks one level deep. If the point (

x

,

y

) is
inside a subcomponent that itself has subcomponents, it does not
go looking down the subcomponent tree.

The

locate

method of

Component

simply
returns the component itself if the (

x

,

y

)
coordinate location is inside its bounding box, and

null

otherwise.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** the component or subcomponent that contains the
(

x

,

y

) location;

null

if the location
is outside this component
**Since:** 1.0
**See Also:** contains(int, int)

- locate

```java
@Deprecated

public
Component
locate​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by getComponentAt(int, int).

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

**Parameters:** x

- the

x

coordinate to search for components at
**Parameters:** y

- the

y

coordinate to search for components at
**Returns:** the component at the specified location or

null

- getComponentAt

```java
public
Component
getComponentAt​(
Point
p)
```

Returns the component or subcomponent that contains the
specified point.

**Parameters:** p

- the point
**Returns:** the component at the specified location or

null
**Since:** 1.1
**See Also:** contains(int, int)

- deliverEvent

```java
@Deprecated

public void deliverEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

.

**Parameters:** e

- the event to deliver

- dispatchEvent

```java
public final void dispatchEvent​(
AWTEvent
e)
```

Dispatches an event to this component or one of its sub components.
Calls

processEvent

before returning for 1.1-style
events which have been enabled for the

Component

.

**Parameters:** e

- the event

- postEvent

```java
@Deprecated

public boolean postEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by dispatchEvent(AWTEvent).

Description copied from interface:

MenuContainer

Posts an event to the listeners.

**Specified by:** postEvent

in interface

MenuContainer
**Parameters:** e

- the event to dispatch
**Returns:** the results of posting the event

- addComponentListener

```java
public void addComponentListener​(
ComponentListener
l)
```

Adds the specified component listener to receive component events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the component listener
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

removeComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

- removeComponentListener

```java
public void removeComponentListener​(
ComponentListener
l)
```

Removes the specified component listener so that it no longer
receives component events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the component listener
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

- getComponentListeners

```java
public
ComponentListener
[] getComponentListeners()
```

Returns an array of all the component listeners
registered on this component.

**Returns:** all

ComponentListener

s of this component
or an empty array if no component
listeners are currently registered
**Since:** 1.4
**See Also:** addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

- addFocusListener

```java
public void addFocusListener​(
FocusListener
l)
```

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the focus listener
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

removeFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

- removeFocusListener

```java
public void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so that it no longer
receives focus events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the focus listener
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

addFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

- getFocusListeners

```java
public
FocusListener
[] getFocusListeners()
```

Returns an array of all the focus listeners
registered on this component.

**Returns:** all of this component's

FocusListener

s
or an empty array if no component
listeners are currently registered
**Since:** 1.4
**See Also:** addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

- addHierarchyListener

```java
public void addHierarchyListener​(
HierarchyListener
l)
```

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

removeHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

- removeHierarchyListener

```java
public void removeHierarchyListener​(
HierarchyListener
l)
```

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

- getHierarchyListeners

```java
public
HierarchyListener
[] getHierarchyListeners()
```

Returns an array of all the hierarchy listeners
registered on this component.

**Returns:** all of this component's

HierarchyListener

s
or an empty array if no hierarchy
listeners are currently registered
**Since:** 1.4
**See Also:** addHierarchyListener(java.awt.event.HierarchyListener)

,

removeHierarchyListener(java.awt.event.HierarchyListener)

- addHierarchyBoundsListener

```java
public void addHierarchyBoundsListener​(
HierarchyBoundsListener
l)
```

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy bounds listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

- removeHierarchyBoundsListener

```java
public void removeHierarchyBoundsListener​(
HierarchyBoundsListener
l)
```

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy bounds listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

- getHierarchyBoundsListeners

```java
public
HierarchyBoundsListener
[] getHierarchyBoundsListeners()
```

Returns an array of all the hierarchy bounds listeners
registered on this component.

**Returns:** all of this component's

HierarchyBoundsListener

s
or an empty array if no hierarchy bounds
listeners are currently registered
**Since:** 1.4
**See Also:** addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

- addKeyListener

```java
public void addKeyListener​(
KeyListener
l)
```

Adds the specified key listener to receive key events from
this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the key listener.
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

removeKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

- removeKeyListener

```java
public void removeKeyListener​(
KeyListener
l)
```

Removes the specified key listener so that it no longer
receives key events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the key listener
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

addKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

- getKeyListeners

```java
public
KeyListener
[] getKeyListeners()
```

Returns an array of all the key listeners
registered on this component.

**Returns:** all of this component's

KeyListener

s
or an empty array if no key
listeners are currently registered
**Since:** 1.4
**See Also:** addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

- addMouseListener

```java
public void addMouseListener​(
MouseListener
l)
```

Adds the specified mouse listener to receive mouse events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

removeMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

- removeMouseListener

```java
public void removeMouseListener​(
MouseListener
l)
```

Removes the specified mouse listener so that it no longer
receives mouse events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

- getMouseListeners

```java
public
MouseListener
[] getMouseListeners()
```

Returns an array of all the mouse listeners
registered on this component.

**Returns:** all of this component's

MouseListener

s
or an empty array if no mouse
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

- addMouseMotionListener

```java
public void addMouseMotionListener​(
MouseMotionListener
l)
```

Adds the specified mouse motion listener to receive mouse motion
events from this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse motion listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

- removeMouseMotionListener

```java
public void removeMouseMotionListener​(
MouseMotionListener
l)
```

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse motion listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

- getMouseMotionListeners

```java
public
MouseMotionListener
[] getMouseMotionListeners()
```

Returns an array of all the mouse motion listeners
registered on this component.

**Returns:** all of this component's

MouseMotionListener

s
or an empty array if no mouse motion
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

- addMouseWheelListener

```java
public void addMouseWheelListener​(
MouseWheelListener
l)
```

Adds the specified mouse wheel listener to receive mouse wheel events
from this component. Containers also receive mouse wheel events from
sub-components.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse wheel listener
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

- removeMouseWheelListener

```java
public void removeMouseWheelListener​(
MouseWheelListener
l)
```

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse wheel listener.
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

- getMouseWheelListeners

```java
public
MouseWheelListener
[] getMouseWheelListeners()
```

Returns an array of all the mouse wheel listeners
registered on this component.

**Returns:** all of this component's

MouseWheelListener

s
or an empty array if no mouse wheel
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseWheelListener(java.awt.event.MouseWheelListener)

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

- addInputMethodListener

```java
public void addInputMethodListener​(
InputMethodListener
l)
```

Adds the specified input method listener to receive
input method events from this component. A component will
only receive input method events from input methods
if it also overrides

getInputMethodRequests

to return an

InputMethodRequests

instance.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the input method listener
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

removeInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

,

getInputMethodRequests()

- removeInputMethodListener

```java
public void removeInputMethodListener​(
InputMethodListener
l)
```

Removes the specified input method listener so that it no longer
receives input method events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the input method listener
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

- getInputMethodListeners

```java
public
InputMethodListener
[] getInputMethodListeners()
```

Returns an array of all the input method listeners
registered on this component.

**Returns:** all of this component's

InputMethodListener

s
or an empty array if no input method
listeners are currently registered
**Since:** 1.4
**See Also:** addInputMethodListener(java.awt.event.InputMethodListener)

,

removeInputMethodListener(java.awt.event.InputMethodListener)

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Component c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getComponentListeners()

,

getFocusListeners()

,

getHierarchyListeners()

,

getHierarchyBoundsListeners()

,

getKeyListeners()

,

getMouseListeners()

,

getMouseMotionListeners()

,

getMouseWheelListeners()

,

getInputMethodListeners()

,

getPropertyChangeListeners()

- getInputMethodRequests

```java
public
InputMethodRequests
getInputMethodRequests()
```

Gets the input method request handler which supports
requests from input methods for this component. A component
that supports on-the-spot text input must override this
method to return an

InputMethodRequests

instance.
At the same time, it also has to handle input method events.

**Returns:** the input method request handler for this component,

null

by default
**Since:** 1.2
**See Also:** addInputMethodListener(java.awt.event.InputMethodListener)

- getInputContext

```java
public
InputContext
getInputContext()
```

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component. By default, the input context used for
the parent component is returned. Components may
override this to return a private input context.

**Returns:** the input context used by this component;

null

if no context can be determined
**Since:** 1.2

- enableEvents

```java
protected final void enableEvents​(long eventsToEnable)
```

Enables the events defined by the specified event mask parameter
to be delivered to this component.

Event types are automatically enabled when a listener for
that event type is added to the component.

This method only needs to be invoked by subclasses of

Component

which desire to have the specified event
types delivered to

processEvent

regardless of whether
or not a listener is registered.

**Parameters:** eventsToEnable

- the event mask defining the event types
**Since:** 1.1
**See Also:** processEvent(java.awt.AWTEvent)

,

disableEvents(long)

,

AWTEvent

- disableEvents

```java
protected final void disableEvents​(long eventsToDisable)
```

Disables the events defined by the specified event mask parameter
from being delivered to this component.

**Parameters:** eventsToDisable

- the event mask defining the event types
**Since:** 1.1
**See Also:** enableEvents(long)

- coalesceEvents

```java
protected
AWTEvent
coalesceEvents​(
AWTEvent
existingEvent,

AWTEvent
newEvent)
```

Potentially coalesce an event being posted with an existing
event. This method is called by

EventQueue.postEvent

if an event with the same ID as the event to be posted is found in
the queue (both events must have this component as their source).
This method either returns a coalesced event which replaces
the existing event (and the new event is then discarded), or

null

to indicate that no combining should be done
(add the second event to the end of the queue). Either event
parameter may be modified and returned, as the other one is discarded
unless

null

is returned.

This implementation of

coalesceEvents

coalesces
two event types: mouse move (and drag) events,
and paint (and update) events.
For mouse move events the last event is always returned, causing
intermediate moves to be discarded. For paint events, the new
event is coalesced into a complex

RepaintArea

in the peer.
The new

AWTEvent

is always returned.

**Parameters:** existingEvent

- the event already on the

EventQueue
**Parameters:** newEvent

- the event being posted to the

EventQueue
**Returns:** a coalesced event, or

null

indicating that no
coalescing was done

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events occurring on this component. By default this
method calls the appropriate

process<event type>Event

method for the given class of event.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the event
**Since:** 1.1
**See Also:** processComponentEvent(java.awt.event.ComponentEvent)

,

processFocusEvent(java.awt.event.FocusEvent)

,

processKeyEvent(java.awt.event.KeyEvent)

,

processMouseEvent(java.awt.event.MouseEvent)

,

processMouseMotionEvent(java.awt.event.MouseEvent)

,

processInputMethodEvent(java.awt.event.InputMethodEvent)

,

processHierarchyEvent(java.awt.event.HierarchyEvent)

,

processMouseWheelEvent(java.awt.event.MouseWheelEvent)

- processComponentEvent

```java
protected void processComponentEvent​(
ComponentEvent
e)
```

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

This method is not called unless component events are
enabled for this component. Component events are enabled
when one of the following occurs:

- A

ComponentListener

object is registered
via

addComponentListener

.

Component events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the component event
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

enableEvents(long)

- processFocusEvent

```java
protected void processFocusEvent​(
FocusEvent
e)
```

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

This method is not called unless focus events are
enabled for this component. Focus events are enabled
when one of the following occurs:

- A

FocusListener

object is registered
via

addFocusListener

.

Focus events are enabled via

enableEvents

.

If focus events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a focus event should be dispatched to
registered

FocusListener

objects. If the
events are to be dispatched, the

KeyboardFocusManager

calls the

Component

's

dispatchEvent

method, which results in a call to the

Component

's

processFocusEvent

method.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the focus event
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

KeyboardFocusManager

,

addFocusListener(java.awt.event.FocusListener)

,

enableEvents(long)

,

dispatchEvent(java.awt.AWTEvent)

- processKeyEvent

```java
protected void processKeyEvent​(
KeyEvent
e)
```

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

This method is not called unless key events are
enabled for this component. Key events are enabled
when one of the following occurs:

- A

KeyListener

object is registered
via

addKeyListener

.

Key events are enabled via

enableEvents

.

If key events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a key event should be dispatched to
registered

KeyListener

objects. The

DefaultKeyboardFocusManager

will not dispatch
key events to a

Component

that is not the focus
owner or is not showing.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the key event
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

processEvent(java.awt.AWTEvent)

,

dispatchEvent(java.awt.AWTEvent)

,

addKeyListener(java.awt.event.KeyListener)

,

enableEvents(long)

,

isShowing()

- processMouseEvent

```java
protected void processMouseEvent​(
MouseEvent
e)
```

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

This method is not called unless mouse events are
enabled for this component. Mouse events are enabled
when one of the following occurs:

- A

MouseListener

object is registered
via

addMouseListener

.

Mouse events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse event
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

enableEvents(long)

- processMouseMotionEvent

```java
protected void processMouseMotionEvent​(
MouseEvent
e)
```

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

This method is not called unless mouse motion events are
enabled for this component. Mouse motion events are enabled
when one of the following occurs:

- A

MouseMotionListener

object is registered
via

addMouseMotionListener

.

Mouse motion events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse motion event
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

enableEvents(long)

- processMouseWheelEvent

```java
protected void processMouseWheelEvent​(
MouseWheelEvent
e)
```

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

This method is not called unless mouse wheel events are
enabled for this component. Mouse wheel events are enabled
when one of the following occurs:

- A

MouseWheelListener

object is registered
via

addMouseWheelListener

.

Mouse wheel events are enabled via

enableEvents

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse wheel event
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

enableEvents(long)

- processInputMethodEvent

```java
protected void processInputMethodEvent​(
InputMethodEvent
e)
```

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

This method is not called unless input method events
are enabled for this component. Input method events are enabled
when one of the following occurs:

- An

InputMethodListener

object is registered
via

addInputMethodListener

.

Input method events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the input method event
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

enableEvents(long)

- processHierarchyEvent

```java
protected void processHierarchyEvent​(
HierarchyEvent
e)
```

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

This method is not called unless hierarchy events
are enabled for this component. Hierarchy events are enabled
when one of the following occurs:

- An

HierarchyListener

object is registered
via

addHierarchyListener

.

Hierarchy events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the hierarchy event
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

enableEvents(long)

- processHierarchyBoundsEvent

```java
protected void processHierarchyBoundsEvent​(
HierarchyEvent
e)
```

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

This method is not called unless hierarchy bounds events
are enabled for this component. Hierarchy bounds events are enabled
when one of the following occurs:

- An

HierarchyBoundsListener

object is registered
via

addHierarchyBoundsListener

.

Hierarchy bounds events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the hierarchy event
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

enableEvents(long)

- handleEvent

```java
@Deprecated

public boolean handleEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1
replaced by processEvent(AWTEvent).

**Parameters:** evt

- the event to handle
**Returns:** true

if the event was handled,

false

otherwise

- mouseDown

```java
@Deprecated

public boolean mouseDown​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseDrag

```java
@Deprecated

public boolean mouseDrag​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseUp

```java
@Deprecated

public boolean mouseUp​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseMove

```java
@Deprecated

public boolean mouseMove​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseEnter

```java
@Deprecated

public boolean mouseEnter​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- mouseExit

```java
@Deprecated

public boolean mouseExit​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

- keyDown

```java
@Deprecated

public boolean keyDown​(
Event
evt,
int key)
```

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

**Parameters:** evt

- the event to handle
**Parameters:** key

- the key pressed
**Returns:** false

- keyUp

```java
@Deprecated

public boolean keyUp​(
Event
evt,
int key)
```

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

**Parameters:** evt

- the event to handle
**Parameters:** key

- the key pressed
**Returns:** false

- action

```java
@Deprecated

public boolean action​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
should register this component as ActionListener on component
which fires action events.

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object acted on
**Returns:** false

- addNotify

```java
public void addNotify()
```

Makes this

Component

displayable by connecting it to a
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Since:** 1.0
**See Also:** isDisplayable()

,

removeNotify()

,

invalidate()

- removeNotify

```java
public void removeNotify()
```

Makes this

Component

undisplayable by destroying it native
screen resource.

This method is called by the toolkit internally and should
not be called directly by programs. Code overriding
this method should call

super.removeNotify

as
the first line of the overriding method.

**Since:** 1.0
**See Also:** isDisplayable()

,

addNotify()

- gotFocus

```java
@Deprecated

public boolean gotFocus​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object focused
**Returns:** false

- lostFocus

```java
@Deprecated

public boolean lostFocus​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object focused
**Returns:** false

- isFocusTraversable

```java
@Deprecated

public boolean isFocusTraversable()
```

Deprecated.

As of 1.4, replaced by

isFocusable()

.

Returns whether this

Component

can become the focus
owner.

**Returns:** true

if this

Component

is
focusable;

false

otherwise
**Since:** 1.1
**See Also:** setFocusable(boolean)

- isFocusable

```java
public boolean isFocusable()
```

Returns whether this Component can be focused.

**Returns:** true

if this Component is focusable;

false

otherwise.
**Since:** 1.4
**See Also:** setFocusable(boolean)

- setFocusable

```java
public void setFocusable​(boolean focusable)
```

Sets the focusable state of this Component to the specified value. This
value overrides the Component's default focusability.

**Parameters:** focusable

- indicates whether this Component is focusable
**Since:** 1.4
**See Also:** isFocusable()

- setFocusTraversalKeys

```java
public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)
```

Sets the focus traversal keys for a given traversal operation for this
Component.

The default values for a Component's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Component's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Component. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Parameters:** keystrokes

- the Set of AWTKeyStroke for the specified operation
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Component
**Since:** 1.4
**See Also:** getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

- getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Returns the Set of focus traversal keys for a given traversal operation
for this Component. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Component, then this Component's parent's Set is returned. If no Set
has been explicitly defined for any of this Component's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Returns:** the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

- areFocusTraversalKeysSet

```java
public boolean areFocusTraversalKeysSet​(int id)
```

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component. If
this method returns

false

, this Component is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Returns:** true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4

- setFocusTraversalKeysEnabled

```java
public void setFocusTraversalKeysEnabled​(boolean focusTraversalKeysEnabled)
```

Sets whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Parameters:** focusTraversalKeysEnabled

- whether focus traversal keys are
enabled for this Component
**Since:** 1.4
**See Also:** getFocusTraversalKeysEnabled()

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

- getFocusTraversalKeysEnabled

```java
public boolean getFocusTraversalKeysEnabled()
```

Returns whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Returns:** whether focus traversal keys are enabled for this Component
**Since:** 1.4
**See Also:** setFocusTraversalKeysEnabled(boolean)

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

- requestFocus

```java
public void requestFocus()
```

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window. This
component must be displayable, focusable, visible and all of
its ancestors (with the exception of the top-level Window) must
be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event. If this request is denied because this
Component's top-level Window cannot become the focused Window,
the request will be remembered and will be granted when the
Window is later focused by the user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Since:** 1.0
**See Also:** requestFocusInWindow()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocus

```java
public void requestFocus​(
FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level Window)
must be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of method. If this request is denied because this Component's
top-level Window cannot become the focused Window, the request will be
remembered and will be granted when the Window is later focused by the
user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** cause

- the cause why the focus is requested
**Since:** 9
**See Also:** FocusEvent

,

FocusEvent.Cause

,

requestFocusInWindow(FocusEvent.Cause)

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocus

```java
protected boolean requestFocus​(boolean temporary)
```

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocus

```java
protected boolean requestFocus​(boolean temporary,

FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the {FocusEvent}
generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Parameters:** cause

- the cause why the focus is requested
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 9
**See Also:** FocusEvent

,

FocusEvent.Cause

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocusInWindow

```java
public boolean requestFocusInWindow()
```

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocusInWindow

```java
public boolean requestFocusInWindow​(
FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** cause

- the cause why the focus is requested
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 9
**See Also:** requestFocus(FocusEvent.Cause)

,

FocusEvent

,

FocusEvent.Cause

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- requestFocusInWindow

```java
protected boolean requestFocusInWindow​(boolean temporary)
```

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

- getFocusCycleRootAncestor

```java
public
Container
getFocusCycleRootAncestor()
```

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle. Each focus traversal cycle has only a single
focus cycle root and each Component which is not a Container belongs to
only a single focus traversal cycle. Containers which are focus cycle
roots belong to two cycles: one rooted at the Container itself, and one
rooted at the Container's nearest focus-cycle-root ancestor. For such
Containers, this method will return the Container's nearest focus-cycle-
root ancestor.

**Returns:** this Component's nearest focus-cycle-root ancestor
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- isFocusCycleRoot

```java
public boolean isFocusCycleRoot​(
Container
container)
```

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Component which is not a Container
belongs to only a single focus traversal cycle.

**Parameters:** container

- the Container to be tested
**Returns:** true

if the specified Container is a focus-cycle-
root of this Component;

false

otherwise
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

- transferFocus

```java
public void transferFocus()
```

Transfers the focus to the next component, as though this Component were
the focus owner.

**Since:** 1.1
**See Also:** requestFocus()

- nextFocus

```java
@Deprecated

public void nextFocus()
```

Deprecated.

As of JDK version 1.1,
replaced by transferFocus().

- transferFocusBackward

```java
public void transferFocusBackward()
```

Transfers the focus to the previous component, as though this Component
were the focus owner.

**Since:** 1.4
**See Also:** requestFocus()

- transferFocusUpCycle

```java
public void transferFocusUpCycle()
```

Transfers the focus up one focus traversal cycle. Typically, the focus
owner is set to this Component's focus cycle root, and the current focus
cycle root is set to the new focus owner's focus cycle root. If,
however, this Component's focus cycle root is a Window, then the focus
owner is set to the focus cycle root's default Component to focus, and
the current focus cycle root is unchanged.

**Since:** 1.4
**See Also:** requestFocus()

,

Container.isFocusCycleRoot()

,

Container.setFocusCycleRoot(boolean)

- hasFocus

```java
public boolean hasFocus()
```

Returns

true

if this

Component

is the
focus owner. This method is obsolete, and has been replaced by

isFocusOwner()

.

**Returns:** true

if this

Component

is the
focus owner;

false

otherwise
**Since:** 1.2

- isFocusOwner

```java
public boolean isFocusOwner()
```

Returns

true

if this

Component

is the
focus owner.

**Returns:** true

if this

Component

is the
focus owner;

false

otherwise
**Since:** 1.4

- add

```java
public void add​(
PopupMenu
popup)
```

Adds the specified popup menu to the component.

**Parameters:** popup

- the popup menu to be added to the component.
**Throws:** NullPointerException

- if

popup

is

null
**Since:** 1.1
**See Also:** remove(MenuComponent)

- remove

```java
public void remove​(
MenuComponent
popup)
```

Removes the specified popup menu from the component.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** popup

- the popup menu to be removed
**Since:** 1.1
**See Also:** add(PopupMenu)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this component. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:** a string representation of this component's state
**Since:** 1.0

- toString

```java
public
String
toString()
```

Returns a string representation of this component and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this component
**Since:** 1.0

- list

```java
public void list()
```

Prints a listing of this component to the standard system output
stream

System.out

.

**Since:** 1.0
**See Also:** System.out

- list

```java
public void list​(
PrintStream
out)
```

Prints a listing of this component to the specified output
stream.

**Parameters:** out

- a print stream
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0

- list

```java
public void list​(
PrintStream
out,
int indent)
```

Prints out a list, starting at the specified indentation, to the
specified print stream.

**Parameters:** out

- a print stream
**Parameters:** indent

- number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0
**See Also:** PrintStream.println(java.lang.Object)

- list

```java
public void list​(
PrintWriter
out)
```

Prints a listing to the specified print writer.

**Parameters:** out

- the print writer to print to
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1

- list

```java
public void list​(
PrintWriter
out,
int indent)
```

Prints out a list, starting at the specified indentation, to
the specified print writer.

**Parameters:** out

- the print writer to print to
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1
**See Also:** PrintStream.println(java.lang.Object)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Component's preferred size ("preferredSize")
- this Component's minimum size ("minimumSize")
- this Component's maximum size ("maximumSize")
- this Component's name ("name")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:** listener

- the property change listener to be added
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list. This method
should be used to remove PropertyChangeListeners that were registered
for all bound properties of this class.

If listener is null, no exception is thrown and no action is performed.

**Parameters:** listener

- the PropertyChangeListener to be removed
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this component.

**Returns:** all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

PropertyChangeSupport.getPropertyChangeListeners()

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the property change listener to be added
**See Also:** removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener
list for a specific property. This method should be used to remove

PropertyChangeListener

s
that were registered for a specific bound property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:** propertyName

- a valid property name
**Parameters:** listener

- the PropertyChangeListener to be removed
**See Also:** addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners​(
String
propertyName)
```

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:** propertyName

- the property name
**Returns:** all of the

PropertyChangeListener

s associated with
the named property; if no such listeners have been added or
if

propertyName

is

null

, an empty
array is returned
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes for Object properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.4

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Support for reporting bound property changes for integer properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.4

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- setComponentOrientation

```java
public void setComponentOrientation​(
ComponentOrientation
o)
```

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component. Language-sensitive

LayoutManager

and

Component

subclasses will use this property to
determine how to lay out and draw components.

At construction time, a component's orientation is set to

ComponentOrientation.UNKNOWN

,
indicating that it has not been specified
explicitly. The UNKNOWN orientation behaves the same as

ComponentOrientation.LEFT_TO_RIGHT

.

To set the orientation of a single component, use this method.
To set the orientation of an entire component
hierarchy, use

applyComponentOrientation

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** o

- the orientation to be set
**See Also:** ComponentOrientation

,

invalidate()

- getComponentOrientation

```java
public
ComponentOrientation
getComponentOrientation()
```

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

LayoutManager

and

Component

subclasses that wish to respect orientation should call this method to
get the component's orientation before performing layout or drawing.

**Returns:** the orientation to order the elements or text
**See Also:** ComponentOrientation

- applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
orientation)
```

Sets the

ComponentOrientation

property of this component
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** orientation

- the new component orientation of this component and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** setComponentOrientation(java.awt.ComponentOrientation)

,

getComponentOrientation()

,

invalidate()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated
with this

Component

.
The method implemented by this base
class returns null. Classes that extend

Component

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:** the

AccessibleContext

of this

Component
**Since:** 1.3

- setMixingCutoutShape

```java
public void setMixingCutoutShape​(
Shape
shape)
```

Sets a 'mixing-cutout' shape for this lightweight component.

This method is used exclusively for the purposes of the
Heavyweight/Lightweight Components Mixing feature and will
have no effect if applied to a heavyweight component.

By default a lightweight component is treated as an opaque rectangle for
the purposes of the Heavyweight/Lightweight Components Mixing feature.
This method enables developers to set an arbitrary shape to be cut out
from heavyweight components positioned underneath the lightweight
component in the z-order.

The

shape

argument may have the following values:

- null

- reverts the default cutout shape (the rectangle equal
to the component's

getBounds()

)

empty-shape

- does not cut out anything from heavyweight
components. This makes this lightweight component effectively
transparent. Note that descendants of the lightweight component still
affect the shapes of heavyweight components. An example of an

empty-shape

is

new Rectangle()

.

non-empty-shape

- the given shape will be cut out from
heavyweight components.

The most common example when the 'mixing-cutout' shape is needed is a
glass pane component. The

JRootPane.setGlassPane(java.awt.Component)

method
automatically sets the

empty-shape

as the 'mixing-cutout' shape
for the given glass pane component. If a developer needs some other
'mixing-cutout' shape for the glass pane (which is rare), this must be
changed manually after installing the glass pane to the root pane.

**Parameters:** shape

- the new 'mixing-cutout' shape
**Since:** 9

---

#### Method Detail

getName

```java
public
String
getName()
```

Gets the name of the component.

**Returns:** this component's name
**Since:** 1.1
**See Also:** setName(java.lang.String)

---

#### getName

public

String

getName()

Gets the name of the component.

setName

```java
public void setName​(
String
name)
```

Sets the name of the component to the specified string.

**Parameters:** name

- the string that is to be this
component's name
**Since:** 1.1
**See Also:** getName()

---

#### setName

public void setName​(

String

name)

Sets the name of the component to the specified string.

getParent

```java
public
Container
getParent()
```

Gets the parent of this component.

**Returns:** the parent container of this component
**Since:** 1.0

---

#### getParent

public

Container

getParent()

Gets the parent of this component.

setDropTarget

```java
public void setDropTarget​(
DropTarget
dt)
```

Associate a

DropTarget

with this component.
The

Component

will receive drops only if it
is enabled.

**Parameters:** dt

- The DropTarget
**See Also:** isEnabled()

---

#### setDropTarget

public void setDropTarget​(

DropTarget

dt)

Associate a

DropTarget

with this component.
The

Component

will receive drops only if it
is enabled.

getDropTarget

```java
public
DropTarget
getDropTarget()
```

Gets the

DropTarget

associated with this

Component

.

**Returns:** the drop target

---

#### getDropTarget

public

DropTarget

getDropTarget()

Gets the

DropTarget

associated with this

Component

.

getGraphicsConfiguration

```java
public
GraphicsConfiguration
getGraphicsConfiguration()
```

Gets the

GraphicsConfiguration

associated with this

Component

.
If the

Component

has not been assigned a specific

GraphicsConfiguration

,
the

GraphicsConfiguration

of the

Component

object's top-level container is
returned.
If the

Component

has been created, but not yet added
to a

Container

, this method returns

null

.

**Returns:** the

GraphicsConfiguration

used by this

Component

or

null
**Since:** 1.3

---

#### getGraphicsConfiguration

public

GraphicsConfiguration

getGraphicsConfiguration()

Gets the

GraphicsConfiguration

associated with this

Component

.
If the

Component

has not been assigned a specific

GraphicsConfiguration

,
the

GraphicsConfiguration

of the

Component

object's top-level container is
returned.
If the

Component

has been created, but not yet added
to a

Container

, this method returns

null

.

getTreeLock

```java
public final
Object
getTreeLock()
```

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

**Returns:** this component's locking object

---

#### getTreeLock

public final

Object

getTreeLock()

Gets this component's locking object (the object that owns the thread
synchronization monitor) for AWT component-tree and layout
operations.

getToolkit

```java
public
Toolkit
getToolkit()
```

Gets the toolkit of this component. Note that
the frame that contains a component controls which
toolkit is used by that component. Therefore if the component
is moved from one frame to another, the toolkit it uses may change.

**Returns:** the toolkit of this component
**Since:** 1.0

---

#### getToolkit

public

Toolkit

getToolkit()

Gets the toolkit of this component. Note that
the frame that contains a component controls which
toolkit is used by that component. Therefore if the component
is moved from one frame to another, the toolkit it uses may change.

isValid

```java
public boolean isValid()
```

Determines whether this component is valid. A component is valid
when it is correctly sized and positioned within its parent
container and all its children are also valid.
In order to account for peers' size requirements, components are invalidated
before they are first shown on the screen. By the time the parent container
is fully realized, all its components will be valid.

**Returns:** true

if the component is valid,

false

otherwise
**Since:** 1.0
**See Also:** validate()

,

invalidate()

---

#### isValid

public boolean isValid()

Determines whether this component is valid. A component is valid
when it is correctly sized and positioned within its parent
container and all its children are also valid.
In order to account for peers' size requirements, components are invalidated
before they are first shown on the screen. By the time the parent container
is fully realized, all its components will be valid.

isDisplayable

```java
public boolean isDisplayable()
```

Determines whether this component is displayable. A component is
displayable when it is connected to a native screen resource.

A component is made displayable either when it is added to
a displayable containment hierarchy or when its containment
hierarchy is made displayable.
A containment hierarchy is made displayable when its ancestor
window is either packed or made visible.

A component is made undisplayable either when it is removed from
a displayable containment hierarchy or when its containment hierarchy
is made undisplayable. A containment hierarchy is made
undisplayable when its ancestor window is disposed.

**Returns:** true

if the component is displayable,

false

otherwise
**Since:** 1.2
**See Also:** Container.add(Component)

,

Window.pack()

,

Window.show()

,

Container.remove(Component)

,

Window.dispose()

---

#### isDisplayable

public boolean isDisplayable()

Determines whether this component is displayable. A component is
displayable when it is connected to a native screen resource.

A component is made displayable either when it is added to
a displayable containment hierarchy or when its containment
hierarchy is made displayable.
A containment hierarchy is made displayable when its ancestor
window is either packed or made visible.

A component is made undisplayable either when it is removed from
a displayable containment hierarchy or when its containment hierarchy
is made undisplayable. A containment hierarchy is made
undisplayable when its ancestor window is disposed.

A component is made displayable either when it is added to
a displayable containment hierarchy or when its containment
hierarchy is made displayable.
A containment hierarchy is made displayable when its ancestor
window is either packed or made visible.

A component is made undisplayable either when it is removed from
a displayable containment hierarchy or when its containment hierarchy
is made undisplayable. A containment hierarchy is made
undisplayable when its ancestor window is disposed.

A component is made undisplayable either when it is removed from
a displayable containment hierarchy or when its containment hierarchy
is made undisplayable. A containment hierarchy is made
undisplayable when its ancestor window is disposed.

isVisible

```java
public boolean isVisible()
```

Determines whether this component should be visible when its
parent is visible. Components are
initially visible, with the exception of top level components such
as

Frame

objects.

**Returns:** true

if the component is visible,

false

otherwise
**Since:** 1.0
**See Also:** setVisible(boolean)

---

#### isVisible

public boolean isVisible()

Determines whether this component should be visible when its
parent is visible. Components are
initially visible, with the exception of top level components such
as

Frame

objects.

getMousePosition

```java
public
Point
getMousePosition()
throws
HeadlessException
```

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.
If the

Component

is not showing on the screen, this method
returns

null

even if the mouse pointer is above the area
where the

Component

would be displayed.
If the

Component

is partially or fully obscured by other

Component

s or native windows, this method returns a non-null
value only if the mouse pointer is located above the unobscured part of the

Component

.

For

Container

s it returns a non-null value if the mouse is
above the

Container

itself or above any of its descendants.
Use

Container.getMousePosition(boolean)

if you need to exclude children.

Sometimes the exact mouse coordinates are not important, and the only thing
that matters is whether a specific

Component

is under the mouse
pointer. If the return value of this method is

null

, mouse
pointer is not directly above the

Component

.

**Returns:** mouse coordinates relative to this

Component

, or null
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** isShowing()

,

Container.getMousePosition(boolean)

---

#### getMousePosition

public

Point

getMousePosition()
throws

HeadlessException

Returns the position of the mouse pointer in this

Component

's
coordinate space if the

Component

is directly under the mouse
pointer, otherwise returns

null

.
If the

Component

is not showing on the screen, this method
returns

null

even if the mouse pointer is above the area
where the

Component

would be displayed.
If the

Component

is partially or fully obscured by other

Component

s or native windows, this method returns a non-null
value only if the mouse pointer is located above the unobscured part of the

Component

.

For

Container

s it returns a non-null value if the mouse is
above the

Container

itself or above any of its descendants.
Use

Container.getMousePosition(boolean)

if you need to exclude children.

Sometimes the exact mouse coordinates are not important, and the only thing
that matters is whether a specific

Component

is under the mouse
pointer. If the return value of this method is

null

, mouse
pointer is not directly above the

Component

.

For

Container

s it returns a non-null value if the mouse is
above the

Container

itself or above any of its descendants.
Use

Container.getMousePosition(boolean)

if you need to exclude children.

Sometimes the exact mouse coordinates are not important, and the only thing
that matters is whether a specific

Component

is under the mouse
pointer. If the return value of this method is

null

, mouse
pointer is not directly above the

Component

.

Sometimes the exact mouse coordinates are not important, and the only thing
that matters is whether a specific

Component

is under the mouse
pointer. If the return value of this method is

null

, mouse
pointer is not directly above the

Component

.

isShowing

```java
public boolean isShowing()
```

Determines whether this component is showing on screen. This means
that the component must be visible, and it must be in a container
that is visible and showing.

Note:

sometimes there is no way to detect whether the

Component

is actually visible to the user. This can happen when:

- the component has been added to a visible

ScrollPane

but
the

Component

is not currently in the scroll pane's view port.

the

Component

is obscured by another

Component

or

Container

.

**Returns:** true

if the component is showing,

false

otherwise
**Since:** 1.0
**See Also:** setVisible(boolean)

---

#### isShowing

public boolean isShowing()

Determines whether this component is showing on screen. This means
that the component must be visible, and it must be in a container
that is visible and showing.

Note:

sometimes there is no way to detect whether the

Component

is actually visible to the user. This can happen when:

- the component has been added to a visible

ScrollPane

but
the

Component

is not currently in the scroll pane's view port.

the

Component

is obscured by another

Component

or

Container

.

Note:

sometimes there is no way to detect whether the

Component

is actually visible to the user. This can happen when:

- the component has been added to a visible

ScrollPane

but
the

Component

is not currently in the scroll pane's view port.

the

Component

is obscured by another

Component

or

Container

.

the component has been added to a visible

ScrollPane

but
the

Component

is not currently in the scroll pane's view port.

the

Component

is obscured by another

Component

or

Container

.

isEnabled

```java
public boolean isEnabled()
```

Determines whether this component is enabled. An enabled component
can respond to user input and generate events. Components are
enabled initially by default. A component may be enabled or disabled by
calling its

setEnabled

method.

**Returns:** true

if the component is enabled,

false

otherwise
**Since:** 1.0
**See Also:** setEnabled(boolean)

---

#### isEnabled

public boolean isEnabled()

Determines whether this component is enabled. An enabled component
can respond to user input and generate events. Components are
enabled initially by default. A component may be enabled or disabled by
calling its

setEnabled

method.

setEnabled

```java
public void setEnabled​(boolean b)
```

Enables or disables this component, depending on the value of the
parameter

b

. An enabled component can respond to user
input and generate events. Components are enabled initially by default.

Note: Disabling a lightweight component does not prevent it from
receiving MouseEvents.

Note: Disabling a heavyweight container prevents all components
in this container from receiving any input events. But disabling a
lightweight container affects only this container.

**Parameters:** b

- If

true

, this component is
enabled; otherwise this component is disabled
**Since:** 1.1
**See Also:** isEnabled()

,

isLightweight()

---

#### setEnabled

public void setEnabled​(boolean b)

Enables or disables this component, depending on the value of the
parameter

b

. An enabled component can respond to user
input and generate events. Components are enabled initially by default.

Note: Disabling a lightweight component does not prevent it from
receiving MouseEvents.

Note: Disabling a heavyweight container prevents all components
in this container from receiving any input events. But disabling a
lightweight container affects only this container.

Note: Disabling a lightweight component does not prevent it from
receiving MouseEvents.

Note: Disabling a heavyweight container prevents all components
in this container from receiving any input events. But disabling a
lightweight container affects only this container.

Note: Disabling a heavyweight container prevents all components
in this container from receiving any input events. But disabling a
lightweight container affects only this container.

enable

```java
@Deprecated

public void enable()
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

---

#### enable

@Deprecated

public void enable()

enable

```java
@Deprecated

public void enable​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

Enables or disables this component.

**Parameters:** b

-

true

to enable this component;
otherwise

false

---

#### enable

@Deprecated

public void enable​(boolean b)

Enables or disables this component.

disable

```java
@Deprecated

public void disable()
```

Deprecated.

As of JDK version 1.1,
replaced by

setEnabled(boolean)

.

---

#### disable

@Deprecated

public void disable()

isDoubleBuffered

```java
public boolean isDoubleBuffered()
```

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later. Component
subclasses that support double buffering should override this
method to return true if double buffering is enabled.

**Returns:** false by default

---

#### isDoubleBuffered

public boolean isDoubleBuffered()

Returns true if this component is painted to an offscreen image
("buffer") that's copied to the screen later. Component
subclasses that support double buffering should override this
method to return true if double buffering is enabled.

enableInputMethods

```java
public void enableInputMethods​(boolean enable)
```

Enables or disables input method support for this component. If input
method support is enabled and the component also processes key events,
incoming events are offered to
the current input method and will only be processed by the component or
dispatched to its listeners if the input method does not consume them.
By default, input method support is enabled.

**Parameters:** enable

- true to enable, false to disable
**Since:** 1.2
**See Also:** processKeyEvent(java.awt.event.KeyEvent)

---

#### enableInputMethods

public void enableInputMethods​(boolean enable)

Enables or disables input method support for this component. If input
method support is enabled and the component also processes key events,
incoming events are offered to
the current input method and will only be processed by the component or
dispatched to its listeners if the input method does not consume them.
By default, input method support is enabled.

setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this component depending on the value of parameter

b

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** b

- if

true

, shows this component;
otherwise, hides this component
**Since:** 1.1
**See Also:** isVisible()

,

invalidate()

---

#### setVisible

public void setVisible​(boolean b)

Shows or hides this component depending on the value of parameter

b

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

---

#### show

@Deprecated

public void show()

show

```java
@Deprecated

public void show​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

Makes this component visible or invisible.

**Parameters:** b

-

true

to make this component visible;
otherwise

false

---

#### show

@Deprecated

public void show​(boolean b)

Makes this component visible or invisible.

hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.1,
replaced by

setVisible(boolean)

.

---

#### hide

@Deprecated

public void hide()

getForeground

```java
public
Color
getForeground()
```

Gets the foreground color of this component.

**Returns:** this component's foreground color; if this component does
not have a foreground color, the foreground color of its parent
is returned
**Since:** 1.0
**See Also:** setForeground(java.awt.Color)

---

#### getForeground

public

Color

getForeground()

Gets the foreground color of this component.

setForeground

```java
public void setForeground​(
Color
c)
```

Sets the foreground color of this component.

**Parameters:** c

- the color to become this component's
foreground color; if this parameter is

null

then this component will inherit
the foreground color of its parent
**Since:** 1.0
**See Also:** getForeground()

---

#### setForeground

public void setForeground​(

Color

c)

Sets the foreground color of this component.

isForegroundSet

```java
public boolean isForegroundSet()
```

Returns whether the foreground color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its foreground color from an ancestor.

**Returns:** true

if the foreground color has been explicitly
set for this Component;

false

otherwise.
**Since:** 1.4

---

#### isForegroundSet

public boolean isForegroundSet()

Returns whether the foreground color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its foreground color from an ancestor.

getBackground

```java
public
Color
getBackground()
```

Gets the background color of this component.

**Returns:** this component's background color; if this component does
not have a background color,
the background color of its parent is returned
**Since:** 1.0
**See Also:** setBackground(java.awt.Color)

---

#### getBackground

public

Color

getBackground()

Gets the background color of this component.

setBackground

```java
public void setBackground​(
Color
c)
```

Sets the background color of this component.

The background color affects each component differently and the
parts of the component that are affected by the background color
may differ between operating systems.

**Parameters:** c

- the color to become this component's color;
if this parameter is

null

, then this
component will inherit the background color of its parent
**Since:** 1.0
**See Also:** getBackground()

---

#### setBackground

public void setBackground​(

Color

c)

Sets the background color of this component.

The background color affects each component differently and the
parts of the component that are affected by the background color
may differ between operating systems.

The background color affects each component differently and the
parts of the component that are affected by the background color
may differ between operating systems.

isBackgroundSet

```java
public boolean isBackgroundSet()
```

Returns whether the background color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its background color from an ancestor.

**Returns:** true

if the background color has been explicitly
set for this Component;

false

otherwise.
**Since:** 1.4

---

#### isBackgroundSet

public boolean isBackgroundSet()

Returns whether the background color has been explicitly set for this
Component. If this method returns

false

, this Component is
inheriting its background color from an ancestor.

getFont

```java
public
Font
getFont()
```

Gets the font of this component.

**Specified by:** getFont

in interface

MenuContainer
**Returns:** this component's font; if a font has not been set
for this component, the font of its parent is returned
**Since:** 1.0
**See Also:** setFont(java.awt.Font)

---

#### getFont

public

Font

getFont()

Gets the font of this component.

setFont

```java
public void setFont​(
Font
f)
```

Sets the font of this component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** f

- the font to become this component's font;
if this parameter is

null

then this
component will inherit the font of its parent
**Since:** 1.0
**See Also:** getFont()

,

invalidate()

---

#### setFont

public void setFont​(

Font

f)

Sets the font of this component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

isFontSet

```java
public boolean isFontSet()
```

Returns whether the font has been explicitly set for this Component. If
this method returns

false

, this Component is inheriting its
font from an ancestor.

**Returns:** true

if the font has been explicitly set for this
Component;

false

otherwise.
**Since:** 1.4

---

#### isFontSet

public boolean isFontSet()

Returns whether the font has been explicitly set for this Component. If
this method returns

false

, this Component is inheriting its
font from an ancestor.

getLocale

```java
public
Locale
getLocale()
```

Gets the locale of this component.

**Returns:** this component's locale; if this component does not
have a locale, the locale of its parent is returned
**Throws:** IllegalComponentStateException

- if the

Component

does not have its own locale and has not yet been added to
a containment hierarchy such that the locale can be determined
from the containing parent
**Since:** 1.1
**See Also:** setLocale(java.util.Locale)

---

#### getLocale

public

Locale

getLocale()

Gets the locale of this component.

setLocale

```java
public void setLocale​(
Locale
l)
```

Sets the locale of this component. This is a bound property.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** l

- the locale to become this component's locale
**Since:** 1.1
**See Also:** getLocale()

,

invalidate()

---

#### setLocale

public void setLocale​(

Locale

l)

Sets the locale of this component. This is a bound property.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

getColorModel

```java
public
ColorModel
getColorModel()
```

Gets the instance of

ColorModel

used to display
the component on the output device.

**Returns:** the color model used by this component
**Since:** 1.0
**See Also:** ColorModel

,

ComponentPeer.getColorModel()

,

Toolkit.getColorModel()

---

#### getColorModel

public

ColorModel

getColorModel()

Gets the instance of

ColorModel

used to display
the component on the output device.

getLocation

```java
public
Point
getLocation()
```

Gets the location of this component in the form of a
point specifying the component's top-left corner.
The location will be relative to the parent's coordinate space.

Due to the asynchronous nature of native event handling, this
method can return outdated values (for instance, after several calls
of

setLocation()

in rapid succession). For this
reason, the recommended method of obtaining a component's position is
within

java.awt.event.ComponentListener.componentMoved()

,
which is called after the operating system has finished moving the
component.

**Returns:** an instance of

Point

representing
the top-left corner of the component's bounds in
the coordinate space of the component's parent
**Since:** 1.1
**See Also:** setLocation(int, int)

,

getLocationOnScreen()

---

#### getLocation

public

Point

getLocation()

Gets the location of this component in the form of a
point specifying the component's top-left corner.
The location will be relative to the parent's coordinate space.

Due to the asynchronous nature of native event handling, this
method can return outdated values (for instance, after several calls
of

setLocation()

in rapid succession). For this
reason, the recommended method of obtaining a component's position is
within

java.awt.event.ComponentListener.componentMoved()

,
which is called after the operating system has finished moving the
component.

Due to the asynchronous nature of native event handling, this
method can return outdated values (for instance, after several calls
of

setLocation()

in rapid succession). For this
reason, the recommended method of obtaining a component's position is
within

java.awt.event.ComponentListener.componentMoved()

,
which is called after the operating system has finished moving the
component.

getLocationOnScreen

```java
public
Point
getLocationOnScreen()
```

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

**Returns:** an instance of

Point

representing
the top-left corner of the component's bounds in the
coordinate space of the screen
**Throws:** IllegalComponentStateException

- if the
component is not showing on the screen
**See Also:** setLocation(int, int)

,

getLocation()

---

#### getLocationOnScreen

public

Point

getLocationOnScreen()

Gets the location of this component in the form of a point
specifying the component's top-left corner in the screen's
coordinate space.

location

```java
@Deprecated

public
Point
location()
```

Deprecated.

As of JDK version 1.1,
replaced by

getLocation()

.

Returns the location of this component's top left corner.

**Returns:** the location of this component's top left corner

---

#### location

@Deprecated

public

Point

location()

Returns the location of this component's top left corner.

setLocation

```java
public void setLocation​(int x,
int y)
```

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Since:** 1.1
**See Also:** getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

---

#### setLocation

public void setLocation​(int x,
int y)

Moves this component to a new location. The top-left corner of
the new location is specified by the

x

and

y

parameters in the coordinate space of this component's parent.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

move

```java
@Deprecated

public void move​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by

setLocation(int, int)

.

Moves this component to a new location.

**Parameters:** x

- the

x

-coordinate of the new location's
top-left corner in the parent's coordinate space
**Parameters:** y

- the

y

-coordinate of the new location's
top-left corner in the parent's coordinate space

---

#### move

@Deprecated

public void move​(int x,
int y)

Moves this component to a new location.

setLocation

```java
public void setLocation​(
Point
p)
```

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** p

- the point defining the top-left corner
of the new location, given in the coordinate space of this
component's parent
**Since:** 1.1
**See Also:** getLocation()

,

setBounds(int, int, int, int)

,

invalidate()

---

#### setLocation

public void setLocation​(

Point

p)

Moves this component to a new location. The top-left corner of
the new location is specified by point

p

. Point

p

is given in the parent's coordinate space.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

getSize

```java
public
Dimension
getSize()
```

Returns the size of this component in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this component's height, and the

width

field of the

Dimension

object contains
this component's width.

**Returns:** a

Dimension

object that indicates the
size of this component
**Since:** 1.1
**See Also:** setSize(int, int)

---

#### getSize

public

Dimension

getSize()

Returns the size of this component in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this component's height, and the

width

field of the

Dimension

object contains
this component's width.

size

```java
@Deprecated

public
Dimension
size()
```

Deprecated.

As of JDK version 1.1,
replaced by

getSize()

.

Returns the size of this component in the form of a

Dimension

object.

**Returns:** the

Dimension

object that indicates the
size of this component

---

#### size

@Deprecated

public

Dimension

size()

Returns the size of this component in the form of a

Dimension

object.

setSize

```java
public void setSize​(int width,
int height)
```

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** width

- the new width of this component in pixels
**Parameters:** height

- the new height of this component in pixels
**Since:** 1.1
**See Also:** getSize()

,

setBounds(int, int, int, int)

,

invalidate()

---

#### setSize

public void setSize​(int width,
int height)

Resizes this component so that it has width

width

and height

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

resize

```java
@Deprecated

public void resize​(int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setSize(int, int)

.

Resizes this component.

**Parameters:** width

- the new width of the component
**Parameters:** height

- the new height of the component

---

#### resize

@Deprecated

public void resize​(int width,
int height)

Resizes this component.

setSize

```java
public void setSize​(
Dimension
d)
```

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** d

- the dimension specifying the new size
of this component
**Throws:** NullPointerException

- if

d

is

null
**Since:** 1.1
**See Also:** setSize(int, int)

,

setBounds(int, int, int, int)

,

invalidate()

---

#### setSize

public void setSize​(

Dimension

d)

Resizes this component so that it has width

d.width

and height

d.height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

resize

```java
@Deprecated

public void resize​(
Dimension
d)
```

Deprecated.

As of JDK version 1.1,
replaced by

setSize(Dimension)

.

Resizes this component so that it has width

d.width

and height

d.height

.

**Parameters:** d

- the new size of this component

---

#### resize

@Deprecated

public void resize​(

Dimension

d)

Resizes this component so that it has width

d.width

and height

d.height

.

getBounds

```java
public
Rectangle
getBounds()
```

Gets the bounds of this component in the form of a

Rectangle

object. The bounds specify this
component's width, height, and location relative to
its parent.

**Returns:** a rectangle indicating this component's bounds
**See Also:** setBounds(int, int, int, int)

,

getLocation()

,

getSize()

---

#### getBounds

public

Rectangle

getBounds()

Gets the bounds of this component in the form of a

Rectangle

object. The bounds specify this
component's width, height, and location relative to
its parent.

bounds

```java
@Deprecated

public
Rectangle
bounds()
```

Deprecated.

As of JDK version 1.1,
replaced by

getBounds()

.

Returns the bounding rectangle of this component.

**Returns:** the bounding rectangle for this component

---

#### bounds

@Deprecated

public

Rectangle

bounds()

Returns the bounding rectangle of this component.

setBounds

```java
public void setBounds​(int x,
int y,
int width,
int height)
```

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** x

- the new

x

-coordinate of this component
**Parameters:** y

- the new

y

-coordinate of this component
**Parameters:** width

- the new

width

of this component
**Parameters:** height

- the new

height

of this
component
**Since:** 1.1
**See Also:** getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

---

#### setBounds

public void setBounds​(int x,
int y,
int width,
int height)

Moves and resizes this component. The new location of the top-left
corner is specified by

x

and

y

, and the
new size is specified by

width

and

height

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

reshape

```java
@Deprecated

public void reshape​(int x,
int y,
int width,
int height)
```

Deprecated.

As of JDK version 1.1,
replaced by

setBounds(int, int, int, int)

.

Reshapes the bounding rectangle for this component.

**Parameters:** x

- the

x

coordinate of the upper left corner of the rectangle
**Parameters:** y

- the

y

coordinate of the upper left corner of the rectangle
**Parameters:** width

- the width of the rectangle
**Parameters:** height

- the height of the rectangle

---

#### reshape

@Deprecated

public void reshape​(int x,
int y,
int width,
int height)

Reshapes the bounding rectangle for this component.

setBounds

```java
public void setBounds​(
Rectangle
r)
```

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** r

- the new bounding rectangle for this component
**Throws:** NullPointerException

- if

r

is

null
**Since:** 1.1
**See Also:** getBounds()

,

setLocation(int, int)

,

setLocation(Point)

,

setSize(int, int)

,

setSize(Dimension)

,

invalidate()

---

#### setBounds

public void setBounds​(

Rectangle

r)

Moves and resizes this component to conform to the new
bounding rectangle

r

. This component's new
position is specified by

r.x

and

r.y

,
and its new size is specified by

r.width

and

r.height

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

getX

```java
public int getX()
```

Returns the current x coordinate of the components origin.
This method is preferable to writing

component.getBounds().x

,
or

component.getLocation().x

because it doesn't
cause any heap allocations.

**Returns:** the current x coordinate of the components origin
**Since:** 1.2

---

#### getX

public int getX()

Returns the current x coordinate of the components origin.
This method is preferable to writing

component.getBounds().x

,
or

component.getLocation().x

because it doesn't
cause any heap allocations.

getY

```java
public int getY()
```

Returns the current y coordinate of the components origin.
This method is preferable to writing

component.getBounds().y

,
or

component.getLocation().y

because it
doesn't cause any heap allocations.

**Returns:** the current y coordinate of the components origin
**Since:** 1.2

---

#### getY

public int getY()

Returns the current y coordinate of the components origin.
This method is preferable to writing

component.getBounds().y

,
or

component.getLocation().y

because it
doesn't cause any heap allocations.

getWidth

```java
public int getWidth()
```

Returns the current width of this component.
This method is preferable to writing

component.getBounds().width

,
or

component.getSize().width

because it
doesn't cause any heap allocations.

**Returns:** the current width of this component
**Since:** 1.2

---

#### getWidth

public int getWidth()

Returns the current width of this component.
This method is preferable to writing

component.getBounds().width

,
or

component.getSize().width

because it
doesn't cause any heap allocations.

getHeight

```java
public int getHeight()
```

Returns the current height of this component.
This method is preferable to writing

component.getBounds().height

,
or

component.getSize().height

because it
doesn't cause any heap allocations.

**Returns:** the current height of this component
**Since:** 1.2

---

#### getHeight

public int getHeight()

Returns the current height of this component.
This method is preferable to writing

component.getBounds().height

,
or

component.getSize().height

because it
doesn't cause any heap allocations.

getBounds

```java
public
Rectangle
getBounds​(
Rectangle
rv)
```

Stores the bounds of this component into "return value"

rv

and
return

rv

. If rv is

null

a new

Rectangle

is allocated.
This version of

getBounds

is useful if the caller
wants to avoid allocating a new

Rectangle

object
on the heap.

**Parameters:** rv

- the return value, modified to the components bounds
**Returns:** rv

---

#### getBounds

public

Rectangle

getBounds​(

Rectangle

rv)

Stores the bounds of this component into "return value"

rv

and
return

rv

. If rv is

null

a new

Rectangle

is allocated.
This version of

getBounds

is useful if the caller
wants to avoid allocating a new

Rectangle

object
on the heap.

getSize

```java
public
Dimension
getSize​(
Dimension
rv)
```

Stores the width/height of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Dimension

object is allocated. This version of

getSize

is useful if the caller wants to avoid
allocating a new

Dimension

object on the heap.

**Parameters:** rv

- the return value, modified to the components size
**Returns:** rv

---

#### getSize

public

Dimension

getSize​(

Dimension

rv)

Stores the width/height of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Dimension

object is allocated. This version of

getSize

is useful if the caller wants to avoid
allocating a new

Dimension

object on the heap.

getLocation

```java
public
Point
getLocation​(
Point
rv)
```

Stores the x,y origin of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Point

is allocated.
This version of

getLocation

is useful if the
caller wants to avoid allocating a new

Point

object on the heap.

**Parameters:** rv

- the return value, modified to the components location
**Returns:** rv

---

#### getLocation

public

Point

getLocation​(

Point

rv)

Stores the x,y origin of this component into "return value"

rv

and return

rv

. If rv is

null

a new

Point

is allocated.
This version of

getLocation

is useful if the
caller wants to avoid allocating a new

Point

object on the heap.

isOpaque

```java
public boolean isOpaque()
```

Returns true if this component is completely opaque, returns
false by default.

An opaque component paints every pixel within its
rectangular region. A non-opaque component paints only some of
its pixels, allowing the pixels underneath it to "show through".
A component that does not fully paint its pixels therefore
provides a degree of transparency.

Subclasses that guarantee to always completely paint their
contents should override this method and return true.

**Returns:** true if this component is completely opaque
**Since:** 1.2
**See Also:** isLightweight()

---

#### isOpaque

public boolean isOpaque()

Returns true if this component is completely opaque, returns
false by default.

An opaque component paints every pixel within its
rectangular region. A non-opaque component paints only some of
its pixels, allowing the pixels underneath it to "show through".
A component that does not fully paint its pixels therefore
provides a degree of transparency.

Subclasses that guarantee to always completely paint their
contents should override this method and return true.

An opaque component paints every pixel within its
rectangular region. A non-opaque component paints only some of
its pixels, allowing the pixels underneath it to "show through".
A component that does not fully paint its pixels therefore
provides a degree of transparency.

Subclasses that guarantee to always completely paint their
contents should override this method and return true.

Subclasses that guarantee to always completely paint their
contents should override this method and return true.

isLightweight

```java
public boolean isLightweight()
```

A lightweight component doesn't have a native toolkit peer.
Subclasses of

Component

and

Container

,
other than the ones defined in this package like

Button

or

Scrollbar

, are lightweight.
All of the Swing components are lightweights.

This method will always return

false

if this component
is not displayable because it is impossible to determine the
weight of an undisplayable component.

**Returns:** true if this component has a lightweight peer; false if
it has a native peer or no peer
**Since:** 1.2
**See Also:** isDisplayable()

---

#### isLightweight

public boolean isLightweight()

A lightweight component doesn't have a native toolkit peer.
Subclasses of

Component

and

Container

,
other than the ones defined in this package like

Button

or

Scrollbar

, are lightweight.
All of the Swing components are lightweights.

This method will always return

false

if this component
is not displayable because it is impossible to determine the
weight of an undisplayable component.

This method will always return

false

if this component
is not displayable because it is impossible to determine the
weight of an undisplayable component.

setPreferredSize

```java
public void setPreferredSize​(
Dimension
preferredSize)
```

Sets the preferred size of this component to a constant
value. Subsequent calls to

getPreferredSize

will always
return this value. Setting the preferred size to

null

restores the default behavior.

**Parameters:** preferredSize

- The new preferred size, or null
**Since:** 1.5
**See Also:** getPreferredSize()

,

isPreferredSizeSet()

---

#### setPreferredSize

public void setPreferredSize​(

Dimension

preferredSize)

Sets the preferred size of this component to a constant
value. Subsequent calls to

getPreferredSize

will always
return this value. Setting the preferred size to

null

restores the default behavior.

isPreferredSizeSet

```java
public boolean isPreferredSizeSet()
```

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

**Returns:** true if

setPreferredSize

has been invoked
with a non-null value.
**Since:** 1.5

---

#### isPreferredSizeSet

public boolean isPreferredSizeSet()

Returns true if the preferred size has been set to a
non-

null

value otherwise returns false.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Gets the preferred size of this component.

**Returns:** a dimension object indicating this component's preferred size
**See Also:** getMinimumSize()

,

LayoutManager

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Gets the preferred size of this component.

preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Returns the component's preferred size.

**Returns:** the component's preferred size

---

#### preferredSize

@Deprecated

public

Dimension

preferredSize()

Returns the component's preferred size.

setMinimumSize

```java
public void setMinimumSize​(
Dimension
minimumSize)
```

Sets the minimum size of this component to a constant
value. Subsequent calls to

getMinimumSize

will always
return this value. Setting the minimum size to

null

restores the default behavior.

**Parameters:** minimumSize

- the new minimum size of this component
**Since:** 1.5
**See Also:** getMinimumSize()

,

isMinimumSizeSet()

---

#### setMinimumSize

public void setMinimumSize​(

Dimension

minimumSize)

Sets the minimum size of this component to a constant
value. Subsequent calls to

getMinimumSize

will always
return this value. Setting the minimum size to

null

restores the default behavior.

isMinimumSizeSet

```java
public boolean isMinimumSizeSet()
```

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

**Returns:** true if

setMinimumSize

has been invoked with a
non-null value.
**Since:** 1.5

---

#### isMinimumSizeSet

public boolean isMinimumSizeSet()

Returns whether or not

setMinimumSize

has been
invoked with a non-null value.

getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Gets the minimum size of this component.

**Returns:** a dimension object indicating this component's minimum size
**See Also:** getPreferredSize()

,

LayoutManager

---

#### getMinimumSize

public

Dimension

getMinimumSize()

Gets the minimum size of this component.

minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Returns the minimum size of this component.

**Returns:** the minimum size of this component

---

#### minimumSize

@Deprecated

public

Dimension

minimumSize()

Returns the minimum size of this component.

setMaximumSize

```java
public void setMaximumSize​(
Dimension
maximumSize)
```

Sets the maximum size of this component to a constant
value. Subsequent calls to

getMaximumSize

will always
return this value. Setting the maximum size to

null

restores the default behavior.

**Parameters:** maximumSize

- a

Dimension

containing the
desired maximum allowable size
**Since:** 1.5
**See Also:** getMaximumSize()

,

isMaximumSizeSet()

---

#### setMaximumSize

public void setMaximumSize​(

Dimension

maximumSize)

Sets the maximum size of this component to a constant
value. Subsequent calls to

getMaximumSize

will always
return this value. Setting the maximum size to

null

restores the default behavior.

isMaximumSizeSet

```java
public boolean isMaximumSizeSet()
```

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

**Returns:** true if

maximumSize

is non-

null

,
false otherwise
**Since:** 1.5

---

#### isMaximumSizeSet

public boolean isMaximumSizeSet()

Returns true if the maximum size has been set to a non-

null

value otherwise returns false.

getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Gets the maximum size of this component.

**Returns:** a dimension object indicating this component's maximum size
**See Also:** getMinimumSize()

,

getPreferredSize()

,

LayoutManager

---

#### getMaximumSize

public

Dimension

getMaximumSize()

Gets the maximum size of this component.

getAlignmentX

```java
public float getAlignmentX()
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:** the horizontal alignment of this component

---

#### getAlignmentX

public float getAlignmentX()

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

getAlignmentY

```java
public float getAlignmentY()
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Returns:** the vertical alignment of this component

---

#### getAlignmentY

public float getAlignmentY()

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

getBaseline

```java
public int getBaseline​(int width,
int height)
```

Returns the baseline. The baseline is measured from the top of
the component. This method is primarily meant for

LayoutManager

s to align components along their
baseline. A return value less than 0 indicates this component
does not have a reasonable baseline and that

LayoutManager

s should not align this component on
its baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** getBaselineResizeBehavior()

,

FontMetrics

---

#### getBaseline

public int getBaseline​(int width,
int height)

Returns the baseline. The baseline is measured from the top of
the component. This method is primarily meant for

LayoutManager

s to align components along their
baseline. A return value less than 0 indicates this component
does not have a reasonable baseline and that

LayoutManager

s should not align this component on
its baseline.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

The default implementation returns -1. Subclasses that support
baseline should override appropriately. If a value >= 0 is
returned, then the component has a valid baseline for any
size >= the minimum size and

getBaselineResizeBehavior

can be used to determine how the baseline changes with size.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior()
```

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

. Subclasses that have a
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

**Returns:** an enum indicating how the baseline changes as the component
size changes
**Since:** 1.6
**See Also:** getBaseline(int, int)

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior()

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

The default implementation returns

BaselineResizeBehavior.OTHER

. Subclasses that have a
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

The default implementation returns

BaselineResizeBehavior.OTHER

. Subclasses that have a
baseline should override appropriately. Subclasses should
never return

null

; if the baseline can not be
calculated return

BaselineResizeBehavior.OTHER

. Callers
should first ask for the baseline using

getBaseline

and if a value >= 0 is returned use
this method. It is acceptable for this method to return a
value other than

BaselineResizeBehavior.OTHER

even if

getBaseline

returns a value less than 0.

doLayout

```java
public void doLayout()
```

Prompts the layout manager to lay out this component. This is
usually called when the component (more specifically, container)
is validated.

**See Also:** validate()

,

LayoutManager

---

#### doLayout

public void doLayout()

Prompts the layout manager to lay out this component. This is
usually called when the component (more specifically, container)
is validated.

layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

---

#### layout

@Deprecated

public void layout()

validate

```java
public void validate()
```

Validates this component.

The meaning of the term

validating

is defined by the ancestors of
this class. See

Container.validate()

for more details.

**Since:** 1.0
**See Also:** invalidate()

,

doLayout()

,

LayoutManager

,

Container.validate()

---

#### validate

public void validate()

Validates this component.

The meaning of the term

validating

is defined by the ancestors of
this class. See

Container.validate()

for more details.

The meaning of the term

validating

is defined by the ancestors of
this class. See

Container.validate()

for more details.

invalidate

```java
public void invalidate()
```

Invalidates this component and its ancestors.

By default, all the ancestors of the component up to the top-most
container of the hierarchy are marked invalid. If the

java.awt.smartInvalidate

system property is set to

true

,
invalidation stops on the nearest validate root of this component.
Marking a container

invalid

indicates that the container needs to
be laid out.

This method is called automatically when any layout-related information
changes (e.g. setting the bounds of the component, or adding the
component to a container).

This method might be called often, so it should work fast.

**Since:** 1.0
**See Also:** validate()

,

doLayout()

,

LayoutManager

,

Container.isValidateRoot()

---

#### invalidate

public void invalidate()

Invalidates this component and its ancestors.

By default, all the ancestors of the component up to the top-most
container of the hierarchy are marked invalid. If the

java.awt.smartInvalidate

system property is set to

true

,
invalidation stops on the nearest validate root of this component.
Marking a container

invalid

indicates that the container needs to
be laid out.

This method is called automatically when any layout-related information
changes (e.g. setting the bounds of the component, or adding the
component to a container).

This method might be called often, so it should work fast.

By default, all the ancestors of the component up to the top-most
container of the hierarchy are marked invalid. If the

java.awt.smartInvalidate

system property is set to

true

,
invalidation stops on the nearest validate root of this component.
Marking a container

invalid

indicates that the container needs to
be laid out.

This method is called automatically when any layout-related information
changes (e.g. setting the bounds of the component, or adding the
component to a container).

This method might be called often, so it should work fast.

This method is called automatically when any layout-related information
changes (e.g. setting the bounds of the component, or adding the
component to a container).

This method might be called often, so it should work fast.

This method might be called often, so it should work fast.

revalidate

```java
public void revalidate()
```

Revalidates the component hierarchy up to the nearest validate root.

This method first invalidates the component hierarchy starting from this
component up to the nearest validate root. Afterwards, the component
hierarchy is validated starting from the nearest validate root.

This is a convenience method supposed to help application developers
avoid looking for validate roots manually. Basically, it's equivalent to
first calling the

invalidate()

method on this component, and
then calling the

validate()

method on the nearest validate
root.

**Since:** 1.7
**See Also:** Container.isValidateRoot()

---

#### revalidate

public void revalidate()

Revalidates the component hierarchy up to the nearest validate root.

This method first invalidates the component hierarchy starting from this
component up to the nearest validate root. Afterwards, the component
hierarchy is validated starting from the nearest validate root.

This is a convenience method supposed to help application developers
avoid looking for validate roots manually. Basically, it's equivalent to
first calling the

invalidate()

method on this component, and
then calling the

validate()

method on the nearest validate
root.

This method first invalidates the component hierarchy starting from this
component up to the nearest validate root. Afterwards, the component
hierarchy is validated starting from the nearest validate root.

This is a convenience method supposed to help application developers
avoid looking for validate roots manually. Basically, it's equivalent to
first calling the

invalidate()

method on this component, and
then calling the

validate()

method on the nearest validate
root.

This is a convenience method supposed to help application developers
avoid looking for validate roots manually. Basically, it's equivalent to
first calling the

invalidate()

method on this component, and
then calling the

validate()

method on the nearest validate
root.

getGraphics

```java
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

---

#### getGraphics

public

Graphics

getGraphics()

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
font)
```

Gets the font metrics for the specified font.
Warning: Since Font metrics are affected by the

FontRenderContext

and
this method does not provide one, it can return only metrics for
the default render context which may not match that used when
rendering on the Component if

Graphics2D

functionality is being
used. Instead metrics can be obtained at rendering time by calling

Graphics.getFontMetrics()

or text measurement APIs on the

Font

class.

**Parameters:** font

- the font for which font metrics is to be
obtained
**Returns:** the font metrics for

font
**Since:** 1.0
**See Also:** getFont()

,

ComponentPeer.getFontMetrics(Font)

,

Toolkit.getFontMetrics(Font)

---

#### getFontMetrics

public

FontMetrics

getFontMetrics​(

Font

font)

Gets the font metrics for the specified font.
Warning: Since Font metrics are affected by the

FontRenderContext

and
this method does not provide one, it can return only metrics for
the default render context which may not match that used when
rendering on the Component if

Graphics2D

functionality is being
used. Instead metrics can be obtained at rendering time by calling

Graphics.getFontMetrics()

or text measurement APIs on the

Font

class.

setCursor

```java
public void setCursor​(
Cursor
cursor)
```

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

**Parameters:** cursor

- One of the constants defined
by the

Cursor

class;
if this parameter is

null

then this component will inherit
the cursor of its parent
**Since:** 1.1
**See Also:** isEnabled()

,

isShowing()

,

getCursor()

,

contains(int, int)

,

Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

,

Cursor

---

#### setCursor

public void setCursor​(

Cursor

cursor)

Sets the cursor image to the specified cursor. This cursor
image is displayed when the

contains

method for
this component returns true for the current cursor location, and
this Component is visible, displayable, and enabled. Setting the
cursor of a

Container

causes that cursor to be displayed
within all of the container's subcomponents, except for those
that have a non-

null

cursor.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

The method may have no visual effect if the Java platform
implementation and/or the native system do not support
changing the mouse cursor shape.

getCursor

```java
public
Cursor
getCursor()
```

Gets the cursor set in the component. If the component does
not have a cursor set, the cursor of its parent is returned.
If no cursor is set in the entire hierarchy,

Cursor.DEFAULT_CURSOR

is returned.

**Returns:** the cursor for this component
**Since:** 1.1
**See Also:** setCursor(java.awt.Cursor)

---

#### getCursor

public

Cursor

getCursor()

Gets the cursor set in the component. If the component does
not have a cursor set, the cursor of its parent is returned.
If no cursor is set in the entire hierarchy,

Cursor.DEFAULT_CURSOR

is returned.

isCursorSet

```java
public boolean isCursorSet()
```

Returns whether the cursor has been explicitly set for this Component.
If this method returns

false

, this Component is inheriting
its cursor from an ancestor.

**Returns:** true

if the cursor has been explicitly set for this
Component;

false

otherwise.
**Since:** 1.4

---

#### isCursorSet

public boolean isCursorSet()

Returns whether the cursor has been explicitly set for this Component.
If this method returns

false

, this Component is inheriting
its cursor from an ancestor.

paint

```java
public void paint​(
Graphics
g)
```

Paints this component.

This method is called when the contents of the component should
be painted; such as when the component is first being shown or
is damaged and in need of repair. The clip rectangle in the

Graphics

parameter is set to the area
which needs to be painted.
Subclasses of

Component

that override this
method need not call

super.paint(g)

.

For performance reasons,

Component

s with zero width
or height aren't considered to need painting when they are first shown,
and also aren't considered to need repair.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** g

- the graphics context to use for painting
**Since:** 1.0
**See Also:** update(java.awt.Graphics)

---

#### paint

public void paint​(

Graphics

g)

Paints this component.

This method is called when the contents of the component should
be painted; such as when the component is first being shown or
is damaged and in need of repair. The clip rectangle in the

Graphics

parameter is set to the area
which needs to be painted.
Subclasses of

Component

that override this
method need not call

super.paint(g)

.

For performance reasons,

Component

s with zero width
or height aren't considered to need painting when they are first shown,
and also aren't considered to need repair.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

This method is called when the contents of the component should
be painted; such as when the component is first being shown or
is damaged and in need of repair. The clip rectangle in the

Graphics

parameter is set to the area
which needs to be painted.
Subclasses of

Component

that override this
method need not call

super.paint(g)

.

For performance reasons,

Component

s with zero width
or height aren't considered to need painting when they are first shown,
and also aren't considered to need repair.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

For performance reasons,

Component

s with zero width
or height aren't considered to need painting when they are first shown,
and also aren't considered to need repair.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

update

```java
public void update​(
Graphics
g)
```

Updates this component.

If this component is not a lightweight component, the
AWT calls the

update

method in response to
a call to

repaint

. You can assume that
the background is not cleared.

The

update

method of

Component

calls this component's

paint

method to redraw
this component. This method is commonly overridden by subclasses
which need to do additional work in response to a call to

repaint

.
Subclasses of Component that override this method should either
call

super.update(g)

, or call

paint(g)

directly from their

update

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** g

- the specified context to use for updating
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

,

repaint()

---

#### update

public void update​(

Graphics

g)

Updates this component.

If this component is not a lightweight component, the
AWT calls the

update

method in response to
a call to

repaint

. You can assume that
the background is not cleared.

The

update

method of

Component

calls this component's

paint

method to redraw
this component. This method is commonly overridden by subclasses
which need to do additional work in response to a call to

repaint

.
Subclasses of Component that override this method should either
call

super.update(g)

, or call

paint(g)

directly from their

update

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

If this component is not a lightweight component, the
AWT calls the

update

method in response to
a call to

repaint

. You can assume that
the background is not cleared.

The

update

method of

Component

calls this component's

paint

method to redraw
this component. This method is commonly overridden by subclasses
which need to do additional work in response to a call to

repaint

.
Subclasses of Component that override this method should either
call

super.update(g)

, or call

paint(g)

directly from their

update

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

The

update

method of

Component

calls this component's

paint

method to redraw
this component. This method is commonly overridden by subclasses
which need to do additional work in response to a call to

repaint

.
Subclasses of Component that override this method should either
call

super.update(g)

, or call

paint(g)

directly from their

update

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

paintAll

```java
public void paintAll​(
Graphics
g)
```

Paints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for painting
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

---

#### paintAll

public void paintAll​(

Graphics

g)

Paints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

repaint

```java
public void repaint()
```

Repaints this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method as soon as possible. Otherwise, this method causes
a call to this component's

update

method as soon
as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Since:** 1.0
**See Also:** update(Graphics)

---

#### repaint

public void repaint()

Repaints this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method as soon as possible. Otherwise, this method causes
a call to this component's

update

method as soon
as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

If this component is a lightweight component, this method
causes a call to this component's

paint

method as soon as possible. Otherwise, this method causes
a call to this component's

update

method as soon
as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

repaint

```java
public void repaint​(long tm)
```

Repaints the component. If this component is a lightweight
component, this results in a call to

paint

within

tm

milliseconds.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** tm

- maximum time in milliseconds before update
**Since:** 1.0
**See Also:** paint(java.awt.Graphics)

,

update(Graphics)

---

#### repaint

public void repaint​(long tm)

Repaints the component. If this component is a lightweight
component, this results in a call to

paint

within

tm

milliseconds.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

repaint

```java
public void repaint​(int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method
as soon as possible. Otherwise, this method causes a call to
this component's

update

method as soon as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.0
**See Also:** update(Graphics)

---

#### repaint

public void repaint​(int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component.

If this component is a lightweight component, this method
causes a call to this component's

paint

method
as soon as possible. Otherwise, this method causes a call to
this component's

update

method as soon as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

If this component is a lightweight component, this method
causes a call to this component's

paint

method
as soon as possible. Otherwise, this method causes a call to
this component's

update

method as soon as possible.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

tm

milliseconds.

If this component is a lightweight component, this method causes
a call to this component's

paint

method.
Otherwise, this method causes a call to this component's

update

method.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

**Parameters:** tm

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.0
**See Also:** update(Graphics)

---

#### repaint

public void repaint​(long tm,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

tm

milliseconds.

If this component is a lightweight component, this method causes
a call to this component's

paint

method.
Otherwise, this method causes a call to this component's

update

method.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

If this component is a lightweight component, this method causes
a call to this component's

paint

method.
Otherwise, this method causes a call to this component's

update

method.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

Note

: For more information on the paint mechanisms utilitized
by AWT and Swing, including information on how to write the most
efficient painting code, see

Painting in AWT and Swing

.

print

```java
public void print​(
Graphics
g)
```

Prints this component. Applications should override this method
for components that must do special processing before being
printed or should be printed differently than they are painted.

The default implementation of this method calls the

paint

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for printing
**Since:** 1.0
**See Also:** paint(Graphics)

---

#### print

public void print​(

Graphics

g)

Prints this component. Applications should override this method
for components that must do special processing before being
printed or should be printed differently than they are painted.

The default implementation of this method calls the

paint

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

The default implementation of this method calls the

paint

method.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

printAll

```java
public void printAll​(
Graphics
g)
```

Prints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

**Parameters:** g

- the graphics context to use for printing
**Since:** 1.0
**See Also:** print(Graphics)

---

#### printAll

public void printAll​(

Graphics

g)

Prints this component and all of its subcomponents.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

The origin of the graphics context, its
(

0

,

0

) coordinate point, is the
top-left corner of this component. The clipping region of the
graphics context is the bounding rectangle of this component.

imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:** imageUpdate

in interface

ImageObserver
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**Since:** 1.0
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### imageUpdate

public boolean imageUpdate​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

createImage

```java
public
Image
createImage​(
ImageProducer
producer)
```

Creates an image from the specified image producer.

**Parameters:** producer

- the image producer
**Returns:** the image produced
**Since:** 1.0

---

#### createImage

public

Image

createImage​(

ImageProducer

producer)

Creates an image from the specified image producer.

createImage

```java
public
Image
createImage​(int width,
int height)
```

Creates an off-screen drawable image to be used for double buffering.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Returns:** an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.0
**See Also:** isDisplayable()

,

GraphicsEnvironment.isHeadless()

---

#### createImage

public

Image

createImage​(int width,
int height)

Creates an off-screen drawable image to be used for double buffering.

createVolatileImage

```java
public
VolatileImage
createVolatileImage​(int width,
int height)
```

Creates a volatile off-screen drawable image to be used for double
buffering.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Returns:** an off-screen drawable image, which can be used for double
buffering. The

null

value if the component is not
displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** VolatileImage

,

isDisplayable()

,

GraphicsEnvironment.isHeadless()

---

#### createVolatileImage

public

VolatileImage

createVolatileImage​(int width,
int height)

Creates a volatile off-screen drawable image to be used for double
buffering.

createVolatileImage

```java
public
VolatileImage
createVolatileImage​(int width,
int height,

ImageCapabilities
caps)
throws
AWTException
```

Creates a volatile off-screen drawable image, with the given
capabilities. The contents of this image may be lost at any time due to
operating system issues, so the image must be managed via the

VolatileImage

interface.

**Parameters:** width

- the specified width
**Parameters:** height

- the specified height
**Parameters:** caps

- the image capabilities
**Returns:** a VolatileImage object, which can be used to manage surface
contents loss and capabilities. The

null

value if the
component is not displayable or

GraphicsEnvironment.isHeadless()

returns

true

.
**Throws:** AWTException

- if an image with the specified capabilities cannot
be created
**Since:** 1.4
**See Also:** VolatileImage

---

#### createVolatileImage

public

VolatileImage

createVolatileImage​(int width,
int height,

ImageCapabilities

caps)
throws

AWTException

Creates a volatile off-screen drawable image, with the given
capabilities. The contents of this image may be lost at any time due to
operating system issues, so the image must be managed via the

VolatileImage

interface.

prepareImage

```java
public boolean prepareImage​(
Image
image,

ImageObserver
observer)
```

Prepares an image for rendering on this component. The image
data is downloaded asynchronously in another thread and the
appropriate screen representation of the image is generated.

**Parameters:** image

- the

Image

for which to
prepare a screen representation
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** true

if the image has already been fully
prepared;

false

otherwise
**Since:** 1.0

---

#### prepareImage

public boolean prepareImage​(

Image

image,

ImageObserver

observer)

Prepares an image for rendering on this component. The image
data is downloaded asynchronously in another thread and the
appropriate screen representation of the image is generated.

prepareImage

```java
public boolean prepareImage​(
Image
image,
int width,
int height,

ImageObserver
observer)
```

Prepares an image for rendering on this component at the
specified width and height.

The image data is downloaded asynchronously in another thread,
and an appropriately scaled screen representation of the image is
generated.

**Parameters:** image

- the instance of

Image

for which to prepare a screen representation
**Parameters:** width

- the width of the desired screen representation
**Parameters:** height

- the height of the desired screen representation
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** true

if the image has already been fully
prepared;

false

otherwise
**Since:** 1.0
**See Also:** ImageObserver

---

#### prepareImage

public boolean prepareImage​(

Image

image,
int width,
int height,

ImageObserver

observer)

Prepares an image for rendering on this component at the
specified width and height.

The image data is downloaded asynchronously in another thread,
and an appropriately scaled screen representation of the image is
generated.

The image data is downloaded asynchronously in another thread,
and an appropriately scaled screen representation of the image is
generated.

checkImage

```java
public int checkImage​(
Image
image,

ImageObserver
observer)
```

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:** image

- the

Image

object whose status
is being checked
**Parameters:** observer

- the

ImageObserver

object to be notified as the image is being prepared
**Returns:** the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available
**Since:** 1.0
**See Also:** prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

---

#### checkImage

public int checkImage​(

Image

image,

ImageObserver

observer)

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

checkImage

```java
public int checkImage​(
Image
image,
int width,
int height,

ImageObserver
observer)
```

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

The

checkImage

method of

Component

calls its peer's

checkImage

method to calculate
the flags. If this component does not yet have a peer, the
component's toolkit's

checkImage

method is called
instead.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

**Parameters:** image

- the

Image

object whose status
is being checked
**Parameters:** width

- the width of the scaled version
whose status is to be checked
**Parameters:** height

- the height of the scaled version
whose status is to be checked
**Parameters:** observer

- the

ImageObserver

object
to be notified as the image is being prepared
**Returns:** the bitwise inclusive

OR

of

ImageObserver

flags indicating what
information about the image is currently available
**Since:** 1.0
**See Also:** prepareImage(Image, int, int, java.awt.image.ImageObserver)

,

Toolkit.checkImage(Image, int, int, java.awt.image.ImageObserver)

,

ImageObserver

---

#### checkImage

public int checkImage​(

Image

image,
int width,
int height,

ImageObserver

observer)

Returns the status of the construction of a screen representation
of the specified image.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

The

checkImage

method of

Component

calls its peer's

checkImage

method to calculate
the flags. If this component does not yet have a peer, the
component's toolkit's

checkImage

method is called
instead.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

This method does not cause the image to begin loading. An
application must use the

prepareImage

method
to force the loading of an image.

The

checkImage

method of

Component

calls its peer's

checkImage

method to calculate
the flags. If this component does not yet have a peer, the
component's toolkit's

checkImage

method is called
instead.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

The

checkImage

method of

Component

calls its peer's

checkImage

method to calculate
the flags. If this component does not yet have a peer, the
component's toolkit's

checkImage

method is called
instead.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

Information on the flags returned by this method can be found
with the discussion of the

ImageObserver

interface.

setIgnoreRepaint

```java
public void setIgnoreRepaint​(boolean ignoreRepaint)
```

Sets whether or not paint messages received from the operating system
should be ignored. This does not affect paint events generated in
software by the AWT, unless they are an immediate response to an
OS-level paint message.

This is useful, for example, if running under full-screen mode and
better performance is desired, or if page-flipping is used as the
buffer strategy.

**Parameters:** ignoreRepaint

-

true

if the paint messages from the OS
should be ignored; otherwise

false
**Since:** 1.4
**See Also:** getIgnoreRepaint()

,

Canvas.createBufferStrategy(int)

,

Window.createBufferStrategy(int)

,

BufferStrategy

,

GraphicsDevice.setFullScreenWindow(java.awt.Window)

---

#### setIgnoreRepaint

public void setIgnoreRepaint​(boolean ignoreRepaint)

Sets whether or not paint messages received from the operating system
should be ignored. This does not affect paint events generated in
software by the AWT, unless they are an immediate response to an
OS-level paint message.

This is useful, for example, if running under full-screen mode and
better performance is desired, or if page-flipping is used as the
buffer strategy.

This is useful, for example, if running under full-screen mode and
better performance is desired, or if page-flipping is used as the
buffer strategy.

getIgnoreRepaint

```java
public boolean getIgnoreRepaint()
```

**Returns:** whether or not paint messages received from the operating system
should be ignored.
**Since:** 1.4
**See Also:** setIgnoreRepaint(boolean)

---

#### getIgnoreRepaint

public boolean getIgnoreRepaint()

contains

```java
public boolean contains​(int x,
int y)
```

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the point is within the component;
otherwise

false
**Since:** 1.1
**See Also:** getComponentAt(int, int)

---

#### contains

public boolean contains​(int x,
int y)

Checks whether this component "contains" the specified point,
where

x

and

y

are defined to be
relative to the coordinate system of this component.

inside

```java
@Deprecated

public boolean inside​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by contains(int, int).

Checks whether the point is inside of this component.

**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the point is within the component;
otherwise

false

---

#### inside

@Deprecated

public boolean inside​(int x,
int y)

Checks whether the point is inside of this component.

contains

```java
public boolean contains​(
Point
p)
```

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

**Parameters:** p

- the point
**Returns:** true

if the point is within the component;
otherwise

false
**Throws:** NullPointerException

- if

p

is

null
**Since:** 1.1
**See Also:** getComponentAt(Point)

---

#### contains

public boolean contains​(

Point

p)

Checks whether this component "contains" the specified point,
where the point's

x

and

y

coordinates are defined
to be relative to the coordinate system of this component.

getComponentAt

```java
public
Component
getComponentAt​(int x,
int y)
```

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component. This method only
looks one level deep. If the point (

x

,

y

) is
inside a subcomponent that itself has subcomponents, it does not
go looking down the subcomponent tree.

The

locate

method of

Component

simply
returns the component itself if the (

x

,

y

)
coordinate location is inside its bounding box, and

null

otherwise.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** the component or subcomponent that contains the
(

x

,

y

) location;

null

if the location
is outside this component
**Since:** 1.0
**See Also:** contains(int, int)

---

#### getComponentAt

public

Component

getComponentAt​(int x,
int y)

Determines if this component or one of its immediate
subcomponents contains the (

x

,

y

) location,
and if so, returns the containing component. This method only
looks one level deep. If the point (

x

,

y

) is
inside a subcomponent that itself has subcomponents, it does not
go looking down the subcomponent tree.

The

locate

method of

Component

simply
returns the component itself if the (

x

,

y

)
coordinate location is inside its bounding box, and

null

otherwise.

The

locate

method of

Component

simply
returns the component itself if the (

x

,

y

)
coordinate location is inside its bounding box, and

null

otherwise.

locate

```java
@Deprecated

public
Component
locate​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by getComponentAt(int, int).

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

**Parameters:** x

- the

x

coordinate to search for components at
**Parameters:** y

- the

y

coordinate to search for components at
**Returns:** the component at the specified location or

null

---

#### locate

@Deprecated

public

Component

locate​(int x,
int y)

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

getComponentAt

```java
public
Component
getComponentAt​(
Point
p)
```

Returns the component or subcomponent that contains the
specified point.

**Parameters:** p

- the point
**Returns:** the component at the specified location or

null
**Since:** 1.1
**See Also:** contains(int, int)

---

#### getComponentAt

public

Component

getComponentAt​(

Point

p)

Returns the component or subcomponent that contains the
specified point.

deliverEvent

```java
@Deprecated

public void deliverEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

.

**Parameters:** e

- the event to deliver

---

#### deliverEvent

@Deprecated

public void deliverEvent​(

Event

e)

dispatchEvent

```java
public final void dispatchEvent​(
AWTEvent
e)
```

Dispatches an event to this component or one of its sub components.
Calls

processEvent

before returning for 1.1-style
events which have been enabled for the

Component

.

**Parameters:** e

- the event

---

#### dispatchEvent

public final void dispatchEvent​(

AWTEvent

e)

Dispatches an event to this component or one of its sub components.
Calls

processEvent

before returning for 1.1-style
events which have been enabled for the

Component

.

postEvent

```java
@Deprecated

public boolean postEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by dispatchEvent(AWTEvent).

Description copied from interface:

MenuContainer

Posts an event to the listeners.

**Specified by:** postEvent

in interface

MenuContainer
**Parameters:** e

- the event to dispatch
**Returns:** the results of posting the event

---

#### postEvent

@Deprecated

public boolean postEvent​(

Event

e)

Description copied from interface:

MenuContainer

Posts an event to the listeners.

addComponentListener

```java
public void addComponentListener​(
ComponentListener
l)
```

Adds the specified component listener to receive component events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the component listener
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

removeComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

---

#### addComponentListener

public void addComponentListener​(

ComponentListener

l)

Adds the specified component listener to receive component events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeComponentListener

```java
public void removeComponentListener​(
ComponentListener
l)
```

Removes the specified component listener so that it no longer
receives component events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the component listener
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

getComponentListeners()

---

#### removeComponentListener

public void removeComponentListener​(

ComponentListener

l)

Removes the specified component listener so that it no longer
receives component events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getComponentListeners

```java
public
ComponentListener
[] getComponentListeners()
```

Returns an array of all the component listeners
registered on this component.

**Returns:** all

ComponentListener

s of this component
or an empty array if no component
listeners are currently registered
**Since:** 1.4
**See Also:** addComponentListener(java.awt.event.ComponentListener)

,

removeComponentListener(java.awt.event.ComponentListener)

---

#### getComponentListeners

public

ComponentListener

[] getComponentListeners()

Returns an array of all the component listeners
registered on this component.

addFocusListener

```java
public void addFocusListener​(
FocusListener
l)
```

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the focus listener
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

removeFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

---

#### addFocusListener

public void addFocusListener​(

FocusListener

l)

Adds the specified focus listener to receive focus events from
this component when this component gains input focus.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeFocusListener

```java
public void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so that it no longer
receives focus events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the focus listener
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

addFocusListener(java.awt.event.FocusListener)

,

getFocusListeners()

---

#### removeFocusListener

public void removeFocusListener​(

FocusListener

l)

Removes the specified focus listener so that it no longer
receives focus events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getFocusListeners

```java
public
FocusListener
[] getFocusListeners()
```

Returns an array of all the focus listeners
registered on this component.

**Returns:** all of this component's

FocusListener

s
or an empty array if no component
listeners are currently registered
**Since:** 1.4
**See Also:** addFocusListener(java.awt.event.FocusListener)

,

removeFocusListener(java.awt.event.FocusListener)

---

#### getFocusListeners

public

FocusListener

[] getFocusListeners()

Returns an array of all the focus listeners
registered on this component.

addHierarchyListener

```java
public void addHierarchyListener​(
HierarchyListener
l)
```

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

removeHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

---

#### addHierarchyListener

public void addHierarchyListener​(

HierarchyListener

l)

Adds the specified hierarchy listener to receive hierarchy changed
events from this component when the hierarchy to which this container
belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeHierarchyListener

```java
public void removeHierarchyListener​(
HierarchyListener
l)
```

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

getHierarchyListeners()

---

#### removeHierarchyListener

public void removeHierarchyListener​(

HierarchyListener

l)

Removes the specified hierarchy listener so that it no longer
receives hierarchy changed events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getHierarchyListeners

```java
public
HierarchyListener
[] getHierarchyListeners()
```

Returns an array of all the hierarchy listeners
registered on this component.

**Returns:** all of this component's

HierarchyListener

s
or an empty array if no hierarchy
listeners are currently registered
**Since:** 1.4
**See Also:** addHierarchyListener(java.awt.event.HierarchyListener)

,

removeHierarchyListener(java.awt.event.HierarchyListener)

---

#### getHierarchyListeners

public

HierarchyListener

[] getHierarchyListeners()

Returns an array of all the hierarchy listeners
registered on this component.

addHierarchyBoundsListener

```java
public void addHierarchyBoundsListener​(
HierarchyBoundsListener
l)
```

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy bounds listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

---

#### addHierarchyBoundsListener

public void addHierarchyBoundsListener​(

HierarchyBoundsListener

l)

Adds the specified hierarchy bounds listener to receive hierarchy
bounds events from this component when the hierarchy to which this
container belongs changes.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeHierarchyBoundsListener

```java
public void removeHierarchyBoundsListener​(
HierarchyBoundsListener
l)
```

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the hierarchy bounds listener
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

getHierarchyBoundsListeners()

---

#### removeHierarchyBoundsListener

public void removeHierarchyBoundsListener​(

HierarchyBoundsListener

l)

Removes the specified hierarchy bounds listener so that it no longer
receives hierarchy bounds events from this component. This method
performs no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getHierarchyBoundsListeners

```java
public
HierarchyBoundsListener
[] getHierarchyBoundsListeners()
```

Returns an array of all the hierarchy bounds listeners
registered on this component.

**Returns:** all of this component's

HierarchyBoundsListener

s
or an empty array if no hierarchy bounds
listeners are currently registered
**Since:** 1.4
**See Also:** addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

---

#### getHierarchyBoundsListeners

public

HierarchyBoundsListener

[] getHierarchyBoundsListeners()

Returns an array of all the hierarchy bounds listeners
registered on this component.

addKeyListener

```java
public void addKeyListener​(
KeyListener
l)
```

Adds the specified key listener to receive key events from
this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the key listener.
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

removeKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

---

#### addKeyListener

public void addKeyListener​(

KeyListener

l)

Adds the specified key listener to receive key events from
this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeKeyListener

```java
public void removeKeyListener​(
KeyListener
l)
```

Removes the specified key listener so that it no longer
receives key events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the key listener
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

addKeyListener(java.awt.event.KeyListener)

,

getKeyListeners()

---

#### removeKeyListener

public void removeKeyListener​(

KeyListener

l)

Removes the specified key listener so that it no longer
receives key events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getKeyListeners

```java
public
KeyListener
[] getKeyListeners()
```

Returns an array of all the key listeners
registered on this component.

**Returns:** all of this component's

KeyListener

s
or an empty array if no key
listeners are currently registered
**Since:** 1.4
**See Also:** addKeyListener(java.awt.event.KeyListener)

,

removeKeyListener(java.awt.event.KeyListener)

---

#### getKeyListeners

public

KeyListener

[] getKeyListeners()

Returns an array of all the key listeners
registered on this component.

addMouseListener

```java
public void addMouseListener​(
MouseListener
l)
```

Adds the specified mouse listener to receive mouse events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

removeMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

---

#### addMouseListener

public void addMouseListener​(

MouseListener

l)

Adds the specified mouse listener to receive mouse events from
this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeMouseListener

```java
public void removeMouseListener​(
MouseListener
l)
```

Removes the specified mouse listener so that it no longer
receives mouse events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

getMouseListeners()

---

#### removeMouseListener

public void removeMouseListener​(

MouseListener

l)

Removes the specified mouse listener so that it no longer
receives mouse events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getMouseListeners

```java
public
MouseListener
[] getMouseListeners()
```

Returns an array of all the mouse listeners
registered on this component.

**Returns:** all of this component's

MouseListener

s
or an empty array if no mouse
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseListener(java.awt.event.MouseListener)

,

removeMouseListener(java.awt.event.MouseListener)

---

#### getMouseListeners

public

MouseListener

[] getMouseListeners()

Returns an array of all the mouse listeners
registered on this component.

addMouseMotionListener

```java
public void addMouseMotionListener​(
MouseMotionListener
l)
```

Adds the specified mouse motion listener to receive mouse motion
events from this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse motion listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

---

#### addMouseMotionListener

public void addMouseMotionListener​(

MouseMotionListener

l)

Adds the specified mouse motion listener to receive mouse motion
events from this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeMouseMotionListener

```java
public void removeMouseMotionListener​(
MouseMotionListener
l)
```

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse motion listener
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

getMouseMotionListeners()

---

#### removeMouseMotionListener

public void removeMouseMotionListener​(

MouseMotionListener

l)

Removes the specified mouse motion listener so that it no longer
receives mouse motion events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getMouseMotionListeners

```java
public
MouseMotionListener
[] getMouseMotionListeners()
```

Returns an array of all the mouse motion listeners
registered on this component.

**Returns:** all of this component's

MouseMotionListener

s
or an empty array if no mouse motion
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseMotionListener(java.awt.event.MouseMotionListener)

,

removeMouseMotionListener(java.awt.event.MouseMotionListener)

---

#### getMouseMotionListeners

public

MouseMotionListener

[] getMouseMotionListeners()

Returns an array of all the mouse motion listeners
registered on this component.

addMouseWheelListener

```java
public void addMouseWheelListener​(
MouseWheelListener
l)
```

Adds the specified mouse wheel listener to receive mouse wheel events
from this component. Containers also receive mouse wheel events from
sub-components.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse wheel listener
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

---

#### addMouseWheelListener

public void addMouseWheelListener​(

MouseWheelListener

l)

Adds the specified mouse wheel listener to receive mouse wheel events
from this component. Containers also receive mouse wheel events from
sub-components.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

If l is

null

, no exception is thrown and no
action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeMouseWheelListener

```java
public void removeMouseWheelListener​(
MouseWheelListener
l)
```

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the mouse wheel listener.
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

getMouseWheelListeners()

---

#### removeMouseWheelListener

public void removeMouseWheelListener​(

MouseWheelListener

l)

Removes the specified mouse wheel listener so that it no longer
receives mouse wheel events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getMouseWheelListeners

```java
public
MouseWheelListener
[] getMouseWheelListeners()
```

Returns an array of all the mouse wheel listeners
registered on this component.

**Returns:** all of this component's

MouseWheelListener

s
or an empty array if no mouse wheel
listeners are currently registered
**Since:** 1.4
**See Also:** addMouseWheelListener(java.awt.event.MouseWheelListener)

,

removeMouseWheelListener(java.awt.event.MouseWheelListener)

---

#### getMouseWheelListeners

public

MouseWheelListener

[] getMouseWheelListeners()

Returns an array of all the mouse wheel listeners
registered on this component.

addInputMethodListener

```java
public void addInputMethodListener​(
InputMethodListener
l)
```

Adds the specified input method listener to receive
input method events from this component. A component will
only receive input method events from input methods
if it also overrides

getInputMethodRequests

to return an

InputMethodRequests

instance.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the input method listener
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

removeInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

,

getInputMethodRequests()

---

#### addInputMethodListener

public void addInputMethodListener​(

InputMethodListener

l)

Adds the specified input method listener to receive
input method events from this component. A component will
only receive input method events from input methods
if it also overrides

getInputMethodRequests

to return an

InputMethodRequests

instance.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeInputMethodListener

```java
public void removeInputMethodListener​(
InputMethodListener
l)
```

Removes the specified input method listener so that it no longer
receives input method events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the input method listener
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

getInputMethodListeners()

---

#### removeInputMethodListener

public void removeInputMethodListener​(

InputMethodListener

l)

Removes the specified input method listener so that it no longer
receives input method events from this component. This method performs
no function, nor does it throw an exception, if the listener
specified by the argument was not previously added to this component.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getInputMethodListeners

```java
public
InputMethodListener
[] getInputMethodListeners()
```

Returns an array of all the input method listeners
registered on this component.

**Returns:** all of this component's

InputMethodListener

s
or an empty array if no input method
listeners are currently registered
**Since:** 1.4
**See Also:** addInputMethodListener(java.awt.event.InputMethodListener)

,

removeInputMethodListener(java.awt.event.InputMethodListener)

---

#### getInputMethodListeners

public

InputMethodListener

[] getInputMethodListeners()

Returns an array of all the input method listeners
registered on this component.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Component c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getComponentListeners()

,

getFocusListeners()

,

getHierarchyListeners()

,

getHierarchyBoundsListeners()

,

getKeyListeners()

,

getMouseListeners()

,

getMouseMotionListeners()

,

getMouseWheelListeners()

,

getInputMethodListeners()

,

getPropertyChangeListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Component

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Component c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Component c

for its mouse listeners with the following code:

```java
MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));
```

If no such listeners exist, this method returns an empty array.

MouseListener[] mls = (MouseListener[])(c.getListeners(MouseListener.class));

getInputMethodRequests

```java
public
InputMethodRequests
getInputMethodRequests()
```

Gets the input method request handler which supports
requests from input methods for this component. A component
that supports on-the-spot text input must override this
method to return an

InputMethodRequests

instance.
At the same time, it also has to handle input method events.

**Returns:** the input method request handler for this component,

null

by default
**Since:** 1.2
**See Also:** addInputMethodListener(java.awt.event.InputMethodListener)

---

#### getInputMethodRequests

public

InputMethodRequests

getInputMethodRequests()

Gets the input method request handler which supports
requests from input methods for this component. A component
that supports on-the-spot text input must override this
method to return an

InputMethodRequests

instance.
At the same time, it also has to handle input method events.

getInputContext

```java
public
InputContext
getInputContext()
```

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component. By default, the input context used for
the parent component is returned. Components may
override this to return a private input context.

**Returns:** the input context used by this component;

null

if no context can be determined
**Since:** 1.2

---

#### getInputContext

public

InputContext

getInputContext()

Gets the input context used by this component for handling
the communication with input methods when text is entered
in this component. By default, the input context used for
the parent component is returned. Components may
override this to return a private input context.

enableEvents

```java
protected final void enableEvents​(long eventsToEnable)
```

Enables the events defined by the specified event mask parameter
to be delivered to this component.

Event types are automatically enabled when a listener for
that event type is added to the component.

This method only needs to be invoked by subclasses of

Component

which desire to have the specified event
types delivered to

processEvent

regardless of whether
or not a listener is registered.

**Parameters:** eventsToEnable

- the event mask defining the event types
**Since:** 1.1
**See Also:** processEvent(java.awt.AWTEvent)

,

disableEvents(long)

,

AWTEvent

---

#### enableEvents

protected final void enableEvents​(long eventsToEnable)

Enables the events defined by the specified event mask parameter
to be delivered to this component.

Event types are automatically enabled when a listener for
that event type is added to the component.

This method only needs to be invoked by subclasses of

Component

which desire to have the specified event
types delivered to

processEvent

regardless of whether
or not a listener is registered.

Event types are automatically enabled when a listener for
that event type is added to the component.

This method only needs to be invoked by subclasses of

Component

which desire to have the specified event
types delivered to

processEvent

regardless of whether
or not a listener is registered.

This method only needs to be invoked by subclasses of

Component

which desire to have the specified event
types delivered to

processEvent

regardless of whether
or not a listener is registered.

disableEvents

```java
protected final void disableEvents​(long eventsToDisable)
```

Disables the events defined by the specified event mask parameter
from being delivered to this component.

**Parameters:** eventsToDisable

- the event mask defining the event types
**Since:** 1.1
**See Also:** enableEvents(long)

---

#### disableEvents

protected final void disableEvents​(long eventsToDisable)

Disables the events defined by the specified event mask parameter
from being delivered to this component.

coalesceEvents

```java
protected
AWTEvent
coalesceEvents​(
AWTEvent
existingEvent,

AWTEvent
newEvent)
```

Potentially coalesce an event being posted with an existing
event. This method is called by

EventQueue.postEvent

if an event with the same ID as the event to be posted is found in
the queue (both events must have this component as their source).
This method either returns a coalesced event which replaces
the existing event (and the new event is then discarded), or

null

to indicate that no combining should be done
(add the second event to the end of the queue). Either event
parameter may be modified and returned, as the other one is discarded
unless

null

is returned.

This implementation of

coalesceEvents

coalesces
two event types: mouse move (and drag) events,
and paint (and update) events.
For mouse move events the last event is always returned, causing
intermediate moves to be discarded. For paint events, the new
event is coalesced into a complex

RepaintArea

in the peer.
The new

AWTEvent

is always returned.

**Parameters:** existingEvent

- the event already on the

EventQueue
**Parameters:** newEvent

- the event being posted to the

EventQueue
**Returns:** a coalesced event, or

null

indicating that no
coalescing was done

---

#### coalesceEvents

protected

AWTEvent

coalesceEvents​(

AWTEvent

existingEvent,

AWTEvent

newEvent)

Potentially coalesce an event being posted with an existing
event. This method is called by

EventQueue.postEvent

if an event with the same ID as the event to be posted is found in
the queue (both events must have this component as their source).
This method either returns a coalesced event which replaces
the existing event (and the new event is then discarded), or

null

to indicate that no combining should be done
(add the second event to the end of the queue). Either event
parameter may be modified and returned, as the other one is discarded
unless

null

is returned.

This implementation of

coalesceEvents

coalesces
two event types: mouse move (and drag) events,
and paint (and update) events.
For mouse move events the last event is always returned, causing
intermediate moves to be discarded. For paint events, the new
event is coalesced into a complex

RepaintArea

in the peer.
The new

AWTEvent

is always returned.

This implementation of

coalesceEvents

coalesces
two event types: mouse move (and drag) events,
and paint (and update) events.
For mouse move events the last event is always returned, causing
intermediate moves to be discarded. For paint events, the new
event is coalesced into a complex

RepaintArea

in the peer.
The new

AWTEvent

is always returned.

processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events occurring on this component. By default this
method calls the appropriate

process<event type>Event

method for the given class of event.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the event
**Since:** 1.1
**See Also:** processComponentEvent(java.awt.event.ComponentEvent)

,

processFocusEvent(java.awt.event.FocusEvent)

,

processKeyEvent(java.awt.event.KeyEvent)

,

processMouseEvent(java.awt.event.MouseEvent)

,

processMouseMotionEvent(java.awt.event.MouseEvent)

,

processInputMethodEvent(java.awt.event.InputMethodEvent)

,

processHierarchyEvent(java.awt.event.HierarchyEvent)

,

processMouseWheelEvent(java.awt.event.MouseWheelEvent)

---

#### processEvent

protected void processEvent​(

AWTEvent

e)

Processes events occurring on this component. By default this
method calls the appropriate

process<event type>Event

method for the given class of event.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processComponentEvent

```java
protected void processComponentEvent​(
ComponentEvent
e)
```

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

This method is not called unless component events are
enabled for this component. Component events are enabled
when one of the following occurs:

- A

ComponentListener

object is registered
via

addComponentListener

.

Component events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the component event
**Since:** 1.1
**See Also:** ComponentEvent

,

ComponentListener

,

addComponentListener(java.awt.event.ComponentListener)

,

enableEvents(long)

---

#### processComponentEvent

protected void processComponentEvent​(

ComponentEvent

e)

Processes component events occurring on this component by
dispatching them to any registered

ComponentListener

objects.

This method is not called unless component events are
enabled for this component. Component events are enabled
when one of the following occurs:

- A

ComponentListener

object is registered
via

addComponentListener

.

Component events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless component events are
enabled for this component. Component events are enabled
when one of the following occurs:

- A

ComponentListener

object is registered
via

addComponentListener

.

Component events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

A

ComponentListener

object is registered
via

addComponentListener

.

Component events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processFocusEvent

```java
protected void processFocusEvent​(
FocusEvent
e)
```

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

This method is not called unless focus events are
enabled for this component. Focus events are enabled
when one of the following occurs:

- A

FocusListener

object is registered
via

addFocusListener

.

Focus events are enabled via

enableEvents

.

If focus events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a focus event should be dispatched to
registered

FocusListener

objects. If the
events are to be dispatched, the

KeyboardFocusManager

calls the

Component

's

dispatchEvent

method, which results in a call to the

Component

's

processFocusEvent

method.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the focus event
**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

KeyboardFocusManager

,

addFocusListener(java.awt.event.FocusListener)

,

enableEvents(long)

,

dispatchEvent(java.awt.AWTEvent)

---

#### processFocusEvent

protected void processFocusEvent​(

FocusEvent

e)

Processes focus events occurring on this component by
dispatching them to any registered

FocusListener

objects.

This method is not called unless focus events are
enabled for this component. Focus events are enabled
when one of the following occurs:

- A

FocusListener

object is registered
via

addFocusListener

.

Focus events are enabled via

enableEvents

.

If focus events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a focus event should be dispatched to
registered

FocusListener

objects. If the
events are to be dispatched, the

KeyboardFocusManager

calls the

Component

's

dispatchEvent

method, which results in a call to the

Component

's

processFocusEvent

method.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless focus events are
enabled for this component. Focus events are enabled
when one of the following occurs:

- A

FocusListener

object is registered
via

addFocusListener

.

Focus events are enabled via

enableEvents

.

If focus events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a focus event should be dispatched to
registered

FocusListener

objects. If the
events are to be dispatched, the

KeyboardFocusManager

calls the

Component

's

dispatchEvent

method, which results in a call to the

Component

's

processFocusEvent

method.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

A

FocusListener

object is registered
via

addFocusListener

.

Focus events are enabled via

enableEvents

.

If focus events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a focus event should be dispatched to
registered

FocusListener

objects. If the
events are to be dispatched, the

KeyboardFocusManager

calls the

Component

's

dispatchEvent

method, which results in a call to the

Component

's

processFocusEvent

method.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

If focus events are enabled for a

Component

, calling
the

Component

's

dispatchEvent

method
with a

FocusEvent

as the argument will result in a
call to the

Component

's

processFocusEvent

method regardless of the current

KeyboardFocusManager

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processKeyEvent

```java
protected void processKeyEvent​(
KeyEvent
e)
```

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

This method is not called unless key events are
enabled for this component. Key events are enabled
when one of the following occurs:

- A

KeyListener

object is registered
via

addKeyListener

.

Key events are enabled via

enableEvents

.

If key events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a key event should be dispatched to
registered

KeyListener

objects. The

DefaultKeyboardFocusManager

will not dispatch
key events to a

Component

that is not the focus
owner or is not showing.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the key event
**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

processEvent(java.awt.AWTEvent)

,

dispatchEvent(java.awt.AWTEvent)

,

addKeyListener(java.awt.event.KeyListener)

,

enableEvents(long)

,

isShowing()

---

#### processKeyEvent

protected void processKeyEvent​(

KeyEvent

e)

Processes key events occurring on this component by
dispatching them to any registered

KeyListener

objects.

This method is not called unless key events are
enabled for this component. Key events are enabled
when one of the following occurs:

- A

KeyListener

object is registered
via

addKeyListener

.

Key events are enabled via

enableEvents

.

If key events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a key event should be dispatched to
registered

KeyListener

objects. The

DefaultKeyboardFocusManager

will not dispatch
key events to a

Component

that is not the focus
owner or is not showing.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless key events are
enabled for this component. Key events are enabled
when one of the following occurs:

- A

KeyListener

object is registered
via

addKeyListener

.

Key events are enabled via

enableEvents

.

If key events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a key event should be dispatched to
registered

KeyListener

objects. The

DefaultKeyboardFocusManager

will not dispatch
key events to a

Component

that is not the focus
owner or is not showing.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

A

KeyListener

object is registered
via

addKeyListener

.

Key events are enabled via

enableEvents

.

If key events are enabled for a

Component

,
the current

KeyboardFocusManager

determines
whether or not a key event should be dispatched to
registered

KeyListener

objects. The

DefaultKeyboardFocusManager

will not dispatch
key events to a

Component

that is not the focus
owner or is not showing.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

As of J2SE 1.4,

KeyEvent

s are redirected to
the focus owner. Please see the

Focus Specification

for further information.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

Calling a

Component

's

dispatchEvent

method with a

KeyEvent

as the argument will
result in a call to the

Component

's

processKeyEvent

method regardless of the
current

KeyboardFocusManager

as long as the
component is showing, focused, and enabled, and key events
are enabled on it.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

If the event parameter is

null

the behavior is unspecified and may result in an
exception.

processMouseEvent

```java
protected void processMouseEvent​(
MouseEvent
e)
```

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

This method is not called unless mouse events are
enabled for this component. Mouse events are enabled
when one of the following occurs:

- A

MouseListener

object is registered
via

addMouseListener

.

Mouse events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse event
**Since:** 1.1
**See Also:** MouseEvent

,

MouseListener

,

addMouseListener(java.awt.event.MouseListener)

,

enableEvents(long)

---

#### processMouseEvent

protected void processMouseEvent​(

MouseEvent

e)

Processes mouse events occurring on this component by
dispatching them to any registered

MouseListener

objects.

This method is not called unless mouse events are
enabled for this component. Mouse events are enabled
when one of the following occurs:

- A

MouseListener

object is registered
via

addMouseListener

.

Mouse events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless mouse events are
enabled for this component. Mouse events are enabled
when one of the following occurs:

- A

MouseListener

object is registered
via

addMouseListener

.

Mouse events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

A

MouseListener

object is registered
via

addMouseListener

.

Mouse events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processMouseMotionEvent

```java
protected void processMouseMotionEvent​(
MouseEvent
e)
```

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

This method is not called unless mouse motion events are
enabled for this component. Mouse motion events are enabled
when one of the following occurs:

- A

MouseMotionListener

object is registered
via

addMouseMotionListener

.

Mouse motion events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse motion event
**Since:** 1.1
**See Also:** MouseEvent

,

MouseMotionListener

,

addMouseMotionListener(java.awt.event.MouseMotionListener)

,

enableEvents(long)

---

#### processMouseMotionEvent

protected void processMouseMotionEvent​(

MouseEvent

e)

Processes mouse motion events occurring on this component by
dispatching them to any registered

MouseMotionListener

objects.

This method is not called unless mouse motion events are
enabled for this component. Mouse motion events are enabled
when one of the following occurs:

- A

MouseMotionListener

object is registered
via

addMouseMotionListener

.

Mouse motion events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless mouse motion events are
enabled for this component. Mouse motion events are enabled
when one of the following occurs:

- A

MouseMotionListener

object is registered
via

addMouseMotionListener

.

Mouse motion events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

A

MouseMotionListener

object is registered
via

addMouseMotionListener

.

Mouse motion events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processMouseWheelEvent

```java
protected void processMouseWheelEvent​(
MouseWheelEvent
e)
```

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

This method is not called unless mouse wheel events are
enabled for this component. Mouse wheel events are enabled
when one of the following occurs:

- A

MouseWheelListener

object is registered
via

addMouseWheelListener

.

Mouse wheel events are enabled via

enableEvents

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the mouse wheel event
**Since:** 1.4
**See Also:** MouseWheelEvent

,

MouseWheelListener

,

addMouseWheelListener(java.awt.event.MouseWheelListener)

,

enableEvents(long)

---

#### processMouseWheelEvent

protected void processMouseWheelEvent​(

MouseWheelEvent

e)

Processes mouse wheel events occurring on this component by
dispatching them to any registered

MouseWheelListener

objects.

This method is not called unless mouse wheel events are
enabled for this component. Mouse wheel events are enabled
when one of the following occurs:

- A

MouseWheelListener

object is registered
via

addMouseWheelListener

.

Mouse wheel events are enabled via

enableEvents

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless mouse wheel events are
enabled for this component. Mouse wheel events are enabled
when one of the following occurs:

- A

MouseWheelListener

object is registered
via

addMouseWheelListener

.

Mouse wheel events are enabled via

enableEvents

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

A

MouseWheelListener

object is registered
via

addMouseWheelListener

.

Mouse wheel events are enabled via

enableEvents

.

For information on how mouse wheel events are dispatched, see
the class description for

MouseWheelEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processInputMethodEvent

```java
protected void processInputMethodEvent​(
InputMethodEvent
e)
```

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

This method is not called unless input method events
are enabled for this component. Input method events are enabled
when one of the following occurs:

- An

InputMethodListener

object is registered
via

addInputMethodListener

.

Input method events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the input method event
**Since:** 1.2
**See Also:** InputMethodEvent

,

InputMethodListener

,

addInputMethodListener(java.awt.event.InputMethodListener)

,

enableEvents(long)

---

#### processInputMethodEvent

protected void processInputMethodEvent​(

InputMethodEvent

e)

Processes input method events occurring on this component by
dispatching them to any registered

InputMethodListener

objects.

This method is not called unless input method events
are enabled for this component. Input method events are enabled
when one of the following occurs:

- An

InputMethodListener

object is registered
via

addInputMethodListener

.

Input method events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless input method events
are enabled for this component. Input method events are enabled
when one of the following occurs:

- An

InputMethodListener

object is registered
via

addInputMethodListener

.

Input method events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

An

InputMethodListener

object is registered
via

addInputMethodListener

.

Input method events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processHierarchyEvent

```java
protected void processHierarchyEvent​(
HierarchyEvent
e)
```

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

This method is not called unless hierarchy events
are enabled for this component. Hierarchy events are enabled
when one of the following occurs:

- An

HierarchyListener

object is registered
via

addHierarchyListener

.

Hierarchy events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the hierarchy event
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyListener

,

addHierarchyListener(java.awt.event.HierarchyListener)

,

enableEvents(long)

---

#### processHierarchyEvent

protected void processHierarchyEvent​(

HierarchyEvent

e)

Processes hierarchy events occurring on this component by
dispatching them to any registered

HierarchyListener

objects.

This method is not called unless hierarchy events
are enabled for this component. Hierarchy events are enabled
when one of the following occurs:

- An

HierarchyListener

object is registered
via

addHierarchyListener

.

Hierarchy events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless hierarchy events
are enabled for this component. Hierarchy events are enabled
when one of the following occurs:

- An

HierarchyListener

object is registered
via

addHierarchyListener

.

Hierarchy events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

An

HierarchyListener

object is registered
via

addHierarchyListener

.

Hierarchy events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processHierarchyBoundsEvent

```java
protected void processHierarchyBoundsEvent​(
HierarchyEvent
e)
```

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

This method is not called unless hierarchy bounds events
are enabled for this component. Hierarchy bounds events are enabled
when one of the following occurs:

- An

HierarchyBoundsListener

object is registered
via

addHierarchyBoundsListener

.

Hierarchy bounds events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the hierarchy event
**Since:** 1.3
**See Also:** HierarchyEvent

,

HierarchyBoundsListener

,

addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)

,

enableEvents(long)

---

#### processHierarchyBoundsEvent

protected void processHierarchyBoundsEvent​(

HierarchyEvent

e)

Processes hierarchy bounds events occurring on this component by
dispatching them to any registered

HierarchyBoundsListener

objects.

This method is not called unless hierarchy bounds events
are enabled for this component. Hierarchy bounds events are enabled
when one of the following occurs:

- An

HierarchyBoundsListener

object is registered
via

addHierarchyBoundsListener

.

Hierarchy bounds events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless hierarchy bounds events
are enabled for this component. Hierarchy bounds events are enabled
when one of the following occurs:

- An

HierarchyBoundsListener

object is registered
via

addHierarchyBoundsListener

.

Hierarchy bounds events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

An

HierarchyBoundsListener

object is registered
via

addHierarchyBoundsListener

.

Hierarchy bounds events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

handleEvent

```java
@Deprecated

public boolean handleEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1
replaced by processEvent(AWTEvent).

**Parameters:** evt

- the event to handle
**Returns:** true

if the event was handled,

false

otherwise

---

#### handleEvent

@Deprecated

public boolean handleEvent​(

Event

evt)

mouseDown

```java
@Deprecated

public boolean mouseDown​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

---

#### mouseDown

@Deprecated

public boolean mouseDown​(

Event

evt,
int x,
int y)

mouseDrag

```java
@Deprecated

public boolean mouseDrag​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

---

#### mouseDrag

@Deprecated

public boolean mouseDrag​(

Event

evt,
int x,
int y)

mouseUp

```java
@Deprecated

public boolean mouseUp​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

---

#### mouseUp

@Deprecated

public boolean mouseUp​(

Event

evt,
int x,
int y)

mouseMove

```java
@Deprecated

public boolean mouseMove​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseMotionEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

---

#### mouseMove

@Deprecated

public boolean mouseMove​(

Event

evt,
int x,
int y)

mouseEnter

```java
@Deprecated

public boolean mouseEnter​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

---

#### mouseEnter

@Deprecated

public boolean mouseEnter​(

Event

evt,
int x,
int y)

mouseExit

```java
@Deprecated

public boolean mouseExit​(
Event
evt,
int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by processMouseEvent(MouseEvent).

**Parameters:** evt

- the event to handle
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** false

---

#### mouseExit

@Deprecated

public boolean mouseExit​(

Event

evt,
int x,
int y)

keyDown

```java
@Deprecated

public boolean keyDown​(
Event
evt,
int key)
```

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

**Parameters:** evt

- the event to handle
**Parameters:** key

- the key pressed
**Returns:** false

---

#### keyDown

@Deprecated

public boolean keyDown​(

Event

evt,
int key)

keyUp

```java
@Deprecated

public boolean keyUp​(
Event
evt,
int key)
```

Deprecated.

As of JDK version 1.1,
replaced by processKeyEvent(KeyEvent).

**Parameters:** evt

- the event to handle
**Parameters:** key

- the key pressed
**Returns:** false

---

#### keyUp

@Deprecated

public boolean keyUp​(

Event

evt,
int key)

action

```java
@Deprecated

public boolean action​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
should register this component as ActionListener on component
which fires action events.

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object acted on
**Returns:** false

---

#### action

@Deprecated

public boolean action​(

Event

evt,

Object

what)

addNotify

```java
public void addNotify()
```

Makes this

Component

displayable by connecting it to a
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Since:** 1.0
**See Also:** isDisplayable()

,

removeNotify()

,

invalidate()

---

#### addNotify

public void addNotify()

Makes this

Component

displayable by connecting it to a
native screen resource.
This method is called internally by the toolkit and should
not be called directly by programs.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

removeNotify

```java
public void removeNotify()
```

Makes this

Component

undisplayable by destroying it native
screen resource.

This method is called by the toolkit internally and should
not be called directly by programs. Code overriding
this method should call

super.removeNotify

as
the first line of the overriding method.

**Since:** 1.0
**See Also:** isDisplayable()

,

addNotify()

---

#### removeNotify

public void removeNotify()

Makes this

Component

undisplayable by destroying it native
screen resource.

This method is called by the toolkit internally and should
not be called directly by programs. Code overriding
this method should call

super.removeNotify

as
the first line of the overriding method.

This method is called by the toolkit internally and should
not be called directly by programs. Code overriding
this method should call

super.removeNotify

as
the first line of the overriding method.

gotFocus

```java
@Deprecated

public boolean gotFocus​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object focused
**Returns:** false

---

#### gotFocus

@Deprecated

public boolean gotFocus​(

Event

evt,

Object

what)

lostFocus

```java
@Deprecated

public boolean lostFocus​(
Event
evt,

Object
what)
```

Deprecated.

As of JDK version 1.1,
replaced by processFocusEvent(FocusEvent).

**Parameters:** evt

- the event to handle
**Parameters:** what

- the object focused
**Returns:** false

---

#### lostFocus

@Deprecated

public boolean lostFocus​(

Event

evt,

Object

what)

isFocusTraversable

```java
@Deprecated

public boolean isFocusTraversable()
```

Deprecated.

As of 1.4, replaced by

isFocusable()

.

Returns whether this

Component

can become the focus
owner.

**Returns:** true

if this

Component

is
focusable;

false

otherwise
**Since:** 1.1
**See Also:** setFocusable(boolean)

---

#### isFocusTraversable

@Deprecated

public boolean isFocusTraversable()

Returns whether this

Component

can become the focus
owner.

isFocusable

```java
public boolean isFocusable()
```

Returns whether this Component can be focused.

**Returns:** true

if this Component is focusable;

false

otherwise.
**Since:** 1.4
**See Also:** setFocusable(boolean)

---

#### isFocusable

public boolean isFocusable()

Returns whether this Component can be focused.

setFocusable

```java
public void setFocusable​(boolean focusable)
```

Sets the focusable state of this Component to the specified value. This
value overrides the Component's default focusability.

**Parameters:** focusable

- indicates whether this Component is focusable
**Since:** 1.4
**See Also:** isFocusable()

---

#### setFocusable

public void setFocusable​(boolean focusable)

Sets the focusable state of this Component to the specified value. This
value overrides the Component's default focusability.

setFocusTraversalKeys

```java
public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)
```

Sets the focus traversal keys for a given traversal operation for this
Component.

The default values for a Component's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Component's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Component. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Parameters:** keystrokes

- the Set of AWTKeyStroke for the specified operation
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Component
**Since:** 1.4
**See Also:** getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

---

#### setFocusTraversalKeys

public void setFocusTraversalKeys​(int id,

Set

<? extends

AWTKeyStroke

> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Component.

The default values for a Component's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Component's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Component. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

The default values for a Component's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Component's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Component. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Component. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

If a value of null is specified for the Set, this Component inherits the
Set from its parent. If all ancestors of this Component have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Returns the Set of focus traversal keys for a given traversal operation
for this Component. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Component, then this Component's parent's Set is returned. If no Set
has been explicitly defined for any of this Component's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Returns:** the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

---

#### getFocusTraversalKeys

public

Set

<

AWTKeyStroke

> getFocusTraversalKeys​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Component. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Component, then this Component's parent's Set is returned. If no Set
has been explicitly defined for any of this Component's ancestors, then
the current KeyboardFocusManager's default Set is returned.

If a Set of traversal keys has not been explicitly defined for this
Component, then this Component's parent's Set is returned. If no Set
has been explicitly defined for any of this Component's ancestors, then
the current KeyboardFocusManager's default Set is returned.

areFocusTraversalKeysSet

```java
public boolean areFocusTraversalKeysSet​(int id)
```

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component. If
this method returns

false

, this Component is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Returns:** true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS, or
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4

---

#### areFocusTraversalKeysSet

public boolean areFocusTraversalKeysSet​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Component. If
this method returns

false

, this Component is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

setFocusTraversalKeysEnabled

```java
public void setFocusTraversalKeysEnabled​(boolean focusTraversalKeysEnabled)
```

Sets whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Parameters:** focusTraversalKeysEnabled

- whether focus traversal keys are
enabled for this Component
**Since:** 1.4
**See Also:** getFocusTraversalKeysEnabled()

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

---

#### setFocusTraversalKeysEnabled

public void setFocusTraversalKeysEnabled​(boolean focusTraversalKeysEnabled)

Sets whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

getFocusTraversalKeysEnabled

```java
public boolean getFocusTraversalKeysEnabled()
```

Returns whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

**Returns:** whether focus traversal keys are enabled for this Component
**Since:** 1.4
**See Also:** setFocusTraversalKeysEnabled(boolean)

,

setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

getFocusTraversalKeys(int)

---

#### getFocusTraversalKeysEnabled

public boolean getFocusTraversalKeysEnabled()

Returns whether focus traversal keys are enabled for this Component.
Components for which focus traversal keys are disabled receive key
events for focus traversal keys. Components for which focus traversal
keys are enabled do not see these events; instead, the events are
automatically converted to traversal operations.

requestFocus

```java
public void requestFocus()
```

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window. This
component must be displayable, focusable, visible and all of
its ancestors (with the exception of the top-level Window) must
be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event. If this request is denied because this
Component's top-level Window cannot become the focused Window,
the request will be remembered and will be granted when the
Window is later focused by the user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Since:** 1.0
**See Also:** requestFocusInWindow()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

---

#### requestFocus

public void requestFocus()

Requests that this Component get the input focus, and that this
Component's top-level ancestor become the focused Window. This
component must be displayable, focusable, visible and all of
its ancestors (with the exception of the top-level Window) must
be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event. If this request is denied because this
Component's top-level Window cannot become the focused Window,
the request will be remembered and will be granted when the
Window is later focused by the user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

requestFocus

```java
public void requestFocus​(
FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level Window)
must be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of method. If this request is denied because this Component's
top-level Window cannot become the focused Window, the request will be
remembered and will be granted when the Window is later focused by the
user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** cause

- the cause why the focus is requested
**Since:** 9
**See Also:** FocusEvent

,

FocusEvent.Cause

,

requestFocusInWindow(FocusEvent.Cause)

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

---

#### requestFocus

public void requestFocus​(

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this Component get the input
focus, and that this Component's top-level ancestor become the
focused Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level Window)
must be visible for the request to be granted. Every effort will be
made to honor the request; however, in some cases it may be
impossible to do so. Developers must never assume that this
Component is the focus owner until this Component receives a
FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of method. If this request is denied because this Component's
top-level Window cannot become the focused Window, the request will be
remembered and will be granted when the Window is later focused by the
user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of method. If this request is denied because this Component's
top-level Window cannot become the focused Window, the request will be
remembered and will be granted when the Window is later focused by the
user.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow(FocusEvent.Cause)

when possible.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

requestFocus

```java
protected boolean requestFocus​(boolean temporary)
```

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

---

#### requestFocus

protected boolean requestFocus​(boolean temporary)

Requests that this

Component

get the input focus,
and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

requestFocus

```java
protected boolean requestFocus​(boolean temporary,

FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the {FocusEvent}
generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Parameters:** cause

- the cause why the focus is requested
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 9
**See Also:** FocusEvent

,

FocusEvent.Cause

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

---

#### requestFocus

protected boolean requestFocus​(boolean temporary,

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this

Component

get
the input focus, and that this

Component

's top-level ancestor
become the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED
event. If this request is denied because this component's
top-level window cannot become the focused window, the request
will be remembered and will be granted when the window is later
focused by the user.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the {FocusEvent}
generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the {FocusEvent}
generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

The focus request effect may also depend on the provided
cause value. If this request is succeed the {FocusEvent}
generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Because the focus behavior of this method is platform-dependent,
developers are strongly encouraged to use

requestFocusInWindow

when possible.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight

Component

s.
This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

requestFocusInWindow

```java
public boolean requestFocusInWindow()
```

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

---

#### requestFocusInWindow

public boolean requestFocusInWindow()

Requests that this Component get the input focus, if this
Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

requestFocusInWindow

```java
public boolean requestFocusInWindow​(
FocusEvent.Cause
cause)
```

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** cause

- the cause why the focus is requested
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 9
**See Also:** requestFocus(FocusEvent.Cause)

,

FocusEvent

,

FocusEvent.Cause

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

---

#### requestFocusInWindow

public boolean requestFocusInWindow​(

FocusEvent.Cause

cause)

Requests by the reason of

cause

that this Component get the input
focus, if this Component's top-level ancestor is already the focused
Window. This component must be displayable, focusable, visible
and all of its ancestors (with the exception of the top-level
Window) must be visible for the request to be granted. Every
effort will be made to honor the request; however, in some
cases it may be impossible to do so. Developers must never
assume that this Component is the focus owner until this
Component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the Component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this Component is
the focus owner until this Component receives a FOCUS_GAINED event.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

The focus request effect may also depend on the provided
cause value. If this request is succeed the

FocusEvent

generated in the result will receive the cause value specified as the
argument of the method.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method cannot be used to set the focus owner to no Component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner()

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus(FocusEvent.Cause)

when possible.
Code which relies on

requestFocus(FocusEvent.Cause)

may exhibit
different focus behavior on different platforms.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

requestFocusInWindow

```java
protected boolean requestFocusInWindow​(boolean temporary)
```

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

**Parameters:** temporary

- true if the focus change is temporary,
such as when the window loses the focus; for
more information on temporary focus changes see the

Focus Specification
**Returns:** false

if the focus change request is guaranteed to
fail;

true

if it is likely to succeed
**Since:** 1.4
**See Also:** requestFocus()

,

FocusEvent

,

addFocusListener(java.awt.event.FocusListener)

,

isFocusable()

,

isDisplayable()

,

KeyboardFocusManager.clearGlobalFocusOwner()

---

#### requestFocusInWindow

protected boolean requestFocusInWindow​(boolean temporary)

Requests that this

Component

get the input focus,
if this

Component

's top-level ancestor is already
the focused

Window

. This component must be
displayable, focusable, visible and all of its ancestors (with
the exception of the top-level Window) must be visible for the
request to be granted. Every effort will be made to honor the
request; however, in some cases it may be impossible to do
so. Developers must never assume that this component is the
focus owner until this component receives a FOCUS_GAINED event.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method returns a boolean value. If

false

is returned,
the request is

guaranteed to fail

. If

true

is
returned, the request will succeed

unless

it is vetoed, or an
extraordinary event, such as disposal of the component's peer, occurs
before the request can be granted by the native windowing system. Again,
while a return value of

true

indicates that the request is
likely to succeed, developers must never assume that this component is
the focus owner until this component receives a FOCUS_GAINED event.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

This method cannot be used to set the focus owner to no component at
all. Use

KeyboardFocusManager.clearGlobalFocusOwner

instead.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

The focus behavior of this method can be implemented uniformly across
platforms, and thus developers are strongly encouraged to use this
method over

requestFocus

when possible. Code which relies
on

requestFocus

may exhibit different focus behavior on
different platforms.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Every effort will be made to ensure that

FocusEvent

s
generated as a
result of this request will have the specified temporary value. However,
because specifying an arbitrary temporary state may not be implementable
on all native windowing systems, correct behavior for this method can be
guaranteed only for lightweight components. This method is not intended
for general use, but exists instead as a hook for lightweight component
libraries, such as Swing.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

Note: Not all focus transfers result from invoking this method. As
such, a component may receive focus without this or any of the other

requestFocus

methods of

Component

being invoked.

getFocusCycleRootAncestor

```java
public
Container
getFocusCycleRootAncestor()
```

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle. Each focus traversal cycle has only a single
focus cycle root and each Component which is not a Container belongs to
only a single focus traversal cycle. Containers which are focus cycle
roots belong to two cycles: one rooted at the Container itself, and one
rooted at the Container's nearest focus-cycle-root ancestor. For such
Containers, this method will return the Container's nearest focus-cycle-
root ancestor.

**Returns:** this Component's nearest focus-cycle-root ancestor
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

---

#### getFocusCycleRootAncestor

public

Container

getFocusCycleRootAncestor()

Returns the Container which is the focus cycle root of this Component's
focus traversal cycle. Each focus traversal cycle has only a single
focus cycle root and each Component which is not a Container belongs to
only a single focus traversal cycle. Containers which are focus cycle
roots belong to two cycles: one rooted at the Container itself, and one
rooted at the Container's nearest focus-cycle-root ancestor. For such
Containers, this method will return the Container's nearest focus-cycle-
root ancestor.

isFocusCycleRoot

```java
public boolean isFocusCycleRoot​(
Container
container)
```

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Component which is not a Container
belongs to only a single focus traversal cycle.

**Parameters:** container

- the Container to be tested
**Returns:** true

if the specified Container is a focus-cycle-
root of this Component;

false

otherwise
**Since:** 1.4
**See Also:** Container.isFocusCycleRoot()

---

#### isFocusCycleRoot

public boolean isFocusCycleRoot​(

Container

container)

Returns whether the specified Container is the focus cycle root of this
Component's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Component which is not a Container
belongs to only a single focus traversal cycle.

transferFocus

```java
public void transferFocus()
```

Transfers the focus to the next component, as though this Component were
the focus owner.

**Since:** 1.1
**See Also:** requestFocus()

---

#### transferFocus

public void transferFocus()

Transfers the focus to the next component, as though this Component were
the focus owner.

nextFocus

```java
@Deprecated

public void nextFocus()
```

Deprecated.

As of JDK version 1.1,
replaced by transferFocus().

---

#### nextFocus

@Deprecated

public void nextFocus()

transferFocusBackward

```java
public void transferFocusBackward()
```

Transfers the focus to the previous component, as though this Component
were the focus owner.

**Since:** 1.4
**See Also:** requestFocus()

---

#### transferFocusBackward

public void transferFocusBackward()

Transfers the focus to the previous component, as though this Component
were the focus owner.

transferFocusUpCycle

```java
public void transferFocusUpCycle()
```

Transfers the focus up one focus traversal cycle. Typically, the focus
owner is set to this Component's focus cycle root, and the current focus
cycle root is set to the new focus owner's focus cycle root. If,
however, this Component's focus cycle root is a Window, then the focus
owner is set to the focus cycle root's default Component to focus, and
the current focus cycle root is unchanged.

**Since:** 1.4
**See Also:** requestFocus()

,

Container.isFocusCycleRoot()

,

Container.setFocusCycleRoot(boolean)

---

#### transferFocusUpCycle

public void transferFocusUpCycle()

Transfers the focus up one focus traversal cycle. Typically, the focus
owner is set to this Component's focus cycle root, and the current focus
cycle root is set to the new focus owner's focus cycle root. If,
however, this Component's focus cycle root is a Window, then the focus
owner is set to the focus cycle root's default Component to focus, and
the current focus cycle root is unchanged.

hasFocus

```java
public boolean hasFocus()
```

Returns

true

if this

Component

is the
focus owner. This method is obsolete, and has been replaced by

isFocusOwner()

.

**Returns:** true

if this

Component

is the
focus owner;

false

otherwise
**Since:** 1.2

---

#### hasFocus

public boolean hasFocus()

Returns

true

if this

Component

is the
focus owner. This method is obsolete, and has been replaced by

isFocusOwner()

.

isFocusOwner

```java
public boolean isFocusOwner()
```

Returns

true

if this

Component

is the
focus owner.

**Returns:** true

if this

Component

is the
focus owner;

false

otherwise
**Since:** 1.4

---

#### isFocusOwner

public boolean isFocusOwner()

Returns

true

if this

Component

is the
focus owner.

add

```java
public void add​(
PopupMenu
popup)
```

Adds the specified popup menu to the component.

**Parameters:** popup

- the popup menu to be added to the component.
**Throws:** NullPointerException

- if

popup

is

null
**Since:** 1.1
**See Also:** remove(MenuComponent)

---

#### add

public void add​(

PopupMenu

popup)

Adds the specified popup menu to the component.

remove

```java
public void remove​(
MenuComponent
popup)
```

Removes the specified popup menu from the component.

**Specified by:** remove

in interface

MenuContainer
**Parameters:** popup

- the popup menu to be removed
**Since:** 1.1
**See Also:** add(PopupMenu)

---

#### remove

public void remove​(

MenuComponent

popup)

Removes the specified popup menu from the component.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this component. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:** a string representation of this component's state
**Since:** 1.0

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this component. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

toString

```java
public
String
toString()
```

Returns a string representation of this component and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this component
**Since:** 1.0

---

#### toString

public

String

toString()

Returns a string representation of this component and its values.

list

```java
public void list()
```

Prints a listing of this component to the standard system output
stream

System.out

.

**Since:** 1.0
**See Also:** System.out

---

#### list

public void list()

Prints a listing of this component to the standard system output
stream

System.out

.

list

```java
public void list​(
PrintStream
out)
```

Prints a listing of this component to the specified output
stream.

**Parameters:** out

- a print stream
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0

---

#### list

public void list​(

PrintStream

out)

Prints a listing of this component to the specified output
stream.

list

```java
public void list​(
PrintStream
out,
int indent)
```

Prints out a list, starting at the specified indentation, to the
specified print stream.

**Parameters:** out

- a print stream
**Parameters:** indent

- number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0
**See Also:** PrintStream.println(java.lang.Object)

---

#### list

public void list​(

PrintStream

out,
int indent)

Prints out a list, starting at the specified indentation, to the
specified print stream.

list

```java
public void list​(
PrintWriter
out)
```

Prints a listing to the specified print writer.

**Parameters:** out

- the print writer to print to
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1

---

#### list

public void list​(

PrintWriter

out)

Prints a listing to the specified print writer.

list

```java
public void list​(
PrintWriter
out,
int indent)
```

Prints out a list, starting at the specified indentation, to
the specified print writer.

**Parameters:** out

- the print writer to print to
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1
**See Also:** PrintStream.println(java.lang.Object)

---

#### list

public void list​(

PrintWriter

out,
int indent)

Prints out a list, starting at the specified indentation, to
the specified print writer.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Component's preferred size ("preferredSize")
- this Component's minimum size ("minimumSize")
- this Component's maximum size ("maximumSize")
- this Component's name ("name")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

listener

is

null

,
no exception is thrown and no action is performed.

**Parameters:** listener

- the property change listener to be added
**See Also:** removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Component's preferred size ("preferredSize")
- this Component's minimum size ("minimumSize")
- this Component's maximum size ("maximumSize")
- this Component's name ("name")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

listener

is

null

,
no exception is thrown and no action is performed.

this Component's font ("font")

this Component's background color ("background")

this Component's foreground color ("foreground")

this Component's focusability ("focusable")

this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")

this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")

this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")

this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

this Component's preferred size ("preferredSize")

this Component's minimum size ("minimumSize")

this Component's maximum size ("maximumSize")

this Component's name ("name")

If

listener

is

null

,
no exception is thrown and no action is performed.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list. This method
should be used to remove PropertyChangeListeners that were registered
for all bound properties of this class.

If listener is null, no exception is thrown and no action is performed.

**Parameters:** listener

- the PropertyChangeListener to be removed
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

,

removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list. This method
should be used to remove PropertyChangeListeners that were registered
for all bound properties of this class.

If listener is null, no exception is thrown and no action is performed.

If listener is null, no exception is thrown and no action is performed.

getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this component.

**Returns:** all of this component's

PropertyChangeListener

s
or an empty array if no property change
listeners are currently registered
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

PropertyChangeSupport.getPropertyChangeListeners()

---

#### getPropertyChangeListeners

public

PropertyChangeListener

[] getPropertyChangeListeners()

Returns an array of all the property change listeners
registered on this component.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the property change listener to be added
**See Also:** removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following:

- this Component's font ("font")
- this Component's background color ("background")
- this Component's foreground color ("foreground")
- this Component's focusability ("focusable")
- this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

Note that if this

Component

is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

this Component's font ("font")

this Component's background color ("background")

this Component's foreground color ("foreground")

this Component's focusability ("focusable")

this Component's focus traversal keys enabled state
("focusTraversalKeysEnabled")

this Component's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")

this Component's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")

this Component's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener
list for a specific property. This method should be used to remove

PropertyChangeListener

s
that were registered for a specific bound property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

**Parameters:** propertyName

- a valid property name
**Parameters:** listener

- the PropertyChangeListener to be removed
**See Also:** addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners(java.lang.String)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

String

propertyName,

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener
list for a specific property. This method should be used to remove

PropertyChangeListener

s
that were registered for a specific bound property.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

If

propertyName

or

listener

is

null

,
no exception is thrown and no action is taken.

getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners​(
String
propertyName)
```

Returns an array of all the listeners which have been associated
with the named property.

**Parameters:** propertyName

- the property name
**Returns:** all of the

PropertyChangeListener

s associated with
the named property; if no such listeners have been added or
if

propertyName

is

null

, an empty
array is returned
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)

,

getPropertyChangeListeners()

---

#### getPropertyChangeListeners

public

PropertyChangeListener

[] getPropertyChangeListeners​(

String

propertyName)

Returns an array of all the listeners which have been associated
with the named property.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes for Object properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes for Object properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.4

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,
boolean oldValue,
boolean newValue)

Support for reporting bound property changes for boolean properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Support for reporting bound property changes for integer properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value
**Since:** 1.4

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,
int oldValue,
int newValue)

Support for reporting bound property changes for integer properties.
This method can be called when a bound property has changed and it will
send the appropriate PropertyChangeEvent to any registered
PropertyChangeListeners.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
byte oldValue,
byte newValue)

Reports a bound property change.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
char oldValue,
char newValue)

Reports a bound property change.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
short oldValue,
short newValue)

Reports a bound property change.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
long oldValue,
long newValue)

Reports a bound property change.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
float oldValue,
float newValue)

Reports a bound property change.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Reports a bound property change.

**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**Since:** 1.5
**See Also:** firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
double oldValue,
double newValue)

Reports a bound property change.

setComponentOrientation

```java
public void setComponentOrientation​(
ComponentOrientation
o)
```

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component. Language-sensitive

LayoutManager

and

Component

subclasses will use this property to
determine how to lay out and draw components.

At construction time, a component's orientation is set to

ComponentOrientation.UNKNOWN

,
indicating that it has not been specified
explicitly. The UNKNOWN orientation behaves the same as

ComponentOrientation.LEFT_TO_RIGHT

.

To set the orientation of a single component, use this method.
To set the orientation of an entire component
hierarchy, use

applyComponentOrientation

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** o

- the orientation to be set
**See Also:** ComponentOrientation

,

invalidate()

---

#### setComponentOrientation

public void setComponentOrientation​(

ComponentOrientation

o)

Sets the language-sensitive orientation that is to be used to order
the elements or text within this component. Language-sensitive

LayoutManager

and

Component

subclasses will use this property to
determine how to lay out and draw components.

At construction time, a component's orientation is set to

ComponentOrientation.UNKNOWN

,
indicating that it has not been specified
explicitly. The UNKNOWN orientation behaves the same as

ComponentOrientation.LEFT_TO_RIGHT

.

To set the orientation of a single component, use this method.
To set the orientation of an entire component
hierarchy, use

applyComponentOrientation

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

At construction time, a component's orientation is set to

ComponentOrientation.UNKNOWN

,
indicating that it has not been specified
explicitly. The UNKNOWN orientation behaves the same as

ComponentOrientation.LEFT_TO_RIGHT

.

To set the orientation of a single component, use this method.
To set the orientation of an entire component
hierarchy, use

applyComponentOrientation

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

To set the orientation of a single component, use this method.
To set the orientation of an entire component
hierarchy, use

applyComponentOrientation

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

getComponentOrientation

```java
public
ComponentOrientation
getComponentOrientation()
```

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

LayoutManager

and

Component

subclasses that wish to respect orientation should call this method to
get the component's orientation before performing layout or drawing.

**Returns:** the orientation to order the elements or text
**See Also:** ComponentOrientation

---

#### getComponentOrientation

public

ComponentOrientation

getComponentOrientation()

Retrieves the language-sensitive orientation that is to be used to order
the elements or text within this component.

LayoutManager

and

Component

subclasses that wish to respect orientation should call this method to
get the component's orientation before performing layout or drawing.

applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
orientation)
```

Sets the

ComponentOrientation

property of this component
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** orientation

- the new component orientation of this component and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** setComponentOrientation(java.awt.ComponentOrientation)

,

getComponentOrientation()

,

invalidate()

---

#### applyComponentOrientation

public void applyComponentOrientation​(

ComponentOrientation

orientation)

Sets the

ComponentOrientation

property of this component
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated
with this

Component

.
The method implemented by this base
class returns null. Classes that extend

Component

should implement this method to return the

AccessibleContext

associated with the subclass.

**Returns:** the

AccessibleContext

of this

Component
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated
with this

Component

.
The method implemented by this base
class returns null. Classes that extend

Component

should implement this method to return the

AccessibleContext

associated with the subclass.

setMixingCutoutShape

```java
public void setMixingCutoutShape​(
Shape
shape)
```

Sets a 'mixing-cutout' shape for this lightweight component.

This method is used exclusively for the purposes of the
Heavyweight/Lightweight Components Mixing feature and will
have no effect if applied to a heavyweight component.

By default a lightweight component is treated as an opaque rectangle for
the purposes of the Heavyweight/Lightweight Components Mixing feature.
This method enables developers to set an arbitrary shape to be cut out
from heavyweight components positioned underneath the lightweight
component in the z-order.

The

shape

argument may have the following values:

- null

- reverts the default cutout shape (the rectangle equal
to the component's

getBounds()

)

empty-shape

- does not cut out anything from heavyweight
components. This makes this lightweight component effectively
transparent. Note that descendants of the lightweight component still
affect the shapes of heavyweight components. An example of an

empty-shape

is

new Rectangle()

.

non-empty-shape

- the given shape will be cut out from
heavyweight components.

The most common example when the 'mixing-cutout' shape is needed is a
glass pane component. The

JRootPane.setGlassPane(java.awt.Component)

method
automatically sets the

empty-shape

as the 'mixing-cutout' shape
for the given glass pane component. If a developer needs some other
'mixing-cutout' shape for the glass pane (which is rare), this must be
changed manually after installing the glass pane to the root pane.

**Parameters:** shape

- the new 'mixing-cutout' shape
**Since:** 9

---

#### setMixingCutoutShape

public void setMixingCutoutShape​(

Shape

shape)

Sets a 'mixing-cutout' shape for this lightweight component.

This method is used exclusively for the purposes of the
Heavyweight/Lightweight Components Mixing feature and will
have no effect if applied to a heavyweight component.

By default a lightweight component is treated as an opaque rectangle for
the purposes of the Heavyweight/Lightweight Components Mixing feature.
This method enables developers to set an arbitrary shape to be cut out
from heavyweight components positioned underneath the lightweight
component in the z-order.

The

shape

argument may have the following values:

- null

- reverts the default cutout shape (the rectangle equal
to the component's

getBounds()

)

empty-shape

- does not cut out anything from heavyweight
components. This makes this lightweight component effectively
transparent. Note that descendants of the lightweight component still
affect the shapes of heavyweight components. An example of an

empty-shape

is

new Rectangle()

.

non-empty-shape

- the given shape will be cut out from
heavyweight components.

The most common example when the 'mixing-cutout' shape is needed is a
glass pane component. The

JRootPane.setGlassPane(java.awt.Component)

method
automatically sets the

empty-shape

as the 'mixing-cutout' shape
for the given glass pane component. If a developer needs some other
'mixing-cutout' shape for the glass pane (which is rare), this must be
changed manually after installing the glass pane to the root pane.

The

shape

argument may have the following values:

- null

- reverts the default cutout shape (the rectangle equal
to the component's

getBounds()

)

empty-shape

- does not cut out anything from heavyweight
components. This makes this lightweight component effectively
transparent. Note that descendants of the lightweight component still
affect the shapes of heavyweight components. An example of an

empty-shape

is

new Rectangle()

.

non-empty-shape

- the given shape will be cut out from
heavyweight components.

The most common example when the 'mixing-cutout' shape is needed is a
glass pane component. The

JRootPane.setGlassPane(java.awt.Component)

method
automatically sets the

empty-shape

as the 'mixing-cutout' shape
for the given glass pane component. If a developer needs some other
'mixing-cutout' shape for the glass pane (which is rare), this must be
changed manually after installing the glass pane to the root pane.

null

- reverts the default cutout shape (the rectangle equal
to the component's

getBounds()

)

empty-shape

- does not cut out anything from heavyweight
components. This makes this lightweight component effectively
transparent. Note that descendants of the lightweight component still
affect the shapes of heavyweight components. An example of an

empty-shape

is

new Rectangle()

.

non-empty-shape

- the given shape will be cut out from
heavyweight components.

The most common example when the 'mixing-cutout' shape is needed is a
glass pane component. The

JRootPane.setGlassPane(java.awt.Component)

method
automatically sets the

empty-shape

as the 'mixing-cutout' shape
for the given glass pane component. If a developer needs some other
'mixing-cutout' shape for the glass pane (which is rare), this must be
changed manually after installing the glass pane to the root pane.

---

