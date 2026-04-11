# Class BasicOptionPaneUI.ButtonAreaLayout

**Source:** `java.desktop\javax\swing\plaf\basic\BasicOptionPaneUI.ButtonAreaLayout.html`

### Class Description

```java
public static class
BasicOptionPaneUI.ButtonAreaLayout

extends
Object

implements
LayoutManager
```

ButtonAreaLayout

behaves in a similar manner to

FlowLayout

. It lays out all components from left to
right. If

syncAllWidths

is true, the widths of each
component will be set to the largest preferred size width.

This class should be treated as a "protected" inner class.
Instantiate it only within subclasses of

BasicOptionPaneUI

.

**All Implemented Interfaces:** LayoutManager

---

### Field Details

#### protected boolean syncAllWidths

The value represents if the width of children should be synchronized.

---

#### protected int padding

The padding value.

---

#### protected boolean centersChildren

If true, children are lumped together in parent.

---

### Constructor Details

#### public ButtonAreaLayout​(boolean syncAllWidths,
int padding)

Constructs a new instance of

ButtonAreaLayout

.

**Parameters:**
- syncAllWidths

- if the width of children should be synchronized
- padding

- the padding value

---

### Method Details

#### public void setSyncAllWidths​(boolean newValue)

Sets if the width of children should be synchronized.

**Parameters:**
- newValue

- if the width of children should be synchronized

---

#### public boolean getSyncAllWidths()

Returns if the width of children should be synchronized.

**Returns:**
- if the width of children should be synchronized

---

#### public void setPadding​(int newPadding)

Sets the padding value.

**Parameters:**
- newPadding

- the new padding

---

#### public int getPadding()

Returns the padding.

**Returns:**
- the padding

---

#### public void setCentersChildren​(boolean newValue)

Sets whether or not center children should be used.

**Parameters:**
- newValue

- a new value

---

#### public boolean getCentersChildren()

Returns whether or not center children should be used.

**Returns:**
- whether or not center children should be used

---

### Additional Sections

#### Class BasicOptionPaneUI.ButtonAreaLayout

java.lang.Object

- javax.swing.plaf.basic.BasicOptionPaneUI.ButtonAreaLayout

javax.swing.plaf.basic.BasicOptionPaneUI.ButtonAreaLayout

**All Implemented Interfaces:** LayoutManager

**Enclosing class:** BasicOptionPaneUI

```java
public static class
BasicOptionPaneUI.ButtonAreaLayout

extends
Object

implements
LayoutManager
```

ButtonAreaLayout

behaves in a similar manner to

FlowLayout

. It lays out all components from left to
right. If

syncAllWidths

is true, the widths of each
component will be set to the largest preferred size width.

This class should be treated as a "protected" inner class.
Instantiate it only within subclasses of

BasicOptionPaneUI

.

public static class

BasicOptionPaneUI.ButtonAreaLayout

extends

Object

implements

LayoutManager

ButtonAreaLayout

behaves in a similar manner to

FlowLayout

. It lays out all components from left to
right. If

syncAllWidths

is true, the widths of each
component will be set to the largest preferred size width.

This class should be treated as a "protected" inner class.
Instantiate it only within subclasses of

BasicOptionPaneUI

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

centersChildren

If true, children are lumped together in parent.

protected int

padding

The padding value.

protected boolean

syncAllWidths

The value represents if the width of children should be synchronized.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ButtonAreaLayout

​(boolean syncAllWidths,
int padding)

Constructs a new instance of

ButtonAreaLayout

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

getCentersChildren

()

Returns whether or not center children should be used.

int

getPadding

()

Returns the padding.

boolean

getSyncAllWidths

()

Returns if the width of children should be synchronized.

void

setCentersChildren

​(boolean newValue)

Sets whether or not center children should be used.

void

setPadding

​(int newPadding)

Sets the padding value.

void

setSyncAllWidths

​(boolean newValue)

Sets if the width of children should be synchronized.

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

- Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

centersChildren

If true, children are lumped together in parent.

protected int

padding

The padding value.

protected boolean

syncAllWidths

The value represents if the width of children should be synchronized.

---

#### Field Summary

If true, children are lumped together in parent.

The padding value.

The value represents if the width of children should be synchronized.

Constructor Summary

Constructors

Constructor

Description

ButtonAreaLayout

​(boolean syncAllWidths,
int padding)

Constructs a new instance of

ButtonAreaLayout

.

---

#### Constructor Summary

Constructs a new instance of

ButtonAreaLayout

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

getCentersChildren

()

Returns whether or not center children should be used.

int

getPadding

()

Returns the padding.

boolean

getSyncAllWidths

()

Returns if the width of children should be synchronized.

void

setCentersChildren

​(boolean newValue)

Sets whether or not center children should be used.

void

setPadding

​(int newPadding)

Sets the padding value.

void

setSyncAllWidths

​(boolean newValue)

Sets if the width of children should be synchronized.

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

- Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

---

#### Method Summary

Returns whether or not center children should be used.

Returns the padding.

Returns if the width of children should be synchronized.

Sets whether or not center children should be used.

Sets the padding value.

Sets if the width of children should be synchronized.

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

Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

---

#### Methods declared in interface java.awt. LayoutManager

============ FIELD DETAIL ===========

- Field Detail

- syncAllWidths

```java
protected boolean syncAllWidths
```

The value represents if the width of children should be synchronized.

- padding

```java
protected int padding
```

The padding value.

- centersChildren

```java
protected boolean centersChildren
```

If true, children are lumped together in parent.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ButtonAreaLayout

```java
public ButtonAreaLayout​(boolean syncAllWidths,
int padding)
```

Constructs a new instance of

ButtonAreaLayout

.

**Parameters:** syncAllWidths

- if the width of children should be synchronized
**Parameters:** padding

- the padding value

============ METHOD DETAIL ==========

- Method Detail

- setSyncAllWidths

```java
public void setSyncAllWidths​(boolean newValue)
```

Sets if the width of children should be synchronized.

**Parameters:** newValue

- if the width of children should be synchronized

- getSyncAllWidths

```java
public boolean getSyncAllWidths()
```

Returns if the width of children should be synchronized.

**Returns:** if the width of children should be synchronized

- setPadding

```java
public void setPadding​(int newPadding)
```

Sets the padding value.

**Parameters:** newPadding

- the new padding

- getPadding

```java
public int getPadding()
```

Returns the padding.

**Returns:** the padding

- setCentersChildren

```java
public void setCentersChildren​(boolean newValue)
```

Sets whether or not center children should be used.

**Parameters:** newValue

- a new value

- getCentersChildren

```java
public boolean getCentersChildren()
```

Returns whether or not center children should be used.

**Returns:** whether or not center children should be used

Field Detail

- syncAllWidths

```java
protected boolean syncAllWidths
```

The value represents if the width of children should be synchronized.

- padding

```java
protected int padding
```

The padding value.

- centersChildren

```java
protected boolean centersChildren
```

If true, children are lumped together in parent.

---

#### Field Detail

syncAllWidths

```java
protected boolean syncAllWidths
```

The value represents if the width of children should be synchronized.

---

#### syncAllWidths

protected boolean syncAllWidths

The value represents if the width of children should be synchronized.

padding

```java
protected int padding
```

The padding value.

---

#### padding

protected int padding

The padding value.

centersChildren

```java
protected boolean centersChildren
```

If true, children are lumped together in parent.

---

#### centersChildren

protected boolean centersChildren

If true, children are lumped together in parent.

Constructor Detail

- ButtonAreaLayout

```java
public ButtonAreaLayout​(boolean syncAllWidths,
int padding)
```

Constructs a new instance of

ButtonAreaLayout

.

**Parameters:** syncAllWidths

- if the width of children should be synchronized
**Parameters:** padding

- the padding value

---

#### Constructor Detail

ButtonAreaLayout

```java
public ButtonAreaLayout​(boolean syncAllWidths,
int padding)
```

Constructs a new instance of

ButtonAreaLayout

.

**Parameters:** syncAllWidths

- if the width of children should be synchronized
**Parameters:** padding

- the padding value

---

#### ButtonAreaLayout

public ButtonAreaLayout​(boolean syncAllWidths,
int padding)

Constructs a new instance of

ButtonAreaLayout

.

Method Detail

- setSyncAllWidths

```java
public void setSyncAllWidths​(boolean newValue)
```

Sets if the width of children should be synchronized.

**Parameters:** newValue

- if the width of children should be synchronized

- getSyncAllWidths

```java
public boolean getSyncAllWidths()
```

Returns if the width of children should be synchronized.

**Returns:** if the width of children should be synchronized

- setPadding

```java
public void setPadding​(int newPadding)
```

Sets the padding value.

**Parameters:** newPadding

- the new padding

- getPadding

```java
public int getPadding()
```

Returns the padding.

**Returns:** the padding

- setCentersChildren

```java
public void setCentersChildren​(boolean newValue)
```

Sets whether or not center children should be used.

**Parameters:** newValue

- a new value

- getCentersChildren

```java
public boolean getCentersChildren()
```

Returns whether or not center children should be used.

**Returns:** whether or not center children should be used

---

#### Method Detail

setSyncAllWidths

```java
public void setSyncAllWidths​(boolean newValue)
```

Sets if the width of children should be synchronized.

**Parameters:** newValue

- if the width of children should be synchronized

---

#### setSyncAllWidths

public void setSyncAllWidths​(boolean newValue)

Sets if the width of children should be synchronized.

getSyncAllWidths

```java
public boolean getSyncAllWidths()
```

Returns if the width of children should be synchronized.

**Returns:** if the width of children should be synchronized

---

#### getSyncAllWidths

public boolean getSyncAllWidths()

Returns if the width of children should be synchronized.

setPadding

```java
public void setPadding​(int newPadding)
```

Sets the padding value.

**Parameters:** newPadding

- the new padding

---

#### setPadding

public void setPadding​(int newPadding)

Sets the padding value.

getPadding

```java
public int getPadding()
```

Returns the padding.

**Returns:** the padding

---

#### getPadding

public int getPadding()

Returns the padding.

setCentersChildren

```java
public void setCentersChildren​(boolean newValue)
```

Sets whether or not center children should be used.

**Parameters:** newValue

- a new value

---

#### setCentersChildren

public void setCentersChildren​(boolean newValue)

Sets whether or not center children should be used.

getCentersChildren

```java
public boolean getCentersChildren()
```

Returns whether or not center children should be used.

**Returns:** whether or not center children should be used

---

#### getCentersChildren

public boolean getCentersChildren()

Returns whether or not center children should be used.

---

