# Class MetalLabelUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalLabelUI.html`

### Class Description

```java
public class
MetalLabelUI

extends
BasicLabelUI
```

A Windows L&F implementation of LabelUI. This implementation
is completely static, i.e. there's only one UIView implementation
that's shared by all JLabel objects.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

---

### Field Details

#### protected static
MetalLabelUI
metalLabelUI

The default

MetalLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

---

### Constructor Details

#### public MetalLabelUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns an instance of

MetalLabelUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MetalLabelUI

---

#### protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

**Overrides:**
- paintDisabledText

in class

BasicLabelUI

**Parameters:**
- l

- an instance of

JLabel
- g

- an instance of

Graphics
- s

- a text
- textX

- an X coordinate
- textY

- an Y coordinate

**See Also:**
- BasicLabelUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

BasicLabelUI.paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

---

### Additional Sections

#### Class MetalLabelUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.LabelUI
- - javax.swing.plaf.basic.BasicLabelUI
- - javax.swing.plaf.metal.MetalLabelUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.LabelUI
- - javax.swing.plaf.basic.BasicLabelUI
- - javax.swing.plaf.metal.MetalLabelUI

javax.swing.plaf.LabelUI

- javax.swing.plaf.basic.BasicLabelUI
- - javax.swing.plaf.metal.MetalLabelUI

javax.swing.plaf.basic.BasicLabelUI

- javax.swing.plaf.metal.MetalLabelUI

javax.swing.plaf.metal.MetalLabelUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

```java
public class
MetalLabelUI

extends
BasicLabelUI
```

A Windows L&F implementation of LabelUI. This implementation
is completely static, i.e. there's only one UIView implementation
that's shared by all JLabel objects.

public class

MetalLabelUI

extends

BasicLabelUI

A Windows L&F implementation of LabelUI. This implementation
is completely static, i.e. there's only one UIView implementation
that's shared by all JLabel objects.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

MetalLabelUI

metalLabelUI

The default

MetalLabelUI

instance.

- Fields declared in class javax.swing.plaf.basic.

BasicLabelUI

labelUI

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalLabelUI

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

MetalLabelUI

.

protected void

paintDisabledText

​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

- Methods declared in class javax.swing.plaf.basic.

BasicLabelUI

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

layoutCL

,

paint

,

paintEnabledText

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getPreferredSize

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

Field Summary

Fields

Modifier and Type

Field

Description

protected static

MetalLabelUI

metalLabelUI

The default

MetalLabelUI

instance.

- Fields declared in class javax.swing.plaf.basic.

BasicLabelUI

labelUI

---

#### Field Summary

The default

MetalLabelUI

instance.

Fields declared in class javax.swing.plaf.basic.

BasicLabelUI

labelUI

---

#### Fields declared in class javax.swing.plaf.basic. BasicLabelUI

Constructor Summary

Constructors

Constructor

Description

MetalLabelUI

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

MetalLabelUI

.

protected void

paintDisabledText

​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

- Methods declared in class javax.swing.plaf.basic.

BasicLabelUI

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

layoutCL

,

paint

,

paintEnabledText

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getPreferredSize

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Method Summary

Returns an instance of

MetalLabelUI

.

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

Methods declared in class javax.swing.plaf.basic.

BasicLabelUI

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

layoutCL

,

paint

,

paintEnabledText

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicLabelUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getPreferredSize

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

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

============ FIELD DETAIL ===========

- Field Detail

- metalLabelUI

```java
protected static
MetalLabelUI
metalLabelUI
```

The default

MetalLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalLabelUI

```java
public MetalLabelUI()
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

MetalLabelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalLabelUI

- paintDisabledText

```java
protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

**Overrides:** paintDisabledText

in class

BasicLabelUI
**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** BasicLabelUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

BasicLabelUI.paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

Field Detail

- metalLabelUI

```java
protected static
MetalLabelUI
metalLabelUI
```

The default

MetalLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

---

#### Field Detail

metalLabelUI

```java
protected static
MetalLabelUI
metalLabelUI
```

The default

MetalLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

---

#### metalLabelUI

protected static

MetalLabelUI

metalLabelUI

The default

MetalLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

Constructor Detail

- MetalLabelUI

```java
public MetalLabelUI()
```

---

#### Constructor Detail

MetalLabelUI

```java
public MetalLabelUI()
```

---

#### MetalLabelUI

public MetalLabelUI()

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

MetalLabelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalLabelUI

- paintDisabledText

```java
protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

**Overrides:** paintDisabledText

in class

BasicLabelUI
**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** BasicLabelUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

BasicLabelUI.paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

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

MetalLabelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalLabelUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns an instance of

MetalLabelUI

.

paintDisabledText

```java
protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

**Overrides:** paintDisabledText

in class

BasicLabelUI
**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** BasicLabelUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

BasicLabelUI.paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

---

#### paintDisabledText

protected void paintDisabledText​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Just paint the text gray (Label.disabledForeground) rather than
in the labels foreground color.

---

