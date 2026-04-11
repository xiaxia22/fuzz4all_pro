# Class SynthProgressBarUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthProgressBarUI.html`

### Class Description

```java
public class
SynthProgressBarUI

extends
BasicProgressBarUI

implements
SynthUI
,
PropertyChangeListener
```

Provides the Synth L&F UI delegate for

JProgressBar

.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthProgressBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates a new UI object for the given component.

**Parameters:**
- x

- component to create UI object for

**Returns:**
- the UI object

---

#### public void update​(
Graphics
g,

JComponent
c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:**
- paint

in class

BasicProgressBarUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### protected void paint​(
SynthContext
context,

Graphics
g)

Paints the specified component.

**Parameters:**
- context

- context for the component being painted
- g

- the

Graphics

object used for painting

**See Also:**
- update(Graphics,JComponent)

---

#### protected void paintText​(
SynthContext
context,

Graphics
g,

String
title)

Paints the component's text.

**Parameters:**
- context

- context for the component being painted
- g

-

Graphics

object used for painting
- title

- the text to paint

---

### Additional Sections

#### Class SynthProgressBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ProgressBarUI
- - javax.swing.plaf.basic.BasicProgressBarUI
- - javax.swing.plaf.synth.SynthProgressBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ProgressBarUI
- - javax.swing.plaf.basic.BasicProgressBarUI
- - javax.swing.plaf.synth.SynthProgressBarUI

javax.swing.plaf.ProgressBarUI

- javax.swing.plaf.basic.BasicProgressBarUI
- - javax.swing.plaf.synth.SynthProgressBarUI

javax.swing.plaf.basic.BasicProgressBarUI

- javax.swing.plaf.synth.SynthProgressBarUI

javax.swing.plaf.synth.SynthProgressBarUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthProgressBarUI

extends
BasicProgressBarUI

implements
SynthUI
,
PropertyChangeListener
```

Provides the Synth L&F UI delegate for

JProgressBar

.

**Since:** 1.7

public class

SynthProgressBarUI

extends

BasicProgressBarUI

implements

SynthUI

,

PropertyChangeListener

Provides the Synth L&F UI delegate for

JProgressBar

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

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthProgressBarUI

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

x)

Creates a new UI object for the given component.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

paintText

​(

SynthContext

context,

Graphics

g,

String

title)

Paints the component's text.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

paintDeterminate

,

paintIndeterminate

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

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

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

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

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

Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Fields declared in interface javax.swing.plaf.synth. SynthConstants

Constructor Summary

Constructors

Constructor

Description

SynthProgressBarUI

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

x)

Creates a new UI object for the given component.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

paintText

​(

SynthContext

context,

Graphics

g,

String

title)

Paints the component's text.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

paintDeterminate

,

paintIndeterminate

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

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Method Summary

Creates a new UI object for the given component.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Paints the component's text.

Notifies this UI delegate to repaint the specified component.

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

paintDeterminate

,

paintIndeterminate

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

Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthProgressBarUI

```java
public SynthProgressBarUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new UI object for the given component.

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

BasicProgressBarUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintText

```java
protected void paintText​(
SynthContext
context,

Graphics
g,

String
title)
```

Paints the component's text.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** title

- the text to paint

Constructor Detail

- SynthProgressBarUI

```java
public SynthProgressBarUI()
```

---

#### Constructor Detail

SynthProgressBarUI

```java
public SynthProgressBarUI()
```

---

#### SynthProgressBarUI

public SynthProgressBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new UI object for the given component.

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

BasicProgressBarUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintText

```java
protected void paintText​(
SynthContext
context,

Graphics
g,

String
title)
```

Paints the component's text.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** title

- the text to paint

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new UI object for the given component.

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Creates a new UI object for the given component.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

BasicProgressBarUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

---

#### paint

protected void paint​(

SynthContext

context,

Graphics

g)

Paints the specified component.

paintText

```java
protected void paintText​(
SynthContext
context,

Graphics
g,

String
title)
```

Paints the component's text.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** title

- the text to paint

---

#### paintText

protected void paintText​(

SynthContext

context,

Graphics

g,

String

title)

Paints the component's text.

---

