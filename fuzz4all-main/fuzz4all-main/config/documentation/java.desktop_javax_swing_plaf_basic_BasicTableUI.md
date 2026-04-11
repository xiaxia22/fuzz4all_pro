# Class BasicTableUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicTableUI.html`

### Class Description

```java
public class
BasicTableUI

extends
TableUI
```

BasicTableUI implementation

**Direct Known Subclasses:** SynthTableUI

---

### Field Details

#### protected
JTable
table

The instance of

JTable

.

---

#### protected
CellRendererPane
rendererPane

The instance of

CellRendererPane

.

---

#### protected
KeyListener
keyListener

KeyListener

that are attached to the

JTable

.

---

#### protected
FocusListener
focusListener

FocusListener

that are attached to the

JTable

.

---

#### protected
MouseInputListener
mouseInputListener

MouseInputListener

that are attached to the

JTable

.

---

### Constructor Details

#### public BasicTableUI()

*No description found.*

---

### Method Details

#### protected
KeyListener
createKeyListener()

Creates the key listener for handling keyboard navigation in the

JTable

.

**Returns:**
- the key listener for handling keyboard navigation in the

JTable

---

#### protected
FocusListener
createFocusListener()

Creates the focus listener for handling keyboard navigation in the

JTable

.

**Returns:**
- the focus listener for handling keyboard navigation in the

JTable

---

#### protected
MouseInputListener
createMouseInputListener()

Creates the mouse listener for the

JTable

.

**Returns:**
- the mouse listener for the

JTable

---

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns a new instance of

BasicTableUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicTableUI

---

#### protected void installDefaults()

Initialize JTable properties, e.g. font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

---

#### protected void installListeners()

Attaches listeners to the JTable.

---

#### protected void installKeyboardActions()

Register all keyboard actions on the JTable.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

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

#### public
Dimension
getMinimumSize​(
JComponent
c)

Return the minimum size of the table. The minimum height is the
row height times the number of rows.
The minimum width is the sum of the minimum widths of each column.

**Overrides:**
- getMinimumSize

in class

ComponentUI

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

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

Return the preferred size of the table. The preferred height is the
row height times the number of rows.
The preferred width is the sum of the preferred widths of each column.

**Overrides:**
- getPreferredSize

in class

ComponentUI

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
getMaximumSize​(
JComponent
c)

Return the maximum size of the table. The maximum height is the
row heighttimes the number of rows.
The maximum width is the sum of the maximum widths of each column.

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
- a

Dimension

object or

null

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paint a representation of the

table

instance
that was set in installUI().

**Overrides:**
- paint

in class

ComponentUI

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
- ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

---

### Additional Sections

#### Class BasicTableUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TableUI
- - javax.swing.plaf.basic.BasicTableUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TableUI
- - javax.swing.plaf.basic.BasicTableUI

javax.swing.plaf.TableUI

- javax.swing.plaf.basic.BasicTableUI

javax.swing.plaf.basic.BasicTableUI

**Direct Known Subclasses:** SynthTableUI

```java
public class
BasicTableUI

extends
TableUI
```

BasicTableUI implementation

public class

BasicTableUI

extends

TableUI

BasicTableUI implementation

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicTableUI.FocusHandler

This class should be treated as a "protected" inner class.

class

BasicTableUI.KeyHandler

This class should be treated as a "protected" inner class.

class

BasicTableUI.MouseInputHandler

This class should be treated as a "protected" inner class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

FocusListener

focusListener

FocusListener

that are attached to the

JTable

.

protected

KeyListener

keyListener

KeyListener

that are attached to the

JTable

.

protected

MouseInputListener

mouseInputListener

MouseInputListener

that are attached to the

JTable

.

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

protected

JTable

table

The instance of

JTable

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicTableUI

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

FocusListener

createFocusListener

()

Creates the focus listener for handling keyboard navigation in the

JTable

.

protected

KeyListener

createKeyListener

()

Creates the key listener for handling keyboard navigation in the

JTable

.

protected

MouseInputListener

createMouseInputListener

()

Creates the mouse listener for the

JTable

.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicTableUI

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

Return the maximum size of the table.

Dimension

getMinimumSize

​(

JComponent

c)

Return the minimum size of the table.

Dimension

getPreferredSize

​(

JComponent

c)

Return the preferred size of the table.

protected void

installDefaults

()

Initialize JTable properties, e.g. font, foreground, and background.

protected void

installKeyboardActions

()

Register all keyboard actions on the JTable.

protected void

installListeners

()

Attaches listeners to the JTable.

void

paint

​(

Graphics

g,

JComponent

c)

Paint a representation of the

table

instance
that was set in installUI().

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

installUI

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

BasicTableUI.FocusHandler

This class should be treated as a "protected" inner class.

class

BasicTableUI.KeyHandler

This class should be treated as a "protected" inner class.

class

BasicTableUI.MouseInputHandler

This class should be treated as a "protected" inner class.

---

#### Nested Class Summary

This class should be treated as a "protected" inner class.

Field Summary

Fields

Modifier and Type

Field

Description

protected

FocusListener

focusListener

FocusListener

that are attached to the

JTable

.

protected

KeyListener

keyListener

KeyListener

that are attached to the

JTable

.

protected

MouseInputListener

mouseInputListener

MouseInputListener

that are attached to the

JTable

.

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

protected

JTable

table

The instance of

JTable

.

---

#### Field Summary

FocusListener

that are attached to the

JTable

.

KeyListener

that are attached to the

JTable

.

MouseInputListener

that are attached to the

JTable

.

The instance of

CellRendererPane

.

The instance of

JTable

.

Constructor Summary

Constructors

Constructor

Description

BasicTableUI

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

FocusListener

createFocusListener

()

Creates the focus listener for handling keyboard navigation in the

JTable

.

protected

KeyListener

createKeyListener

()

Creates the key listener for handling keyboard navigation in the

JTable

.

protected

MouseInputListener

createMouseInputListener

()

Creates the mouse listener for the

JTable

.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicTableUI

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

Return the maximum size of the table.

Dimension

getMinimumSize

​(

JComponent

c)

Return the minimum size of the table.

Dimension

getPreferredSize

​(

JComponent

c)

Return the preferred size of the table.

protected void

installDefaults

()

Initialize JTable properties, e.g. font, foreground, and background.

protected void

installKeyboardActions

()

Register all keyboard actions on the JTable.

protected void

installListeners

()

Attaches listeners to the JTable.

void

paint

​(

Graphics

g,

JComponent

c)

Paint a representation of the

table

instance
that was set in installUI().

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

installUI

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

Creates the focus listener for handling keyboard navigation in the

JTable

.

Creates the key listener for handling keyboard navigation in the

JTable

.

Creates the mouse listener for the

JTable

.

Returns a new instance of

BasicTableUI

.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Return the maximum size of the table.

Return the minimum size of the table.

Return the preferred size of the table.

Initialize JTable properties, e.g. font, foreground, and background.

Register all keyboard actions on the JTable.

Attaches listeners to the JTable.

Paint a representation of the

table

instance
that was set in installUI().

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

installUI

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

- table

```java
protected
JTable
table
```

The instance of

JTable

.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

- keyListener

```java
protected
KeyListener
keyListener
```

KeyListener

that are attached to the

JTable

.

- focusListener

```java
protected
FocusListener
focusListener
```

FocusListener

that are attached to the

JTable

.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

MouseInputListener

that are attached to the

JTable

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicTableUI

```java
public BasicTableUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the key listener for handling keyboard navigation in the

JTable

.

**Returns:** the key listener for handling keyboard navigation in the

JTable

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates the focus listener for handling keyboard navigation in the

JTable

.

**Returns:** the focus listener for handling keyboard navigation in the

JTable

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates the mouse listener for the

JTable

.

**Returns:** the mouse listener for the

JTable

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicTableUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicTableUI

- installDefaults

```java
protected void installDefaults()
```

Initialize JTable properties, e.g. font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:** ComponentUI.installUI(javax.swing.JComponent)

- installListeners

```java
protected void installListeners()
```

Attaches listeners to the JTable.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Register all keyboard actions on the JTable.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

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

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Return the minimum size of the table. The minimum height is the
row height times the number of rows.
The minimum width is the sum of the minimum widths of each column.

**Overrides:** getMinimumSize

in class

ComponentUI
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

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Return the preferred size of the table. The preferred height is the
row height times the number of rows.
The preferred width is the sum of the preferred widths of each column.

**Overrides:** getPreferredSize

in class

ComponentUI
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

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Return the maximum size of the table. The maximum height is the
row heighttimes the number of rows.
The maximum width is the sum of the maximum widths of each column.

**Overrides:** getMaximumSize

in class

ComponentUI
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

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paint a representation of the

table

instance
that was set in installUI().

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

Field Detail

- table

```java
protected
JTable
table
```

The instance of

JTable

.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

- keyListener

```java
protected
KeyListener
keyListener
```

KeyListener

that are attached to the

JTable

.

- focusListener

```java
protected
FocusListener
focusListener
```

FocusListener

that are attached to the

JTable

.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

MouseInputListener

that are attached to the

JTable

.

---

#### Field Detail

table

```java
protected
JTable
table
```

The instance of

JTable

.

---

#### table

protected

JTable

table

The instance of

JTable

.

rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

---

#### rendererPane

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

keyListener

```java
protected
KeyListener
keyListener
```

KeyListener

that are attached to the

JTable

.

---

#### keyListener

protected

KeyListener

keyListener

KeyListener

that are attached to the

JTable

.

focusListener

```java
protected
FocusListener
focusListener
```

FocusListener

that are attached to the

JTable

.

---

#### focusListener

protected

FocusListener

focusListener

FocusListener

that are attached to the

JTable

.

mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

MouseInputListener

that are attached to the

JTable

.

---

#### mouseInputListener

protected

MouseInputListener

mouseInputListener

MouseInputListener

that are attached to the

JTable

.

Constructor Detail

- BasicTableUI

```java
public BasicTableUI()
```

---

#### Constructor Detail

BasicTableUI

```java
public BasicTableUI()
```

---

#### BasicTableUI

public BasicTableUI()

Method Detail

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the key listener for handling keyboard navigation in the

JTable

.

**Returns:** the key listener for handling keyboard navigation in the

JTable

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates the focus listener for handling keyboard navigation in the

JTable

.

**Returns:** the focus listener for handling keyboard navigation in the

JTable

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates the mouse listener for the

JTable

.

**Returns:** the mouse listener for the

JTable

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicTableUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicTableUI

- installDefaults

```java
protected void installDefaults()
```

Initialize JTable properties, e.g. font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:** ComponentUI.installUI(javax.swing.JComponent)

- installListeners

```java
protected void installListeners()
```

Attaches listeners to the JTable.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Register all keyboard actions on the JTable.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

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

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Return the minimum size of the table. The minimum height is the
row height times the number of rows.
The minimum width is the sum of the minimum widths of each column.

**Overrides:** getMinimumSize

in class

ComponentUI
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

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Return the preferred size of the table. The preferred height is the
row height times the number of rows.
The preferred width is the sum of the preferred widths of each column.

**Overrides:** getPreferredSize

in class

ComponentUI
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

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Return the maximum size of the table. The maximum height is the
row heighttimes the number of rows.
The maximum width is the sum of the maximum widths of each column.

**Overrides:** getMaximumSize

in class

ComponentUI
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

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paint a representation of the

table

instance
that was set in installUI().

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

---

#### Method Detail

createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the key listener for handling keyboard navigation in the

JTable

.

**Returns:** the key listener for handling keyboard navigation in the

JTable

---

#### createKeyListener

protected

KeyListener

createKeyListener()

Creates the key listener for handling keyboard navigation in the

JTable

.

createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates the focus listener for handling keyboard navigation in the

JTable

.

**Returns:** the focus listener for handling keyboard navigation in the

JTable

---

#### createFocusListener

protected

FocusListener

createFocusListener()

Creates the focus listener for handling keyboard navigation in the

JTable

.

createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates the mouse listener for the

JTable

.

**Returns:** the mouse listener for the

JTable

---

#### createMouseInputListener

protected

MouseInputListener

createMouseInputListener()

Creates the mouse listener for the

JTable

.

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicTableUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicTableUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns a new instance of

BasicTableUI

.

installDefaults

```java
protected void installDefaults()
```

Initialize JTable properties, e.g. font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:** ComponentUI.installUI(javax.swing.JComponent)

---

#### installDefaults

protected void installDefaults()

Initialize JTable properties, e.g. font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

installListeners

```java
protected void installListeners()
```

Attaches listeners to the JTable.

---

#### installListeners

protected void installListeners()

Attaches listeners to the JTable.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Register all keyboard actions on the JTable.

---

#### installKeyboardActions

protected void installKeyboardActions()

Register all keyboard actions on the JTable.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

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

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Return the minimum size of the table. The minimum height is the
row height times the number of rows.
The minimum width is the sum of the minimum widths of each column.

**Overrides:** getMinimumSize

in class

ComponentUI
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

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

JComponent

c)

Return the minimum size of the table. The minimum height is the
row height times the number of rows.
The minimum width is the sum of the minimum widths of each column.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Return the preferred size of the table. The preferred height is the
row height times the number of rows.
The preferred width is the sum of the preferred widths of each column.

**Overrides:** getPreferredSize

in class

ComponentUI
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

Return the preferred size of the table. The preferred height is the
row height times the number of rows.
The preferred width is the sum of the preferred widths of each column.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Return the maximum size of the table. The maximum height is the
row heighttimes the number of rows.
The maximum width is the sum of the maximum widths of each column.

**Overrides:** getMaximumSize

in class

ComponentUI
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

Return the maximum size of the table. The maximum height is the
row heighttimes the number of rows.
The maximum width is the sum of the maximum widths of each column.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paint a representation of the

table

instance
that was set in installUI().

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paint a representation of the

table

instance
that was set in installUI().

---

