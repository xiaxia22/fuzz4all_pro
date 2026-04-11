# Class DefaultDesktopManager

**Source:** `java.desktop\javax\swing\DefaultDesktopManager.html`

### Class Description

```java
public class
DefaultDesktopManager

extends
Object

implements
DesktopManager
,
Serializable
```

This is an implementation of the

DesktopManager

.
It currently implements the basic behaviors for managing

JInternalFrame

s in an arbitrary parent.

JInternalFrame

s that are not children of a

JDesktop

will use this component
to handle their desktop-like actions.

This class provides a policy for the various JInternalFrame methods,
it is not meant to be called directly rather the various JInternalFrame
methods will call into the DesktopManager.

**All Implemented Interfaces:** Serializable

,

DesktopManager

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultDesktopManager()

*No description found.*

---

### Method Details

#### public void openFrame​(
JInternalFrame
f)

Normally this method will not be called. If it is, it
tries to determine the appropriate parent from the desktopIcon of the frame.
Will remove the desktopIcon from its parent if it successfully adds the frame.

**Specified by:**
- openFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JInternalFrame

to be displayed

---

#### public void closeFrame​(
JInternalFrame
f)

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

**Specified by:**
- closeFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JInternalFrame

to be removed

---

#### public void maximizeFrame​(
JInternalFrame
f)

Resizes the frame to fill its parents bounds.

**Specified by:**
- maximizeFrame

in interface

DesktopManager

**Parameters:**
- f

- the frame to be resized

---

#### public void minimizeFrame​(
JInternalFrame
f)

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

**Specified by:**
- minimizeFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JInternalFrame

to be restored

---

#### public void iconifyFrame​(
JInternalFrame
f)

Removes the frame from its parent and adds its

desktopIcon

to the parent.

**Specified by:**
- iconifyFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JInternalFrame

to be iconified

---

#### public void deiconifyFrame​(
JInternalFrame
f)

Removes the desktopIcon from its parent and adds its frame
to the parent.

**Specified by:**
- deiconifyFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JInternalFrame

to be de-iconified

---

#### public void activateFrame​(
JInternalFrame
f)

This will activate

f

moving it to the front. It will
set the current active frame's (if any)

IS_SELECTED_PROPERTY

to

false

.
There can be only one active frame across all Layers.

**Specified by:**
- activateFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JInternalFrame

to be activated

---

#### public void dragFrame​(
JComponent
f,
int newX,
int newY)

Moves the visible location of the frame being dragged
to the location specified. The means by which this occurs can vary depending
on the dragging algorithm being used. The actual logical location of the frame
might not change until

endDraggingFrame

is called.

**Specified by:**
- dragFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JComponent

being dragged
- newX

- the new x-coordinate
- newY

- the new y-coordinate

---

#### public void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)

Calls

setBoundsForFrame

with the new values.

**Specified by:**
- resizeFrame

in interface

DesktopManager

**Parameters:**
- f

- the component to be resized
- newX

- the new x-coordinate
- newY

- the new y-coordinate
- newWidth

- the new width
- newHeight

- the new height

---

#### public void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)

This moves the

JComponent

and repaints the damaged areas.

**Specified by:**
- setBoundsForFrame

in interface

DesktopManager

**Parameters:**
- f

- the

JComponent

being moved or resized
- newX

- the new x-coordinate
- newY

- the new y-coordinate
- newWidth

- the new width
- newHeight

- the new height

---

#### protected void removeIconFor​(
JInternalFrame
f)

Convenience method to remove the desktopIcon of

f

is necessary.

**Parameters:**
- f

- the

JInternalFrame

for which to remove the

desktopIcon

---

#### protected
Rectangle
getBoundsForIconOf​(
JInternalFrame
f)

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

**Parameters:**
- f

- the

JInternalFrame

of interest

**Returns:**
- a

Rectangle

containing bounds for the

desktopIcon

---

#### protected void setPreviousBounds​(
JInternalFrame
f,

Rectangle
r)

Stores the bounds of the component just before a maximize call.

**Parameters:**
- f

- the component about to be resized
- r

- the normal bounds to be saved away

---

#### protected
Rectangle
getPreviousBounds​(
JInternalFrame
f)

Gets the normal bounds of the component prior to the component
being maximized.

**Parameters:**
- f

- the

JInternalFrame

of interest

**Returns:**
- the normal bounds of the component

---

#### protected void setWasIcon​(
JInternalFrame
f,

Boolean
value)

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

**Parameters:**
- f

- the

JInternalFrame

of interest
- value

- a

Boolean

signifying if component has been iconized

---

#### protected boolean wasIcon​(
JInternalFrame
f)

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

**Parameters:**
- f

- the

JInternalFrame

of interest

**Returns:**
- true

if the component has been iconized;
otherwise returns

false

---

### Additional Sections

#### Class DefaultDesktopManager

java.lang.Object

- javax.swing.DefaultDesktopManager

javax.swing.DefaultDesktopManager

**All Implemented Interfaces:** Serializable

,

DesktopManager

```java
public class
DefaultDesktopManager

extends
Object

implements
DesktopManager
,
Serializable
```

This is an implementation of the

DesktopManager

.
It currently implements the basic behaviors for managing

JInternalFrame

s in an arbitrary parent.

JInternalFrame

s that are not children of a

JDesktop

will use this component
to handle their desktop-like actions.

This class provides a policy for the various JInternalFrame methods,
it is not meant to be called directly rather the various JInternalFrame
methods will call into the DesktopManager.

**Since:** 1.2
**See Also:** JDesktopPane

,

JInternalFrame

,

Serialized Form

public class

DefaultDesktopManager

extends

Object

implements

DesktopManager

,

Serializable

This is an implementation of the

DesktopManager

.
It currently implements the basic behaviors for managing

JInternalFrame

s in an arbitrary parent.

JInternalFrame

s that are not children of a

JDesktop

will use this component
to handle their desktop-like actions.

This class provides a policy for the various JInternalFrame methods,
it is not meant to be called directly rather the various JInternalFrame
methods will call into the DesktopManager.

This class provides a policy for the various JInternalFrame methods,
it is not meant to be called directly rather the various JInternalFrame
methods will call into the DesktopManager.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultDesktopManager

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

activateFrame

​(

JInternalFrame

f)

This will activate

f

moving it to the front.

void

closeFrame

​(

JInternalFrame

f)

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

void

deiconifyFrame

​(

JInternalFrame

f)

Removes the desktopIcon from its parent and adds its frame
to the parent.

void

dragFrame

​(

JComponent

f,
int newX,
int newY)

Moves the visible location of the frame being dragged
to the location specified.

protected

Rectangle

getBoundsForIconOf

​(

JInternalFrame

f)

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

protected

Rectangle

getPreviousBounds

​(

JInternalFrame

f)

Gets the normal bounds of the component prior to the component
being maximized.

void

iconifyFrame

​(

JInternalFrame

f)

Removes the frame from its parent and adds its

desktopIcon

to the parent.

void

maximizeFrame

​(

JInternalFrame

f)

Resizes the frame to fill its parents bounds.

void

minimizeFrame

​(

JInternalFrame

f)

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

void

openFrame

​(

JInternalFrame

f)

Normally this method will not be called.

protected void

removeIconFor

​(

JInternalFrame

f)

Convenience method to remove the desktopIcon of

f

is necessary.

void

resizeFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

Calls

setBoundsForFrame

with the new values.

void

setBoundsForFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

This moves the

JComponent

and repaints the damaged areas.

protected void

setPreviousBounds

​(

JInternalFrame

f,

Rectangle

r)

Stores the bounds of the component just before a maximize call.

protected void

setWasIcon

​(

JInternalFrame

f,

Boolean

value)

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

protected boolean

wasIcon

​(

JInternalFrame

f)

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.swing.

DesktopManager

beginDraggingFrame

,

beginResizingFrame

,

deactivateFrame

,

endDraggingFrame

,

endResizingFrame

Constructor Summary

Constructors

Constructor

Description

DefaultDesktopManager

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

activateFrame

​(

JInternalFrame

f)

This will activate

f

moving it to the front.

void

closeFrame

​(

JInternalFrame

f)

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

void

deiconifyFrame

​(

JInternalFrame

f)

Removes the desktopIcon from its parent and adds its frame
to the parent.

void

dragFrame

​(

JComponent

f,
int newX,
int newY)

Moves the visible location of the frame being dragged
to the location specified.

protected

Rectangle

getBoundsForIconOf

​(

JInternalFrame

f)

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

protected

Rectangle

getPreviousBounds

​(

JInternalFrame

f)

Gets the normal bounds of the component prior to the component
being maximized.

void

iconifyFrame

​(

JInternalFrame

f)

Removes the frame from its parent and adds its

desktopIcon

to the parent.

void

maximizeFrame

​(

JInternalFrame

f)

Resizes the frame to fill its parents bounds.

void

minimizeFrame

​(

JInternalFrame

f)

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

void

openFrame

​(

JInternalFrame

f)

Normally this method will not be called.

protected void

removeIconFor

​(

JInternalFrame

f)

Convenience method to remove the desktopIcon of

f

is necessary.

void

resizeFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

Calls

setBoundsForFrame

with the new values.

void

setBoundsForFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

This moves the

JComponent

and repaints the damaged areas.

protected void

setPreviousBounds

​(

JInternalFrame

f,

Rectangle

r)

Stores the bounds of the component just before a maximize call.

protected void

setWasIcon

​(

JInternalFrame

f,

Boolean

value)

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

protected boolean

wasIcon

​(

JInternalFrame

f)

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.swing.

DesktopManager

beginDraggingFrame

,

beginResizingFrame

,

deactivateFrame

,

endDraggingFrame

,

endResizingFrame

---

#### Method Summary

This will activate

f

moving it to the front.

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

Removes the desktopIcon from its parent and adds its frame
to the parent.

Moves the visible location of the frame being dragged
to the location specified.

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

Gets the normal bounds of the component prior to the component
being maximized.

Removes the frame from its parent and adds its

desktopIcon

to the parent.

Resizes the frame to fill its parents bounds.

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

Normally this method will not be called.

Convenience method to remove the desktopIcon of

f

is necessary.

Calls

setBoundsForFrame

with the new values.

This moves the

JComponent

and repaints the damaged areas.

Stores the bounds of the component just before a maximize call.

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface javax.swing.

DesktopManager

beginDraggingFrame

,

beginResizingFrame

,

deactivateFrame

,

endDraggingFrame

,

endResizingFrame

---

#### Methods declared in interface javax.swing. DesktopManager

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultDesktopManager

```java
public DefaultDesktopManager()
```

============ METHOD DETAIL ==========

- Method Detail

- openFrame

```java
public void openFrame​(
JInternalFrame
f)
```

Normally this method will not be called. If it is, it
tries to determine the appropriate parent from the desktopIcon of the frame.
Will remove the desktopIcon from its parent if it successfully adds the frame.

**Specified by:** openFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be displayed

- closeFrame

```java
public void closeFrame​(
JInternalFrame
f)
```

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

**Specified by:** closeFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be removed

- maximizeFrame

```java
public void maximizeFrame​(
JInternalFrame
f)
```

Resizes the frame to fill its parents bounds.

**Specified by:** maximizeFrame

in interface

DesktopManager
**Parameters:** f

- the frame to be resized

- minimizeFrame

```java
public void minimizeFrame​(
JInternalFrame
f)
```

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

**Specified by:** minimizeFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be restored

- iconifyFrame

```java
public void iconifyFrame​(
JInternalFrame
f)
```

Removes the frame from its parent and adds its

desktopIcon

to the parent.

**Specified by:** iconifyFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be iconified

- deiconifyFrame

```java
public void deiconifyFrame​(
JInternalFrame
f)
```

Removes the desktopIcon from its parent and adds its frame
to the parent.

**Specified by:** deiconifyFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be de-iconified

- activateFrame

```java
public void activateFrame​(
JInternalFrame
f)
```

This will activate

f

moving it to the front. It will
set the current active frame's (if any)

IS_SELECTED_PROPERTY

to

false

.
There can be only one active frame across all Layers.

**Specified by:** activateFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be activated

- dragFrame

```java
public void dragFrame​(
JComponent
f,
int newX,
int newY)
```

Moves the visible location of the frame being dragged
to the location specified. The means by which this occurs can vary depending
on the dragging algorithm being used. The actual logical location of the frame
might not change until

endDraggingFrame

is called.

**Specified by:** dragFrame

in interface

DesktopManager
**Parameters:** f

- the

JComponent

being dragged
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate

- resizeFrame

```java
public void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

Calls

setBoundsForFrame

with the new values.

**Specified by:** resizeFrame

in interface

DesktopManager
**Parameters:** f

- the component to be resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

- setBoundsForFrame

```java
public void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

This moves the

JComponent

and repaints the damaged areas.

**Specified by:** setBoundsForFrame

in interface

DesktopManager
**Parameters:** f

- the

JComponent

being moved or resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

- removeIconFor

```java
protected void removeIconFor​(
JInternalFrame
f)
```

Convenience method to remove the desktopIcon of

f

is necessary.

**Parameters:** f

- the

JInternalFrame

for which to remove the

desktopIcon

- getBoundsForIconOf

```java
protected
Rectangle
getBoundsForIconOf​(
JInternalFrame
f)
```

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** a

Rectangle

containing bounds for the

desktopIcon

- setPreviousBounds

```java
protected void setPreviousBounds​(
JInternalFrame
f,

Rectangle
r)
```

Stores the bounds of the component just before a maximize call.

**Parameters:** f

- the component about to be resized
**Parameters:** r

- the normal bounds to be saved away

- getPreviousBounds

```java
protected
Rectangle
getPreviousBounds​(
JInternalFrame
f)
```

Gets the normal bounds of the component prior to the component
being maximized.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** the normal bounds of the component

- setWasIcon

```java
protected void setWasIcon​(
JInternalFrame
f,

Boolean
value)
```

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

**Parameters:** f

- the

JInternalFrame

of interest
**Parameters:** value

- a

Boolean

signifying if component has been iconized

- wasIcon

```java
protected boolean wasIcon​(
JInternalFrame
f)
```

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** true

if the component has been iconized;
otherwise returns

false

Constructor Detail

- DefaultDesktopManager

```java
public DefaultDesktopManager()
```

---

#### Constructor Detail

DefaultDesktopManager

```java
public DefaultDesktopManager()
```

---

#### DefaultDesktopManager

public DefaultDesktopManager()

Method Detail

- openFrame

```java
public void openFrame​(
JInternalFrame
f)
```

Normally this method will not be called. If it is, it
tries to determine the appropriate parent from the desktopIcon of the frame.
Will remove the desktopIcon from its parent if it successfully adds the frame.

**Specified by:** openFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be displayed

- closeFrame

```java
public void closeFrame​(
JInternalFrame
f)
```

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

**Specified by:** closeFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be removed

- maximizeFrame

```java
public void maximizeFrame​(
JInternalFrame
f)
```

Resizes the frame to fill its parents bounds.

**Specified by:** maximizeFrame

in interface

DesktopManager
**Parameters:** f

- the frame to be resized

- minimizeFrame

```java
public void minimizeFrame​(
JInternalFrame
f)
```

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

**Specified by:** minimizeFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be restored

- iconifyFrame

```java
public void iconifyFrame​(
JInternalFrame
f)
```

Removes the frame from its parent and adds its

desktopIcon

to the parent.

**Specified by:** iconifyFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be iconified

- deiconifyFrame

```java
public void deiconifyFrame​(
JInternalFrame
f)
```

Removes the desktopIcon from its parent and adds its frame
to the parent.

**Specified by:** deiconifyFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be de-iconified

- activateFrame

```java
public void activateFrame​(
JInternalFrame
f)
```

This will activate

f

moving it to the front. It will
set the current active frame's (if any)

IS_SELECTED_PROPERTY

to

false

.
There can be only one active frame across all Layers.

**Specified by:** activateFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be activated

- dragFrame

```java
public void dragFrame​(
JComponent
f,
int newX,
int newY)
```

Moves the visible location of the frame being dragged
to the location specified. The means by which this occurs can vary depending
on the dragging algorithm being used. The actual logical location of the frame
might not change until

endDraggingFrame

is called.

**Specified by:** dragFrame

in interface

DesktopManager
**Parameters:** f

- the

JComponent

being dragged
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate

- resizeFrame

```java
public void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

Calls

setBoundsForFrame

with the new values.

**Specified by:** resizeFrame

in interface

DesktopManager
**Parameters:** f

- the component to be resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

- setBoundsForFrame

```java
public void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

This moves the

JComponent

and repaints the damaged areas.

**Specified by:** setBoundsForFrame

in interface

DesktopManager
**Parameters:** f

- the

JComponent

being moved or resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

- removeIconFor

```java
protected void removeIconFor​(
JInternalFrame
f)
```

Convenience method to remove the desktopIcon of

f

is necessary.

**Parameters:** f

- the

JInternalFrame

for which to remove the

desktopIcon

- getBoundsForIconOf

```java
protected
Rectangle
getBoundsForIconOf​(
JInternalFrame
f)
```

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** a

Rectangle

containing bounds for the

desktopIcon

- setPreviousBounds

```java
protected void setPreviousBounds​(
JInternalFrame
f,

Rectangle
r)
```

Stores the bounds of the component just before a maximize call.

**Parameters:** f

- the component about to be resized
**Parameters:** r

- the normal bounds to be saved away

- getPreviousBounds

```java
protected
Rectangle
getPreviousBounds​(
JInternalFrame
f)
```

Gets the normal bounds of the component prior to the component
being maximized.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** the normal bounds of the component

- setWasIcon

```java
protected void setWasIcon​(
JInternalFrame
f,

Boolean
value)
```

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

**Parameters:** f

- the

JInternalFrame

of interest
**Parameters:** value

- a

Boolean

signifying if component has been iconized

- wasIcon

```java
protected boolean wasIcon​(
JInternalFrame
f)
```

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** true

if the component has been iconized;
otherwise returns

false

---

#### Method Detail

openFrame

```java
public void openFrame​(
JInternalFrame
f)
```

Normally this method will not be called. If it is, it
tries to determine the appropriate parent from the desktopIcon of the frame.
Will remove the desktopIcon from its parent if it successfully adds the frame.

**Specified by:** openFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be displayed

---

#### openFrame

public void openFrame​(

JInternalFrame

f)

Normally this method will not be called. If it is, it
tries to determine the appropriate parent from the desktopIcon of the frame.
Will remove the desktopIcon from its parent if it successfully adds the frame.

closeFrame

```java
public void closeFrame​(
JInternalFrame
f)
```

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

**Specified by:** closeFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be removed

---

#### closeFrame

public void closeFrame​(

JInternalFrame

f)

Removes the frame, and, if necessary, the

desktopIcon

, from its parent.

maximizeFrame

```java
public void maximizeFrame​(
JInternalFrame
f)
```

Resizes the frame to fill its parents bounds.

**Specified by:** maximizeFrame

in interface

DesktopManager
**Parameters:** f

- the frame to be resized

---

#### maximizeFrame

public void maximizeFrame​(

JInternalFrame

f)

Resizes the frame to fill its parents bounds.

minimizeFrame

```java
public void minimizeFrame​(
JInternalFrame
f)
```

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

**Specified by:** minimizeFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be restored

---

#### minimizeFrame

public void minimizeFrame​(

JInternalFrame

f)

Restores the frame back to its size and position prior
to a

maximizeFrame

call.

iconifyFrame

```java
public void iconifyFrame​(
JInternalFrame
f)
```

Removes the frame from its parent and adds its

desktopIcon

to the parent.

**Specified by:** iconifyFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be iconified

---

#### iconifyFrame

public void iconifyFrame​(

JInternalFrame

f)

Removes the frame from its parent and adds its

desktopIcon

to the parent.

deiconifyFrame

```java
public void deiconifyFrame​(
JInternalFrame
f)
```

Removes the desktopIcon from its parent and adds its frame
to the parent.

**Specified by:** deiconifyFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be de-iconified

---

#### deiconifyFrame

public void deiconifyFrame​(

JInternalFrame

f)

Removes the desktopIcon from its parent and adds its frame
to the parent.

activateFrame

```java
public void activateFrame​(
JInternalFrame
f)
```

This will activate

f

moving it to the front. It will
set the current active frame's (if any)

IS_SELECTED_PROPERTY

to

false

.
There can be only one active frame across all Layers.

**Specified by:** activateFrame

in interface

DesktopManager
**Parameters:** f

- the

JInternalFrame

to be activated

---

#### activateFrame

public void activateFrame​(

JInternalFrame

f)

This will activate

f

moving it to the front. It will
set the current active frame's (if any)

IS_SELECTED_PROPERTY

to

false

.
There can be only one active frame across all Layers.

dragFrame

```java
public void dragFrame​(
JComponent
f,
int newX,
int newY)
```

Moves the visible location of the frame being dragged
to the location specified. The means by which this occurs can vary depending
on the dragging algorithm being used. The actual logical location of the frame
might not change until

endDraggingFrame

is called.

**Specified by:** dragFrame

in interface

DesktopManager
**Parameters:** f

- the

JComponent

being dragged
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate

---

#### dragFrame

public void dragFrame​(

JComponent

f,
int newX,
int newY)

Moves the visible location of the frame being dragged
to the location specified. The means by which this occurs can vary depending
on the dragging algorithm being used. The actual logical location of the frame
might not change until

endDraggingFrame

is called.

resizeFrame

```java
public void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

Calls

setBoundsForFrame

with the new values.

**Specified by:** resizeFrame

in interface

DesktopManager
**Parameters:** f

- the component to be resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

---

#### resizeFrame

public void resizeFrame​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

Calls

setBoundsForFrame

with the new values.

setBoundsForFrame

```java
public void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

This moves the

JComponent

and repaints the damaged areas.

**Specified by:** setBoundsForFrame

in interface

DesktopManager
**Parameters:** f

- the

JComponent

being moved or resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

---

#### setBoundsForFrame

public void setBoundsForFrame​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

This moves the

JComponent

and repaints the damaged areas.

removeIconFor

```java
protected void removeIconFor​(
JInternalFrame
f)
```

Convenience method to remove the desktopIcon of

f

is necessary.

**Parameters:** f

- the

JInternalFrame

for which to remove the

desktopIcon

---

#### removeIconFor

protected void removeIconFor​(

JInternalFrame

f)

Convenience method to remove the desktopIcon of

f

is necessary.

getBoundsForIconOf

```java
protected
Rectangle
getBoundsForIconOf​(
JInternalFrame
f)
```

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** a

Rectangle

containing bounds for the

desktopIcon

---

#### getBoundsForIconOf

protected

Rectangle

getBoundsForIconOf​(

JInternalFrame

f)

The

iconifyFrame()

code calls this to determine the proper bounds
for the desktopIcon.

setPreviousBounds

```java
protected void setPreviousBounds​(
JInternalFrame
f,

Rectangle
r)
```

Stores the bounds of the component just before a maximize call.

**Parameters:** f

- the component about to be resized
**Parameters:** r

- the normal bounds to be saved away

---

#### setPreviousBounds

protected void setPreviousBounds​(

JInternalFrame

f,

Rectangle

r)

Stores the bounds of the component just before a maximize call.

getPreviousBounds

```java
protected
Rectangle
getPreviousBounds​(
JInternalFrame
f)
```

Gets the normal bounds of the component prior to the component
being maximized.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** the normal bounds of the component

---

#### getPreviousBounds

protected

Rectangle

getPreviousBounds​(

JInternalFrame

f)

Gets the normal bounds of the component prior to the component
being maximized.

setWasIcon

```java
protected void setWasIcon​(
JInternalFrame
f,

Boolean
value)
```

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

**Parameters:** f

- the

JInternalFrame

of interest
**Parameters:** value

- a

Boolean

signifying if component has been iconized

---

#### setWasIcon

protected void setWasIcon​(

JInternalFrame

f,

Boolean

value)

Sets that the component has been iconized and the bounds of the

desktopIcon

are valid.

wasIcon

```java
protected boolean wasIcon​(
JInternalFrame
f)
```

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

**Parameters:** f

- the

JInternalFrame

of interest
**Returns:** true

if the component has been iconized;
otherwise returns

false

---

#### wasIcon

protected boolean wasIcon​(

JInternalFrame

f)

Returns

true

if the component has been iconized
and the bounds of the

desktopIcon

are valid,
otherwise returns

false

.

---

