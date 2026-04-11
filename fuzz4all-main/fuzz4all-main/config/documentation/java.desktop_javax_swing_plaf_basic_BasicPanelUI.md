# Class BasicPanelUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicPanelUI.html`

### Class Description

```java
public class
BasicPanelUI

extends
PanelUI
```

BasicPanel implementation

**Direct Known Subclasses:** SynthPanelUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicPanelUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns an instance of

BasicPanelUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

BasicPanelUI

---

#### protected void installDefaults​(
JPanel
p)

Method for installing panel properties.

**Parameters:**
- p

- an instance of

JPanel

---

#### protected void uninstallDefaults​(
JPanel
p)

Method for uninstalling panel properties.

**Parameters:**
- p

- an instance of

JPanel

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

### Additional Sections

#### Class BasicPanelUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.PanelUI
- - javax.swing.plaf.basic.BasicPanelUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.PanelUI
- - javax.swing.plaf.basic.BasicPanelUI

javax.swing.plaf.PanelUI

- javax.swing.plaf.basic.BasicPanelUI

javax.swing.plaf.basic.BasicPanelUI

**Direct Known Subclasses:** SynthPanelUI

```java
public class
BasicPanelUI

extends
PanelUI
```

BasicPanel implementation

public class

BasicPanelUI

extends

PanelUI

BasicPanel implementation

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicPanelUI

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

Returns an instance of

BasicPanelUI

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

protected void

installDefaults

​(

JPanel

p)

Method for installing panel properties.

protected void

uninstallDefaults

​(

JPanel

p)

Method for uninstalling panel properties.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

BasicPanelUI

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

Returns an instance of

BasicPanelUI

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

protected void

installDefaults

​(

JPanel

p)

Method for installing panel properties.

protected void

uninstallDefaults

​(

JPanel

p)

Method for uninstalling panel properties.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

Returns an instance of

BasicPanelUI

.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Method for installing panel properties.

Method for uninstalling panel properties.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- BasicPanelUI

```java
public BasicPanelUI()
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

Returns an instance of

BasicPanelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicPanelUI

- installDefaults

```java
protected void installDefaults​(
JPanel
p)
```

Method for installing panel properties.

**Parameters:** p

- an instance of

JPanel

- uninstallDefaults

```java
protected void uninstallDefaults​(
JPanel
p)
```

Method for uninstalling panel properties.

**Parameters:** p

- an instance of

JPanel

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

Constructor Detail

- BasicPanelUI

```java
public BasicPanelUI()
```

---

#### Constructor Detail

BasicPanelUI

```java
public BasicPanelUI()
```

---

#### BasicPanelUI

public BasicPanelUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

BasicPanelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicPanelUI

- installDefaults

```java
protected void installDefaults​(
JPanel
p)
```

Method for installing panel properties.

**Parameters:** p

- an instance of

JPanel

- uninstallDefaults

```java
protected void uninstallDefaults​(
JPanel
p)
```

Method for uninstalling panel properties.

**Parameters:** p

- an instance of

JPanel

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

Returns an instance of

BasicPanelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicPanelUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns an instance of

BasicPanelUI

.

installDefaults

```java
protected void installDefaults​(
JPanel
p)
```

Method for installing panel properties.

**Parameters:** p

- an instance of

JPanel

---

#### installDefaults

protected void installDefaults​(

JPanel

p)

Method for installing panel properties.

uninstallDefaults

```java
protected void uninstallDefaults​(
JPanel
p)
```

Method for uninstalling panel properties.

**Parameters:** p

- an instance of

JPanel

---

#### uninstallDefaults

protected void uninstallDefaults​(

JPanel

p)

Method for uninstalling panel properties.

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

---

