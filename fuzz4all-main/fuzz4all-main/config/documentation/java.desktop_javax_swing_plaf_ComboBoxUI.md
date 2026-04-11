# Class ComboBoxUI

**Source:** `java.desktop\javax\swing\plaf\ComboBoxUI.html`

### Class Description

```java
public abstract class
ComboBoxUI

extends
ComponentUI
```

Pluggable look and feel interface for JComboBox.

**Direct Known Subclasses:** BasicComboBoxUI

,

MultiComboBoxUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public ComboBoxUI()

*No description found.*

---

### Method Details

#### public abstract void setPopupVisible​(
JComboBox
<?> c,
boolean v)

Set the visibility of the popup

**Parameters:**
- c

- a

JComboBox
- v

- a

boolean

determining the visibilty of the popup

---

#### public abstract boolean isPopupVisible​(
JComboBox
<?> c)

Determine the visibility of the popup

**Parameters:**
- c

- a

JComboBox

**Returns:**
- true if popup of the

JComboBox

is visible

---

#### public abstract boolean isFocusTraversable​(
JComboBox
<?> c)

Determine whether or not the combo box itself is traversable

**Parameters:**
- c

- a

JComboBox

**Returns:**
- true if the given

JComboBox

is traversable

---

### Additional Sections

#### Class ComboBoxUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ComboBoxUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ComboBoxUI

javax.swing.plaf.ComboBoxUI

**Direct Known Subclasses:** BasicComboBoxUI

,

MultiComboBoxUI

```java
public abstract class
ComboBoxUI

extends
ComponentUI
```

Pluggable look and feel interface for JComboBox.

public abstract class

ComboBoxUI

extends

ComponentUI

Pluggable look and feel interface for JComboBox.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ComboBoxUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

isFocusTraversable

​(

JComboBox

<?> c)

Determine whether or not the combo box itself is traversable

abstract boolean

isPopupVisible

​(

JComboBox

<?> c)

Determine the visibility of the popup

abstract void

setPopupVisible

​(

JComboBox

<?> c,
boolean v)

Set the visibility of the popup

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

ComboBoxUI

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

abstract boolean

isFocusTraversable

​(

JComboBox

<?> c)

Determine whether or not the combo box itself is traversable

abstract boolean

isPopupVisible

​(

JComboBox

<?> c)

Determine the visibility of the popup

abstract void

setPopupVisible

​(

JComboBox

<?> c,
boolean v)

Set the visibility of the popup

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

Determine whether or not the combo box itself is traversable

Determine the visibility of the popup

Set the visibility of the popup

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

- ComboBoxUI

```java
public ComboBoxUI()
```

============ METHOD DETAIL ==========

- Method Detail

- setPopupVisible

```java
public abstract void setPopupVisible​(
JComboBox
<?> c,
boolean v)
```

Set the visibility of the popup

**Parameters:** c

- a

JComboBox
**Parameters:** v

- a

boolean

determining the visibilty of the popup

- isPopupVisible

```java
public abstract boolean isPopupVisible​(
JComboBox
<?> c)
```

Determine the visibility of the popup

**Parameters:** c

- a

JComboBox
**Returns:** true if popup of the

JComboBox

is visible

- isFocusTraversable

```java
public abstract boolean isFocusTraversable​(
JComboBox
<?> c)
```

Determine whether or not the combo box itself is traversable

**Parameters:** c

- a

JComboBox
**Returns:** true if the given

JComboBox

is traversable

Constructor Detail

- ComboBoxUI

```java
public ComboBoxUI()
```

---

#### Constructor Detail

ComboBoxUI

```java
public ComboBoxUI()
```

---

#### ComboBoxUI

public ComboBoxUI()

Method Detail

- setPopupVisible

```java
public abstract void setPopupVisible​(
JComboBox
<?> c,
boolean v)
```

Set the visibility of the popup

**Parameters:** c

- a

JComboBox
**Parameters:** v

- a

boolean

determining the visibilty of the popup

- isPopupVisible

```java
public abstract boolean isPopupVisible​(
JComboBox
<?> c)
```

Determine the visibility of the popup

**Parameters:** c

- a

JComboBox
**Returns:** true if popup of the

JComboBox

is visible

- isFocusTraversable

```java
public abstract boolean isFocusTraversable​(
JComboBox
<?> c)
```

Determine whether or not the combo box itself is traversable

**Parameters:** c

- a

JComboBox
**Returns:** true if the given

JComboBox

is traversable

---

#### Method Detail

setPopupVisible

```java
public abstract void setPopupVisible​(
JComboBox
<?> c,
boolean v)
```

Set the visibility of the popup

**Parameters:** c

- a

JComboBox
**Parameters:** v

- a

boolean

determining the visibilty of the popup

---

#### setPopupVisible

public abstract void setPopupVisible​(

JComboBox

<?> c,
boolean v)

Set the visibility of the popup

isPopupVisible

```java
public abstract boolean isPopupVisible​(
JComboBox
<?> c)
```

Determine the visibility of the popup

**Parameters:** c

- a

JComboBox
**Returns:** true if popup of the

JComboBox

is visible

---

#### isPopupVisible

public abstract boolean isPopupVisible​(

JComboBox

<?> c)

Determine the visibility of the popup

isFocusTraversable

```java
public abstract boolean isFocusTraversable​(
JComboBox
<?> c)
```

Determine whether or not the combo box itself is traversable

**Parameters:** c

- a

JComboBox
**Returns:** true if the given

JComboBox

is traversable

---

#### isFocusTraversable

public abstract boolean isFocusTraversable​(

JComboBox

<?> c)

Determine whether or not the combo box itself is traversable

---

