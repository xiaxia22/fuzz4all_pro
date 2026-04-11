# Class BasicFormattedTextFieldUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicFormattedTextFieldUI.html`

### Class Description

```java
public class
BasicFormattedTextFieldUI

extends
BasicTextFieldUI
```

Provides the look and feel implementation for

JFormattedTextField

.

**All Implemented Interfaces:** ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicFormattedTextFieldUI()

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

#### Class BasicFormattedTextFieldUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicFormattedTextFieldUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicFormattedTextFieldUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicFormattedTextFieldUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicFormattedTextFieldUI

javax.swing.plaf.basic.BasicTextFieldUI

- javax.swing.plaf.basic.BasicFormattedTextFieldUI

javax.swing.plaf.basic.BasicFormattedTextFieldUI

**All Implemented Interfaces:** ViewFactory

```java
public class
BasicFormattedTextFieldUI

extends
BasicTextFieldUI
```

Provides the look and feel implementation for

JFormattedTextField

.

**Since:** 1.4

public class

BasicFormattedTextFieldUI

extends

BasicTextFieldUI

Provides the look and feel implementation for

JFormattedTextField

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

BasicFormattedTextFieldUI

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

paintBackground

,

paintSafely

,

propertyChange

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

BasicFormattedTextFieldUI

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

paintBackground

,

paintSafely

,

propertyChange

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

Creates a UI for a JFormattedTextField.

Fetches the name used as a key to lookup properties through the
UIManager.

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

paintBackground

,

paintSafely

,

propertyChange

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

- BasicFormattedTextFieldUI

```java
public BasicFormattedTextFieldUI()
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

- BasicFormattedTextFieldUI

```java
public BasicFormattedTextFieldUI()
```

---

#### Constructor Detail

BasicFormattedTextFieldUI

```java
public BasicFormattedTextFieldUI()
```

---

#### BasicFormattedTextFieldUI

public BasicFormattedTextFieldUI()

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

