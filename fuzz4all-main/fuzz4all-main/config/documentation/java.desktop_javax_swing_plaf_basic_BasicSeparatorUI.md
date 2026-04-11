# Class BasicSeparatorUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicSeparatorUI.html`

### Class Description

```java
public class
BasicSeparatorUI

extends
SeparatorUI
```

A Basic L&F implementation of SeparatorUI. This implementation
is a "combined" view/controller.

**Direct Known Subclasses:** BasicPopupMenuSeparatorUI

,

BasicToolBarSeparatorUI

,

MetalSeparatorUI

---

### Field Details

#### protected
Color
shadow

The color of the shadow.

---

#### protected
Color
highlight

The color of the highlighting.

---

### Constructor Details

#### public BasicSeparatorUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns a new instance of

BasicSeparatorUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicSeparatorUI

---

#### protected void installDefaults​(
JSeparator
s)

Installs default properties.

**Parameters:**
- s

- an instance of

JSeparator

---

#### protected void uninstallDefaults​(
JSeparator
s)

Uninstalls default properties.

**Parameters:**
- s

- an instance of

JSeparator

---

#### protected void installListeners​(
JSeparator
s)

Registers listeners.

**Parameters:**
- s

- an instance of

JSeparator

---

#### protected void uninstallListeners​(
JSeparator
s)

Unregisters listeners.

**Parameters:**
- s

- an instance of

JSeparator

---

### Additional Sections

#### Class BasicSeparatorUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SeparatorUI
- - javax.swing.plaf.basic.BasicSeparatorUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SeparatorUI
- - javax.swing.plaf.basic.BasicSeparatorUI

javax.swing.plaf.SeparatorUI

- javax.swing.plaf.basic.BasicSeparatorUI

javax.swing.plaf.basic.BasicSeparatorUI

**Direct Known Subclasses:** BasicPopupMenuSeparatorUI

,

BasicToolBarSeparatorUI

,

MetalSeparatorUI

```java
public class
BasicSeparatorUI

extends
SeparatorUI
```

A Basic L&F implementation of SeparatorUI. This implementation
is a "combined" view/controller.

public class

BasicSeparatorUI

extends

SeparatorUI

A Basic L&F implementation of SeparatorUI. This implementation
is a "combined" view/controller.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Color

highlight

The color of the highlighting.

protected

Color

shadow

The color of the shadow.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicSeparatorUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicSeparatorUI

.

protected void

installDefaults

​(

JSeparator

s)

Installs default properties.

protected void

installListeners

​(

JSeparator

s)

Registers listeners.

protected void

uninstallDefaults

​(

JSeparator

s)

Uninstalls default properties.

protected void

uninstallListeners

​(

JSeparator

s)

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Color

highlight

The color of the highlighting.

protected

Color

shadow

The color of the shadow.

---

#### Field Summary

The color of the highlighting.

The color of the shadow.

Constructor Summary

Constructors

Constructor

Description

BasicSeparatorUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicSeparatorUI

.

protected void

installDefaults

​(

JSeparator

s)

Installs default properties.

protected void

installListeners

​(

JSeparator

s)

Registers listeners.

protected void

uninstallDefaults

​(

JSeparator

s)

Uninstalls default properties.

protected void

uninstallListeners

​(

JSeparator

s)

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

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

Returns a new instance of

BasicSeparatorUI

.

Installs default properties.

Registers listeners.

Uninstalls default properties.

Unregisters listeners.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

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

============ FIELD DETAIL ===========

- Field Detail

- shadow

```java
protected
Color
shadow
```

The color of the shadow.

- highlight

```java
protected
Color
highlight
```

The color of the highlighting.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicSeparatorUI

```java
public BasicSeparatorUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicSeparatorUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicSeparatorUI

- installDefaults

```java
protected void installDefaults​(
JSeparator
s)
```

Installs default properties.

**Parameters:** s

- an instance of

JSeparator

- uninstallDefaults

```java
protected void uninstallDefaults​(
JSeparator
s)
```

Uninstalls default properties.

**Parameters:** s

- an instance of

JSeparator

- installListeners

```java
protected void installListeners​(
JSeparator
s)
```

Registers listeners.

**Parameters:** s

- an instance of

JSeparator

- uninstallListeners

```java
protected void uninstallListeners​(
JSeparator
s)
```

Unregisters listeners.

**Parameters:** s

- an instance of

JSeparator

Field Detail

- shadow

```java
protected
Color
shadow
```

The color of the shadow.

- highlight

```java
protected
Color
highlight
```

The color of the highlighting.

---

#### Field Detail

shadow

```java
protected
Color
shadow
```

The color of the shadow.

---

#### shadow

protected

Color

shadow

The color of the shadow.

highlight

```java
protected
Color
highlight
```

The color of the highlighting.

---

#### highlight

protected

Color

highlight

The color of the highlighting.

Constructor Detail

- BasicSeparatorUI

```java
public BasicSeparatorUI()
```

---

#### Constructor Detail

BasicSeparatorUI

```java
public BasicSeparatorUI()
```

---

#### BasicSeparatorUI

public BasicSeparatorUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicSeparatorUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicSeparatorUI

- installDefaults

```java
protected void installDefaults​(
JSeparator
s)
```

Installs default properties.

**Parameters:** s

- an instance of

JSeparator

- uninstallDefaults

```java
protected void uninstallDefaults​(
JSeparator
s)
```

Uninstalls default properties.

**Parameters:** s

- an instance of

JSeparator

- installListeners

```java
protected void installListeners​(
JSeparator
s)
```

Registers listeners.

**Parameters:** s

- an instance of

JSeparator

- uninstallListeners

```java
protected void uninstallListeners​(
JSeparator
s)
```

Unregisters listeners.

**Parameters:** s

- an instance of

JSeparator

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicSeparatorUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicSeparatorUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns a new instance of

BasicSeparatorUI

.

installDefaults

```java
protected void installDefaults​(
JSeparator
s)
```

Installs default properties.

**Parameters:** s

- an instance of

JSeparator

---

#### installDefaults

protected void installDefaults​(

JSeparator

s)

Installs default properties.

uninstallDefaults

```java
protected void uninstallDefaults​(
JSeparator
s)
```

Uninstalls default properties.

**Parameters:** s

- an instance of

JSeparator

---

#### uninstallDefaults

protected void uninstallDefaults​(

JSeparator

s)

Uninstalls default properties.

installListeners

```java
protected void installListeners​(
JSeparator
s)
```

Registers listeners.

**Parameters:** s

- an instance of

JSeparator

---

#### installListeners

protected void installListeners​(

JSeparator

s)

Registers listeners.

uninstallListeners

```java
protected void uninstallListeners​(
JSeparator
s)
```

Unregisters listeners.

**Parameters:** s

- an instance of

JSeparator

---

#### uninstallListeners

protected void uninstallListeners​(

JSeparator

s)

Unregisters listeners.

---

