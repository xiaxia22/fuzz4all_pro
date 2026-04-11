# Class BasicTextPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicTextPaneUI.html`

### Class Description

```java
public class
BasicTextPaneUI

extends
BasicEditorPaneUI
```

Provides the look and feel for a styled text editor.

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

**All Implemented Interfaces:** ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicTextPaneUI()

Creates a new BasicTextPaneUI.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a UI for the JTextPane.

**Parameters:**
- c

- the JTextPane object

**Returns:**
- the UI

---

#### protected
String
getPropertyPrefix()

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Overrides:**
- getPropertyPrefix

in class

BasicEditorPaneUI

**Returns:**
- the name ("TextPane")

---

#### protected void propertyChange​(
PropertyChangeEvent
evt)

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
If the font, foreground or document has changed, the
the appropriate property is set in the default style of
the document.

**Overrides:**
- propertyChange

in class

BasicEditorPaneUI

**Parameters:**
- evt

- the property change event

---

### Additional Sections

#### Class BasicTextPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.basic.BasicTextPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.basic.BasicTextPaneUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.basic.BasicTextPaneUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.basic.BasicTextPaneUI

javax.swing.plaf.basic.BasicEditorPaneUI

- javax.swing.plaf.basic.BasicTextPaneUI

javax.swing.plaf.basic.BasicTextPaneUI

**All Implemented Interfaces:** ViewFactory

```java
public class
BasicTextPaneUI

extends
BasicEditorPaneUI
```

Provides the look and feel for a styled text editor.

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

BasicTextPaneUI

extends

BasicEditorPaneUI

Provides the look and feel for a styled text editor.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicTextPaneUI

()

Creates a new BasicTextPaneUI.

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

Creates a UI for the JTextPane.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

- Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

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

update

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

Constructor Summary

Constructors

Constructor

Description

BasicTextPaneUI

()

Creates a new BasicTextPaneUI.

---

#### Constructor Summary

Creates a new BasicTextPaneUI.

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

Creates a UI for the JTextPane.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

- Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

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

update

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

---

#### Method Summary

Creates a UI for the JTextPane.

Fetches the name used as a key to lookup properties through the
UIManager.

This method gets called when a bound property is changed
on the associated JTextComponent.

Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

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

update

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicTextPaneUI

```java
public BasicTextPaneUI()
```

Creates a new BasicTextPaneUI.

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

Creates a UI for the JTextPane.

**Parameters:** c

- the JTextPane object
**Returns:** the UI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Overrides:** getPropertyPrefix

in class

BasicEditorPaneUI
**Returns:** the name ("TextPane")

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
If the font, foreground or document has changed, the
the appropriate property is set in the default style of
the document.

**Overrides:** propertyChange

in class

BasicEditorPaneUI
**Parameters:** evt

- the property change event

Constructor Detail

- BasicTextPaneUI

```java
public BasicTextPaneUI()
```

Creates a new BasicTextPaneUI.

---

#### Constructor Detail

BasicTextPaneUI

```java
public BasicTextPaneUI()
```

Creates a new BasicTextPaneUI.

---

#### BasicTextPaneUI

public BasicTextPaneUI()

Creates a new BasicTextPaneUI.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a UI for the JTextPane.

**Parameters:** c

- the JTextPane object
**Returns:** the UI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Overrides:** getPropertyPrefix

in class

BasicEditorPaneUI
**Returns:** the name ("TextPane")

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
If the font, foreground or document has changed, the
the appropriate property is set in the default style of
the document.

**Overrides:** propertyChange

in class

BasicEditorPaneUI
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
c)
```

Creates a UI for the JTextPane.

**Parameters:** c

- the JTextPane object
**Returns:** the UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a UI for the JTextPane.

getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Overrides:** getPropertyPrefix

in class

BasicEditorPaneUI
**Returns:** the name ("TextPane")

---

#### getPropertyPrefix

protected

String

getPropertyPrefix()

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

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
If the font, foreground or document has changed, the
the appropriate property is set in the default style of
the document.

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
If the font, foreground or document has changed, the
the appropriate property is set in the default style of
the document.

---

