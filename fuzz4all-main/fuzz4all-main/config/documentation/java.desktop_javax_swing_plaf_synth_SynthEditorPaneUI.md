# Class SynthEditorPaneUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthEditorPaneUI.html`

### Class Description

```java
public class
SynthEditorPaneUI

extends
BasicEditorPaneUI

implements
SynthUI
```

Provides the Synth L&F UI delegate for

JEditorPane

.

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthEditorPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a new UI object for the given component.

**Parameters:**
- c

- component to create UI object for

**Returns:**
- the UI object

---

#### protected void propertyChange​(
PropertyChangeEvent
evt)

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the ActionMap based upon an
EditorKit change.

**Overrides:**
- propertyChange

in class

BasicEditorPaneUI

**Parameters:**
- evt

- the property change event

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

BasicTextUI

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

### Additional Sections

#### Class SynthEditorPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI

javax.swing.plaf.basic.BasicEditorPaneUI

- javax.swing.plaf.synth.SynthEditorPaneUI

javax.swing.plaf.synth.SynthEditorPaneUI

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

**Direct Known Subclasses:** SynthTextPaneUI

```java
public class
SynthEditorPaneUI

extends
BasicEditorPaneUI

implements
SynthUI
```

Provides the Synth L&F UI delegate for

JEditorPane

.

**Since:** 1.7

public class

SynthEditorPaneUI

extends

BasicEditorPaneUI

implements

SynthUI

Provides the Synth L&F UI delegate for

JEditorPane

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTextUI

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

=========== FIELD SUMMARY ===========

- Field Summary

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

SynthEditorPaneUI

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

Creates a new UI object for the given component.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

,

getPropertyPrefix

,

installUI

,

uninstallUI

- Methods declared in class javax.swing.plaf.basic.

BasicTextUI

create

,

create

,

createCaret

,

createHighlighter

,

createKeymap

,

damageRange

,

damageRange

,

getComponent

,

getKeymapName

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

getRootView

,

getToolTipText

,

getVisibleEditorRect

,

installDefaults

,

installKeyboardActions

,

installListeners

,

modelChanged

,

modelToView

,

modelToView

,

paint

,

paintBackground

,

paintSafely

,

setView

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

viewToModel

,

viewToModel

- Methods declared in class javax.swing.plaf.

TextUI

getNextVisualPositionFrom

,

getToolTipText2D

,

modelToView2D

,

viewToModel2D

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

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTextUI

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTextUI

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicTextUI

Field Summary

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

SynthEditorPaneUI

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

Creates a new UI object for the given component.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

,

getPropertyPrefix

,

installUI

,

uninstallUI

- Methods declared in class javax.swing.plaf.basic.

BasicTextUI

create

,

create

,

createCaret

,

createHighlighter

,

createKeymap

,

damageRange

,

damageRange

,

getComponent

,

getKeymapName

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

getRootView

,

getToolTipText

,

getVisibleEditorRect

,

installDefaults

,

installKeyboardActions

,

installListeners

,

modelChanged

,

modelToView

,

modelToView

,

paint

,

paintBackground

,

paintSafely

,

setView

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

viewToModel

,

viewToModel

- Methods declared in class javax.swing.plaf.

TextUI

getNextVisualPositionFrom

,

getToolTipText2D

,

modelToView2D

,

viewToModel2D

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

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Method Summary

Creates a new UI object for the given component.

Paints the specified component.

This method gets called when a bound property is changed
on the associated JTextComponent.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

,

getPropertyPrefix

,

installUI

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf.basic. BasicEditorPaneUI

Methods declared in class javax.swing.plaf.basic.

BasicTextUI

create

,

create

,

createCaret

,

createHighlighter

,

createKeymap

,

damageRange

,

damageRange

,

getComponent

,

getKeymapName

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

getRootView

,

getToolTipText

,

getVisibleEditorRect

,

installDefaults

,

installKeyboardActions

,

installListeners

,

modelChanged

,

modelToView

,

modelToView

,

paint

,

paintBackground

,

paintSafely

,

setView

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

viewToModel

,

viewToModel

---

#### Methods declared in class javax.swing.plaf.basic. BasicTextUI

Methods declared in class javax.swing.plaf.

TextUI

getNextVisualPositionFrom

,

getToolTipText2D

,

modelToView2D

,

viewToModel2D

---

#### Methods declared in class javax.swing.plaf. TextUI

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

Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthEditorPaneUI

```java
public SynthEditorPaneUI()
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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- propertyChange

```java
protected void propertyChange​(
PropertyChangeEvent
evt)
```

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the ActionMap based upon an
EditorKit change.

**Overrides:** propertyChange

in class

BasicEditorPaneUI
**Parameters:** evt

- the property change event

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

BasicTextUI
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

Constructor Detail

- SynthEditorPaneUI

```java
public SynthEditorPaneUI()
```

---

#### Constructor Detail

SynthEditorPaneUI

```java
public SynthEditorPaneUI()
```

---

#### SynthEditorPaneUI

public SynthEditorPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- propertyChange

```java
protected void propertyChange​(
PropertyChangeEvent
evt)
```

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the ActionMap based upon an
EditorKit change.

**Overrides:** propertyChange

in class

BasicEditorPaneUI
**Parameters:** evt

- the property change event

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

BasicTextUI
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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a new UI object for the given component.

propertyChange

```java
protected void propertyChange​(
PropertyChangeEvent
evt)
```

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the ActionMap based upon an
EditorKit change.

**Overrides:** propertyChange

in class

BasicEditorPaneUI
**Parameters:** evt

- the property change event

---

#### propertyChange

protected void propertyChange​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the ActionMap based upon an
EditorKit change.

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

BasicTextUI
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

---

