# Class RepaintManager

**Source:** `java.desktop\javax\swing\RepaintManager.html`

### Class Description

```java
public class
RepaintManager

extends
Object
```

This class manages repaint requests, allowing the number
of repaints to be minimized, for example by collapsing multiple
requests into a single repaint for members of a component tree.

As of 1.6

RepaintManager

handles repaint requests
for Swing's top level components (

JApplet

,

JWindow

,

JFrame

and

JDialog

).
Any calls to

repaint

on one of these will call into the
appropriate

addDirtyRegion

method.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

#### public RepaintManager()

Create a new RepaintManager instance. You rarely call this constructor.
directly. To get the default RepaintManager, use
RepaintManager.currentManager(JComponent) (normally "this").

---

### Method Details

#### public static
RepaintManager
currentManager​(
Component
c)

Return the RepaintManager for the calling thread given a Component.

**Parameters:**
- c

- a Component -- unused in the default implementation, but could
be used by an overridden version to return a different RepaintManager
depending on the Component

**Returns:**
- the RepaintManager object

---

#### public static
RepaintManager
currentManager​(
JComponent
c)

Return the RepaintManager for the calling thread given a JComponent.

Note: This method exists for backward binary compatibility with earlier
versions of the Swing library. It simply returns the result returned by

currentManager(Component)

.

**Parameters:**
- c

- a JComponent -- unused

**Returns:**
- the RepaintManager object

---

#### public static void setCurrentManager​(
RepaintManager
aRepaintManager)

Set the RepaintManager that should be used for the calling
thread.

aRepaintManager

will become the current RepaintManager
for the calling thread's thread group.

**Parameters:**
- aRepaintManager

- the RepaintManager object to use

---

#### public void addInvalidComponent​(
JComponent
invalidComponent)

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

**Parameters:**
- invalidComponent

- a component

**See Also:**
- JComponent.isValidateRoot()

,

removeInvalidComponent(javax.swing.JComponent)

---

#### public void removeInvalidComponent​(
JComponent
component)

Remove a component from the list of invalid components.

**Parameters:**
- component

- a component

**See Also:**
- addInvalidComponent(javax.swing.JComponent)

---

#### public void addDirtyRegion​(
JComponent
c,
int x,
int y,
int w,
int h)

Add a component in the list of components that should be refreshed.
If

c

already has a dirty region, the rectangle

(x,y,w,h)

will be unioned with the region that should be redrawn.

**Parameters:**
- c

- Component to repaint, null results in nothing happening.
- x

- X coordinate of the region to repaint
- y

- Y coordinate of the region to repaint
- w

- Width of the region to repaint
- h

- Height of the region to repaint

**See Also:**
- JComponent.repaint(long, int, int, int, int)

---

#### public void addDirtyRegion​(
Window
window,
int x,
int y,
int w,
int h)

Adds

window

to the list of

Component

s that
need to be repainted.

**Parameters:**
- window

- Window to repaint, null results in nothing happening.
- x

- X coordinate of the region to repaint
- y

- Y coordinate of the region to repaint
- w

- Width of the region to repaint
- h

- Height of the region to repaint

**See Also:**
- JFrame.repaint(long, int, int, int, int)

,

JWindow.repaint(long, int, int, int, int)

,

JDialog.repaint(long, int, int, int, int)

**Since:**
- 1.6

---

#### @Deprecated
(
since
="9")
public void addDirtyRegion​(
Applet
applet,
int x,
int y,
int w,
int h)

Adds

applet

to the list of

Component

s that
need to be repainted.

**Parameters:**
- applet

- Applet to repaint, null results in nothing happening.
- x

- X coordinate of the region to repaint
- y

- Y coordinate of the region to repaint
- w

- Width of the region to repaint
- h

- Height of the region to repaint

**See Also:**
- JApplet.repaint(long, int, int, int, int)

**Since:**
- 1.6

---

#### public
Rectangle
getDirtyRegion​(
JComponent
aComponent)

Return the current dirty region for a component.
Return an empty rectangle if the component is not
dirty.

**Parameters:**
- aComponent

- a component

**Returns:**
- the region

---

#### public void markCompletelyDirty​(
JComponent
aComponent)

Mark a component completely dirty.

aComponent

will be
completely painted during the next paintDirtyRegions() call.

**Parameters:**
- aComponent

- a component

---

#### public void markCompletelyClean​(
JComponent
aComponent)

Mark a component completely clean.

aComponent

will not
get painted during the next paintDirtyRegions() call.

**Parameters:**
- aComponent

- a component

---

#### public boolean isCompletelyDirty​(
JComponent
aComponent)

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions(). If computing dirty regions is
expensive for your component, use this method and avoid computing dirty region
if it return true.

**Parameters:**
- aComponent

- a component

**Returns:**
- true

if

aComponent

will be completely
painted during the next paintDirtyRegions().

---

#### public void validateInvalidComponents()

Validate all of the components that have been marked invalid.

**See Also:**
- addInvalidComponent(javax.swing.JComponent)

---

#### public void paintDirtyRegions()

Paint all of the components that have been marked dirty.

**See Also:**
- addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### public
String
toString()

Returns a string that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this object

---

#### public
Image
getOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)

Return the offscreen buffer that should be used as a double buffer with
the component

c

.
By default there is a double buffer per RepaintManager.
The buffer might be smaller than

(proposedWidth,proposedHeight)

This happens when the maximum double buffer size as been set for the receiving
repaint manager.

**Parameters:**
- c

- the component
- proposedWidth

- the width of the buffer
- proposedHeight

- the height of the buffer

**Returns:**
- the image

---

#### public
Image
getVolatileOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.
The image returned will be an instance of VolatileImage, or null
if a VolatileImage object could not be instantiated.
This buffer might be smaller than

(proposedWidth,proposedHeight)

.
This happens when the maximum double buffer size has been set for this
repaint manager.

**Parameters:**
- c

- the component
- proposedWidth

- the width of the buffer
- proposedHeight

- the height of the buffer

**Returns:**
- the volatile image

**See Also:**
- VolatileImage

**Since:**
- 1.4

---

#### public void setDoubleBufferMaximumSize​(
Dimension
d)

Set the maximum double buffer size.

**Parameters:**
- d

- the dimension

---

#### public
Dimension
getDoubleBufferMaximumSize()

Returns the maximum double buffer size.

**Returns:**
- a Dimension object representing the maximum size

---

#### public void setDoubleBufferingEnabled​(boolean aFlag)

Enables or disables double buffering in this RepaintManager.
CAUTION: The default value for this property is set for optimal
paint performance on the given platform and it is not recommended
that programs modify this property directly.

**Parameters:**
- aFlag

- true to activate double buffering

**See Also:**
- isDoubleBufferingEnabled()

---

#### public boolean isDoubleBufferingEnabled()

Returns true if this RepaintManager is double buffered.
The default value for this property may vary from platform
to platform. On platforms where native double buffering
is supported in the AWT, the default value will be

false

to avoid unnecessary buffering in Swing.
On platforms where native double buffering is not supported,
the default value will be

true

.

**Returns:**
- true if this object is double buffered

---

### Additional Sections

#### Class RepaintManager

java.lang.Object

- javax.swing.RepaintManager

javax.swing.RepaintManager

```java
public class
RepaintManager

extends
Object
```

This class manages repaint requests, allowing the number
of repaints to be minimized, for example by collapsing multiple
requests into a single repaint for members of a component tree.

As of 1.6

RepaintManager

handles repaint requests
for Swing's top level components (

JApplet

,

JWindow

,

JFrame

and

JDialog

).
Any calls to

repaint

on one of these will call into the
appropriate

addDirtyRegion

method.

**Since:** 1.2

public class

RepaintManager

extends

Object

This class manages repaint requests, allowing the number
of repaints to be minimized, for example by collapsing multiple
requests into a single repaint for members of a component tree.

As of 1.6

RepaintManager

handles repaint requests
for Swing's top level components (

JApplet

,

JWindow

,

JFrame

and

JDialog

).
Any calls to

repaint

on one of these will call into the
appropriate

addDirtyRegion

method.

As of 1.6

RepaintManager

handles repaint requests
for Swing's top level components (

JApplet

,

JWindow

,

JFrame

and

JDialog

).
Any calls to

repaint

on one of these will call into the
appropriate

addDirtyRegion

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RepaintManager

()

Create a new RepaintManager instance.

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

addDirtyRegion

​(

Applet

applet,
int x,
int y,
int w,
int h)

Deprecated.

The Applet API is deprecated.

void

addDirtyRegion

​(

Window

window,
int x,
int y,
int w,
int h)

Adds

window

to the list of

Component

s that
need to be repainted.

void

addDirtyRegion

​(

JComponent

c,
int x,
int y,
int w,
int h)

Add a component in the list of components that should be refreshed.

void

addInvalidComponent

​(

JComponent

invalidComponent)

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

static

RepaintManager

currentManager

​(

Component

c)

Return the RepaintManager for the calling thread given a Component.

static

RepaintManager

currentManager

​(

JComponent

c)

Return the RepaintManager for the calling thread given a JComponent.

Rectangle

getDirtyRegion

​(

JComponent

aComponent)

Return the current dirty region for a component.

Dimension

getDoubleBufferMaximumSize

()

Returns the maximum double buffer size.

Image

getOffscreenBuffer

​(

Component

c,
int proposedWidth,
int proposedHeight)

Return the offscreen buffer that should be used as a double buffer with
the component

c

.

Image

getVolatileOffscreenBuffer

​(

Component

c,
int proposedWidth,
int proposedHeight)

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.

boolean

isCompletelyDirty

​(

JComponent

aComponent)

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions().

boolean

isDoubleBufferingEnabled

()

Returns true if this RepaintManager is double buffered.

void

markCompletelyClean

​(

JComponent

aComponent)

Mark a component completely clean.

void

markCompletelyDirty

​(

JComponent

aComponent)

Mark a component completely dirty.

void

paintDirtyRegions

()

Paint all of the components that have been marked dirty.

void

removeInvalidComponent

​(

JComponent

component)

Remove a component from the list of invalid components.

static void

setCurrentManager

​(

RepaintManager

aRepaintManager)

Set the RepaintManager that should be used for the calling
thread.

void

setDoubleBufferingEnabled

​(boolean aFlag)

Enables or disables double buffering in this RepaintManager.

void

setDoubleBufferMaximumSize

​(

Dimension

d)

Set the maximum double buffer size.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

validateInvalidComponents

()

Validate all of the components that have been marked invalid.

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

Constructor Summary

Constructors

Constructor

Description

RepaintManager

()

Create a new RepaintManager instance.

---

#### Constructor Summary

Create a new RepaintManager instance.

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

addDirtyRegion

​(

Applet

applet,
int x,
int y,
int w,
int h)

Deprecated.

The Applet API is deprecated.

void

addDirtyRegion

​(

Window

window,
int x,
int y,
int w,
int h)

Adds

window

to the list of

Component

s that
need to be repainted.

void

addDirtyRegion

​(

JComponent

c,
int x,
int y,
int w,
int h)

Add a component in the list of components that should be refreshed.

void

addInvalidComponent

​(

JComponent

invalidComponent)

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

static

RepaintManager

currentManager

​(

Component

c)

Return the RepaintManager for the calling thread given a Component.

static

RepaintManager

currentManager

​(

JComponent

c)

Return the RepaintManager for the calling thread given a JComponent.

Rectangle

getDirtyRegion

​(

JComponent

aComponent)

Return the current dirty region for a component.

Dimension

getDoubleBufferMaximumSize

()

Returns the maximum double buffer size.

Image

getOffscreenBuffer

​(

Component

c,
int proposedWidth,
int proposedHeight)

Return the offscreen buffer that should be used as a double buffer with
the component

c

.

Image

getVolatileOffscreenBuffer

​(

Component

c,
int proposedWidth,
int proposedHeight)

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.

boolean

isCompletelyDirty

​(

JComponent

aComponent)

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions().

boolean

isDoubleBufferingEnabled

()

Returns true if this RepaintManager is double buffered.

void

markCompletelyClean

​(

JComponent

aComponent)

Mark a component completely clean.

void

markCompletelyDirty

​(

JComponent

aComponent)

Mark a component completely dirty.

void

paintDirtyRegions

()

Paint all of the components that have been marked dirty.

void

removeInvalidComponent

​(

JComponent

component)

Remove a component from the list of invalid components.

static void

setCurrentManager

​(

RepaintManager

aRepaintManager)

Set the RepaintManager that should be used for the calling
thread.

void

setDoubleBufferingEnabled

​(boolean aFlag)

Enables or disables double buffering in this RepaintManager.

void

setDoubleBufferMaximumSize

​(

Dimension

d)

Set the maximum double buffer size.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

validateInvalidComponents

()

Validate all of the components that have been marked invalid.

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

The Applet API is deprecated.

Adds

window

to the list of

Component

s that
need to be repainted.

Add a component in the list of components that should be refreshed.

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

Return the RepaintManager for the calling thread given a Component.

Return the RepaintManager for the calling thread given a JComponent.

Return the current dirty region for a component.

Returns the maximum double buffer size.

Return the offscreen buffer that should be used as a double buffer with
the component

c

.

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions().

Returns true if this RepaintManager is double buffered.

Mark a component completely clean.

Mark a component completely dirty.

Paint all of the components that have been marked dirty.

Remove a component from the list of invalid components.

Set the RepaintManager that should be used for the calling
thread.

Enables or disables double buffering in this RepaintManager.

Set the maximum double buffer size.

Returns a string that displays and identifies this
object's properties.

Validate all of the components that have been marked invalid.

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

- RepaintManager

```java
public RepaintManager()
```

Create a new RepaintManager instance. You rarely call this constructor.
directly. To get the default RepaintManager, use
RepaintManager.currentManager(JComponent) (normally "this").

============ METHOD DETAIL ==========

- Method Detail

- currentManager

```java
public static
RepaintManager
currentManager​(
Component
c)
```

Return the RepaintManager for the calling thread given a Component.

**Parameters:** c

- a Component -- unused in the default implementation, but could
be used by an overridden version to return a different RepaintManager
depending on the Component
**Returns:** the RepaintManager object

- currentManager

```java
public static
RepaintManager
currentManager​(
JComponent
c)
```

Return the RepaintManager for the calling thread given a JComponent.

Note: This method exists for backward binary compatibility with earlier
versions of the Swing library. It simply returns the result returned by

currentManager(Component)

.

**Parameters:** c

- a JComponent -- unused
**Returns:** the RepaintManager object

- setCurrentManager

```java
public static void setCurrentManager​(
RepaintManager
aRepaintManager)
```

Set the RepaintManager that should be used for the calling
thread.

aRepaintManager

will become the current RepaintManager
for the calling thread's thread group.

**Parameters:** aRepaintManager

- the RepaintManager object to use

- addInvalidComponent

```java
public void addInvalidComponent​(
JComponent
invalidComponent)
```

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

**Parameters:** invalidComponent

- a component
**See Also:** JComponent.isValidateRoot()

,

removeInvalidComponent(javax.swing.JComponent)

- removeInvalidComponent

```java
public void removeInvalidComponent​(
JComponent
component)
```

Remove a component from the list of invalid components.

**Parameters:** component

- a component
**See Also:** addInvalidComponent(javax.swing.JComponent)

- addDirtyRegion

```java
public void addDirtyRegion​(
JComponent
c,
int x,
int y,
int w,
int h)
```

Add a component in the list of components that should be refreshed.
If

c

already has a dirty region, the rectangle

(x,y,w,h)

will be unioned with the region that should be redrawn.

**Parameters:** c

- Component to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**See Also:** JComponent.repaint(long, int, int, int, int)

- addDirtyRegion

```java
public void addDirtyRegion​(
Window
window,
int x,
int y,
int w,
int h)
```

Adds

window

to the list of

Component

s that
need to be repainted.

**Parameters:** window

- Window to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**Since:** 1.6
**See Also:** JFrame.repaint(long, int, int, int, int)

,

JWindow.repaint(long, int, int, int, int)

,

JDialog.repaint(long, int, int, int, int)

- addDirtyRegion

```java
@Deprecated
(
since
="9")
public void addDirtyRegion​(
Applet
applet,
int x,
int y,
int w,
int h)
```

Deprecated.

The Applet API is deprecated. See the

java.applet package
documentation

for further information.

Adds

applet

to the list of

Component

s that
need to be repainted.

**Parameters:** applet

- Applet to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**Since:** 1.6
**See Also:** JApplet.repaint(long, int, int, int, int)

- getDirtyRegion

```java
public
Rectangle
getDirtyRegion​(
JComponent
aComponent)
```

Return the current dirty region for a component.
Return an empty rectangle if the component is not
dirty.

**Parameters:** aComponent

- a component
**Returns:** the region

- markCompletelyDirty

```java
public void markCompletelyDirty​(
JComponent
aComponent)
```

Mark a component completely dirty.

aComponent

will be
completely painted during the next paintDirtyRegions() call.

**Parameters:** aComponent

- a component

- markCompletelyClean

```java
public void markCompletelyClean​(
JComponent
aComponent)
```

Mark a component completely clean.

aComponent

will not
get painted during the next paintDirtyRegions() call.

**Parameters:** aComponent

- a component

- isCompletelyDirty

```java
public boolean isCompletelyDirty​(
JComponent
aComponent)
```

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions(). If computing dirty regions is
expensive for your component, use this method and avoid computing dirty region
if it return true.

**Parameters:** aComponent

- a component
**Returns:** true

if

aComponent

will be completely
painted during the next paintDirtyRegions().

- validateInvalidComponents

```java
public void validateInvalidComponents()
```

Validate all of the components that have been marked invalid.

**See Also:** addInvalidComponent(javax.swing.JComponent)

- paintDirtyRegions

```java
public void paintDirtyRegions()
```

Paint all of the components that have been marked dirty.

**See Also:** addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

- getOffscreenBuffer

```java
public
Image
getOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)
```

Return the offscreen buffer that should be used as a double buffer with
the component

c

.
By default there is a double buffer per RepaintManager.
The buffer might be smaller than

(proposedWidth,proposedHeight)

This happens when the maximum double buffer size as been set for the receiving
repaint manager.

**Parameters:** c

- the component
**Parameters:** proposedWidth

- the width of the buffer
**Parameters:** proposedHeight

- the height of the buffer
**Returns:** the image

- getVolatileOffscreenBuffer

```java
public
Image
getVolatileOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)
```

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.
The image returned will be an instance of VolatileImage, or null
if a VolatileImage object could not be instantiated.
This buffer might be smaller than

(proposedWidth,proposedHeight)

.
This happens when the maximum double buffer size has been set for this
repaint manager.

**Parameters:** c

- the component
**Parameters:** proposedWidth

- the width of the buffer
**Parameters:** proposedHeight

- the height of the buffer
**Returns:** the volatile image
**Since:** 1.4
**See Also:** VolatileImage

- setDoubleBufferMaximumSize

```java
public void setDoubleBufferMaximumSize​(
Dimension
d)
```

Set the maximum double buffer size.

**Parameters:** d

- the dimension

- getDoubleBufferMaximumSize

```java
public
Dimension
getDoubleBufferMaximumSize()
```

Returns the maximum double buffer size.

**Returns:** a Dimension object representing the maximum size

- setDoubleBufferingEnabled

```java
public void setDoubleBufferingEnabled​(boolean aFlag)
```

Enables or disables double buffering in this RepaintManager.
CAUTION: The default value for this property is set for optimal
paint performance on the given platform and it is not recommended
that programs modify this property directly.

**Parameters:** aFlag

- true to activate double buffering
**See Also:** isDoubleBufferingEnabled()

- isDoubleBufferingEnabled

```java
public boolean isDoubleBufferingEnabled()
```

Returns true if this RepaintManager is double buffered.
The default value for this property may vary from platform
to platform. On platforms where native double buffering
is supported in the AWT, the default value will be

false

to avoid unnecessary buffering in Swing.
On platforms where native double buffering is not supported,
the default value will be

true

.

**Returns:** true if this object is double buffered

Constructor Detail

- RepaintManager

```java
public RepaintManager()
```

Create a new RepaintManager instance. You rarely call this constructor.
directly. To get the default RepaintManager, use
RepaintManager.currentManager(JComponent) (normally "this").

---

#### Constructor Detail

RepaintManager

```java
public RepaintManager()
```

Create a new RepaintManager instance. You rarely call this constructor.
directly. To get the default RepaintManager, use
RepaintManager.currentManager(JComponent) (normally "this").

---

#### RepaintManager

public RepaintManager()

Create a new RepaintManager instance. You rarely call this constructor.
directly. To get the default RepaintManager, use
RepaintManager.currentManager(JComponent) (normally "this").

Method Detail

- currentManager

```java
public static
RepaintManager
currentManager​(
Component
c)
```

Return the RepaintManager for the calling thread given a Component.

**Parameters:** c

- a Component -- unused in the default implementation, but could
be used by an overridden version to return a different RepaintManager
depending on the Component
**Returns:** the RepaintManager object

- currentManager

```java
public static
RepaintManager
currentManager​(
JComponent
c)
```

Return the RepaintManager for the calling thread given a JComponent.

Note: This method exists for backward binary compatibility with earlier
versions of the Swing library. It simply returns the result returned by

currentManager(Component)

.

**Parameters:** c

- a JComponent -- unused
**Returns:** the RepaintManager object

- setCurrentManager

```java
public static void setCurrentManager​(
RepaintManager
aRepaintManager)
```

Set the RepaintManager that should be used for the calling
thread.

aRepaintManager

will become the current RepaintManager
for the calling thread's thread group.

**Parameters:** aRepaintManager

- the RepaintManager object to use

- addInvalidComponent

```java
public void addInvalidComponent​(
JComponent
invalidComponent)
```

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

**Parameters:** invalidComponent

- a component
**See Also:** JComponent.isValidateRoot()

,

removeInvalidComponent(javax.swing.JComponent)

- removeInvalidComponent

```java
public void removeInvalidComponent​(
JComponent
component)
```

Remove a component from the list of invalid components.

**Parameters:** component

- a component
**See Also:** addInvalidComponent(javax.swing.JComponent)

- addDirtyRegion

```java
public void addDirtyRegion​(
JComponent
c,
int x,
int y,
int w,
int h)
```

Add a component in the list of components that should be refreshed.
If

c

already has a dirty region, the rectangle

(x,y,w,h)

will be unioned with the region that should be redrawn.

**Parameters:** c

- Component to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**See Also:** JComponent.repaint(long, int, int, int, int)

- addDirtyRegion

```java
public void addDirtyRegion​(
Window
window,
int x,
int y,
int w,
int h)
```

Adds

window

to the list of

Component

s that
need to be repainted.

**Parameters:** window

- Window to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**Since:** 1.6
**See Also:** JFrame.repaint(long, int, int, int, int)

,

JWindow.repaint(long, int, int, int, int)

,

JDialog.repaint(long, int, int, int, int)

- addDirtyRegion

```java
@Deprecated
(
since
="9")
public void addDirtyRegion​(
Applet
applet,
int x,
int y,
int w,
int h)
```

Deprecated.

The Applet API is deprecated. See the

java.applet package
documentation

for further information.

Adds

applet

to the list of

Component

s that
need to be repainted.

**Parameters:** applet

- Applet to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**Since:** 1.6
**See Also:** JApplet.repaint(long, int, int, int, int)

- getDirtyRegion

```java
public
Rectangle
getDirtyRegion​(
JComponent
aComponent)
```

Return the current dirty region for a component.
Return an empty rectangle if the component is not
dirty.

**Parameters:** aComponent

- a component
**Returns:** the region

- markCompletelyDirty

```java
public void markCompletelyDirty​(
JComponent
aComponent)
```

Mark a component completely dirty.

aComponent

will be
completely painted during the next paintDirtyRegions() call.

**Parameters:** aComponent

- a component

- markCompletelyClean

```java
public void markCompletelyClean​(
JComponent
aComponent)
```

Mark a component completely clean.

aComponent

will not
get painted during the next paintDirtyRegions() call.

**Parameters:** aComponent

- a component

- isCompletelyDirty

```java
public boolean isCompletelyDirty​(
JComponent
aComponent)
```

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions(). If computing dirty regions is
expensive for your component, use this method and avoid computing dirty region
if it return true.

**Parameters:** aComponent

- a component
**Returns:** true

if

aComponent

will be completely
painted during the next paintDirtyRegions().

- validateInvalidComponents

```java
public void validateInvalidComponents()
```

Validate all of the components that have been marked invalid.

**See Also:** addInvalidComponent(javax.swing.JComponent)

- paintDirtyRegions

```java
public void paintDirtyRegions()
```

Paint all of the components that have been marked dirty.

**See Also:** addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

- getOffscreenBuffer

```java
public
Image
getOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)
```

Return the offscreen buffer that should be used as a double buffer with
the component

c

.
By default there is a double buffer per RepaintManager.
The buffer might be smaller than

(proposedWidth,proposedHeight)

This happens when the maximum double buffer size as been set for the receiving
repaint manager.

**Parameters:** c

- the component
**Parameters:** proposedWidth

- the width of the buffer
**Parameters:** proposedHeight

- the height of the buffer
**Returns:** the image

- getVolatileOffscreenBuffer

```java
public
Image
getVolatileOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)
```

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.
The image returned will be an instance of VolatileImage, or null
if a VolatileImage object could not be instantiated.
This buffer might be smaller than

(proposedWidth,proposedHeight)

.
This happens when the maximum double buffer size has been set for this
repaint manager.

**Parameters:** c

- the component
**Parameters:** proposedWidth

- the width of the buffer
**Parameters:** proposedHeight

- the height of the buffer
**Returns:** the volatile image
**Since:** 1.4
**See Also:** VolatileImage

- setDoubleBufferMaximumSize

```java
public void setDoubleBufferMaximumSize​(
Dimension
d)
```

Set the maximum double buffer size.

**Parameters:** d

- the dimension

- getDoubleBufferMaximumSize

```java
public
Dimension
getDoubleBufferMaximumSize()
```

Returns the maximum double buffer size.

**Returns:** a Dimension object representing the maximum size

- setDoubleBufferingEnabled

```java
public void setDoubleBufferingEnabled​(boolean aFlag)
```

Enables or disables double buffering in this RepaintManager.
CAUTION: The default value for this property is set for optimal
paint performance on the given platform and it is not recommended
that programs modify this property directly.

**Parameters:** aFlag

- true to activate double buffering
**See Also:** isDoubleBufferingEnabled()

- isDoubleBufferingEnabled

```java
public boolean isDoubleBufferingEnabled()
```

Returns true if this RepaintManager is double buffered.
The default value for this property may vary from platform
to platform. On platforms where native double buffering
is supported in the AWT, the default value will be

false

to avoid unnecessary buffering in Swing.
On platforms where native double buffering is not supported,
the default value will be

true

.

**Returns:** true if this object is double buffered

---

#### Method Detail

currentManager

```java
public static
RepaintManager
currentManager​(
Component
c)
```

Return the RepaintManager for the calling thread given a Component.

**Parameters:** c

- a Component -- unused in the default implementation, but could
be used by an overridden version to return a different RepaintManager
depending on the Component
**Returns:** the RepaintManager object

---

#### currentManager

public static

RepaintManager

currentManager​(

Component

c)

Return the RepaintManager for the calling thread given a Component.

currentManager

```java
public static
RepaintManager
currentManager​(
JComponent
c)
```

Return the RepaintManager for the calling thread given a JComponent.

Note: This method exists for backward binary compatibility with earlier
versions of the Swing library. It simply returns the result returned by

currentManager(Component)

.

**Parameters:** c

- a JComponent -- unused
**Returns:** the RepaintManager object

---

#### currentManager

public static

RepaintManager

currentManager​(

JComponent

c)

Return the RepaintManager for the calling thread given a JComponent.

Note: This method exists for backward binary compatibility with earlier
versions of the Swing library. It simply returns the result returned by

currentManager(Component)

.

Note: This method exists for backward binary compatibility with earlier
versions of the Swing library. It simply returns the result returned by

currentManager(Component)

.

setCurrentManager

```java
public static void setCurrentManager​(
RepaintManager
aRepaintManager)
```

Set the RepaintManager that should be used for the calling
thread.

aRepaintManager

will become the current RepaintManager
for the calling thread's thread group.

**Parameters:** aRepaintManager

- the RepaintManager object to use

---

#### setCurrentManager

public static void setCurrentManager​(

RepaintManager

aRepaintManager)

Set the RepaintManager that should be used for the calling
thread.

aRepaintManager

will become the current RepaintManager
for the calling thread's thread group.

addInvalidComponent

```java
public void addInvalidComponent​(
JComponent
invalidComponent)
```

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

**Parameters:** invalidComponent

- a component
**See Also:** JComponent.isValidateRoot()

,

removeInvalidComponent(javax.swing.JComponent)

---

#### addInvalidComponent

public void addInvalidComponent​(

JComponent

invalidComponent)

Mark the component as in need of layout and queue a runnable
for the event dispatching thread that will validate the components
first isValidateRoot() ancestor.

removeInvalidComponent

```java
public void removeInvalidComponent​(
JComponent
component)
```

Remove a component from the list of invalid components.

**Parameters:** component

- a component
**See Also:** addInvalidComponent(javax.swing.JComponent)

---

#### removeInvalidComponent

public void removeInvalidComponent​(

JComponent

component)

Remove a component from the list of invalid components.

addDirtyRegion

```java
public void addDirtyRegion​(
JComponent
c,
int x,
int y,
int w,
int h)
```

Add a component in the list of components that should be refreshed.
If

c

already has a dirty region, the rectangle

(x,y,w,h)

will be unioned with the region that should be redrawn.

**Parameters:** c

- Component to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**See Also:** JComponent.repaint(long, int, int, int, int)

---

#### addDirtyRegion

public void addDirtyRegion​(

JComponent

c,
int x,
int y,
int w,
int h)

Add a component in the list of components that should be refreshed.
If

c

already has a dirty region, the rectangle

(x,y,w,h)

will be unioned with the region that should be redrawn.

addDirtyRegion

```java
public void addDirtyRegion​(
Window
window,
int x,
int y,
int w,
int h)
```

Adds

window

to the list of

Component

s that
need to be repainted.

**Parameters:** window

- Window to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**Since:** 1.6
**See Also:** JFrame.repaint(long, int, int, int, int)

,

JWindow.repaint(long, int, int, int, int)

,

JDialog.repaint(long, int, int, int, int)

---

#### addDirtyRegion

public void addDirtyRegion​(

Window

window,
int x,
int y,
int w,
int h)

Adds

window

to the list of

Component

s that
need to be repainted.

addDirtyRegion

```java
@Deprecated
(
since
="9")
public void addDirtyRegion​(
Applet
applet,
int x,
int y,
int w,
int h)
```

Deprecated.

The Applet API is deprecated. See the

java.applet package
documentation

for further information.

Adds

applet

to the list of

Component

s that
need to be repainted.

**Parameters:** applet

- Applet to repaint, null results in nothing happening.
**Parameters:** x

- X coordinate of the region to repaint
**Parameters:** y

- Y coordinate of the region to repaint
**Parameters:** w

- Width of the region to repaint
**Parameters:** h

- Height of the region to repaint
**Since:** 1.6
**See Also:** JApplet.repaint(long, int, int, int, int)

---

#### addDirtyRegion

@Deprecated

(

since

="9")
public void addDirtyRegion​(

Applet

applet,
int x,
int y,
int w,
int h)

Adds

applet

to the list of

Component

s that
need to be repainted.

getDirtyRegion

```java
public
Rectangle
getDirtyRegion​(
JComponent
aComponent)
```

Return the current dirty region for a component.
Return an empty rectangle if the component is not
dirty.

**Parameters:** aComponent

- a component
**Returns:** the region

---

#### getDirtyRegion

public

Rectangle

getDirtyRegion​(

JComponent

aComponent)

Return the current dirty region for a component.
Return an empty rectangle if the component is not
dirty.

markCompletelyDirty

```java
public void markCompletelyDirty​(
JComponent
aComponent)
```

Mark a component completely dirty.

aComponent

will be
completely painted during the next paintDirtyRegions() call.

**Parameters:** aComponent

- a component

---

#### markCompletelyDirty

public void markCompletelyDirty​(

JComponent

aComponent)

Mark a component completely dirty.

aComponent

will be
completely painted during the next paintDirtyRegions() call.

markCompletelyClean

```java
public void markCompletelyClean​(
JComponent
aComponent)
```

Mark a component completely clean.

aComponent

will not
get painted during the next paintDirtyRegions() call.

**Parameters:** aComponent

- a component

---

#### markCompletelyClean

public void markCompletelyClean​(

JComponent

aComponent)

Mark a component completely clean.

aComponent

will not
get painted during the next paintDirtyRegions() call.

isCompletelyDirty

```java
public boolean isCompletelyDirty​(
JComponent
aComponent)
```

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions(). If computing dirty regions is
expensive for your component, use this method and avoid computing dirty region
if it return true.

**Parameters:** aComponent

- a component
**Returns:** true

if

aComponent

will be completely
painted during the next paintDirtyRegions().

---

#### isCompletelyDirty

public boolean isCompletelyDirty​(

JComponent

aComponent)

Convenience method that returns true if

aComponent

will be completely
painted during the next paintDirtyRegions(). If computing dirty regions is
expensive for your component, use this method and avoid computing dirty region
if it return true.

validateInvalidComponents

```java
public void validateInvalidComponents()
```

Validate all of the components that have been marked invalid.

**See Also:** addInvalidComponent(javax.swing.JComponent)

---

#### validateInvalidComponents

public void validateInvalidComponents()

Validate all of the components that have been marked invalid.

paintDirtyRegions

```java
public void paintDirtyRegions()
```

Paint all of the components that have been marked dirty.

**See Also:** addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### paintDirtyRegions

public void paintDirtyRegions()

Paint all of the components that have been marked dirty.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

getOffscreenBuffer

```java
public
Image
getOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)
```

Return the offscreen buffer that should be used as a double buffer with
the component

c

.
By default there is a double buffer per RepaintManager.
The buffer might be smaller than

(proposedWidth,proposedHeight)

This happens when the maximum double buffer size as been set for the receiving
repaint manager.

**Parameters:** c

- the component
**Parameters:** proposedWidth

- the width of the buffer
**Parameters:** proposedHeight

- the height of the buffer
**Returns:** the image

---

#### getOffscreenBuffer

public

Image

getOffscreenBuffer​(

Component

c,
int proposedWidth,
int proposedHeight)

Return the offscreen buffer that should be used as a double buffer with
the component

c

.
By default there is a double buffer per RepaintManager.
The buffer might be smaller than

(proposedWidth,proposedHeight)

This happens when the maximum double buffer size as been set for the receiving
repaint manager.

getVolatileOffscreenBuffer

```java
public
Image
getVolatileOffscreenBuffer​(
Component
c,
int proposedWidth,
int proposedHeight)
```

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.
The image returned will be an instance of VolatileImage, or null
if a VolatileImage object could not be instantiated.
This buffer might be smaller than

(proposedWidth,proposedHeight)

.
This happens when the maximum double buffer size has been set for this
repaint manager.

**Parameters:** c

- the component
**Parameters:** proposedWidth

- the width of the buffer
**Parameters:** proposedHeight

- the height of the buffer
**Returns:** the volatile image
**Since:** 1.4
**See Also:** VolatileImage

---

#### getVolatileOffscreenBuffer

public

Image

getVolatileOffscreenBuffer​(

Component

c,
int proposedWidth,
int proposedHeight)

Return a volatile offscreen buffer that should be used as a
double buffer with the specified component

c

.
The image returned will be an instance of VolatileImage, or null
if a VolatileImage object could not be instantiated.
This buffer might be smaller than

(proposedWidth,proposedHeight)

.
This happens when the maximum double buffer size has been set for this
repaint manager.

setDoubleBufferMaximumSize

```java
public void setDoubleBufferMaximumSize​(
Dimension
d)
```

Set the maximum double buffer size.

**Parameters:** d

- the dimension

---

#### setDoubleBufferMaximumSize

public void setDoubleBufferMaximumSize​(

Dimension

d)

Set the maximum double buffer size.

getDoubleBufferMaximumSize

```java
public
Dimension
getDoubleBufferMaximumSize()
```

Returns the maximum double buffer size.

**Returns:** a Dimension object representing the maximum size

---

#### getDoubleBufferMaximumSize

public

Dimension

getDoubleBufferMaximumSize()

Returns the maximum double buffer size.

setDoubleBufferingEnabled

```java
public void setDoubleBufferingEnabled​(boolean aFlag)
```

Enables or disables double buffering in this RepaintManager.
CAUTION: The default value for this property is set for optimal
paint performance on the given platform and it is not recommended
that programs modify this property directly.

**Parameters:** aFlag

- true to activate double buffering
**See Also:** isDoubleBufferingEnabled()

---

#### setDoubleBufferingEnabled

public void setDoubleBufferingEnabled​(boolean aFlag)

Enables or disables double buffering in this RepaintManager.
CAUTION: The default value for this property is set for optimal
paint performance on the given platform and it is not recommended
that programs modify this property directly.

isDoubleBufferingEnabled

```java
public boolean isDoubleBufferingEnabled()
```

Returns true if this RepaintManager is double buffered.
The default value for this property may vary from platform
to platform. On platforms where native double buffering
is supported in the AWT, the default value will be

false

to avoid unnecessary buffering in Swing.
On platforms where native double buffering is not supported,
the default value will be

true

.

**Returns:** true if this object is double buffered

---

#### isDoubleBufferingEnabled

public boolean isDoubleBufferingEnabled()

Returns true if this RepaintManager is double buffered.
The default value for this property may vary from platform
to platform. On platforms where native double buffering
is supported in the AWT, the default value will be

false

to avoid unnecessary buffering in Swing.
On platforms where native double buffering is not supported,
the default value will be

true

.

---

