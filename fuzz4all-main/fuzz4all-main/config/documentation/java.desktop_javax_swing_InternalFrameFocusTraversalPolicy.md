# Class InternalFrameFocusTraversalPolicy

**Source:** `java.desktop\javax\swing\InternalFrameFocusTraversalPolicy.html`

### Class Description

```java
public abstract class
InternalFrameFocusTraversalPolicy

extends
FocusTraversalPolicy
```

A FocusTraversalPolicy which can optionally provide an algorithm for
determining a JInternalFrame's initial Component. The initial Component is
the first to receive focus when the JInternalFrame is first selected. By
default, this is the same as the JInternalFrame's default Component to
focus.

**Direct Known Subclasses:** SortingFocusTraversalPolicy

---

### Field Details

*No entries found.*

### Constructor Details

#### public InternalFrameFocusTraversalPolicy()

*No description found.*

---

### Method Details

#### public
Component
getInitialComponent​(
JInternalFrame
frame)

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time. Once the JInternalFrame
has been selected by a call to

setSelected(true)

, the
initial Component will not be used again. Instead, if the JInternalFrame
loses and subsequently regains selection, or is made invisible or
undisplayable and subsequently made visible and displayable, the
JInternalFrame's most recently focused Component will become the focus
owner. The default implementation of this method returns the
JInternalFrame's default Component to focus.

**Parameters:**
- frame

- the JInternalFrame whose initial Component is to be
returned

**Returns:**
- the Component that should receive the focus when frame is
selected for the first time, or null if no suitable Component
can be found

**Throws:**
- IllegalArgumentException

- if window is null

**See Also:**
- JInternalFrame.getMostRecentFocusOwner()

---

### Additional Sections

#### Class InternalFrameFocusTraversalPolicy

java.lang.Object

- java.awt.FocusTraversalPolicy
- - javax.swing.InternalFrameFocusTraversalPolicy

java.awt.FocusTraversalPolicy

- javax.swing.InternalFrameFocusTraversalPolicy

javax.swing.InternalFrameFocusTraversalPolicy

**Direct Known Subclasses:** SortingFocusTraversalPolicy

```java
public abstract class
InternalFrameFocusTraversalPolicy

extends
FocusTraversalPolicy
```

A FocusTraversalPolicy which can optionally provide an algorithm for
determining a JInternalFrame's initial Component. The initial Component is
the first to receive focus when the JInternalFrame is first selected. By
default, this is the same as the JInternalFrame's default Component to
focus.

**Since:** 1.4

public abstract class

InternalFrameFocusTraversalPolicy

extends

FocusTraversalPolicy

A FocusTraversalPolicy which can optionally provide an algorithm for
determining a JInternalFrame's initial Component. The initial Component is
the first to receive focus when the JInternalFrame is first selected. By
default, this is the same as the JInternalFrame's default Component to
focus.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InternalFrameFocusTraversalPolicy

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Component

getInitialComponent

​(

JInternalFrame

frame)

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time.

- Methods declared in class java.awt.

FocusTraversalPolicy

getComponentAfter

,

getComponentBefore

,

getDefaultComponent

,

getFirstComponent

,

getInitialComponent

,

getLastComponent

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

InternalFrameFocusTraversalPolicy

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

Component

getInitialComponent

​(

JInternalFrame

frame)

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time.

- Methods declared in class java.awt.

FocusTraversalPolicy

getComponentAfter

,

getComponentBefore

,

getDefaultComponent

,

getFirstComponent

,

getInitialComponent

,

getLastComponent

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

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time.

Methods declared in class java.awt.

FocusTraversalPolicy

getComponentAfter

,

getComponentBefore

,

getDefaultComponent

,

getFirstComponent

,

getInitialComponent

,

getLastComponent

---

#### Methods declared in class java.awt. FocusTraversalPolicy

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

- InternalFrameFocusTraversalPolicy

```java
public InternalFrameFocusTraversalPolicy()
```

============ METHOD DETAIL ==========

- Method Detail

- getInitialComponent

```java
public
Component
getInitialComponent​(
JInternalFrame
frame)
```

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time. Once the JInternalFrame
has been selected by a call to

setSelected(true)

, the
initial Component will not be used again. Instead, if the JInternalFrame
loses and subsequently regains selection, or is made invisible or
undisplayable and subsequently made visible and displayable, the
JInternalFrame's most recently focused Component will become the focus
owner. The default implementation of this method returns the
JInternalFrame's default Component to focus.

**Parameters:** frame

- the JInternalFrame whose initial Component is to be
returned
**Returns:** the Component that should receive the focus when frame is
selected for the first time, or null if no suitable Component
can be found
**Throws:** IllegalArgumentException

- if window is null
**See Also:** JInternalFrame.getMostRecentFocusOwner()

Constructor Detail

- InternalFrameFocusTraversalPolicy

```java
public InternalFrameFocusTraversalPolicy()
```

---

#### Constructor Detail

InternalFrameFocusTraversalPolicy

```java
public InternalFrameFocusTraversalPolicy()
```

---

#### InternalFrameFocusTraversalPolicy

public InternalFrameFocusTraversalPolicy()

Method Detail

- getInitialComponent

```java
public
Component
getInitialComponent​(
JInternalFrame
frame)
```

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time. Once the JInternalFrame
has been selected by a call to

setSelected(true)

, the
initial Component will not be used again. Instead, if the JInternalFrame
loses and subsequently regains selection, or is made invisible or
undisplayable and subsequently made visible and displayable, the
JInternalFrame's most recently focused Component will become the focus
owner. The default implementation of this method returns the
JInternalFrame's default Component to focus.

**Parameters:** frame

- the JInternalFrame whose initial Component is to be
returned
**Returns:** the Component that should receive the focus when frame is
selected for the first time, or null if no suitable Component
can be found
**Throws:** IllegalArgumentException

- if window is null
**See Also:** JInternalFrame.getMostRecentFocusOwner()

---

#### Method Detail

getInitialComponent

```java
public
Component
getInitialComponent​(
JInternalFrame
frame)
```

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time. Once the JInternalFrame
has been selected by a call to

setSelected(true)

, the
initial Component will not be used again. Instead, if the JInternalFrame
loses and subsequently regains selection, or is made invisible or
undisplayable and subsequently made visible and displayable, the
JInternalFrame's most recently focused Component will become the focus
owner. The default implementation of this method returns the
JInternalFrame's default Component to focus.

**Parameters:** frame

- the JInternalFrame whose initial Component is to be
returned
**Returns:** the Component that should receive the focus when frame is
selected for the first time, or null if no suitable Component
can be found
**Throws:** IllegalArgumentException

- if window is null
**See Also:** JInternalFrame.getMostRecentFocusOwner()

---

#### getInitialComponent

public

Component

getInitialComponent​(

JInternalFrame

frame)

Returns the Component that should receive the focus when a
JInternalFrame is selected for the first time. Once the JInternalFrame
has been selected by a call to

setSelected(true)

, the
initial Component will not be used again. Instead, if the JInternalFrame
loses and subsequently regains selection, or is made invisible or
undisplayable and subsequently made visible and displayable, the
JInternalFrame's most recently focused Component will become the focus
owner. The default implementation of this method returns the
JInternalFrame's default Component to focus.

---

