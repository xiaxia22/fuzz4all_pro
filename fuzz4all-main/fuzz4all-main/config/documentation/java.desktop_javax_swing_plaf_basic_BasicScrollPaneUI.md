# Class BasicScrollPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicScrollPaneUI.html`

### Class Description

```java
public class
BasicScrollPaneUI

extends
ScrollPaneUI

implements
ScrollPaneConstants
```

A default L&F implementation of ScrollPaneUI.

**All Implemented Interfaces:** ScrollPaneConstants

---

### Field Details

#### protected
JScrollPane
scrollpane

The instance of

JScrollPane

.

---

#### protected
ChangeListener
vsbChangeListener

ChangeListener

installed on the vertical scrollbar.

---

#### protected
ChangeListener
hsbChangeListener

ChangeListener

installed on the horizontal scrollbar.

---

#### protected
ChangeListener
viewportChangeListener

ChangeListener

installed on the viewport.

---

#### protected
PropertyChangeListener
spPropertyChangeListener

PropertyChangeListener

installed on the scroll pane.

---

### Constructor Details

#### public BasicScrollPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Returns a new instance of

BasicScrollPaneUI

.

**Parameters:**
- x

- a component.

**Returns:**
- a new instance of

BasicScrollPaneUI

---

#### public
Dimension
getMaximumSize​(
JComponent
c)

Description copied from class:

ComponentUI

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- new Dimension(Short.MAX_VALUE, Short.MAX_VALUE)

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### protected void installDefaults​(
JScrollPane
scrollpane)

Installs default properties.

**Parameters:**
- scrollpane

- an instance of

JScrollPane

---

#### protected void installListeners​(
JScrollPane
c)

Registers listeners.

**Parameters:**
- c

- an instance of

JScrollPane

---

#### protected void installKeyboardActions​(
JScrollPane
c)

Registers keyboard actions.

**Parameters:**
- c

- an instance of

JScrollPane

---

#### protected void uninstallDefaults​(
JScrollPane
c)

Uninstalls default properties.

**Parameters:**
- c

- an instance of

JScrollPane

---

#### protected void uninstallListeners​(
JComponent
c)

Unregisters listeners.

**Parameters:**
- c

- a component

---

#### protected void uninstallKeyboardActions​(
JScrollPane
c)

Unregisters keyboard actions.

**Parameters:**
- c

- an instance of

JScrollPane

---

#### protected void syncScrollPaneWithViewport()

Synchronizes the

JScrollPane

with

Viewport

.

---

#### public int getBaseline​(
JComponent
c,
int width,
int height)

Returns the baseline.

**Overrides:**
- getBaseline

in class

ComponentUI

**Parameters:**
- c

-

JComponent

baseline is being requested for
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- baseline or a value < 0 indicating there is no reasonable
baseline

**Throws:**
- NullPointerException

- if

c

is

null
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:**
- getBaselineResizeBehavior

in class

ComponentUI

**Parameters:**
- c

-

JComponent

to return baseline resize behavior for

**Returns:**
- an enum indicating how the baseline changes as the component
size changes

**Throws:**
- NullPointerException

- if

c

is

null

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### protected
ChangeListener
createViewportChangeListener()

Returns an instance of viewport

ChangeListener

.

**Returns:**
- an instance of viewport

ChangeListener

---

#### protected
ChangeListener
createHSBChangeListener()

Returns an instance of horizontal scroll bar

ChangeListener

.

**Returns:**
- an instance of horizontal scroll bar

ChangeListener

---

#### protected
ChangeListener
createVSBChangeListener()

Returns an instance of vertical scroll bar

ChangeListener

.

**Returns:**
- an instance of vertical scroll bar

ChangeListener

---

#### protected
MouseWheelListener
createMouseWheelListener()

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI(). The returned MouseWheelListener is used
to handle mouse wheel-driven scrolling.

**Returns:**
- MouseWheelListener which implements wheel-driven scrolling

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

,

BasicScrollPaneUI.MouseWheelHandler

**Since:**
- 1.4

---

#### protected void updateScrollBarDisplayPolicy​(
PropertyChangeEvent
e)

Updates a scroll bar display policy.

**Parameters:**
- e

- the property change event

---

#### protected void updateViewport​(
PropertyChangeEvent
e)

Updates viewport.

**Parameters:**
- e

- the property change event

---

#### protected void updateRowHeader​(
PropertyChangeEvent
e)

Updates row header.

**Parameters:**
- e

- the property change event

---

#### protected void updateColumnHeader​(
PropertyChangeEvent
e)

Updates column header.

**Parameters:**
- e

- the property change event

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

. Subclasses can override
this method to return a custom

PropertyChangeListener

, e.g.

```java
class MyScrollPaneUI extends BasicScrollPaneUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeListener {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("viewport")) {
// do some extra work when the viewport changes
}
super.propertyChange(e);
}
}
}
```

**Returns:**
- an instance of

PropertyChangeListener

**See Also:**
- PropertyChangeListener

,

ComponentUI.installUI(javax.swing.JComponent)

---

### Additional Sections

#### Class BasicScrollPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ScrollPaneUI
- - javax.swing.plaf.basic.BasicScrollPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ScrollPaneUI
- - javax.swing.plaf.basic.BasicScrollPaneUI

javax.swing.plaf.ScrollPaneUI

- javax.swing.plaf.basic.BasicScrollPaneUI

javax.swing.plaf.basic.BasicScrollPaneUI

**All Implemented Interfaces:** ScrollPaneConstants

**Direct Known Subclasses:** MetalScrollPaneUI

,

SynthScrollPaneUI

```java
public class
BasicScrollPaneUI

extends
ScrollPaneUI

implements
ScrollPaneConstants
```

A default L&F implementation of ScrollPaneUI.

public class

BasicScrollPaneUI

extends

ScrollPaneUI

implements

ScrollPaneConstants

A default L&F implementation of ScrollPaneUI.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicScrollPaneUI.HSBChangeListener

Horizontal scrollbar listener.

protected class

BasicScrollPaneUI.MouseWheelHandler

MouseWheelHandler is an inner class which implements the
MouseWheelListener interface.

class

BasicScrollPaneUI.PropertyChangeHandler

Property change handler.

class

BasicScrollPaneUI.ViewportChangeHandler

Listener for viewport events.

class

BasicScrollPaneUI.VSBChangeListener

Vertical scrollbar listener.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeListener

hsbChangeListener

ChangeListener

installed on the horizontal scrollbar.

protected

JScrollPane

scrollpane

The instance of

JScrollPane

.

protected

PropertyChangeListener

spPropertyChangeListener

PropertyChangeListener

installed on the scroll pane.

protected

ChangeListener

viewportChangeListener

ChangeListener

installed on the viewport.

protected

ChangeListener

vsbChangeListener

ChangeListener

installed on the vertical scrollbar.

- Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicScrollPaneUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

ChangeListener

createHSBChangeListener

()

Returns an instance of horizontal scroll bar

ChangeListener

.

protected

MouseWheelListener

createMouseWheelListener

()

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI().

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

.

static

ComponentUI

createUI

​(

JComponent

x)

Returns a new instance of

BasicScrollPaneUI

.

protected

ChangeListener

createViewportChangeListener

()

Returns an instance of viewport

ChangeListener

.

protected

ChangeListener

createVSBChangeListener

()

Returns an instance of vertical scroll bar

ChangeListener

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the specified component's maximum size appropriate for
the look and feel.

protected void

installDefaults

​(

JScrollPane

scrollpane)

Installs default properties.

protected void

installKeyboardActions

​(

JScrollPane

c)

Registers keyboard actions.

protected void

installListeners

​(

JScrollPane

c)

Registers listeners.

protected void

syncScrollPaneWithViewport

()

Synchronizes the

JScrollPane

with

Viewport

.

protected void

uninstallDefaults

​(

JScrollPane

c)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

JScrollPane

c)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

JComponent

c)

Unregisters listeners.

protected void

updateColumnHeader

​(

PropertyChangeEvent

e)

Updates column header.

protected void

updateRowHeader

​(

PropertyChangeEvent

e)

Updates row header.

protected void

updateScrollBarDisplayPolicy

​(

PropertyChangeEvent

e)

Updates a scroll bar display policy.

protected void

updateViewport

​(

PropertyChangeEvent

e)

Updates viewport.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicScrollPaneUI.HSBChangeListener

Horizontal scrollbar listener.

protected class

BasicScrollPaneUI.MouseWheelHandler

MouseWheelHandler is an inner class which implements the
MouseWheelListener interface.

class

BasicScrollPaneUI.PropertyChangeHandler

Property change handler.

class

BasicScrollPaneUI.ViewportChangeHandler

Listener for viewport events.

class

BasicScrollPaneUI.VSBChangeListener

Vertical scrollbar listener.

---

#### Nested Class Summary

Horizontal scrollbar listener.

MouseWheelHandler is an inner class which implements the
MouseWheelListener interface.

Property change handler.

Listener for viewport events.

Vertical scrollbar listener.

Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeListener

hsbChangeListener

ChangeListener

installed on the horizontal scrollbar.

protected

JScrollPane

scrollpane

The instance of

JScrollPane

.

protected

PropertyChangeListener

spPropertyChangeListener

PropertyChangeListener

installed on the scroll pane.

protected

ChangeListener

viewportChangeListener

ChangeListener

installed on the viewport.

protected

ChangeListener

vsbChangeListener

ChangeListener

installed on the vertical scrollbar.

- Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

---

#### Field Summary

ChangeListener

installed on the horizontal scrollbar.

The instance of

JScrollPane

.

PropertyChangeListener

installed on the scroll pane.

ChangeListener

installed on the viewport.

ChangeListener

installed on the vertical scrollbar.

Fields declared in interface javax.swing.

ScrollPaneConstants

COLUMN_HEADER

,

HORIZONTAL_SCROLLBAR

,

HORIZONTAL_SCROLLBAR_ALWAYS

,

HORIZONTAL_SCROLLBAR_AS_NEEDED

,

HORIZONTAL_SCROLLBAR_NEVER

,

HORIZONTAL_SCROLLBAR_POLICY

,

LOWER_LEADING_CORNER

,

LOWER_LEFT_CORNER

,

LOWER_RIGHT_CORNER

,

LOWER_TRAILING_CORNER

,

ROW_HEADER

,

UPPER_LEADING_CORNER

,

UPPER_LEFT_CORNER

,

UPPER_RIGHT_CORNER

,

UPPER_TRAILING_CORNER

,

VERTICAL_SCROLLBAR

,

VERTICAL_SCROLLBAR_ALWAYS

,

VERTICAL_SCROLLBAR_AS_NEEDED

,

VERTICAL_SCROLLBAR_NEVER

,

VERTICAL_SCROLLBAR_POLICY

,

VIEWPORT

---

#### Fields declared in interface javax.swing. ScrollPaneConstants

Constructor Summary

Constructors

Constructor

Description

BasicScrollPaneUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

ChangeListener

createHSBChangeListener

()

Returns an instance of horizontal scroll bar

ChangeListener

.

protected

MouseWheelListener

createMouseWheelListener

()

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI().

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

.

static

ComponentUI

createUI

​(

JComponent

x)

Returns a new instance of

BasicScrollPaneUI

.

protected

ChangeListener

createViewportChangeListener

()

Returns an instance of viewport

ChangeListener

.

protected

ChangeListener

createVSBChangeListener

()

Returns an instance of vertical scroll bar

ChangeListener

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the specified component's maximum size appropriate for
the look and feel.

protected void

installDefaults

​(

JScrollPane

scrollpane)

Installs default properties.

protected void

installKeyboardActions

​(

JScrollPane

c)

Registers keyboard actions.

protected void

installListeners

​(

JScrollPane

c)

Registers listeners.

protected void

syncScrollPaneWithViewport

()

Synchronizes the

JScrollPane

with

Viewport

.

protected void

uninstallDefaults

​(

JScrollPane

c)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

JScrollPane

c)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

JComponent

c)

Unregisters listeners.

protected void

updateColumnHeader

​(

PropertyChangeEvent

e)

Updates column header.

protected void

updateRowHeader

​(

PropertyChangeEvent

e)

Updates row header.

protected void

updateScrollBarDisplayPolicy

​(

PropertyChangeEvent

e)

Updates a scroll bar display policy.

protected void

updateViewport

​(

PropertyChangeEvent

e)

Updates viewport.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

---

#### Method Summary

Returns an instance of horizontal scroll bar

ChangeListener

.

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI().

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

.

Returns a new instance of

BasicScrollPaneUI

.

Returns an instance of viewport

ChangeListener

.

Returns an instance of vertical scroll bar

ChangeListener

.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Returns the specified component's maximum size appropriate for
the look and feel.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Synchronizes the

JScrollPane

with

Viewport

.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

Updates column header.

Updates row header.

Updates a scroll bar display policy.

Updates viewport.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

============ FIELD DETAIL ===========

- Field Detail

- scrollpane

```java
protected
JScrollPane
scrollpane
```

The instance of

JScrollPane

.

- vsbChangeListener

```java
protected
ChangeListener
vsbChangeListener
```

ChangeListener

installed on the vertical scrollbar.

- hsbChangeListener

```java
protected
ChangeListener
hsbChangeListener
```

ChangeListener

installed on the horizontal scrollbar.

- viewportChangeListener

```java
protected
ChangeListener
viewportChangeListener
```

ChangeListener

installed on the viewport.

- spPropertyChangeListener

```java
protected
PropertyChangeListener
spPropertyChangeListener
```

PropertyChangeListener

installed on the scroll pane.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicScrollPaneUI

```java
public BasicScrollPaneUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Returns a new instance of

BasicScrollPaneUI

.

**Parameters:** x

- a component.
**Returns:** a new instance of

BasicScrollPaneUI

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** new Dimension(Short.MAX_VALUE, Short.MAX_VALUE)
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- installDefaults

```java
protected void installDefaults​(
JScrollPane
scrollpane)
```

Installs default properties.

**Parameters:** scrollpane

- an instance of

JScrollPane

- installListeners

```java
protected void installListeners​(
JScrollPane
c)
```

Registers listeners.

**Parameters:** c

- an instance of

JScrollPane

- installKeyboardActions

```java
protected void installKeyboardActions​(
JScrollPane
c)
```

Registers keyboard actions.

**Parameters:** c

- an instance of

JScrollPane

- uninstallDefaults

```java
protected void uninstallDefaults​(
JScrollPane
c)
```

Uninstalls default properties.

**Parameters:** c

- an instance of

JScrollPane

- uninstallListeners

```java
protected void uninstallListeners​(
JComponent
c)
```

Unregisters listeners.

**Parameters:** c

- a component

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JScrollPane
c)
```

Unregisters keyboard actions.

**Parameters:** c

- an instance of

JScrollPane

- syncScrollPaneWithViewport

```java
protected void syncScrollPaneWithViewport()
```

Synchronizes the

JScrollPane

with

Viewport

.

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- createViewportChangeListener

```java
protected
ChangeListener
createViewportChangeListener()
```

Returns an instance of viewport

ChangeListener

.

**Returns:** an instance of viewport

ChangeListener

- createHSBChangeListener

```java
protected
ChangeListener
createHSBChangeListener()
```

Returns an instance of horizontal scroll bar

ChangeListener

.

**Returns:** an instance of horizontal scroll bar

ChangeListener

- createVSBChangeListener

```java
protected
ChangeListener
createVSBChangeListener()
```

Returns an instance of vertical scroll bar

ChangeListener

.

**Returns:** an instance of vertical scroll bar

ChangeListener

- createMouseWheelListener

```java
protected
MouseWheelListener
createMouseWheelListener()
```

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI(). The returned MouseWheelListener is used
to handle mouse wheel-driven scrolling.

**Returns:** MouseWheelListener which implements wheel-driven scrolling
**Since:** 1.4
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

BasicScrollPaneUI.MouseWheelHandler

- updateScrollBarDisplayPolicy

```java
protected void updateScrollBarDisplayPolicy​(
PropertyChangeEvent
e)
```

Updates a scroll bar display policy.

**Parameters:** e

- the property change event

- updateViewport

```java
protected void updateViewport​(
PropertyChangeEvent
e)
```

Updates viewport.

**Parameters:** e

- the property change event

- updateRowHeader

```java
protected void updateRowHeader​(
PropertyChangeEvent
e)
```

Updates row header.

**Parameters:** e

- the property change event

- updateColumnHeader

```java
protected void updateColumnHeader​(
PropertyChangeEvent
e)
```

Updates column header.

**Parameters:** e

- the property change event

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

. Subclasses can override
this method to return a custom

PropertyChangeListener

, e.g.

```java
class MyScrollPaneUI extends BasicScrollPaneUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeListener {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("viewport")) {
// do some extra work when the viewport changes
}
super.propertyChange(e);
}
}
}
```

**Returns:** an instance of

PropertyChangeListener
**See Also:** PropertyChangeListener

,

ComponentUI.installUI(javax.swing.JComponent)

Field Detail

- scrollpane

```java
protected
JScrollPane
scrollpane
```

The instance of

JScrollPane

.

- vsbChangeListener

```java
protected
ChangeListener
vsbChangeListener
```

ChangeListener

installed on the vertical scrollbar.

- hsbChangeListener

```java
protected
ChangeListener
hsbChangeListener
```

ChangeListener

installed on the horizontal scrollbar.

- viewportChangeListener

```java
protected
ChangeListener
viewportChangeListener
```

ChangeListener

installed on the viewport.

- spPropertyChangeListener

```java
protected
PropertyChangeListener
spPropertyChangeListener
```

PropertyChangeListener

installed on the scroll pane.

---

#### Field Detail

scrollpane

```java
protected
JScrollPane
scrollpane
```

The instance of

JScrollPane

.

---

#### scrollpane

protected

JScrollPane

scrollpane

The instance of

JScrollPane

.

vsbChangeListener

```java
protected
ChangeListener
vsbChangeListener
```

ChangeListener

installed on the vertical scrollbar.

---

#### vsbChangeListener

protected

ChangeListener

vsbChangeListener

ChangeListener

installed on the vertical scrollbar.

hsbChangeListener

```java
protected
ChangeListener
hsbChangeListener
```

ChangeListener

installed on the horizontal scrollbar.

---

#### hsbChangeListener

protected

ChangeListener

hsbChangeListener

ChangeListener

installed on the horizontal scrollbar.

viewportChangeListener

```java
protected
ChangeListener
viewportChangeListener
```

ChangeListener

installed on the viewport.

---

#### viewportChangeListener

protected

ChangeListener

viewportChangeListener

ChangeListener

installed on the viewport.

spPropertyChangeListener

```java
protected
PropertyChangeListener
spPropertyChangeListener
```

PropertyChangeListener

installed on the scroll pane.

---

#### spPropertyChangeListener

protected

PropertyChangeListener

spPropertyChangeListener

PropertyChangeListener

installed on the scroll pane.

Constructor Detail

- BasicScrollPaneUI

```java
public BasicScrollPaneUI()
```

---

#### Constructor Detail

BasicScrollPaneUI

```java
public BasicScrollPaneUI()
```

---

#### BasicScrollPaneUI

public BasicScrollPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Returns a new instance of

BasicScrollPaneUI

.

**Parameters:** x

- a component.
**Returns:** a new instance of

BasicScrollPaneUI

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** new Dimension(Short.MAX_VALUE, Short.MAX_VALUE)
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- installDefaults

```java
protected void installDefaults​(
JScrollPane
scrollpane)
```

Installs default properties.

**Parameters:** scrollpane

- an instance of

JScrollPane

- installListeners

```java
protected void installListeners​(
JScrollPane
c)
```

Registers listeners.

**Parameters:** c

- an instance of

JScrollPane

- installKeyboardActions

```java
protected void installKeyboardActions​(
JScrollPane
c)
```

Registers keyboard actions.

**Parameters:** c

- an instance of

JScrollPane

- uninstallDefaults

```java
protected void uninstallDefaults​(
JScrollPane
c)
```

Uninstalls default properties.

**Parameters:** c

- an instance of

JScrollPane

- uninstallListeners

```java
protected void uninstallListeners​(
JComponent
c)
```

Unregisters listeners.

**Parameters:** c

- a component

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JScrollPane
c)
```

Unregisters keyboard actions.

**Parameters:** c

- an instance of

JScrollPane

- syncScrollPaneWithViewport

```java
protected void syncScrollPaneWithViewport()
```

Synchronizes the

JScrollPane

with

Viewport

.

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- createViewportChangeListener

```java
protected
ChangeListener
createViewportChangeListener()
```

Returns an instance of viewport

ChangeListener

.

**Returns:** an instance of viewport

ChangeListener

- createHSBChangeListener

```java
protected
ChangeListener
createHSBChangeListener()
```

Returns an instance of horizontal scroll bar

ChangeListener

.

**Returns:** an instance of horizontal scroll bar

ChangeListener

- createVSBChangeListener

```java
protected
ChangeListener
createVSBChangeListener()
```

Returns an instance of vertical scroll bar

ChangeListener

.

**Returns:** an instance of vertical scroll bar

ChangeListener

- createMouseWheelListener

```java
protected
MouseWheelListener
createMouseWheelListener()
```

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI(). The returned MouseWheelListener is used
to handle mouse wheel-driven scrolling.

**Returns:** MouseWheelListener which implements wheel-driven scrolling
**Since:** 1.4
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

BasicScrollPaneUI.MouseWheelHandler

- updateScrollBarDisplayPolicy

```java
protected void updateScrollBarDisplayPolicy​(
PropertyChangeEvent
e)
```

Updates a scroll bar display policy.

**Parameters:** e

- the property change event

- updateViewport

```java
protected void updateViewport​(
PropertyChangeEvent
e)
```

Updates viewport.

**Parameters:** e

- the property change event

- updateRowHeader

```java
protected void updateRowHeader​(
PropertyChangeEvent
e)
```

Updates row header.

**Parameters:** e

- the property change event

- updateColumnHeader

```java
protected void updateColumnHeader​(
PropertyChangeEvent
e)
```

Updates column header.

**Parameters:** e

- the property change event

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

. Subclasses can override
this method to return a custom

PropertyChangeListener

, e.g.

```java
class MyScrollPaneUI extends BasicScrollPaneUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeListener {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("viewport")) {
// do some extra work when the viewport changes
}
super.propertyChange(e);
}
}
}
```

**Returns:** an instance of

PropertyChangeListener
**See Also:** PropertyChangeListener

,

ComponentUI.installUI(javax.swing.JComponent)

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Returns a new instance of

BasicScrollPaneUI

.

**Parameters:** x

- a component.
**Returns:** a new instance of

BasicScrollPaneUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Returns a new instance of

BasicScrollPaneUI

.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** new Dimension(Short.MAX_VALUE, Short.MAX_VALUE)
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

c)

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

installDefaults

```java
protected void installDefaults​(
JScrollPane
scrollpane)
```

Installs default properties.

**Parameters:** scrollpane

- an instance of

JScrollPane

---

#### installDefaults

protected void installDefaults​(

JScrollPane

scrollpane)

Installs default properties.

installListeners

```java
protected void installListeners​(
JScrollPane
c)
```

Registers listeners.

**Parameters:** c

- an instance of

JScrollPane

---

#### installListeners

protected void installListeners​(

JScrollPane

c)

Registers listeners.

installKeyboardActions

```java
protected void installKeyboardActions​(
JScrollPane
c)
```

Registers keyboard actions.

**Parameters:** c

- an instance of

JScrollPane

---

#### installKeyboardActions

protected void installKeyboardActions​(

JScrollPane

c)

Registers keyboard actions.

uninstallDefaults

```java
protected void uninstallDefaults​(
JScrollPane
c)
```

Uninstalls default properties.

**Parameters:** c

- an instance of

JScrollPane

---

#### uninstallDefaults

protected void uninstallDefaults​(

JScrollPane

c)

Uninstalls default properties.

uninstallListeners

```java
protected void uninstallListeners​(
JComponent
c)
```

Unregisters listeners.

**Parameters:** c

- a component

---

#### uninstallListeners

protected void uninstallListeners​(

JComponent

c)

Unregisters listeners.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JScrollPane
c)
```

Unregisters keyboard actions.

**Parameters:** c

- an instance of

JScrollPane

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions​(

JScrollPane

c)

Unregisters keyboard actions.

syncScrollPaneWithViewport

```java
protected void syncScrollPaneWithViewport()
```

Synchronizes the

JScrollPane

with

Viewport

.

---

#### syncScrollPaneWithViewport

protected void syncScrollPaneWithViewport()

Synchronizes the

JScrollPane

with

Viewport

.

getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaseline

public int getBaseline​(

JComponent

c,
int width,
int height)

Returns the baseline.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

createViewportChangeListener

```java
protected
ChangeListener
createViewportChangeListener()
```

Returns an instance of viewport

ChangeListener

.

**Returns:** an instance of viewport

ChangeListener

---

#### createViewportChangeListener

protected

ChangeListener

createViewportChangeListener()

Returns an instance of viewport

ChangeListener

.

createHSBChangeListener

```java
protected
ChangeListener
createHSBChangeListener()
```

Returns an instance of horizontal scroll bar

ChangeListener

.

**Returns:** an instance of horizontal scroll bar

ChangeListener

---

#### createHSBChangeListener

protected

ChangeListener

createHSBChangeListener()

Returns an instance of horizontal scroll bar

ChangeListener

.

createVSBChangeListener

```java
protected
ChangeListener
createVSBChangeListener()
```

Returns an instance of vertical scroll bar

ChangeListener

.

**Returns:** an instance of vertical scroll bar

ChangeListener

---

#### createVSBChangeListener

protected

ChangeListener

createVSBChangeListener()

Returns an instance of vertical scroll bar

ChangeListener

.

createMouseWheelListener

```java
protected
MouseWheelListener
createMouseWheelListener()
```

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI(). The returned MouseWheelListener is used
to handle mouse wheel-driven scrolling.

**Returns:** MouseWheelListener which implements wheel-driven scrolling
**Since:** 1.4
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

BasicScrollPaneUI.MouseWheelHandler

---

#### createMouseWheelListener

protected

MouseWheelListener

createMouseWheelListener()

Creates an instance of MouseWheelListener, which is added to the
JScrollPane by installUI(). The returned MouseWheelListener is used
to handle mouse wheel-driven scrolling.

updateScrollBarDisplayPolicy

```java
protected void updateScrollBarDisplayPolicy​(
PropertyChangeEvent
e)
```

Updates a scroll bar display policy.

**Parameters:** e

- the property change event

---

#### updateScrollBarDisplayPolicy

protected void updateScrollBarDisplayPolicy​(

PropertyChangeEvent

e)

Updates a scroll bar display policy.

updateViewport

```java
protected void updateViewport​(
PropertyChangeEvent
e)
```

Updates viewport.

**Parameters:** e

- the property change event

---

#### updateViewport

protected void updateViewport​(

PropertyChangeEvent

e)

Updates viewport.

updateRowHeader

```java
protected void updateRowHeader​(
PropertyChangeEvent
e)
```

Updates row header.

**Parameters:** e

- the property change event

---

#### updateRowHeader

protected void updateRowHeader​(

PropertyChangeEvent

e)

Updates row header.

updateColumnHeader

```java
protected void updateColumnHeader​(
PropertyChangeEvent
e)
```

Updates column header.

**Parameters:** e

- the property change event

---

#### updateColumnHeader

protected void updateColumnHeader​(

PropertyChangeEvent

e)

Updates column header.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

. Subclasses can override
this method to return a custom

PropertyChangeListener

, e.g.

```java
class MyScrollPaneUI extends BasicScrollPaneUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeListener {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("viewport")) {
// do some extra work when the viewport changes
}
super.propertyChange(e);
}
}
}
```

**Returns:** an instance of

PropertyChangeListener
**See Also:** PropertyChangeListener

,

ComponentUI.installUI(javax.swing.JComponent)

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates an instance of

PropertyChangeListener

that's added to
the

JScrollPane

by

installUI()

. Subclasses can override
this method to return a custom

PropertyChangeListener

, e.g.

```java
class MyScrollPaneUI extends BasicScrollPaneUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeListener {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("viewport")) {
// do some extra work when the viewport changes
}
super.propertyChange(e);
}
}
}
```

class MyScrollPaneUI extends BasicScrollPaneUI {
protected PropertyChangeListener

createPropertyChangeListener

() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeListener {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("viewport")) {
// do some extra work when the viewport changes
}
super.propertyChange(e);
}
}
}

---

