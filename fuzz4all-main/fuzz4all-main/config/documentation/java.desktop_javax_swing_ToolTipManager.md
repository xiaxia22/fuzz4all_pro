# Class ToolTipManager

**Source:** `java.desktop\javax\swing\ToolTipManager.html`

### Class Description

```java
public class
ToolTipManager

extends
MouseAdapter

implements
MouseMotionListener
```

Manages all the

ToolTips

in the system.

ToolTipManager contains numerous properties for configuring how long it
will take for the tooltips to become visible, and how long till they
hide. Consider a component that has a different tooltip based on where
the mouse is, such as JTree. When the mouse moves into the JTree and
over a region that has a valid tooltip, the tooltip will become
visible after

initialDelay

milliseconds. After

dismissDelay

milliseconds the tooltip will be hidden. If
the mouse is over a region that has a valid tooltip, and the tooltip
is currently visible, when the mouse moves to a region that doesn't have
a valid tooltip the tooltip will be hidden. If the mouse then moves back
into a region that has a valid tooltip within

reshowDelay

milliseconds, the tooltip will immediately be shown, otherwise the
tooltip will be shown again after

initialDelay

milliseconds.

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

EventListener

---

### Field Details

#### protected boolean lightWeightPopupEnabled

Lightweight popup enabled.

---

#### protected boolean heavyWeightPopupEnabled

Heavyweight popup enabled.

---

### Constructor Details

*No entries found.*

### Method Details

#### public void setEnabled​(boolean flag)

Enables or disables the tooltip.

**Parameters:**
- flag

- true to enable the tip, false otherwise

---

#### public boolean isEnabled()

Returns true if this object is enabled.

**Returns:**
- true if this object is enabled, false otherwise

---

#### public void setLightWeightPopupEnabled​(boolean aFlag)

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits. This method allows you to
disable this feature. You have to do disable it if your
application mixes light weight and heavy weights components.

**Parameters:**
- aFlag

- true if a lightweight panel is desired, false otherwise

---

#### public boolean isLightWeightPopupEnabled()

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

**Returns:**
- true if lightweight

ToolTips

are in use

---

#### public void setInitialDelay​(int milliseconds)

Specifies the initial delay value.

**Parameters:**
- milliseconds

- the number of milliseconds to delay
(after the cursor has paused) before displaying the
tooltip

**See Also:**
- getInitialDelay()

---

#### public int getInitialDelay()

Returns the initial delay value.

**Returns:**
- an integer representing the initial delay value,
in milliseconds

**See Also:**
- setInitialDelay(int)

---

#### public void setDismissDelay​(int milliseconds)

Specifies the dismissal delay value.

**Parameters:**
- milliseconds

- the number of milliseconds to delay
before taking away the tooltip

**See Also:**
- getDismissDelay()

---

#### public int getDismissDelay()

Returns the dismissal delay value.

**Returns:**
- an integer representing the dismissal delay value,
in milliseconds

**See Also:**
- setDismissDelay(int)

---

#### public void setReshowDelay​(int milliseconds)

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown. That is, if the tooltip is hidden, and the user moves into
a region of the same Component that has a valid tooltip within

milliseconds

milliseconds the tooltip will immediately
be shown. Otherwise, if the user moves into a region with a valid
tooltip after

milliseconds

milliseconds, the user
will have to wait an additional

initialDelay

milliseconds before the tooltip is shown again.

**Parameters:**
- milliseconds

- time in milliseconds

**See Also:**
- getReshowDelay()

---

#### public int getReshowDelay()

Returns the reshow delay property.

**Returns:**
- reshown delay property

**See Also:**
- setReshowDelay(int)

---

#### public static
ToolTipManager
sharedInstance()

Returns a shared

ToolTipManager

instance.

**Returns:**
- a shared

ToolTipManager

object

---

#### public void registerComponent​(
JComponent
component)

Registers a component for tooltip management.

This will register key bindings to show and hide the tooltip text
only if

component

has focus bindings. This is done
so that components that are not normally focus traversable, such
as

JLabel

, are not made focus traversable as a result
of invoking this method.

**Parameters:**
- component

- a

JComponent

object to add

**See Also:**
- Component.isFocusTraversable()

---

#### public void unregisterComponent​(
JComponent
component)

Removes a component from tooltip control.

**Parameters:**
- component

- a

JComponent

object to remove

---

#### public void mouseEntered​(
MouseEvent
event)

Called when the mouse enters the region of a component.
This determines whether the tool tip should be shown.

**Specified by:**
- mouseEntered

in interface

MouseListener

**Parameters:**
- event

- the event in question

---

#### public void mouseExited​(
MouseEvent
event)

Called when the mouse exits the region of a component.
Any tool tip showing should be hidden.

**Specified by:**
- mouseExited

in interface

MouseListener

**Parameters:**
- event

- the event in question

---

#### public void mousePressed​(
MouseEvent
event)

Called when the mouse is pressed.
Any tool tip showing should be hidden.

**Specified by:**
- mousePressed

in interface

MouseListener

**Parameters:**
- event

- the event in question

---

#### public void mouseDragged​(
MouseEvent
event)

Called when the mouse is pressed and dragged.
Does nothing.

**Specified by:**
- mouseDragged

in interface

MouseMotionListener

**Overrides:**
- mouseDragged

in class

MouseAdapter

**Parameters:**
- event

- the event in question

---

#### public void mouseMoved​(
MouseEvent
event)

Called when the mouse is moved.
Determines whether the tool tip should be displayed.

**Specified by:**
- mouseMoved

in interface

MouseMotionListener

**Overrides:**
- mouseMoved

in class

MouseAdapter

**Parameters:**
- event

- the event in question

---

### Additional Sections

#### Class ToolTipManager

java.lang.Object

- java.awt.event.MouseAdapter
- - javax.swing.ToolTipManager

java.awt.event.MouseAdapter

- javax.swing.ToolTipManager

javax.swing.ToolTipManager

**All Implemented Interfaces:** MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

EventListener

```java
public class
ToolTipManager

extends
MouseAdapter

implements
MouseMotionListener
```

Manages all the

ToolTips

in the system.

ToolTipManager contains numerous properties for configuring how long it
will take for the tooltips to become visible, and how long till they
hide. Consider a component that has a different tooltip based on where
the mouse is, such as JTree. When the mouse moves into the JTree and
over a region that has a valid tooltip, the tooltip will become
visible after

initialDelay

milliseconds. After

dismissDelay

milliseconds the tooltip will be hidden. If
the mouse is over a region that has a valid tooltip, and the tooltip
is currently visible, when the mouse moves to a region that doesn't have
a valid tooltip the tooltip will be hidden. If the mouse then moves back
into a region that has a valid tooltip within

reshowDelay

milliseconds, the tooltip will immediately be shown, otherwise the
tooltip will be shown again after

initialDelay

milliseconds.

**Since:** 1.2
**See Also:** JComponent.createToolTip()

public class

ToolTipManager

extends

MouseAdapter

implements

MouseMotionListener

Manages all the

ToolTips

in the system.

ToolTipManager contains numerous properties for configuring how long it
will take for the tooltips to become visible, and how long till they
hide. Consider a component that has a different tooltip based on where
the mouse is, such as JTree. When the mouse moves into the JTree and
over a region that has a valid tooltip, the tooltip will become
visible after

initialDelay

milliseconds. After

dismissDelay

milliseconds the tooltip will be hidden. If
the mouse is over a region that has a valid tooltip, and the tooltip
is currently visible, when the mouse moves to a region that doesn't have
a valid tooltip the tooltip will be hidden. If the mouse then moves back
into a region that has a valid tooltip within

reshowDelay

milliseconds, the tooltip will immediately be shown, otherwise the
tooltip will be shown again after

initialDelay

milliseconds.

ToolTipManager contains numerous properties for configuring how long it
will take for the tooltips to become visible, and how long till they
hide. Consider a component that has a different tooltip based on where
the mouse is, such as JTree. When the mouse moves into the JTree and
over a region that has a valid tooltip, the tooltip will become
visible after

initialDelay

milliseconds. After

dismissDelay

milliseconds the tooltip will be hidden. If
the mouse is over a region that has a valid tooltip, and the tooltip
is currently visible, when the mouse moves to a region that doesn't have
a valid tooltip the tooltip will be hidden. If the mouse then moves back
into a region that has a valid tooltip within

reshowDelay

milliseconds, the tooltip will immediately be shown, otherwise the
tooltip will be shown again after

initialDelay

milliseconds.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

ToolTipManager.insideTimerAction

Inside timer action.

protected class

ToolTipManager.outsideTimerAction

Outside timer action.

protected class

ToolTipManager.stillInsideTimerAction

Still inside timer action.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

heavyWeightPopupEnabled

Heavyweight popup enabled.

protected boolean

lightWeightPopupEnabled

Lightweight popup enabled.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDismissDelay

()

Returns the dismissal delay value.

int

getInitialDelay

()

Returns the initial delay value.

int

getReshowDelay

()

Returns the reshow delay property.

boolean

isEnabled

()

Returns true if this object is enabled.

boolean

isLightWeightPopupEnabled

()

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

void

mouseDragged

​(

MouseEvent

event)

Called when the mouse is pressed and dragged.

void

mouseEntered

​(

MouseEvent

event)

Called when the mouse enters the region of a component.

void

mouseExited

​(

MouseEvent

event)

Called when the mouse exits the region of a component.

void

mouseMoved

​(

MouseEvent

event)

Called when the mouse is moved.

void

mousePressed

​(

MouseEvent

event)

Called when the mouse is pressed.

void

registerComponent

​(

JComponent

component)

Registers a component for tooltip management.

void

setDismissDelay

​(int milliseconds)

Specifies the dismissal delay value.

void

setEnabled

​(boolean flag)

Enables or disables the tooltip.

void

setInitialDelay

​(int milliseconds)

Specifies the initial delay value.

void

setLightWeightPopupEnabled

​(boolean aFlag)

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits.

void

setReshowDelay

​(int milliseconds)

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown.

static

ToolTipManager

sharedInstance

()

Returns a shared

ToolTipManager

instance.

void

unregisterComponent

​(

JComponent

component)

Removes a component from tooltip control.

- Methods declared in class java.awt.event.

MouseAdapter

mouseWheelMoved

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

- Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseReleased

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

ToolTipManager.insideTimerAction

Inside timer action.

protected class

ToolTipManager.outsideTimerAction

Outside timer action.

protected class

ToolTipManager.stillInsideTimerAction

Still inside timer action.

---

#### Nested Class Summary

Inside timer action.

Outside timer action.

Still inside timer action.

Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

heavyWeightPopupEnabled

Heavyweight popup enabled.

protected boolean

lightWeightPopupEnabled

Lightweight popup enabled.

---

#### Field Summary

Heavyweight popup enabled.

Lightweight popup enabled.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDismissDelay

()

Returns the dismissal delay value.

int

getInitialDelay

()

Returns the initial delay value.

int

getReshowDelay

()

Returns the reshow delay property.

boolean

isEnabled

()

Returns true if this object is enabled.

boolean

isLightWeightPopupEnabled

()

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

void

mouseDragged

​(

MouseEvent

event)

Called when the mouse is pressed and dragged.

void

mouseEntered

​(

MouseEvent

event)

Called when the mouse enters the region of a component.

void

mouseExited

​(

MouseEvent

event)

Called when the mouse exits the region of a component.

void

mouseMoved

​(

MouseEvent

event)

Called when the mouse is moved.

void

mousePressed

​(

MouseEvent

event)

Called when the mouse is pressed.

void

registerComponent

​(

JComponent

component)

Registers a component for tooltip management.

void

setDismissDelay

​(int milliseconds)

Specifies the dismissal delay value.

void

setEnabled

​(boolean flag)

Enables or disables the tooltip.

void

setInitialDelay

​(int milliseconds)

Specifies the initial delay value.

void

setLightWeightPopupEnabled

​(boolean aFlag)

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits.

void

setReshowDelay

​(int milliseconds)

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown.

static

ToolTipManager

sharedInstance

()

Returns a shared

ToolTipManager

instance.

void

unregisterComponent

​(

JComponent

component)

Removes a component from tooltip control.

- Methods declared in class java.awt.event.

MouseAdapter

mouseWheelMoved

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

- Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseReleased

---

#### Method Summary

Returns the dismissal delay value.

Returns the initial delay value.

Returns the reshow delay property.

Returns true if this object is enabled.

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

Called when the mouse is pressed and dragged.

Called when the mouse enters the region of a component.

Called when the mouse exits the region of a component.

Called when the mouse is moved.

Called when the mouse is pressed.

Registers a component for tooltip management.

Specifies the dismissal delay value.

Enables or disables the tooltip.

Specifies the initial delay value.

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits.

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown.

Returns a shared

ToolTipManager

instance.

Removes a component from tooltip control.

Methods declared in class java.awt.event.

MouseAdapter

mouseWheelMoved

---

#### Methods declared in class java.awt.event. MouseAdapter

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

Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseReleased

---

#### Methods declared in interface java.awt.event. MouseListener

============ FIELD DETAIL ===========

- Field Detail

- lightWeightPopupEnabled

```java
protected boolean lightWeightPopupEnabled
```

Lightweight popup enabled.

- heavyWeightPopupEnabled

```java
protected boolean heavyWeightPopupEnabled
```

Heavyweight popup enabled.

============ METHOD DETAIL ==========

- Method Detail

- setEnabled

```java
public void setEnabled​(boolean flag)
```

Enables or disables the tooltip.

**Parameters:** flag

- true to enable the tip, false otherwise

- isEnabled

```java
public boolean isEnabled()
```

Returns true if this object is enabled.

**Returns:** true if this object is enabled, false otherwise

- setLightWeightPopupEnabled

```java
public void setLightWeightPopupEnabled​(boolean aFlag)
```

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits. This method allows you to
disable this feature. You have to do disable it if your
application mixes light weight and heavy weights components.

**Parameters:** aFlag

- true if a lightweight panel is desired, false otherwise

- isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

**Returns:** true if lightweight

ToolTips

are in use

- setInitialDelay

```java
public void setInitialDelay​(int milliseconds)
```

Specifies the initial delay value.

**Parameters:** milliseconds

- the number of milliseconds to delay
(after the cursor has paused) before displaying the
tooltip
**See Also:** getInitialDelay()

- getInitialDelay

```java
public int getInitialDelay()
```

Returns the initial delay value.

**Returns:** an integer representing the initial delay value,
in milliseconds
**See Also:** setInitialDelay(int)

- setDismissDelay

```java
public void setDismissDelay​(int milliseconds)
```

Specifies the dismissal delay value.

**Parameters:** milliseconds

- the number of milliseconds to delay
before taking away the tooltip
**See Also:** getDismissDelay()

- getDismissDelay

```java
public int getDismissDelay()
```

Returns the dismissal delay value.

**Returns:** an integer representing the dismissal delay value,
in milliseconds
**See Also:** setDismissDelay(int)

- setReshowDelay

```java
public void setReshowDelay​(int milliseconds)
```

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown. That is, if the tooltip is hidden, and the user moves into
a region of the same Component that has a valid tooltip within

milliseconds

milliseconds the tooltip will immediately
be shown. Otherwise, if the user moves into a region with a valid
tooltip after

milliseconds

milliseconds, the user
will have to wait an additional

initialDelay

milliseconds before the tooltip is shown again.

**Parameters:** milliseconds

- time in milliseconds
**See Also:** getReshowDelay()

- getReshowDelay

```java
public int getReshowDelay()
```

Returns the reshow delay property.

**Returns:** reshown delay property
**See Also:** setReshowDelay(int)

- sharedInstance

```java
public static
ToolTipManager
sharedInstance()
```

Returns a shared

ToolTipManager

instance.

**Returns:** a shared

ToolTipManager

object

- registerComponent

```java
public void registerComponent​(
JComponent
component)
```

Registers a component for tooltip management.

This will register key bindings to show and hide the tooltip text
only if

component

has focus bindings. This is done
so that components that are not normally focus traversable, such
as

JLabel

, are not made focus traversable as a result
of invoking this method.

**Parameters:** component

- a

JComponent

object to add
**See Also:** Component.isFocusTraversable()

- unregisterComponent

```java
public void unregisterComponent​(
JComponent
component)
```

Removes a component from tooltip control.

**Parameters:** component

- a

JComponent

object to remove

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
event)
```

Called when the mouse enters the region of a component.
This determines whether the tool tip should be shown.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** event

- the event in question

- mouseExited

```java
public void mouseExited​(
MouseEvent
event)
```

Called when the mouse exits the region of a component.
Any tool tip showing should be hidden.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** event

- the event in question

- mousePressed

```java
public void mousePressed​(
MouseEvent
event)
```

Called when the mouse is pressed.
Any tool tip showing should be hidden.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** event

- the event in question

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
event)
```

Called when the mouse is pressed and dragged.
Does nothing.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Overrides:** mouseDragged

in class

MouseAdapter
**Parameters:** event

- the event in question

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
event)
```

Called when the mouse is moved.
Determines whether the tool tip should be displayed.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Overrides:** mouseMoved

in class

MouseAdapter
**Parameters:** event

- the event in question

Field Detail

- lightWeightPopupEnabled

```java
protected boolean lightWeightPopupEnabled
```

Lightweight popup enabled.

- heavyWeightPopupEnabled

```java
protected boolean heavyWeightPopupEnabled
```

Heavyweight popup enabled.

---

#### Field Detail

lightWeightPopupEnabled

```java
protected boolean lightWeightPopupEnabled
```

Lightweight popup enabled.

---

#### lightWeightPopupEnabled

protected boolean lightWeightPopupEnabled

Lightweight popup enabled.

heavyWeightPopupEnabled

```java
protected boolean heavyWeightPopupEnabled
```

Heavyweight popup enabled.

---

#### heavyWeightPopupEnabled

protected boolean heavyWeightPopupEnabled

Heavyweight popup enabled.

Method Detail

- setEnabled

```java
public void setEnabled​(boolean flag)
```

Enables or disables the tooltip.

**Parameters:** flag

- true to enable the tip, false otherwise

- isEnabled

```java
public boolean isEnabled()
```

Returns true if this object is enabled.

**Returns:** true if this object is enabled, false otherwise

- setLightWeightPopupEnabled

```java
public void setLightWeightPopupEnabled​(boolean aFlag)
```

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits. This method allows you to
disable this feature. You have to do disable it if your
application mixes light weight and heavy weights components.

**Parameters:** aFlag

- true if a lightweight panel is desired, false otherwise

- isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

**Returns:** true if lightweight

ToolTips

are in use

- setInitialDelay

```java
public void setInitialDelay​(int milliseconds)
```

Specifies the initial delay value.

**Parameters:** milliseconds

- the number of milliseconds to delay
(after the cursor has paused) before displaying the
tooltip
**See Also:** getInitialDelay()

- getInitialDelay

```java
public int getInitialDelay()
```

Returns the initial delay value.

**Returns:** an integer representing the initial delay value,
in milliseconds
**See Also:** setInitialDelay(int)

- setDismissDelay

```java
public void setDismissDelay​(int milliseconds)
```

Specifies the dismissal delay value.

**Parameters:** milliseconds

- the number of milliseconds to delay
before taking away the tooltip
**See Also:** getDismissDelay()

- getDismissDelay

```java
public int getDismissDelay()
```

Returns the dismissal delay value.

**Returns:** an integer representing the dismissal delay value,
in milliseconds
**See Also:** setDismissDelay(int)

- setReshowDelay

```java
public void setReshowDelay​(int milliseconds)
```

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown. That is, if the tooltip is hidden, and the user moves into
a region of the same Component that has a valid tooltip within

milliseconds

milliseconds the tooltip will immediately
be shown. Otherwise, if the user moves into a region with a valid
tooltip after

milliseconds

milliseconds, the user
will have to wait an additional

initialDelay

milliseconds before the tooltip is shown again.

**Parameters:** milliseconds

- time in milliseconds
**See Also:** getReshowDelay()

- getReshowDelay

```java
public int getReshowDelay()
```

Returns the reshow delay property.

**Returns:** reshown delay property
**See Also:** setReshowDelay(int)

- sharedInstance

```java
public static
ToolTipManager
sharedInstance()
```

Returns a shared

ToolTipManager

instance.

**Returns:** a shared

ToolTipManager

object

- registerComponent

```java
public void registerComponent​(
JComponent
component)
```

Registers a component for tooltip management.

This will register key bindings to show and hide the tooltip text
only if

component

has focus bindings. This is done
so that components that are not normally focus traversable, such
as

JLabel

, are not made focus traversable as a result
of invoking this method.

**Parameters:** component

- a

JComponent

object to add
**See Also:** Component.isFocusTraversable()

- unregisterComponent

```java
public void unregisterComponent​(
JComponent
component)
```

Removes a component from tooltip control.

**Parameters:** component

- a

JComponent

object to remove

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
event)
```

Called when the mouse enters the region of a component.
This determines whether the tool tip should be shown.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** event

- the event in question

- mouseExited

```java
public void mouseExited​(
MouseEvent
event)
```

Called when the mouse exits the region of a component.
Any tool tip showing should be hidden.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** event

- the event in question

- mousePressed

```java
public void mousePressed​(
MouseEvent
event)
```

Called when the mouse is pressed.
Any tool tip showing should be hidden.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** event

- the event in question

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
event)
```

Called when the mouse is pressed and dragged.
Does nothing.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Overrides:** mouseDragged

in class

MouseAdapter
**Parameters:** event

- the event in question

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
event)
```

Called when the mouse is moved.
Determines whether the tool tip should be displayed.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Overrides:** mouseMoved

in class

MouseAdapter
**Parameters:** event

- the event in question

---

#### Method Detail

setEnabled

```java
public void setEnabled​(boolean flag)
```

Enables or disables the tooltip.

**Parameters:** flag

- true to enable the tip, false otherwise

---

#### setEnabled

public void setEnabled​(boolean flag)

Enables or disables the tooltip.

isEnabled

```java
public boolean isEnabled()
```

Returns true if this object is enabled.

**Returns:** true if this object is enabled, false otherwise

---

#### isEnabled

public boolean isEnabled()

Returns true if this object is enabled.

setLightWeightPopupEnabled

```java
public void setLightWeightPopupEnabled​(boolean aFlag)
```

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits. This method allows you to
disable this feature. You have to do disable it if your
application mixes light weight and heavy weights components.

**Parameters:** aFlag

- true if a lightweight panel is desired, false otherwise

---

#### setLightWeightPopupEnabled

public void setLightWeightPopupEnabled​(boolean aFlag)

When displaying the

JToolTip

, the

ToolTipManager

chooses to use a lightweight

JPanel

if it fits. This method allows you to
disable this feature. You have to do disable it if your
application mixes light weight and heavy weights components.

isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

**Returns:** true if lightweight

ToolTips

are in use

---

#### isLightWeightPopupEnabled

public boolean isLightWeightPopupEnabled()

Returns true if lightweight (all-Java)

Tooltips

are in use, or false if heavyweight (native peer)

Tooltips

are being used.

setInitialDelay

```java
public void setInitialDelay​(int milliseconds)
```

Specifies the initial delay value.

**Parameters:** milliseconds

- the number of milliseconds to delay
(after the cursor has paused) before displaying the
tooltip
**See Also:** getInitialDelay()

---

#### setInitialDelay

public void setInitialDelay​(int milliseconds)

Specifies the initial delay value.

getInitialDelay

```java
public int getInitialDelay()
```

Returns the initial delay value.

**Returns:** an integer representing the initial delay value,
in milliseconds
**See Also:** setInitialDelay(int)

---

#### getInitialDelay

public int getInitialDelay()

Returns the initial delay value.

setDismissDelay

```java
public void setDismissDelay​(int milliseconds)
```

Specifies the dismissal delay value.

**Parameters:** milliseconds

- the number of milliseconds to delay
before taking away the tooltip
**See Also:** getDismissDelay()

---

#### setDismissDelay

public void setDismissDelay​(int milliseconds)

Specifies the dismissal delay value.

getDismissDelay

```java
public int getDismissDelay()
```

Returns the dismissal delay value.

**Returns:** an integer representing the dismissal delay value,
in milliseconds
**See Also:** setDismissDelay(int)

---

#### getDismissDelay

public int getDismissDelay()

Returns the dismissal delay value.

setReshowDelay

```java
public void setReshowDelay​(int milliseconds)
```

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown. That is, if the tooltip is hidden, and the user moves into
a region of the same Component that has a valid tooltip within

milliseconds

milliseconds the tooltip will immediately
be shown. Otherwise, if the user moves into a region with a valid
tooltip after

milliseconds

milliseconds, the user
will have to wait an additional

initialDelay

milliseconds before the tooltip is shown again.

**Parameters:** milliseconds

- time in milliseconds
**See Also:** getReshowDelay()

---

#### setReshowDelay

public void setReshowDelay​(int milliseconds)

Used to specify the amount of time before the user has to wait

initialDelay

milliseconds before a tooltip will be
shown. That is, if the tooltip is hidden, and the user moves into
a region of the same Component that has a valid tooltip within

milliseconds

milliseconds the tooltip will immediately
be shown. Otherwise, if the user moves into a region with a valid
tooltip after

milliseconds

milliseconds, the user
will have to wait an additional

initialDelay

milliseconds before the tooltip is shown again.

getReshowDelay

```java
public int getReshowDelay()
```

Returns the reshow delay property.

**Returns:** reshown delay property
**See Also:** setReshowDelay(int)

---

#### getReshowDelay

public int getReshowDelay()

Returns the reshow delay property.

sharedInstance

```java
public static
ToolTipManager
sharedInstance()
```

Returns a shared

ToolTipManager

instance.

**Returns:** a shared

ToolTipManager

object

---

#### sharedInstance

public static

ToolTipManager

sharedInstance()

Returns a shared

ToolTipManager

instance.

registerComponent

```java
public void registerComponent​(
JComponent
component)
```

Registers a component for tooltip management.

This will register key bindings to show and hide the tooltip text
only if

component

has focus bindings. This is done
so that components that are not normally focus traversable, such
as

JLabel

, are not made focus traversable as a result
of invoking this method.

**Parameters:** component

- a

JComponent

object to add
**See Also:** Component.isFocusTraversable()

---

#### registerComponent

public void registerComponent​(

JComponent

component)

Registers a component for tooltip management.

This will register key bindings to show and hide the tooltip text
only if

component

has focus bindings. This is done
so that components that are not normally focus traversable, such
as

JLabel

, are not made focus traversable as a result
of invoking this method.

This will register key bindings to show and hide the tooltip text
only if

component

has focus bindings. This is done
so that components that are not normally focus traversable, such
as

JLabel

, are not made focus traversable as a result
of invoking this method.

unregisterComponent

```java
public void unregisterComponent​(
JComponent
component)
```

Removes a component from tooltip control.

**Parameters:** component

- a

JComponent

object to remove

---

#### unregisterComponent

public void unregisterComponent​(

JComponent

component)

Removes a component from tooltip control.

mouseEntered

```java
public void mouseEntered​(
MouseEvent
event)
```

Called when the mouse enters the region of a component.
This determines whether the tool tip should be shown.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** event

- the event in question

---

#### mouseEntered

public void mouseEntered​(

MouseEvent

event)

Called when the mouse enters the region of a component.
This determines whether the tool tip should be shown.

mouseExited

```java
public void mouseExited​(
MouseEvent
event)
```

Called when the mouse exits the region of a component.
Any tool tip showing should be hidden.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** event

- the event in question

---

#### mouseExited

public void mouseExited​(

MouseEvent

event)

Called when the mouse exits the region of a component.
Any tool tip showing should be hidden.

mousePressed

```java
public void mousePressed​(
MouseEvent
event)
```

Called when the mouse is pressed.
Any tool tip showing should be hidden.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** event

- the event in question

---

#### mousePressed

public void mousePressed​(

MouseEvent

event)

Called when the mouse is pressed.
Any tool tip showing should be hidden.

mouseDragged

```java
public void mouseDragged​(
MouseEvent
event)
```

Called when the mouse is pressed and dragged.
Does nothing.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Overrides:** mouseDragged

in class

MouseAdapter
**Parameters:** event

- the event in question

---

#### mouseDragged

public void mouseDragged​(

MouseEvent

event)

Called when the mouse is pressed and dragged.
Does nothing.

mouseMoved

```java
public void mouseMoved​(
MouseEvent
event)
```

Called when the mouse is moved.
Determines whether the tool tip should be displayed.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Overrides:** mouseMoved

in class

MouseAdapter
**Parameters:** event

- the event in question

---

#### mouseMoved

public void mouseMoved​(

MouseEvent

event)

Called when the mouse is moved.
Determines whether the tool tip should be displayed.

---

