# Class StyledEditorKit.FontFamilyAction

**Source:** `java.desktop\javax\swing\text\StyledEditorKit.FontFamilyAction.html`

### Class Description

```java
public static class
StyledEditorKit.FontFamilyAction

extends
StyledEditorKit.StyledTextAction
```

An action to set the font family in the associated
JEditorPane. This will use the family specified as
the command string on the ActionEvent if there is one,
otherwise the family that was initialized with will be used.

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

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

---

### Field Details

*No entries found.*

### Constructor Details

#### public FontFamilyAction​(
String
nm,

String
family)

Creates a new FontFamilyAction.

**Parameters:**
- nm

- the action name
- family

- the font family

---

### Method Details

#### public void actionPerformed​(
ActionEvent
e)

Sets the font family.

**Parameters:**
- e

- the event

---

### Additional Sections

#### Class StyledEditorKit.FontFamilyAction

java.lang.Object

- javax.swing.AbstractAction
- - javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.StyledEditorKit.FontFamilyAction

javax.swing.AbstractAction

- javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.StyledEditorKit.FontFamilyAction

javax.swing.text.TextAction

- javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.StyledEditorKit.FontFamilyAction

javax.swing.text.StyledEditorKit.StyledTextAction

- javax.swing.text.StyledEditorKit.FontFamilyAction

javax.swing.text.StyledEditorKit.FontFamilyAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Enclosing class:** StyledEditorKit

```java
public static class
StyledEditorKit.FontFamilyAction

extends
StyledEditorKit.StyledTextAction
```

An action to set the font family in the associated
JEditorPane. This will use the family specified as
the command string on the ActionEvent if there is one,
otherwise the family that was initialized with will be used.

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

**See Also:** Serialized Form

public static class

StyledEditorKit.FontFamilyAction

extends

StyledEditorKit.StyledTextAction

An action to set the font family in the associated
JEditorPane. This will use the family specified as
the command string on the ActionEvent if there is one,
otherwise the family that was initialized with will be used.

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

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.

AbstractAction

changeSupport

,

enabled

- Fields declared in interface javax.swing.

Action

ACCELERATOR_KEY

,

ACTION_COMMAND_KEY

,

DEFAULT

,

DISPLAYED_MNEMONIC_INDEX_KEY

,

LARGE_ICON_KEY

,

LONG_DESCRIPTION

,

MNEMONIC_KEY

,

NAME

,

SELECTED_KEY

,

SHORT_DESCRIPTION

,

SMALL_ICON

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FontFamilyAction

​(

String

nm,

String

family)

Creates a new FontFamilyAction.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

Sets the font family.

- Methods declared in class javax.swing.text.

StyledEditorKit.StyledTextAction

getEditor

,

getStyledDocument

,

getStyledEditorKit

,

setCharacterAttributes

,

setParagraphAttributes

- Methods declared in class javax.swing.text.

TextAction

augmentList

,

getFocusedComponent

,

getTextComponent

- Methods declared in class javax.swing.

AbstractAction

addPropertyChangeListener

,

clone

,

firePropertyChange

,

getKeys

,

getPropertyChangeListeners

,

getValue

,

isEnabled

,

putValue

,

removePropertyChangeListener

,

setEnabled

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.swing.

Action

accept

Field Summary

- Fields declared in class javax.swing.

AbstractAction

changeSupport

,

enabled

- Fields declared in interface javax.swing.

Action

ACCELERATOR_KEY

,

ACTION_COMMAND_KEY

,

DEFAULT

,

DISPLAYED_MNEMONIC_INDEX_KEY

,

LARGE_ICON_KEY

,

LONG_DESCRIPTION

,

MNEMONIC_KEY

,

NAME

,

SELECTED_KEY

,

SHORT_DESCRIPTION

,

SMALL_ICON

---

#### Field Summary

Fields declared in class javax.swing.

AbstractAction

changeSupport

,

enabled

---

#### Fields declared in class javax.swing. AbstractAction

Fields declared in interface javax.swing.

Action

ACCELERATOR_KEY

,

ACTION_COMMAND_KEY

,

DEFAULT

,

DISPLAYED_MNEMONIC_INDEX_KEY

,

LARGE_ICON_KEY

,

LONG_DESCRIPTION

,

MNEMONIC_KEY

,

NAME

,

SELECTED_KEY

,

SHORT_DESCRIPTION

,

SMALL_ICON

---

#### Fields declared in interface javax.swing. Action

Constructor Summary

Constructors

Constructor

Description

FontFamilyAction

​(

String

nm,

String

family)

Creates a new FontFamilyAction.

---

#### Constructor Summary

Creates a new FontFamilyAction.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

Sets the font family.

- Methods declared in class javax.swing.text.

StyledEditorKit.StyledTextAction

getEditor

,

getStyledDocument

,

getStyledEditorKit

,

setCharacterAttributes

,

setParagraphAttributes

- Methods declared in class javax.swing.text.

TextAction

augmentList

,

getFocusedComponent

,

getTextComponent

- Methods declared in class javax.swing.

AbstractAction

addPropertyChangeListener

,

clone

,

firePropertyChange

,

getKeys

,

getPropertyChangeListeners

,

getValue

,

isEnabled

,

putValue

,

removePropertyChangeListener

,

setEnabled

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.swing.

Action

accept

---

#### Method Summary

Sets the font family.

Methods declared in class javax.swing.text.

StyledEditorKit.StyledTextAction

getEditor

,

getStyledDocument

,

getStyledEditorKit

,

setCharacterAttributes

,

setParagraphAttributes

---

#### Methods declared in class javax.swing.text. StyledEditorKit.StyledTextAction

Methods declared in class javax.swing.text.

TextAction

augmentList

,

getFocusedComponent

,

getTextComponent

---

#### Methods declared in class javax.swing.text. TextAction

Methods declared in class javax.swing.

AbstractAction

addPropertyChangeListener

,

clone

,

firePropertyChange

,

getKeys

,

getPropertyChangeListeners

,

getValue

,

isEnabled

,

putValue

,

removePropertyChangeListener

,

setEnabled

---

#### Methods declared in class javax.swing. AbstractAction

Methods declared in class java.lang.

Object

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

Methods declared in interface javax.swing.

Action

accept

---

#### Methods declared in interface javax.swing. Action

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FontFamilyAction

```java
public FontFamilyAction​(
String
nm,

String
family)
```

Creates a new FontFamilyAction.

**Parameters:** nm

- the action name
**Parameters:** family

- the font family

============ METHOD DETAIL ==========

- Method Detail

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Sets the font family.

**Parameters:** e

- the event

Constructor Detail

- FontFamilyAction

```java
public FontFamilyAction​(
String
nm,

String
family)
```

Creates a new FontFamilyAction.

**Parameters:** nm

- the action name
**Parameters:** family

- the font family

---

#### Constructor Detail

FontFamilyAction

```java
public FontFamilyAction​(
String
nm,

String
family)
```

Creates a new FontFamilyAction.

**Parameters:** nm

- the action name
**Parameters:** family

- the font family

---

#### FontFamilyAction

public FontFamilyAction​(

String

nm,

String

family)

Creates a new FontFamilyAction.

Method Detail

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Sets the font family.

**Parameters:** e

- the event

---

#### Method Detail

actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Sets the font family.

**Parameters:** e

- the event

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

e)

Sets the font family.

---

