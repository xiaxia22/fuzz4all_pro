# Class OptionPaneUI

**Source:** `java.desktop\javax\swing\plaf\OptionPaneUI.html`

### Class Description

```java
public abstract class
OptionPaneUI

extends
ComponentUI
```

Pluggable look and feel interface for JOptionPane.

**Direct Known Subclasses:** BasicOptionPaneUI

,

MultiOptionPaneUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public OptionPaneUI()

*No description found.*

---

### Method Details

#### public abstract void selectInitialValue​(
JOptionPane
op)

Requests the component representing the default value to have
focus.

**Parameters:**
- op

- a

JOptionPane

---

#### public abstract boolean containsCustomComponents​(
JOptionPane
op)

Returns true if the user has supplied instances of Component for
either the options or message.

**Parameters:**
- op

- a

JOptionPane

**Returns:**
- true

if the given

JOptionPane

contains user
created

Component

s

---

### Additional Sections

#### Class OptionPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.OptionPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.OptionPaneUI

javax.swing.plaf.OptionPaneUI

**Direct Known Subclasses:** BasicOptionPaneUI

,

MultiOptionPaneUI

```java
public abstract class
OptionPaneUI

extends
ComponentUI
```

Pluggable look and feel interface for JOptionPane.

public abstract class

OptionPaneUI

extends

ComponentUI

Pluggable look and feel interface for JOptionPane.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OptionPaneUI

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

containsCustomComponents

​(

JOptionPane

op)

Returns true if the user has supplied instances of Component for
either the options or message.

abstract void

selectInitialValue

​(

JOptionPane

op)

Requests the component representing the default value to have
focus.

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

OptionPaneUI

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

containsCustomComponents

​(

JOptionPane

op)

Returns true if the user has supplied instances of Component for
either the options or message.

abstract void

selectInitialValue

​(

JOptionPane

op)

Requests the component representing the default value to have
focus.

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

Returns true if the user has supplied instances of Component for
either the options or message.

Requests the component representing the default value to have
focus.

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

- OptionPaneUI

```java
public OptionPaneUI()
```

============ METHOD DETAIL ==========

- Method Detail

- selectInitialValue

```java
public abstract void selectInitialValue​(
JOptionPane
op)
```

Requests the component representing the default value to have
focus.

**Parameters:** op

- a

JOptionPane

- containsCustomComponents

```java
public abstract boolean containsCustomComponents​(
JOptionPane
op)
```

Returns true if the user has supplied instances of Component for
either the options or message.

**Parameters:** op

- a

JOptionPane
**Returns:** true

if the given

JOptionPane

contains user
created

Component

s

Constructor Detail

- OptionPaneUI

```java
public OptionPaneUI()
```

---

#### Constructor Detail

OptionPaneUI

```java
public OptionPaneUI()
```

---

#### OptionPaneUI

public OptionPaneUI()

Method Detail

- selectInitialValue

```java
public abstract void selectInitialValue​(
JOptionPane
op)
```

Requests the component representing the default value to have
focus.

**Parameters:** op

- a

JOptionPane

- containsCustomComponents

```java
public abstract boolean containsCustomComponents​(
JOptionPane
op)
```

Returns true if the user has supplied instances of Component for
either the options or message.

**Parameters:** op

- a

JOptionPane
**Returns:** true

if the given

JOptionPane

contains user
created

Component

s

---

#### Method Detail

selectInitialValue

```java
public abstract void selectInitialValue​(
JOptionPane
op)
```

Requests the component representing the default value to have
focus.

**Parameters:** op

- a

JOptionPane

---

#### selectInitialValue

public abstract void selectInitialValue​(

JOptionPane

op)

Requests the component representing the default value to have
focus.

containsCustomComponents

```java
public abstract boolean containsCustomComponents​(
JOptionPane
op)
```

Returns true if the user has supplied instances of Component for
either the options or message.

**Parameters:** op

- a

JOptionPane
**Returns:** true

if the given

JOptionPane

contains user
created

Component

s

---

#### containsCustomComponents

public abstract boolean containsCustomComponents​(

JOptionPane

op)

Returns true if the user has supplied instances of Component for
either the options or message.

---

