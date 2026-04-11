# Class SynthTextPaneUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthTextPaneUI.html`

### Class Description

```java
public class
SynthTextPaneUI

extends
SynthEditorPaneUI
```

Provides the look and feel for a styled text editor in the
Synth look and feel.

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

#### public SynthTextPaneUI()

*No description found.*

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
- the UI object

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

#### public void installUI​(
JComponent
c)

Installs the UI for a component. This does the following
things.

- Sets opaqueness of the associated component according to its style,
if the opaque property has not already been set by the client program.

Installs the default caret and highlighter into the
associated component. These properties are only set if their
current value is either

null

or an instance of

UIResource

.

Attaches to the editor and model. If there is no
model, a default one is created.

Creates the view factory and the view hierarchy used
to represent the model.

**Overrides:**
- installUI

in class

BasicEditorPaneUI

**Parameters:**
- c

- the editor component

**See Also:**
- BasicTextUI.installUI(javax.swing.JComponent)

,

ComponentUI.installUI(javax.swing.JComponent)

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

SynthEditorPaneUI

**Parameters:**
- evt

- the property change event

---

### Additional Sections

#### Class SynthTextPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI
- - javax.swing.plaf.synth.SynthTextPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI
- - javax.swing.plaf.synth.SynthTextPaneUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI
- - javax.swing.plaf.synth.SynthTextPaneUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicEditorPaneUI
- - javax.swing.plaf.synth.SynthEditorPaneUI
- - javax.swing.plaf.synth.SynthTextPaneUI

javax.swing.plaf.basic.BasicEditorPaneUI

- javax.swing.plaf.synth.SynthEditorPaneUI
- - javax.swing.plaf.synth.SynthTextPaneUI

javax.swing.plaf.synth.SynthEditorPaneUI

- javax.swing.plaf.synth.SynthTextPaneUI

javax.swing.plaf.synth.SynthTextPaneUI

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

```java
public class
SynthTextPaneUI

extends
SynthEditorPaneUI
```

Provides the look and feel for a styled text editor in the
Synth look and feel.

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

SynthTextPaneUI

extends

SynthEditorPaneUI

Provides the look and feel for a styled text editor in the
Synth look and feel.

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

SynthTextPaneUI

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

Creates a UI for the JTextPane.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

void

installUI

​(

JComponent

c)

Installs the UI for a component.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

- Methods declared in class javax.swing.plaf.synth.

SynthEditorPaneUI

paint

,

update

- Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

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

SynthTextPaneUI

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

Creates a UI for the JTextPane.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

void

installUI

​(

JComponent

c)

Installs the UI for a component.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

- Methods declared in class javax.swing.plaf.synth.

SynthEditorPaneUI

paint

,

update

- Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

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

Creates a UI for the JTextPane.

Fetches the name used as a key to lookup properties through the
UIManager.

Installs the UI for a component.

This method gets called when a bound property is changed
on the associated JTextComponent.

Methods declared in class javax.swing.plaf.synth.

SynthEditorPaneUI

paint

,

update

---

#### Methods declared in class javax.swing.plaf.synth. SynthEditorPaneUI

Methods declared in class javax.swing.plaf.basic.

BasicEditorPaneUI

getEditorKit

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

- SynthTextPaneUI

```java
public SynthTextPaneUI()
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

Creates a UI for the JTextPane.

**Parameters:** c

- the JTextPane object
**Returns:** the UI object

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

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI for a component. This does the following
things.

- Sets opaqueness of the associated component according to its style,
if the opaque property has not already been set by the client program.

Installs the default caret and highlighter into the
associated component. These properties are only set if their
current value is either

null

or an instance of

UIResource

.

Attaches to the editor and model. If there is no
model, a default one is created.

Creates the view factory and the view hierarchy used
to represent the model.

**Overrides:** installUI

in class

BasicEditorPaneUI
**Parameters:** c

- the editor component
**See Also:** BasicTextUI.installUI(javax.swing.JComponent)

,

ComponentUI.installUI(javax.swing.JComponent)

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

SynthEditorPaneUI
**Parameters:** evt

- the property change event

Constructor Detail

- SynthTextPaneUI

```java
public SynthTextPaneUI()
```

---

#### Constructor Detail

SynthTextPaneUI

```java
public SynthTextPaneUI()
```

---

#### SynthTextPaneUI

public SynthTextPaneUI()

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
**Returns:** the UI object

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

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI for a component. This does the following
things.

- Sets opaqueness of the associated component according to its style,
if the opaque property has not already been set by the client program.

Installs the default caret and highlighter into the
associated component. These properties are only set if their
current value is either

null

or an instance of

UIResource

.

Attaches to the editor and model. If there is no
model, a default one is created.

Creates the view factory and the view hierarchy used
to represent the model.

**Overrides:** installUI

in class

BasicEditorPaneUI
**Parameters:** c

- the editor component
**See Also:** BasicTextUI.installUI(javax.swing.JComponent)

,

ComponentUI.installUI(javax.swing.JComponent)

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

SynthEditorPaneUI
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
**Returns:** the UI object

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

installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI for a component. This does the following
things.

- Sets opaqueness of the associated component according to its style,
if the opaque property has not already been set by the client program.

Installs the default caret and highlighter into the
associated component. These properties are only set if their
current value is either

null

or an instance of

UIResource

.

Attaches to the editor and model. If there is no
model, a default one is created.

Creates the view factory and the view hierarchy used
to represent the model.

**Overrides:** installUI

in class

BasicEditorPaneUI
**Parameters:** c

- the editor component
**See Also:** BasicTextUI.installUI(javax.swing.JComponent)

,

ComponentUI.installUI(javax.swing.JComponent)

---

#### installUI

public void installUI​(

JComponent

c)

Installs the UI for a component. This does the following
things.

- Sets opaqueness of the associated component according to its style,
if the opaque property has not already been set by the client program.

Installs the default caret and highlighter into the
associated component. These properties are only set if their
current value is either

null

or an instance of

UIResource

.

Attaches to the editor and model. If there is no
model, a default one is created.

Creates the view factory and the view hierarchy used
to represent the model.

Sets opaqueness of the associated component according to its style,
if the opaque property has not already been set by the client program.

Installs the default caret and highlighter into the
associated component. These properties are only set if their
current value is either

null

or an instance of

UIResource

.

Attaches to the editor and model. If there is no
model, a default one is created.

Creates the view factory and the view hierarchy used
to represent the model.

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

SynthEditorPaneUI
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

