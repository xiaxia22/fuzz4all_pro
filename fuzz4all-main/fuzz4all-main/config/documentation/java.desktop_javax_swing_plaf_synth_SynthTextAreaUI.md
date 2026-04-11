# Class SynthTextAreaUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthTextAreaUI.html`

### Class Description

```java
public class
SynthTextAreaUI

extends
BasicTextAreaUI

implements
SynthUI
```

Provides the look and feel for a plain text editor in the
Synth look and feel. In this implementation the default UI
is extended to act as a simple view factory.

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

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthTextAreaUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
ta)

Creates a UI object for a JTextArea.

**Parameters:**
- ta

- a text area

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

#### protected void paintBackground​(
Graphics
g)

Paints a background for the view. This will only be
called if isOpaque() on the associated component is
true. The default is to paint the background color
of the component.

Overridden to do nothing.

**Overrides:**
- paintBackground

in class

BasicTextUI

**Parameters:**
- g

- the graphics context

---

#### protected void propertyChange​(
PropertyChangeEvent
evt)

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:**
- propertyChange

in class

BasicTextAreaUI

**Parameters:**
- evt

- the property change event

---

### Additional Sections

#### Class SynthTextAreaUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextAreaUI
- - javax.swing.plaf.synth.SynthTextAreaUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextAreaUI
- - javax.swing.plaf.synth.SynthTextAreaUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextAreaUI
- - javax.swing.plaf.synth.SynthTextAreaUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicTextAreaUI
- - javax.swing.plaf.synth.SynthTextAreaUI

javax.swing.plaf.basic.BasicTextAreaUI

- javax.swing.plaf.synth.SynthTextAreaUI

javax.swing.plaf.synth.SynthTextAreaUI

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

```java
public class
SynthTextAreaUI

extends
BasicTextAreaUI

implements
SynthUI
```

Provides the look and feel for a plain text editor in the
Synth look and feel. In this implementation the default UI
is extended to act as a simple view factory.

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

**Since:** 1.7

public class

SynthTextAreaUI

extends

BasicTextAreaUI

implements

SynthUI

Provides the look and feel for a plain text editor in the
Synth look and feel. In this implementation the default UI
is extended to act as a simple view factory.

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

SynthTextAreaUI

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

ta)

Creates a UI object for a JTextArea.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

paintBackground

​(

Graphics

g)

Paints a background for the view.

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

BasicTextAreaUI

create

,

getBaseline

,

getBaselineResizeBehavior

,

getMinimumSize

,

getPreferredSize

,

getPropertyPrefix

- Methods declared in class javax.swing.plaf.basic.

BasicTextUI

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

getEditorKit

,

getKeymapName

,

getMaximumSize

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

installUI

,

modelChanged

,

modelToView

,

modelToView

,

paint

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

uninstallUI

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

SynthTextAreaUI

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

ta)

Creates a UI object for a JTextArea.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

paintBackground

​(

Graphics

g)

Paints a background for the view.

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

BasicTextAreaUI

create

,

getBaseline

,

getBaselineResizeBehavior

,

getMinimumSize

,

getPreferredSize

,

getPropertyPrefix

- Methods declared in class javax.swing.plaf.basic.

BasicTextUI

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

getEditorKit

,

getKeymapName

,

getMaximumSize

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

installUI

,

modelChanged

,

modelToView

,

modelToView

,

paint

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

uninstallUI

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

Creates a UI object for a JTextArea.

Paints the specified component.

Paints a background for the view.

This method gets called when a bound property is changed
on the associated JTextComponent.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicTextAreaUI

create

,

getBaseline

,

getBaselineResizeBehavior

,

getMinimumSize

,

getPreferredSize

,

getPropertyPrefix

---

#### Methods declared in class javax.swing.plaf.basic. BasicTextAreaUI

Methods declared in class javax.swing.plaf.basic.

BasicTextUI

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

getEditorKit

,

getKeymapName

,

getMaximumSize

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

installUI

,

modelChanged

,

modelToView

,

modelToView

,

paint

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

uninstallUI

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

- SynthTextAreaUI

```java
public SynthTextAreaUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
ta)
```

Creates a UI object for a JTextArea.

**Parameters:** ta

- a text area
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

- paintBackground

```java
protected void paintBackground​(
Graphics
g)
```

Paints a background for the view. This will only be
called if isOpaque() on the associated component is
true. The default is to paint the background color
of the component.

Overridden to do nothing.

**Overrides:** paintBackground

in class

BasicTextUI
**Parameters:** g

- the graphics context

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
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:** propertyChange

in class

BasicTextAreaUI
**Parameters:** evt

- the property change event

Constructor Detail

- SynthTextAreaUI

```java
public SynthTextAreaUI()
```

---

#### Constructor Detail

SynthTextAreaUI

```java
public SynthTextAreaUI()
```

---

#### SynthTextAreaUI

public SynthTextAreaUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
ta)
```

Creates a UI object for a JTextArea.

**Parameters:** ta

- a text area
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

- paintBackground

```java
protected void paintBackground​(
Graphics
g)
```

Paints a background for the view. This will only be
called if isOpaque() on the associated component is
true. The default is to paint the background color
of the component.

Overridden to do nothing.

**Overrides:** paintBackground

in class

BasicTextUI
**Parameters:** g

- the graphics context

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
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:** propertyChange

in class

BasicTextAreaUI
**Parameters:** evt

- the property change event

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
ta)
```

Creates a UI object for a JTextArea.

**Parameters:** ta

- a text area
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

ta)

Creates a UI object for a JTextArea.

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

paintBackground

```java
protected void paintBackground​(
Graphics
g)
```

Paints a background for the view. This will only be
called if isOpaque() on the associated component is
true. The default is to paint the background color
of the component.

Overridden to do nothing.

**Overrides:** paintBackground

in class

BasicTextUI
**Parameters:** g

- the graphics context

---

#### paintBackground

protected void paintBackground​(

Graphics

g)

Paints a background for the view. This will only be
called if isOpaque() on the associated component is
true. The default is to paint the background color
of the component.

Overridden to do nothing.

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
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:** propertyChange

in class

BasicTextAreaUI
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
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

---

