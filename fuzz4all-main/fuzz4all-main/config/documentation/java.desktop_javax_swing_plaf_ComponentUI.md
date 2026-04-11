# Class ComponentUI

**Source:** `java.desktop\javax\swing\plaf\ComponentUI.html`

### Class Description

```java
public abstract class
ComponentUI

extends
Object
```

The base class for all UI delegate objects in the Swing pluggable
look and feel architecture. The UI delegate object for a Swing
component is responsible for implementing the aspects of the
component that depend on the look and feel.
The

JComponent

class
invokes methods from this class in order to delegate operations
(painting, layout calculations, etc.) that may vary depending on the
look and feel installed.

Client programs should not invoke methods
on this class directly.

**Direct Known Subclasses:** ButtonUI

,

ColorChooserUI

,

ComboBoxUI

,

DesktopIconUI

,

DesktopPaneUI

,

FileChooserUI

,

InternalFrameUI

,

LabelUI

,

LayerUI

,

ListUI

,

MenuBarUI

,

OptionPaneUI

,

PanelUI

,

PopupMenuUI

,

ProgressBarUI

,

RootPaneUI

,

ScrollBarUI

,

ScrollPaneUI

,

SeparatorUI

,

SliderUI

,

SpinnerUI

,

SplitPaneUI

,

TabbedPaneUI

,

TableHeaderUI

,

TableUI

,

TextUI

,

ToolBarUI

,

ToolTipUI

,

TreeUI

,

ViewportUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public ComponentUI()

Sole constructor. (For invocation by subclass constructors,
typically implicit.)

---

### Method Details

#### public void installUI​(
JComponent
c)

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

**Parameters:**
- c

- the component where this UI delegate is being installed

**See Also:**
- uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### public void uninstallUI​(
JComponent
c)

Reverses configuration which was done on the specified component during

installUI

. This method is invoked when this

UIComponent

instance is being removed as the UI delegate
for the specified component. This method should undo the
configuration performed in

installUI

, being careful to
leave the

JComponent

instance in a clean state (no
extraneous listeners, look-and-feel-specific property objects, etc.).
This should include the following:

- Remove any UI-set borders from the component.

Remove any UI-set layout managers on the component.

Remove any UI-added sub-components from the component.

Remove any UI-added event/property listeners from the component.

Remove any UI-installed keyboard UI from the component.

Nullify any allocated instance data objects to allow for GC.

**Parameters:**
- c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paints the specified component appropriately for the look and feel.
This method is invoked from the

ComponentUI.update

method when
the specified component is being painted. Subclasses should override
this method and use the specified

Graphics

object to
render the content of the component.

**Parameters:**
- g

- the

Graphics

context in which to paint
- c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- update(java.awt.Graphics, javax.swing.JComponent)

---

#### public void update​(
Graphics
g,

JComponent
c)

Notifies this UI delegate that it is time to paint the specified
component. This method is invoked by

JComponent

when the specified component is being painted.

By default this method fills the specified component with
its background color if its

opaque

property is

true

,
and then immediately calls

paint

. In general this method need
not be overridden by subclasses; all look-and-feel rendering code should
reside in the

paint

method.

**Parameters:**
- g

- the

Graphics

context in which to paint
- c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

Returns the specified component's preferred size appropriate for
the look and feel. If

null

is returned, the preferred
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method returns

null

.

**Parameters:**
- c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object containing given component's preferred
size appropriate for the look and feel

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Parameters:**
- c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

getPreferredSize(javax.swing.JComponent)

---

#### public
Dimension
getMaximumSize​(
JComponent
c)

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

**Parameters:**
- c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### public boolean contains​(
JComponent
c,
int x,
int y)

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

x

and

y

are defined to be relative
to the coordinate system of the specified component. Although
a component's

bounds

is constrained to a rectangle,
this method provides the means for defining a non-rectangular
shape within those bounds for the purpose of hit detection.

**Parameters:**
- c

- the component where the

x,y

location is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
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

if the specified

x,y

location is contained
within the look and feel's defined shape for the given component

**See Also:**
- JComponent.contains(int, int)

,

Component.contains(int, int)

---

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns an instance of the UI delegate for the specified component.
Each subclass must provide its own static

createUI

method that returns an instance of that UI delegate subclass.
If the UI delegate subclass is stateless, it may return an instance
that is shared by multiple components. If the UI delegate is
stateful, then it should return a new instance per component.
The default implementation of this method throws an error, as it
should never be invoked.

**Parameters:**
- c

- a

JComponent

for which to create a UI delegate

**Returns:**
- a

ComponentUI

object for

c

---

#### public int getBaseline​(
JComponent
c,
int width,
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

This method returns -1. Subclasses that have a meaningful baseline
should override appropriately.

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
- JComponent.getBaseline(int,int)

**Since:**
- 1.6

---

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

This method returns

BaselineResizeBehavior.OTHER

.
Subclasses that support a baseline should override appropriately.

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

#### public int getAccessibleChildrenCount​(
JComponent
c)

Returns the number of accessible children in the object. If all
of the children of this object implement

Accessible

,
this
method should return the number of children of this object.
UIs might wish to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChildrenCount()

instead
of this method.

**Parameters:**
- c

-

JComponent

for which to get count of accessible children

**Returns:**
- the number of accessible children in the object

**See Also:**
- getAccessibleChild(javax.swing.JComponent, int)

---

#### public
Accessible
getAccessibleChild​(
JComponent
c,
int i)

Returns the

i

th

Accessible

child of the object.
UIs might need to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChild()

instead of
this method.

**Parameters:**
- c

- a

JComponent

for which to get a child object
- i

- zero-based index of child

**Returns:**
- the

i

th

Accessible

child of the object

**See Also:**
- getAccessibleChildrenCount(javax.swing.JComponent)

---

### Additional Sections

#### Class ComponentUI

java.lang.Object

- javax.swing.plaf.ComponentUI

javax.swing.plaf.ComponentUI

**Direct Known Subclasses:** ButtonUI

,

ColorChooserUI

,

ComboBoxUI

,

DesktopIconUI

,

DesktopPaneUI

,

FileChooserUI

,

InternalFrameUI

,

LabelUI

,

LayerUI

,

ListUI

,

MenuBarUI

,

OptionPaneUI

,

PanelUI

,

PopupMenuUI

,

ProgressBarUI

,

RootPaneUI

,

ScrollBarUI

,

ScrollPaneUI

,

SeparatorUI

,

SliderUI

,

SpinnerUI

,

SplitPaneUI

,

TabbedPaneUI

,

TableHeaderUI

,

TableUI

,

TextUI

,

ToolBarUI

,

ToolTipUI

,

TreeUI

,

ViewportUI

```java
public abstract class
ComponentUI

extends
Object
```

The base class for all UI delegate objects in the Swing pluggable
look and feel architecture. The UI delegate object for a Swing
component is responsible for implementing the aspects of the
component that depend on the look and feel.
The

JComponent

class
invokes methods from this class in order to delegate operations
(painting, layout calculations, etc.) that may vary depending on the
look and feel installed.

Client programs should not invoke methods
on this class directly.

**See Also:** JComponent

,

UIManager

public abstract class

ComponentUI

extends

Object

The base class for all UI delegate objects in the Swing pluggable
look and feel architecture. The UI delegate object for a Swing
component is responsible for implementing the aspects of the
component that depend on the look and feel.
The

JComponent

class
invokes methods from this class in order to delegate operations
(painting, layout calculations, etc.) that may vary depending on the
look and feel installed.

Client programs should not invoke methods
on this class directly.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ComponentUI

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

JComponent

c,
int x,
int y)

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

static

ComponentUI

createUI

​(

JComponent

c)

Returns an instance of the UI delegate for the specified component.

Accessible

getAccessibleChild

​(

JComponent

c,
int i)

Returns the

i

th

Accessible

child of the object.

int

getAccessibleChildrenCount

​(

JComponent

c)

Returns the number of accessible children in the object.

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

Dimension

getMinimumSize

​(

JComponent

c)

Returns the specified component's minimum size appropriate for
the look and feel.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the specified component's preferred size appropriate for
the look and feel.

void

installUI

​(

JComponent

c)

Configures the specified component appropriately for the look and feel.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component appropriately for the look and feel.

void

uninstallUI

​(

JComponent

c)

Reverses configuration which was done on the specified component during

installUI

.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate that it is time to paint the specified
component.

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

Constructor Summary

Constructors

Constructor

Description

ComponentUI

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

JComponent

c,
int x,
int y)

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

static

ComponentUI

createUI

​(

JComponent

c)

Returns an instance of the UI delegate for the specified component.

Accessible

getAccessibleChild

​(

JComponent

c,
int i)

Returns the

i

th

Accessible

child of the object.

int

getAccessibleChildrenCount

​(

JComponent

c)

Returns the number of accessible children in the object.

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

Dimension

getMinimumSize

​(

JComponent

c)

Returns the specified component's minimum size appropriate for
the look and feel.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the specified component's preferred size appropriate for
the look and feel.

void

installUI

​(

JComponent

c)

Configures the specified component appropriately for the look and feel.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component appropriately for the look and feel.

void

uninstallUI

​(

JComponent

c)

Reverses configuration which was done on the specified component during

installUI

.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate that it is time to paint the specified
component.

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

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

Returns an instance of the UI delegate for the specified component.

Returns the

i

th

Accessible

child of the object.

Returns the number of accessible children in the object.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Returns the specified component's maximum size appropriate for
the look and feel.

Returns the specified component's minimum size appropriate for
the look and feel.

Returns the specified component's preferred size appropriate for
the look and feel.

Configures the specified component appropriately for the look and feel.

Paints the specified component appropriately for the look and feel.

Reverses configuration which was done on the specified component during

installUI

.

Notifies this UI delegate that it is time to paint the specified
component.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ComponentUI

```java
public ComponentUI()
```

Sole constructor. (For invocation by subclass constructors,
typically implicit.)

============ METHOD DETAIL ==========

- Method Detail

- installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Reverses configuration which was done on the specified component during

installUI

. This method is invoked when this

UIComponent

instance is being removed as the UI delegate
for the specified component. This method should undo the
configuration performed in

installUI

, being careful to
leave the

JComponent

instance in a clean state (no
extraneous listeners, look-and-feel-specific property objects, etc.).
This should include the following:

- Remove any UI-set borders from the component.

Remove any UI-set layout managers on the component.

Remove any UI-added sub-components from the component.

Remove any UI-added event/property listeners from the component.

Remove any UI-installed keyboard UI from the component.

Nullify any allocated instance data objects to allow for GC.

**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component appropriately for the look and feel.
This method is invoked from the

ComponentUI.update

method when
the specified component is being painted. Subclasses should override
this method and use the specified

Graphics

object to
render the content of the component.

**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** update(java.awt.Graphics, javax.swing.JComponent)

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate that it is time to paint the specified
component. This method is invoked by

JComponent

when the specified component is being painted.

By default this method fills the specified component with
its background color if its

opaque

property is

true

,
and then immediately calls

paint

. In general this method need
not be overridden by subclasses; all look-and-feel rendering code should
reside in the

paint

method.

**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the specified component's preferred size appropriate for
the look and feel. If

null

is returned, the preferred
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method returns

null

.

**Parameters:** c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

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

**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- contains

```java
public boolean contains​(
JComponent
c,
int x,
int y)
```

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

x

and

y

are defined to be relative
to the coordinate system of the specified component. Although
a component's

bounds

is constrained to a rectangle,
this method provides the means for defining a non-rectangular
shape within those bounds for the purpose of hit detection.

**Parameters:** c

- the component where the

x,y

location is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the specified

x,y

location is contained
within the look and feel's defined shape for the given component
**See Also:** JComponent.contains(int, int)

,

Component.contains(int, int)

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of the UI delegate for the specified component.
Each subclass must provide its own static

createUI

method that returns an instance of that UI delegate subclass.
If the UI delegate subclass is stateless, it may return an instance
that is shared by multiple components. If the UI delegate is
stateful, then it should return a new instance per component.
The default implementation of this method throws an error, as it
should never be invoked.

**Parameters:** c

- a

JComponent

for which to create a UI delegate
**Returns:** a

ComponentUI

object for

c

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
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

This method returns -1. Subclasses that have a meaningful baseline
should override appropriately.

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
**See Also:** JComponent.getBaseline(int,int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

This method returns

BaselineResizeBehavior.OTHER

.
Subclasses that support a baseline should override appropriately.

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

- getAccessibleChildrenCount

```java
public int getAccessibleChildrenCount​(
JComponent
c)
```

Returns the number of accessible children in the object. If all
of the children of this object implement

Accessible

,
this
method should return the number of children of this object.
UIs might wish to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChildrenCount()

instead
of this method.

**Parameters:** c

-

JComponent

for which to get count of accessible children
**Returns:** the number of accessible children in the object
**See Also:** getAccessibleChild(javax.swing.JComponent, int)

- getAccessibleChild

```java
public
Accessible
getAccessibleChild​(
JComponent
c,
int i)
```

Returns the

i

th

Accessible

child of the object.
UIs might need to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChild()

instead of
this method.

**Parameters:** c

- a

JComponent

for which to get a child object
**Parameters:** i

- zero-based index of child
**Returns:** the

i

th

Accessible

child of the object
**See Also:** getAccessibleChildrenCount(javax.swing.JComponent)

Constructor Detail

- ComponentUI

```java
public ComponentUI()
```

Sole constructor. (For invocation by subclass constructors,
typically implicit.)

---

#### Constructor Detail

ComponentUI

```java
public ComponentUI()
```

Sole constructor. (For invocation by subclass constructors,
typically implicit.)

---

#### ComponentUI

public ComponentUI()

Sole constructor. (For invocation by subclass constructors,
typically implicit.)

Method Detail

- installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Reverses configuration which was done on the specified component during

installUI

. This method is invoked when this

UIComponent

instance is being removed as the UI delegate
for the specified component. This method should undo the
configuration performed in

installUI

, being careful to
leave the

JComponent

instance in a clean state (no
extraneous listeners, look-and-feel-specific property objects, etc.).
This should include the following:

- Remove any UI-set borders from the component.

Remove any UI-set layout managers on the component.

Remove any UI-added sub-components from the component.

Remove any UI-added event/property listeners from the component.

Remove any UI-installed keyboard UI from the component.

Nullify any allocated instance data objects to allow for GC.

**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component appropriately for the look and feel.
This method is invoked from the

ComponentUI.update

method when
the specified component is being painted. Subclasses should override
this method and use the specified

Graphics

object to
render the content of the component.

**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** update(java.awt.Graphics, javax.swing.JComponent)

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate that it is time to paint the specified
component. This method is invoked by

JComponent

when the specified component is being painted.

By default this method fills the specified component with
its background color if its

opaque

property is

true

,
and then immediately calls

paint

. In general this method need
not be overridden by subclasses; all look-and-feel rendering code should
reside in the

paint

method.

**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the specified component's preferred size appropriate for
the look and feel. If

null

is returned, the preferred
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method returns

null

.

**Parameters:** c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

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

**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- contains

```java
public boolean contains​(
JComponent
c,
int x,
int y)
```

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

x

and

y

are defined to be relative
to the coordinate system of the specified component. Although
a component's

bounds

is constrained to a rectangle,
this method provides the means for defining a non-rectangular
shape within those bounds for the purpose of hit detection.

**Parameters:** c

- the component where the

x,y

location is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the specified

x,y

location is contained
within the look and feel's defined shape for the given component
**See Also:** JComponent.contains(int, int)

,

Component.contains(int, int)

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of the UI delegate for the specified component.
Each subclass must provide its own static

createUI

method that returns an instance of that UI delegate subclass.
If the UI delegate subclass is stateless, it may return an instance
that is shared by multiple components. If the UI delegate is
stateful, then it should return a new instance per component.
The default implementation of this method throws an error, as it
should never be invoked.

**Parameters:** c

- a

JComponent

for which to create a UI delegate
**Returns:** a

ComponentUI

object for

c

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
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

This method returns -1. Subclasses that have a meaningful baseline
should override appropriately.

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
**See Also:** JComponent.getBaseline(int,int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

This method returns

BaselineResizeBehavior.OTHER

.
Subclasses that support a baseline should override appropriately.

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

- getAccessibleChildrenCount

```java
public int getAccessibleChildrenCount​(
JComponent
c)
```

Returns the number of accessible children in the object. If all
of the children of this object implement

Accessible

,
this
method should return the number of children of this object.
UIs might wish to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChildrenCount()

instead
of this method.

**Parameters:** c

-

JComponent

for which to get count of accessible children
**Returns:** the number of accessible children in the object
**See Also:** getAccessibleChild(javax.swing.JComponent, int)

- getAccessibleChild

```java
public
Accessible
getAccessibleChild​(
JComponent
c,
int i)
```

Returns the

i

th

Accessible

child of the object.
UIs might need to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChild()

instead of
this method.

**Parameters:** c

- a

JComponent

for which to get a child object
**Parameters:** i

- zero-based index of child
**Returns:** the

i

th

Accessible

child of the object
**See Also:** getAccessibleChildrenCount(javax.swing.JComponent)

---

#### Method Detail

installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### installUI

public void installUI​(

JComponent

c)

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Reverses configuration which was done on the specified component during

installUI

. This method is invoked when this

UIComponent

instance is being removed as the UI delegate
for the specified component. This method should undo the
configuration performed in

installUI

, being careful to
leave the

JComponent

instance in a clean state (no
extraneous listeners, look-and-feel-specific property objects, etc.).
This should include the following:

- Remove any UI-set borders from the component.

Remove any UI-set layout managers on the component.

Remove any UI-added sub-components from the component.

Remove any UI-added event/property listeners from the component.

Remove any UI-installed keyboard UI from the component.

Nullify any allocated instance data objects to allow for GC.

**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Reverses configuration which was done on the specified component during

installUI

. This method is invoked when this

UIComponent

instance is being removed as the UI delegate
for the specified component. This method should undo the
configuration performed in

installUI

, being careful to
leave the

JComponent

instance in a clean state (no
extraneous listeners, look-and-feel-specific property objects, etc.).
This should include the following:

- Remove any UI-set borders from the component.

Remove any UI-set layout managers on the component.

Remove any UI-added sub-components from the component.

Remove any UI-added event/property listeners from the component.

Remove any UI-installed keyboard UI from the component.

Nullify any allocated instance data objects to allow for GC.

Remove any UI-set borders from the component.

Remove any UI-set layout managers on the component.

Remove any UI-added sub-components from the component.

Remove any UI-added event/property listeners from the component.

Remove any UI-installed keyboard UI from the component.

Nullify any allocated instance data objects to allow for GC.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component appropriately for the look and feel.
This method is invoked from the

ComponentUI.update

method when
the specified component is being painted. Subclasses should override
this method and use the specified

Graphics

object to
render the content of the component.

**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** update(java.awt.Graphics, javax.swing.JComponent)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paints the specified component appropriately for the look and feel.
This method is invoked from the

ComponentUI.update

method when
the specified component is being painted. Subclasses should override
this method and use the specified

Graphics

object to
render the content of the component.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate that it is time to paint the specified
component. This method is invoked by

JComponent

when the specified component is being painted.

By default this method fills the specified component with
its background color if its

opaque

property is

true

,
and then immediately calls

paint

. In general this method need
not be overridden by subclasses; all look-and-feel rendering code should
reside in the

paint

method.

**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

Notifies this UI delegate that it is time to paint the specified
component. This method is invoked by

JComponent

when the specified component is being painted.

By default this method fills the specified component with
its background color if its

opaque

property is

true

,
and then immediately calls

paint

. In general this method need
not be overridden by subclasses; all look-and-feel rendering code should
reside in the

paint

method.

By default this method fills the specified component with
its background color if its

opaque

property is

true

,
and then immediately calls

paint

. In general this method need
not be overridden by subclasses; all look-and-feel rendering code should
reside in the

paint

method.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the specified component's preferred size appropriate for
the look and feel. If

null

is returned, the preferred
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method returns

null

.

**Parameters:** c

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

c)

Returns the specified component's preferred size appropriate for
the look and feel. If

null

is returned, the preferred
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method returns

null

.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

getPreferredSize(javax.swing.JComponent)

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

JComponent

c)

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

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

**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
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

contains

```java
public boolean contains​(
JComponent
c,
int x,
int y)
```

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

x

and

y

are defined to be relative
to the coordinate system of the specified component. Although
a component's

bounds

is constrained to a rectangle,
this method provides the means for defining a non-rectangular
shape within those bounds for the purpose of hit detection.

**Parameters:** c

- the component where the

x,y

location is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Parameters:** x

- the

x

coordinate of the point
**Parameters:** y

- the

y

coordinate of the point
**Returns:** true

if the specified

x,y

location is contained
within the look and feel's defined shape for the given component
**See Also:** JComponent.contains(int, int)

,

Component.contains(int, int)

---

#### contains

public boolean contains​(

JComponent

c,
int x,
int y)

Returns

true

if the specified

x,y

location is
contained within the look and feel's defined shape of the specified
component.

x

and

y

are defined to be relative
to the coordinate system of the specified component. Although
a component's

bounds

is constrained to a rectangle,
this method provides the means for defining a non-rectangular
shape within those bounds for the purpose of hit detection.

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of the UI delegate for the specified component.
Each subclass must provide its own static

createUI

method that returns an instance of that UI delegate subclass.
If the UI delegate subclass is stateless, it may return an instance
that is shared by multiple components. If the UI delegate is
stateful, then it should return a new instance per component.
The default implementation of this method throws an error, as it
should never be invoked.

**Parameters:** c

- a

JComponent

for which to create a UI delegate
**Returns:** a

ComponentUI

object for

c

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns an instance of the UI delegate for the specified component.
Each subclass must provide its own static

createUI

method that returns an instance of that UI delegate subclass.
If the UI delegate subclass is stateless, it may return an instance
that is shared by multiple components. If the UI delegate is
stateful, then it should return a new instance per component.
The default implementation of this method throws an error, as it
should never be invoked.

getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
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

This method returns -1. Subclasses that have a meaningful baseline
should override appropriately.

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
**See Also:** JComponent.getBaseline(int,int)

---

#### getBaseline

public int getBaseline​(

JComponent

c,
int width,
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

This method returns -1. Subclasses that have a meaningful baseline
should override appropriately.

This method returns -1. Subclasses that have a meaningful baseline
should override appropriately.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

This method returns

BaselineResizeBehavior.OTHER

.
Subclasses that support a baseline should override appropriately.

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
changes as the size changes. This method is primarily meant for
layout managers and GUI builders.

This method returns

BaselineResizeBehavior.OTHER

.
Subclasses that support a baseline should override appropriately.

This method returns

BaselineResizeBehavior.OTHER

.
Subclasses that support a baseline should override appropriately.

getAccessibleChildrenCount

```java
public int getAccessibleChildrenCount​(
JComponent
c)
```

Returns the number of accessible children in the object. If all
of the children of this object implement

Accessible

,
this
method should return the number of children of this object.
UIs might wish to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChildrenCount()

instead
of this method.

**Parameters:** c

-

JComponent

for which to get count of accessible children
**Returns:** the number of accessible children in the object
**See Also:** getAccessibleChild(javax.swing.JComponent, int)

---

#### getAccessibleChildrenCount

public int getAccessibleChildrenCount​(

JComponent

c)

Returns the number of accessible children in the object. If all
of the children of this object implement

Accessible

,
this
method should return the number of children of this object.
UIs might wish to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChildrenCount()

instead
of this method.

getAccessibleChild

```java
public
Accessible
getAccessibleChild​(
JComponent
c,
int i)
```

Returns the

i

th

Accessible

child of the object.
UIs might need to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChild()

instead of
this method.

**Parameters:** c

- a

JComponent

for which to get a child object
**Parameters:** i

- zero-based index of child
**Returns:** the

i

th

Accessible

child of the object
**See Also:** getAccessibleChildrenCount(javax.swing.JComponent)

---

#### getAccessibleChild

public

Accessible

getAccessibleChild​(

JComponent

c,
int i)

Returns the

i

th

Accessible

child of the object.
UIs might need to override this if they present areas on the
screen that can be viewed as components, but actual components
are not used for presenting those areas.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChild()

instead of
this method.

Note: As of v1.3, it is recommended that developers call

Component.AccessibleAWTComponent.getAccessibleChild()

instead of
this method.

---

