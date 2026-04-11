# Class SynthFormattedTextFieldUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthFormattedTextFieldUI.html`

### Class Description

```java
public class
SynthFormattedTextFieldUI

extends
SynthTextFieldUI
```

Provides the Synth L&F UI delegate for

JFormattedTextField

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

#### public SynthFormattedTextFieldUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a UI for a JFormattedTextField.

**Parameters:**
- c

- the formatted text field

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

BasicTextFieldUI

**Returns:**
- the name "FormattedTextField"

---

### Additional Sections

#### Class SynthFormattedTextFieldUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthFormattedTextFieldUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthFormattedTextFieldUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthFormattedTextFieldUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthFormattedTextFieldUI

javax.swing.plaf.basic.BasicTextFieldUI

- javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthFormattedTextFieldUI

javax.swing.plaf.synth.SynthTextFieldUI

- javax.swing.plaf.synth.SynthFormattedTextFieldUI

javax.swing.plaf.synth.SynthFormattedTextFieldUI

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

```java
public class
SynthFormattedTextFieldUI

extends
SynthTextFieldUI
```

Provides the Synth L&F UI delegate for

JFormattedTextField

.

**Since:** 1.7

public class

SynthFormattedTextFieldUI

extends

SynthTextFieldUI

Provides the Synth L&F UI delegate for

JFormattedTextField

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

SynthFormattedTextFieldUI

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

Creates a UI for a JFormattedTextField.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

- Methods declared in class javax.swing.plaf.synth.

SynthTextFieldUI

paint

,

paintBackground

,

propertyChange

,

update

- Methods declared in class javax.swing.plaf.basic.

BasicTextFieldUI

create

,

getBaseline

,

getBaselineResizeBehavior

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

SynthFormattedTextFieldUI

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

Creates a UI for a JFormattedTextField.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

- Methods declared in class javax.swing.plaf.synth.

SynthTextFieldUI

paint

,

paintBackground

,

propertyChange

,

update

- Methods declared in class javax.swing.plaf.basic.

BasicTextFieldUI

create

,

getBaseline

,

getBaselineResizeBehavior

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

Creates a UI for a JFormattedTextField.

Fetches the name used as a key to lookup properties through the
UIManager.

Methods declared in class javax.swing.plaf.synth.

SynthTextFieldUI

paint

,

paintBackground

,

propertyChange

,

update

---

#### Methods declared in class javax.swing.plaf.synth. SynthTextFieldUI

Methods declared in class javax.swing.plaf.basic.

BasicTextFieldUI

create

,

getBaseline

,

getBaselineResizeBehavior

---

#### Methods declared in class javax.swing.plaf.basic. BasicTextFieldUI

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

- SynthFormattedTextFieldUI

```java
public SynthFormattedTextFieldUI()
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

Creates a UI for a JFormattedTextField.

**Parameters:** c

- the formatted text field
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

BasicTextFieldUI
**Returns:** the name "FormattedTextField"

Constructor Detail

- SynthFormattedTextFieldUI

```java
public SynthFormattedTextFieldUI()
```

---

#### Constructor Detail

SynthFormattedTextFieldUI

```java
public SynthFormattedTextFieldUI()
```

---

#### SynthFormattedTextFieldUI

public SynthFormattedTextFieldUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a UI for a JFormattedTextField.

**Parameters:** c

- the formatted text field
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

BasicTextFieldUI
**Returns:** the name "FormattedTextField"

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

Creates a UI for a JFormattedTextField.

**Parameters:** c

- the formatted text field
**Returns:** the UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a UI for a JFormattedTextField.

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

BasicTextFieldUI
**Returns:** the name "FormattedTextField"

---

#### getPropertyPrefix

protected

String

getPropertyPrefix()

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

---

