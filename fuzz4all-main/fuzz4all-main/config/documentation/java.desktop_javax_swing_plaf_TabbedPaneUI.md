# Class TabbedPaneUI

**Source:** `java.desktop\javax\swing\plaf\TabbedPaneUI.html`

### Class Description

```java
public abstract class
TabbedPaneUI

extends
ComponentUI
```

Pluggable look and feel interface for JTabbedPane.

**Direct Known Subclasses:** BasicTabbedPaneUI

,

MultiTabbedPaneUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public TabbedPaneUI()

*No description found.*

---

### Method Details

#### public abstract int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)

Returns the tab for the coordinate.

**Parameters:**
- pane

- the pane
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- the tab for the coordinate

---

#### public abstract
Rectangle
getTabBounds​(
JTabbedPane
pane,
int index)

Returns the rectangle for the tab bounds.

**Parameters:**
- pane

- the pane
- index

- the index

**Returns:**
- the rectangle for the tab bounds

---

#### public abstract int getTabRunCount​(
JTabbedPane
pane)

Returns the tab run count.

**Parameters:**
- pane

- the pane

**Returns:**
- the tab run count

---

### Additional Sections

#### Class TabbedPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TabbedPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TabbedPaneUI

javax.swing.plaf.TabbedPaneUI

**Direct Known Subclasses:** BasicTabbedPaneUI

,

MultiTabbedPaneUI

```java
public abstract class
TabbedPaneUI

extends
ComponentUI
```

Pluggable look and feel interface for JTabbedPane.

public abstract class

TabbedPaneUI

extends

ComponentUI

Pluggable look and feel interface for JTabbedPane.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TabbedPaneUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Rectangle

getTabBounds

​(

JTabbedPane

pane,
int index)

Returns the rectangle for the tab bounds.

abstract int

getTabRunCount

​(

JTabbedPane

pane)

Returns the tab run count.

abstract int

tabForCoordinate

​(

JTabbedPane

pane,
int x,
int y)

Returns the tab for the coordinate.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

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

Constructor Summary

Constructors

Constructor

Description

TabbedPaneUI

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Rectangle

getTabBounds

​(

JTabbedPane

pane,
int index)

Returns the rectangle for the tab bounds.

abstract int

getTabRunCount

​(

JTabbedPane

pane)

Returns the tab run count.

abstract int

tabForCoordinate

​(

JTabbedPane

pane,
int x,
int y)

Returns the tab for the coordinate.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

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

Returns the rectangle for the tab bounds.

Returns the tab run count.

Returns the tab for the coordinate.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TabbedPaneUI

```java
public TabbedPaneUI()
```

============ METHOD DETAIL ==========

- Method Detail

- tabForCoordinate

```java
public abstract int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)
```

Returns the tab for the coordinate.

**Parameters:** pane

- the pane
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** the tab for the coordinate

- getTabBounds

```java
public abstract
Rectangle
getTabBounds​(
JTabbedPane
pane,
int index)
```

Returns the rectangle for the tab bounds.

**Parameters:** pane

- the pane
**Parameters:** index

- the index
**Returns:** the rectangle for the tab bounds

- getTabRunCount

```java
public abstract int getTabRunCount​(
JTabbedPane
pane)
```

Returns the tab run count.

**Parameters:** pane

- the pane
**Returns:** the tab run count

Constructor Detail

- TabbedPaneUI

```java
public TabbedPaneUI()
```

---

#### Constructor Detail

TabbedPaneUI

```java
public TabbedPaneUI()
```

---

#### TabbedPaneUI

public TabbedPaneUI()

Method Detail

- tabForCoordinate

```java
public abstract int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)
```

Returns the tab for the coordinate.

**Parameters:** pane

- the pane
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** the tab for the coordinate

- getTabBounds

```java
public abstract
Rectangle
getTabBounds​(
JTabbedPane
pane,
int index)
```

Returns the rectangle for the tab bounds.

**Parameters:** pane

- the pane
**Parameters:** index

- the index
**Returns:** the rectangle for the tab bounds

- getTabRunCount

```java
public abstract int getTabRunCount​(
JTabbedPane
pane)
```

Returns the tab run count.

**Parameters:** pane

- the pane
**Returns:** the tab run count

---

#### Method Detail

tabForCoordinate

```java
public abstract int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)
```

Returns the tab for the coordinate.

**Parameters:** pane

- the pane
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** the tab for the coordinate

---

#### tabForCoordinate

public abstract int tabForCoordinate​(

JTabbedPane

pane,
int x,
int y)

Returns the tab for the coordinate.

getTabBounds

```java
public abstract
Rectangle
getTabBounds​(
JTabbedPane
pane,
int index)
```

Returns the rectangle for the tab bounds.

**Parameters:** pane

- the pane
**Parameters:** index

- the index
**Returns:** the rectangle for the tab bounds

---

#### getTabBounds

public abstract

Rectangle

getTabBounds​(

JTabbedPane

pane,
int index)

Returns the rectangle for the tab bounds.

getTabRunCount

```java
public abstract int getTabRunCount​(
JTabbedPane
pane)
```

Returns the tab run count.

**Parameters:** pane

- the pane
**Returns:** the tab run count

---

#### getTabRunCount

public abstract int getTabRunCount​(

JTabbedPane

pane)

Returns the tab run count.

---

