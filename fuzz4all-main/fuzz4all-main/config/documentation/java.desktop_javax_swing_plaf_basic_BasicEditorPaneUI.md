# Class BasicEditorPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicEditorPaneUI.html`

### Class Description

```java
public class
BasicEditorPaneUI

extends
BasicTextUI
```

Provides the look and feel for a JEditorPane.

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

#### public BasicEditorPaneUI()

Creates a new BasicEditorPaneUI.

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

- the JTextPane component

**Returns:**
- the UI

---

#### protected
String
getPropertyPrefix()

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:**
- getPropertyPrefix

in class

BasicTextUI

**Returns:**
- the name ("EditorPane")

---

#### public void installUI​(
JComponent
c)

Installs the UI for a component. This does the following
things.

- Sets the associated component to opaque if the opaque property
has not already been set by the client program. This will cause the
component's background color to be painted.

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

BasicTextUI

**Parameters:**
- c

- the editor component

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

**Since:**
- 1.5

---

#### public void uninstallUI​(
JComponent
c)

Deinstalls the UI for a component. This removes the listeners,
uninstalls the highlighter, removes views, and nulls out the keymap.

**Overrides:**
- uninstallUI

in class

BasicTextUI

**Parameters:**
- c

- the editor component

**See Also:**
- ComponentUI.uninstallUI(javax.swing.JComponent)

**Since:**
- 1.5

---

#### public
EditorKit
getEditorKit​(
JTextComponent
tc)

Fetches the EditorKit for the UI. This is whatever is
currently set in the associated JEditorPane.

**Overrides:**
- getEditorKit

in class

BasicTextUI

**Parameters:**
- tc

- the text component for which this UI is installed

**Returns:**
- the editor capabilities

**See Also:**
- TextUI.getEditorKit(javax.swing.text.JTextComponent)

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

BasicTextUI

**Parameters:**
- evt

- the property change event

---

### Additional Sections

#### Class BasicEditorPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicEditorPaneUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicEditorPaneUI

javax.swing.plaf.basic.BasicEditorPaneUI

**All Implemented Interfaces:** ViewFactory

**Direct Known Subclasses:** BasicTextPaneUI

,

SynthEditorPaneUI

```java
public class
BasicEditorPaneUI

extends
BasicTextUI
```

Provides the look and feel for a JEditorPane.

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

BasicEditorPaneUI

extends

BasicTextUI

Provides the look and feel for a JEditorPane.

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

BasicEditorPaneUI

()

Creates a new BasicEditorPaneUI.

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

EditorKit

getEditorKit

​(

JTextComponent

tc)

Fetches the EditorKit for the UI.

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

void

uninstallUI

​(

JComponent

c)

Deinstalls the UI for a component.

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

BasicEditorPaneUI

()

Creates a new BasicEditorPaneUI.

---

#### Constructor Summary

Creates a new BasicEditorPaneUI.

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

EditorKit

getEditorKit

​(

JTextComponent

tc)

Fetches the EditorKit for the UI.

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

void

uninstallUI

​(

JComponent

c)

Deinstalls the UI for a component.

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

Fetches the EditorKit for the UI.

Fetches the name used as a key to lookup properties through the
UIManager.

Installs the UI for a component.

This method gets called when a bound property is changed
on the associated JTextComponent.

Deinstalls the UI for a component.

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

- BasicEditorPaneUI

```java
public BasicEditorPaneUI()
```

Creates a new BasicEditorPaneUI.

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

- the JTextPane component
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

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("EditorPane")

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI for a component. This does the following
things.

- Sets the associated component to opaque if the opaque property
has not already been set by the client program. This will cause the
component's background color to be painted.

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

BasicTextUI
**Parameters:** c

- the editor component
**Since:** 1.5
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Deinstalls the UI for a component. This removes the listeners,
uninstalls the highlighter, removes views, and nulls out the keymap.

**Overrides:** uninstallUI

in class

BasicTextUI
**Parameters:** c

- the editor component
**Since:** 1.5
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

- getEditorKit

```java
public
EditorKit
getEditorKit​(
JTextComponent
tc)
```

Fetches the EditorKit for the UI. This is whatever is
currently set in the associated JEditorPane.

**Overrides:** getEditorKit

in class

BasicTextUI
**Parameters:** tc

- the text component for which this UI is installed
**Returns:** the editor capabilities
**See Also:** TextUI.getEditorKit(javax.swing.text.JTextComponent)

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

BasicTextUI
**Parameters:** evt

- the property change event

Constructor Detail

- BasicEditorPaneUI

```java
public BasicEditorPaneUI()
```

Creates a new BasicEditorPaneUI.

---

#### Constructor Detail

BasicEditorPaneUI

```java
public BasicEditorPaneUI()
```

Creates a new BasicEditorPaneUI.

---

#### BasicEditorPaneUI

public BasicEditorPaneUI()

Creates a new BasicEditorPaneUI.

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

- the JTextPane component
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

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("EditorPane")

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI for a component. This does the following
things.

- Sets the associated component to opaque if the opaque property
has not already been set by the client program. This will cause the
component's background color to be painted.

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

BasicTextUI
**Parameters:** c

- the editor component
**Since:** 1.5
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Deinstalls the UI for a component. This removes the listeners,
uninstalls the highlighter, removes views, and nulls out the keymap.

**Overrides:** uninstallUI

in class

BasicTextUI
**Parameters:** c

- the editor component
**Since:** 1.5
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

- getEditorKit

```java
public
EditorKit
getEditorKit​(
JTextComponent
tc)
```

Fetches the EditorKit for the UI. This is whatever is
currently set in the associated JEditorPane.

**Overrides:** getEditorKit

in class

BasicTextUI
**Parameters:** tc

- the text component for which this UI is installed
**Returns:** the editor capabilities
**See Also:** TextUI.getEditorKit(javax.swing.text.JTextComponent)

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

BasicTextUI
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

- the JTextPane component
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

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("EditorPane")

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

- Sets the associated component to opaque if the opaque property
has not already been set by the client program. This will cause the
component's background color to be painted.

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

BasicTextUI
**Parameters:** c

- the editor component
**Since:** 1.5
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

---

#### installUI

public void installUI​(

JComponent

c)

Installs the UI for a component. This does the following
things.

- Sets the associated component to opaque if the opaque property
has not already been set by the client program. This will cause the
component's background color to be painted.

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

Sets the associated component to opaque if the opaque property
has not already been set by the client program. This will cause the
component's background color to be painted.

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

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Deinstalls the UI for a component. This removes the listeners,
uninstalls the highlighter, removes views, and nulls out the keymap.

**Overrides:** uninstallUI

in class

BasicTextUI
**Parameters:** c

- the editor component
**Since:** 1.5
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Deinstalls the UI for a component. This removes the listeners,
uninstalls the highlighter, removes views, and nulls out the keymap.

getEditorKit

```java
public
EditorKit
getEditorKit​(
JTextComponent
tc)
```

Fetches the EditorKit for the UI. This is whatever is
currently set in the associated JEditorPane.

**Overrides:** getEditorKit

in class

BasicTextUI
**Parameters:** tc

- the text component for which this UI is installed
**Returns:** the editor capabilities
**See Also:** TextUI.getEditorKit(javax.swing.text.JTextComponent)

---

#### getEditorKit

public

EditorKit

getEditorKit​(

JTextComponent

tc)

Fetches the EditorKit for the UI. This is whatever is
currently set in the associated JEditorPane.

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

BasicTextUI
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

---

