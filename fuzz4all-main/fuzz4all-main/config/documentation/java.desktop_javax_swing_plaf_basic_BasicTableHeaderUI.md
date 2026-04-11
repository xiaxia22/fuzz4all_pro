# Class BasicTableHeaderUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicTableHeaderUI.html`

### Class Description

```java
public class
BasicTableHeaderUI

extends
TableHeaderUI
```

BasicTableHeaderUI implementation

**Direct Known Subclasses:** SynthTableHeaderUI

---

### Field Details

#### protected
JTableHeader
header

The

JTableHeader

that is delegating the painting to this UI.

---

#### protected
CellRendererPane
rendererPane

The instance of

CellRendererPane

.

---

#### protected
MouseInputListener
mouseInputListener

Listeners that are attached to the

JTable

---

### Constructor Details

#### public BasicTableHeaderUI()

*No description found.*

---

### Method Details

#### protected
MouseInputListener
createMouseInputListener()

Creates the mouse listener for the

JTableHeader

.

**Returns:**
- the mouse listener for the

JTableHeader

---

#### public static
ComponentUI
createUI​(
JComponent
h)

Returns a new instance of

BasicTableHeaderUI

.

**Parameters:**
- h

- a component.

**Returns:**
- a new instance of

BasicTableHeaderUI

---

#### protected void installDefaults()

Initializes JTableHeader properties such as font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

---

#### protected void installListeners()

Attaches listeners to the JTableHeader.

---

#### protected void installKeyboardActions()

Register all keyboard actions on the JTableHeader.

---

#### protected void uninstallDefaults()

Uninstalls default properties

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void uninstallKeyboardActions()

Unregisters default key actions.

---

#### protected int getRolloverColumn()

Returns the index of the column header over which the mouse
currently is. When the mouse is not over the table header,
-1 is returned.

**Returns:**
- the index of the current rollover column

**See Also:**
- rolloverColumnUpdated(int, int)

**Since:**
- 1.6

---

#### protected void rolloverColumnUpdated​(int oldColumn,
int newColumn)

This method gets called every time when a rollover column in the table
header is updated. Every look and feel that supports a rollover effect
in a table header should override this method and repaint the header.

**Parameters:**
- oldColumn

- the index of the previous rollover column or -1 if the
mouse was not over a column
- newColumn

- the index of the new rollover column or -1 if the mouse
is not over a column

**See Also:**
- getRolloverColumn()

,

JTableHeader.getHeaderRect(int)

**Since:**
- 1.6

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
Dimension
getMinimumSize​(
JComponent
c)

Return the minimum size of the header. The minimum width is the sum
of the minimum widths of each column (plus inter-cell spacing).

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

Return the preferred size of the header. The preferred height is the
maximum of the preferred heights of all of the components provided
by the header renderers. The preferred width is the sum of the
preferred widths of each column (plus inter-cell spacing).

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

Return the maximum size of the header. The maximum width is the sum
of the maximum widths of each column (plus inter-cell spacing).

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

### Additional Sections

#### Class BasicTableHeaderUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TableHeaderUI
- - javax.swing.plaf.basic.BasicTableHeaderUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TableHeaderUI
- - javax.swing.plaf.basic.BasicTableHeaderUI

javax.swing.plaf.TableHeaderUI

- javax.swing.plaf.basic.BasicTableHeaderUI

javax.swing.plaf.basic.BasicTableHeaderUI

**Direct Known Subclasses:** SynthTableHeaderUI

```java
public class
BasicTableHeaderUI

extends
TableHeaderUI
```

BasicTableHeaderUI implementation

public class

BasicTableHeaderUI

extends

TableHeaderUI

BasicTableHeaderUI implementation

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicTableHeaderUI.MouseInputHandler

This class should be treated as a "protected" inner class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JTableHeader

header

The

JTableHeader

that is delegating the painting to this UI.

protected

MouseInputListener

mouseInputListener

Listeners that are attached to the

JTable

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicTableHeaderUI

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

MouseInputListener

createMouseInputListener

()

Creates the mouse listener for the

JTableHeader

.

static

ComponentUI

createUI

​(

JComponent

h)

Returns a new instance of

BasicTableHeaderUI

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Dimension

getMaximumSize

​(

JComponent

c)

Return the maximum size of the header.

Dimension

getMinimumSize

​(

JComponent

c)

Return the minimum size of the header.

Dimension

getPreferredSize

​(

JComponent

c)

Return the preferred size of the header.

protected int

getRolloverColumn

()

Returns the index of the column header over which the mouse
currently is.

protected void

installDefaults

()

Initializes JTableHeader properties such as font, foreground, and background.

protected void

installKeyboardActions

()

Register all keyboard actions on the JTableHeader.

protected void

installListeners

()

Attaches listeners to the JTableHeader.

protected void

rolloverColumnUpdated

​(int oldColumn,
int newColumn)

This method gets called every time when a rollover column in the table
header is updated.

protected void

uninstallDefaults

()

Uninstalls default properties

protected void

uninstallKeyboardActions

()

Unregisters default key actions.

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

getBaselineResizeBehavior

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

BasicTableHeaderUI.MouseInputHandler

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

JTableHeader

header

The

JTableHeader

that is delegating the painting to this UI.

protected

MouseInputListener

mouseInputListener

Listeners that are attached to the

JTable

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

---

#### Field Summary

The

JTableHeader

that is delegating the painting to this UI.

Listeners that are attached to the

JTable

The instance of

CellRendererPane

.

Constructor Summary

Constructors

Constructor

Description

BasicTableHeaderUI

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

MouseInputListener

createMouseInputListener

()

Creates the mouse listener for the

JTableHeader

.

static

ComponentUI

createUI

​(

JComponent

h)

Returns a new instance of

BasicTableHeaderUI

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Dimension

getMaximumSize

​(

JComponent

c)

Return the maximum size of the header.

Dimension

getMinimumSize

​(

JComponent

c)

Return the minimum size of the header.

Dimension

getPreferredSize

​(

JComponent

c)

Return the preferred size of the header.

protected int

getRolloverColumn

()

Returns the index of the column header over which the mouse
currently is.

protected void

installDefaults

()

Initializes JTableHeader properties such as font, foreground, and background.

protected void

installKeyboardActions

()

Register all keyboard actions on the JTableHeader.

protected void

installListeners

()

Attaches listeners to the JTableHeader.

protected void

rolloverColumnUpdated

​(int oldColumn,
int newColumn)

This method gets called every time when a rollover column in the table
header is updated.

protected void

uninstallDefaults

()

Uninstalls default properties

protected void

uninstallKeyboardActions

()

Unregisters default key actions.

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

getBaselineResizeBehavior

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

Creates the mouse listener for the

JTableHeader

.

Returns a new instance of

BasicTableHeaderUI

.

Returns the baseline.

Return the maximum size of the header.

Return the minimum size of the header.

Return the preferred size of the header.

Returns the index of the column header over which the mouse
currently is.

Initializes JTableHeader properties such as font, foreground, and background.

Register all keyboard actions on the JTableHeader.

Attaches listeners to the JTableHeader.

This method gets called every time when a rollover column in the table
header is updated.

Uninstalls default properties

Unregisters default key actions.

Unregisters listeners.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaselineResizeBehavior

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

- header

```java
protected
JTableHeader
header
```

The

JTableHeader

that is delegating the painting to this UI.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

Listeners that are attached to the

JTable

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicTableHeaderUI

```java
public BasicTableHeaderUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates the mouse listener for the

JTableHeader

.

**Returns:** the mouse listener for the

JTableHeader

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
h)
```

Returns a new instance of

BasicTableHeaderUI

.

**Parameters:** h

- a component.
**Returns:** a new instance of

BasicTableHeaderUI

- installDefaults

```java
protected void installDefaults()
```

Initializes JTableHeader properties such as font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:** ComponentUI.installUI(javax.swing.JComponent)

- installListeners

```java
protected void installListeners()
```

Attaches listeners to the JTableHeader.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Register all keyboard actions on the JTableHeader.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters default key actions.

- getRolloverColumn

```java
protected int getRolloverColumn()
```

Returns the index of the column header over which the mouse
currently is. When the mouse is not over the table header,
-1 is returned.

**Returns:** the index of the current rollover column
**Since:** 1.6
**See Also:** rolloverColumnUpdated(int, int)

- rolloverColumnUpdated

```java
protected void rolloverColumnUpdated​(int oldColumn,
int newColumn)
```

This method gets called every time when a rollover column in the table
header is updated. Every look and feel that supports a rollover effect
in a table header should override this method and repaint the header.

**Parameters:** oldColumn

- the index of the previous rollover column or -1 if the
mouse was not over a column
**Parameters:** newColumn

- the index of the new rollover column or -1 if the mouse
is not over a column
**Since:** 1.6
**See Also:** getRolloverColumn()

,

JTableHeader.getHeaderRect(int)

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

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Return the minimum size of the header. The minimum width is the sum
of the minimum widths of each column (plus inter-cell spacing).

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

Return the preferred size of the header. The preferred height is the
maximum of the preferred heights of all of the components provided
by the header renderers. The preferred width is the sum of the
preferred widths of each column (plus inter-cell spacing).

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

Return the maximum size of the header. The maximum width is the sum
of the maximum widths of each column (plus inter-cell spacing).

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

Field Detail

- header

```java
protected
JTableHeader
header
```

The

JTableHeader

that is delegating the painting to this UI.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

Listeners that are attached to the

JTable

---

#### Field Detail

header

```java
protected
JTableHeader
header
```

The

JTableHeader

that is delegating the painting to this UI.

---

#### header

protected

JTableHeader

header

The

JTableHeader

that is delegating the painting to this UI.

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

mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

Listeners that are attached to the

JTable

---

#### mouseInputListener

protected

MouseInputListener

mouseInputListener

Listeners that are attached to the

JTable

Constructor Detail

- BasicTableHeaderUI

```java
public BasicTableHeaderUI()
```

---

#### Constructor Detail

BasicTableHeaderUI

```java
public BasicTableHeaderUI()
```

---

#### BasicTableHeaderUI

public BasicTableHeaderUI()

Method Detail

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates the mouse listener for the

JTableHeader

.

**Returns:** the mouse listener for the

JTableHeader

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
h)
```

Returns a new instance of

BasicTableHeaderUI

.

**Parameters:** h

- a component.
**Returns:** a new instance of

BasicTableHeaderUI

- installDefaults

```java
protected void installDefaults()
```

Initializes JTableHeader properties such as font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:** ComponentUI.installUI(javax.swing.JComponent)

- installListeners

```java
protected void installListeners()
```

Attaches listeners to the JTableHeader.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Register all keyboard actions on the JTableHeader.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters default key actions.

- getRolloverColumn

```java
protected int getRolloverColumn()
```

Returns the index of the column header over which the mouse
currently is. When the mouse is not over the table header,
-1 is returned.

**Returns:** the index of the current rollover column
**Since:** 1.6
**See Also:** rolloverColumnUpdated(int, int)

- rolloverColumnUpdated

```java
protected void rolloverColumnUpdated​(int oldColumn,
int newColumn)
```

This method gets called every time when a rollover column in the table
header is updated. Every look and feel that supports a rollover effect
in a table header should override this method and repaint the header.

**Parameters:** oldColumn

- the index of the previous rollover column or -1 if the
mouse was not over a column
**Parameters:** newColumn

- the index of the new rollover column or -1 if the mouse
is not over a column
**Since:** 1.6
**See Also:** getRolloverColumn()

,

JTableHeader.getHeaderRect(int)

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

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Return the minimum size of the header. The minimum width is the sum
of the minimum widths of each column (plus inter-cell spacing).

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

Return the preferred size of the header. The preferred height is the
maximum of the preferred heights of all of the components provided
by the header renderers. The preferred width is the sum of the
preferred widths of each column (plus inter-cell spacing).

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

Return the maximum size of the header. The maximum width is the sum
of the maximum widths of each column (plus inter-cell spacing).

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

#### Method Detail

createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates the mouse listener for the

JTableHeader

.

**Returns:** the mouse listener for the

JTableHeader

---

#### createMouseInputListener

protected

MouseInputListener

createMouseInputListener()

Creates the mouse listener for the

JTableHeader

.

createUI

```java
public static
ComponentUI
createUI​(
JComponent
h)
```

Returns a new instance of

BasicTableHeaderUI

.

**Parameters:** h

- a component.
**Returns:** a new instance of

BasicTableHeaderUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

h)

Returns a new instance of

BasicTableHeaderUI

.

installDefaults

```java
protected void installDefaults()
```

Initializes JTableHeader properties such as font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

**See Also:** ComponentUI.installUI(javax.swing.JComponent)

---

#### installDefaults

protected void installDefaults()

Initializes JTableHeader properties such as font, foreground, and background.
The font, foreground, and background properties are only set if their
current value is either null or a UIResource, other properties are set
if the current value is null.

installListeners

```java
protected void installListeners()
```

Attaches listeners to the JTableHeader.

---

#### installListeners

protected void installListeners()

Attaches listeners to the JTableHeader.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Register all keyboard actions on the JTableHeader.

---

#### installKeyboardActions

protected void installKeyboardActions()

Register all keyboard actions on the JTableHeader.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties

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

Unregisters default key actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters default key actions.

getRolloverColumn

```java
protected int getRolloverColumn()
```

Returns the index of the column header over which the mouse
currently is. When the mouse is not over the table header,
-1 is returned.

**Returns:** the index of the current rollover column
**Since:** 1.6
**See Also:** rolloverColumnUpdated(int, int)

---

#### getRolloverColumn

protected int getRolloverColumn()

Returns the index of the column header over which the mouse
currently is. When the mouse is not over the table header,
-1 is returned.

rolloverColumnUpdated

```java
protected void rolloverColumnUpdated​(int oldColumn,
int newColumn)
```

This method gets called every time when a rollover column in the table
header is updated. Every look and feel that supports a rollover effect
in a table header should override this method and repaint the header.

**Parameters:** oldColumn

- the index of the previous rollover column or -1 if the
mouse was not over a column
**Parameters:** newColumn

- the index of the new rollover column or -1 if the mouse
is not over a column
**Since:** 1.6
**See Also:** getRolloverColumn()

,

JTableHeader.getHeaderRect(int)

---

#### rolloverColumnUpdated

protected void rolloverColumnUpdated​(int oldColumn,
int newColumn)

This method gets called every time when a rollover column in the table
header is updated. Every look and feel that supports a rollover effect
in a table header should override this method and repaint the header.

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

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Return the minimum size of the header. The minimum width is the sum
of the minimum widths of each column (plus inter-cell spacing).

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

Return the minimum size of the header. The minimum width is the sum
of the minimum widths of each column (plus inter-cell spacing).

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Return the preferred size of the header. The preferred height is the
maximum of the preferred heights of all of the components provided
by the header renderers. The preferred width is the sum of the
preferred widths of each column (plus inter-cell spacing).

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

Return the preferred size of the header. The preferred height is the
maximum of the preferred heights of all of the components provided
by the header renderers. The preferred width is the sum of the
preferred widths of each column (plus inter-cell spacing).

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Return the maximum size of the header. The maximum width is the sum
of the maximum widths of each column (plus inter-cell spacing).

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

Return the maximum size of the header. The maximum width is the sum
of the maximum widths of each column (plus inter-cell spacing).

---

