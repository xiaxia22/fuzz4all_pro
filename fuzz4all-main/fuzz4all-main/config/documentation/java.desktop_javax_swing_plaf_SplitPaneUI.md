# Class SplitPaneUI

**Source:** `java.desktop\javax\swing\plaf\SplitPaneUI.html`

### Class Description

```java
public abstract class
SplitPaneUI

extends
ComponentUI
```

Pluggable look and feel interface for JSplitPane.

**Direct Known Subclasses:** BasicSplitPaneUI

,

MultiSplitPaneUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public SplitPaneUI()

*No description found.*

---

### Method Details

#### public abstract void resetToPreferredSizes​(
JSplitPane
jc)

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

**Parameters:**
- jc

- a

JSplitPane

---

#### public abstract void setDividerLocation​(
JSplitPane
jc,
int location)

Sets the location of the divider to location.

**Parameters:**
- jc

- a

JSplitPane
- location

- an integer specifying the location of the divider

---

#### public abstract int getDividerLocation​(
JSplitPane
jc)

Returns the location of the divider.

**Parameters:**
- jc

- a

JSplitPane

**Returns:**
- an integer specifying the location of the divider

---

#### public abstract int getMinimumDividerLocation​(
JSplitPane
jc)

Returns the minimum possible location of the divider.

**Parameters:**
- jc

- a

JSplitPane

**Returns:**
- and integer specifying the minimum location of the divider

---

#### public abstract int getMaximumDividerLocation​(
JSplitPane
jc)

Returns the maximum possible location of the divider.

**Parameters:**
- jc

- a

JSplitPane

**Returns:**
- an integer specifying the maximum location of the divider

---

#### public abstract void finishedPaintingChildren​(
JSplitPane
jc,

Graphics
g)

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

**Parameters:**
- jc

- a

JSplitPane
- g

- the

Graphics

context

---

### Additional Sections

#### Class SplitPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SplitPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SplitPaneUI

javax.swing.plaf.SplitPaneUI

**Direct Known Subclasses:** BasicSplitPaneUI

,

MultiSplitPaneUI

```java
public abstract class
SplitPaneUI

extends
ComponentUI
```

Pluggable look and feel interface for JSplitPane.

public abstract class

SplitPaneUI

extends

ComponentUI

Pluggable look and feel interface for JSplitPane.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SplitPaneUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

finishedPaintingChildren

​(

JSplitPane

jc,

Graphics

g)

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

abstract int

getDividerLocation

​(

JSplitPane

jc)

Returns the location of the divider.

abstract int

getMaximumDividerLocation

​(

JSplitPane

jc)

Returns the maximum possible location of the divider.

abstract int

getMinimumDividerLocation

​(

JSplitPane

jc)

Returns the minimum possible location of the divider.

abstract void

resetToPreferredSizes

​(

JSplitPane

jc)

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

abstract void

setDividerLocation

​(

JSplitPane

jc,
int location)

Sets the location of the divider to location.

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

SplitPaneUI

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

abstract void

finishedPaintingChildren

​(

JSplitPane

jc,

Graphics

g)

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

abstract int

getDividerLocation

​(

JSplitPane

jc)

Returns the location of the divider.

abstract int

getMaximumDividerLocation

​(

JSplitPane

jc)

Returns the maximum possible location of the divider.

abstract int

getMinimumDividerLocation

​(

JSplitPane

jc)

Returns the minimum possible location of the divider.

abstract void

resetToPreferredSizes

​(

JSplitPane

jc)

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

abstract void

setDividerLocation

​(

JSplitPane

jc,
int location)

Sets the location of the divider to location.

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

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

Returns the location of the divider.

Returns the maximum possible location of the divider.

Returns the minimum possible location of the divider.

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

Sets the location of the divider to location.

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

- SplitPaneUI

```java
public SplitPaneUI()
```

============ METHOD DETAIL ==========

- Method Detail

- resetToPreferredSizes

```java
public abstract void resetToPreferredSizes​(
JSplitPane
jc)
```

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

**Parameters:** jc

- a

JSplitPane

- setDividerLocation

```java
public abstract void setDividerLocation​(
JSplitPane
jc,
int location)
```

Sets the location of the divider to location.

**Parameters:** jc

- a

JSplitPane
**Parameters:** location

- an integer specifying the location of the divider

- getDividerLocation

```java
public abstract int getDividerLocation​(
JSplitPane
jc)
```

Returns the location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the location of the divider

- getMinimumDividerLocation

```java
public abstract int getMinimumDividerLocation​(
JSplitPane
jc)
```

Returns the minimum possible location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** and integer specifying the minimum location of the divider

- getMaximumDividerLocation

```java
public abstract int getMaximumDividerLocation​(
JSplitPane
jc)
```

Returns the maximum possible location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the maximum location of the divider

- finishedPaintingChildren

```java
public abstract void finishedPaintingChildren​(
JSplitPane
jc,

Graphics
g)
```

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

**Parameters:** jc

- a

JSplitPane
**Parameters:** g

- the

Graphics

context

Constructor Detail

- SplitPaneUI

```java
public SplitPaneUI()
```

---

#### Constructor Detail

SplitPaneUI

```java
public SplitPaneUI()
```

---

#### SplitPaneUI

public SplitPaneUI()

Method Detail

- resetToPreferredSizes

```java
public abstract void resetToPreferredSizes​(
JSplitPane
jc)
```

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

**Parameters:** jc

- a

JSplitPane

- setDividerLocation

```java
public abstract void setDividerLocation​(
JSplitPane
jc,
int location)
```

Sets the location of the divider to location.

**Parameters:** jc

- a

JSplitPane
**Parameters:** location

- an integer specifying the location of the divider

- getDividerLocation

```java
public abstract int getDividerLocation​(
JSplitPane
jc)
```

Returns the location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the location of the divider

- getMinimumDividerLocation

```java
public abstract int getMinimumDividerLocation​(
JSplitPane
jc)
```

Returns the minimum possible location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** and integer specifying the minimum location of the divider

- getMaximumDividerLocation

```java
public abstract int getMaximumDividerLocation​(
JSplitPane
jc)
```

Returns the maximum possible location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the maximum location of the divider

- finishedPaintingChildren

```java
public abstract void finishedPaintingChildren​(
JSplitPane
jc,

Graphics
g)
```

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

**Parameters:** jc

- a

JSplitPane
**Parameters:** g

- the

Graphics

context

---

#### Method Detail

resetToPreferredSizes

```java
public abstract void resetToPreferredSizes​(
JSplitPane
jc)
```

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

**Parameters:** jc

- a

JSplitPane

---

#### resetToPreferredSizes

public abstract void resetToPreferredSizes​(

JSplitPane

jc)

Messaged to relayout the JSplitPane based on the preferred size
of the children components.

setDividerLocation

```java
public abstract void setDividerLocation​(
JSplitPane
jc,
int location)
```

Sets the location of the divider to location.

**Parameters:** jc

- a

JSplitPane
**Parameters:** location

- an integer specifying the location of the divider

---

#### setDividerLocation

public abstract void setDividerLocation​(

JSplitPane

jc,
int location)

Sets the location of the divider to location.

getDividerLocation

```java
public abstract int getDividerLocation​(
JSplitPane
jc)
```

Returns the location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the location of the divider

---

#### getDividerLocation

public abstract int getDividerLocation​(

JSplitPane

jc)

Returns the location of the divider.

getMinimumDividerLocation

```java
public abstract int getMinimumDividerLocation​(
JSplitPane
jc)
```

Returns the minimum possible location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** and integer specifying the minimum location of the divider

---

#### getMinimumDividerLocation

public abstract int getMinimumDividerLocation​(

JSplitPane

jc)

Returns the minimum possible location of the divider.

getMaximumDividerLocation

```java
public abstract int getMaximumDividerLocation​(
JSplitPane
jc)
```

Returns the maximum possible location of the divider.

**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the maximum location of the divider

---

#### getMaximumDividerLocation

public abstract int getMaximumDividerLocation​(

JSplitPane

jc)

Returns the maximum possible location of the divider.

finishedPaintingChildren

```java
public abstract void finishedPaintingChildren​(
JSplitPane
jc,

Graphics
g)
```

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

**Parameters:** jc

- a

JSplitPane
**Parameters:** g

- the

Graphics

context

---

#### finishedPaintingChildren

public abstract void finishedPaintingChildren​(

JSplitPane

jc,

Graphics

g)

Messaged after the JSplitPane the receiver is providing the look
and feel for paints its children.

---

