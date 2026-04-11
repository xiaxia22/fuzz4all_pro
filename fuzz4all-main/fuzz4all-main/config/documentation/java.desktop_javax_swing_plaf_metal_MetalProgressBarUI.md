# Class MetalProgressBarUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalProgressBarUI.html`

### Class Description

```java
public class
MetalProgressBarUI

extends
BasicProgressBarUI
```

The Metal implementation of ProgressBarUI.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalProgressBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs an instance of

MetalProgressBarUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MetalProgressBarUI

---

#### public void paintDeterminate​(
Graphics
g,

JComponent
c)

Draws a bit of special highlighting on the progress bar.
The core painting is deferred to the BasicProgressBar's

paintDeterminate

method.

**Overrides:**
- paintDeterminate

in class

BasicProgressBarUI

**Parameters:**
- g

- an instance of

Graphics
- c

- a component

**See Also:**
- BasicProgressBarUI.paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

**Since:**
- 1.4

---

#### public void paintIndeterminate​(
Graphics
g,

JComponent
c)

Draws a bit of special highlighting on the progress bar
and bouncing box.
The core painting is deferred to the BasicProgressBar's

paintIndeterminate

method.

**Overrides:**
- paintIndeterminate

in class

BasicProgressBarUI

**Parameters:**
- g

- an instance of

Graphics
- c

- a component

**See Also:**
- BasicProgressBarUI.paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

**Since:**
- 1.4

---

### Additional Sections

#### Class MetalProgressBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ProgressBarUI
- - javax.swing.plaf.basic.BasicProgressBarUI
- - javax.swing.plaf.metal.MetalProgressBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ProgressBarUI
- - javax.swing.plaf.basic.BasicProgressBarUI
- - javax.swing.plaf.metal.MetalProgressBarUI

javax.swing.plaf.ProgressBarUI

- javax.swing.plaf.basic.BasicProgressBarUI
- - javax.swing.plaf.metal.MetalProgressBarUI

javax.swing.plaf.basic.BasicProgressBarUI

- javax.swing.plaf.metal.MetalProgressBarUI

javax.swing.plaf.metal.MetalProgressBarUI

```java
public class
MetalProgressBarUI

extends
BasicProgressBarUI
```

The Metal implementation of ProgressBarUI.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

public class

MetalProgressBarUI

extends

BasicProgressBarUI

The Metal implementation of ProgressBarUI.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicProgressBarUI

BasicProgressBarUI.ChangeHandler

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicProgressBarUI

boxRect

,

changeListener

,

progressBar

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalProgressBarUI

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

Constructs an instance of

MetalProgressBarUI

.

void

paintDeterminate

​(

Graphics

g,

JComponent

c)

Draws a bit of special highlighting on the progress bar.

void

paintIndeterminate

​(

Graphics

g,

JComponent

c)

Draws a bit of special highlighting on the progress bar
and bouncing box.

- Methods declared in class javax.swing.plaf.basic.

BasicProgressBarUI

getAmountFull

,

getAnimationIndex

,

getBaseline

,

getBaselineResizeBehavior

,

getBox

,

getBoxLength

,

getCellLength

,

getCellSpacing

,

getFrameCount

,

getMinimumSize

,

getPreferredInnerHorizontal

,

getPreferredInnerVertical

,

getSelectionBackground

,

getSelectionForeground

,

getStringPlacement

,

incrementAnimationIndex

,

installDefaults

,

installListeners

,

paint

,

paintString

,

setAnimationIndex

,

setCellLength

,

setCellSpacing

,

startAnimationTimer

,

stopAnimationTimer

,

uninstallDefaults

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

getMaximumSize

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

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicProgressBarUI

BasicProgressBarUI.ChangeHandler

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicProgressBarUI

BasicProgressBarUI.ChangeHandler

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicProgressBarUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicProgressBarUI

boxRect

,

changeListener

,

progressBar

---

#### Field Summary

Fields declared in class javax.swing.plaf.basic.

BasicProgressBarUI

boxRect

,

changeListener

,

progressBar

---

#### Fields declared in class javax.swing.plaf.basic. BasicProgressBarUI

Constructor Summary

Constructors

Constructor

Description

MetalProgressBarUI

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

Constructs an instance of

MetalProgressBarUI

.

void

paintDeterminate

​(

Graphics

g,

JComponent

c)

Draws a bit of special highlighting on the progress bar.

void

paintIndeterminate

​(

Graphics

g,

JComponent

c)

Draws a bit of special highlighting on the progress bar
and bouncing box.

- Methods declared in class javax.swing.plaf.basic.

BasicProgressBarUI

getAmountFull

,

getAnimationIndex

,

getBaseline

,

getBaselineResizeBehavior

,

getBox

,

getBoxLength

,

getCellLength

,

getCellSpacing

,

getFrameCount

,

getMinimumSize

,

getPreferredInnerHorizontal

,

getPreferredInnerVertical

,

getSelectionBackground

,

getSelectionForeground

,

getStringPlacement

,

incrementAnimationIndex

,

installDefaults

,

installListeners

,

paint

,

paintString

,

setAnimationIndex

,

setCellLength

,

setCellSpacing

,

startAnimationTimer

,

stopAnimationTimer

,

uninstallDefaults

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

getMaximumSize

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

---

#### Method Summary

Constructs an instance of

MetalProgressBarUI

.

Draws a bit of special highlighting on the progress bar.

Draws a bit of special highlighting on the progress bar
and bouncing box.

Methods declared in class javax.swing.plaf.basic.

BasicProgressBarUI

getAmountFull

,

getAnimationIndex

,

getBaseline

,

getBaselineResizeBehavior

,

getBox

,

getBoxLength

,

getCellLength

,

getCellSpacing

,

getFrameCount

,

getMinimumSize

,

getPreferredInnerHorizontal

,

getPreferredInnerVertical

,

getSelectionBackground

,

getSelectionForeground

,

getStringPlacement

,

incrementAnimationIndex

,

installDefaults

,

installListeners

,

paint

,

paintString

,

setAnimationIndex

,

setCellLength

,

setCellSpacing

,

startAnimationTimer

,

stopAnimationTimer

,

uninstallDefaults

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicProgressBarUI

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalProgressBarUI

```java
public MetalProgressBarUI()
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

Constructs an instance of

MetalProgressBarUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalProgressBarUI

- paintDeterminate

```java
public void paintDeterminate​(
Graphics
g,

JComponent
c)
```

Draws a bit of special highlighting on the progress bar.
The core painting is deferred to the BasicProgressBar's

paintDeterminate

method.

**Overrides:** paintDeterminate

in class

BasicProgressBarUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** BasicProgressBarUI.paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

- paintIndeterminate

```java
public void paintIndeterminate​(
Graphics
g,

JComponent
c)
```

Draws a bit of special highlighting on the progress bar
and bouncing box.
The core painting is deferred to the BasicProgressBar's

paintIndeterminate

method.

**Overrides:** paintIndeterminate

in class

BasicProgressBarUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** BasicProgressBarUI.paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

Constructor Detail

- MetalProgressBarUI

```java
public MetalProgressBarUI()
```

---

#### Constructor Detail

MetalProgressBarUI

```java
public MetalProgressBarUI()
```

---

#### MetalProgressBarUI

public MetalProgressBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs an instance of

MetalProgressBarUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalProgressBarUI

- paintDeterminate

```java
public void paintDeterminate​(
Graphics
g,

JComponent
c)
```

Draws a bit of special highlighting on the progress bar.
The core painting is deferred to the BasicProgressBar's

paintDeterminate

method.

**Overrides:** paintDeterminate

in class

BasicProgressBarUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** BasicProgressBarUI.paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

- paintIndeterminate

```java
public void paintIndeterminate​(
Graphics
g,

JComponent
c)
```

Draws a bit of special highlighting on the progress bar
and bouncing box.
The core painting is deferred to the BasicProgressBar's

paintIndeterminate

method.

**Overrides:** paintIndeterminate

in class

BasicProgressBarUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** BasicProgressBarUI.paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

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

Constructs an instance of

MetalProgressBarUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalProgressBarUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs an instance of

MetalProgressBarUI

.

paintDeterminate

```java
public void paintDeterminate​(
Graphics
g,

JComponent
c)
```

Draws a bit of special highlighting on the progress bar.
The core painting is deferred to the BasicProgressBar's

paintDeterminate

method.

**Overrides:** paintDeterminate

in class

BasicProgressBarUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** BasicProgressBarUI.paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

---

#### paintDeterminate

public void paintDeterminate​(

Graphics

g,

JComponent

c)

Draws a bit of special highlighting on the progress bar.
The core painting is deferred to the BasicProgressBar's

paintDeterminate

method.

paintIndeterminate

```java
public void paintIndeterminate​(
Graphics
g,

JComponent
c)
```

Draws a bit of special highlighting on the progress bar
and bouncing box.
The core painting is deferred to the BasicProgressBar's

paintIndeterminate

method.

**Overrides:** paintIndeterminate

in class

BasicProgressBarUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** BasicProgressBarUI.paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

---

#### paintIndeterminate

public void paintIndeterminate​(

Graphics

g,

JComponent

c)

Draws a bit of special highlighting on the progress bar
and bouncing box.
The core painting is deferred to the BasicProgressBar's

paintIndeterminate

method.

---

