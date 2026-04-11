# Class StyledEditorKit.StyledTextAction

**Source:** `java.desktop\javax\swing\text\StyledEditorKit.StyledTextAction.html`

### Class Description

```java
public abstract static class
StyledEditorKit.StyledTextAction

extends
TextAction
```

An action that assumes it's being fired on a JEditorPane
with a StyledEditorKit (or subclass) installed. This has
some convenience methods for causing character or paragraph
level attribute changes. The convenience methods will
throw an IllegalArgumentException if the assumption of
a StyledDocument, a JEditorPane, or a StyledEditorKit
fail to be true.

The component that gets acted upon by the action
will be the source of the ActionEvent if the source
can be narrowed to a JEditorPane type. If the source
can't be narrowed, the most recently focused text
component is changed. If neither of these are the
case, the action cannot be performed.

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

#### public StyledTextAction​(
String
nm)

Creates a new StyledTextAction from a string action name.

**Parameters:**
- nm

- the name of the action

---

### Method Details

#### protected final
JEditorPane
getEditor​(
ActionEvent
e)

Gets the target editor for an action.

**Parameters:**
- e

- the action event

**Returns:**
- the editor

---

#### protected final
StyledDocument
getStyledDocument​(
JEditorPane
e)

Gets the document associated with an editor pane.

**Parameters:**
- e

- the editor

**Returns:**
- the document

**Throws:**
- IllegalArgumentException

- for the wrong document type

---

#### protected final
StyledEditorKit
getStyledEditorKit​(
JEditorPane
e)

Gets the editor kit associated with an editor pane.

**Parameters:**
- e

- the editor pane

**Returns:**
- the kit

**Throws:**
- IllegalArgumentException

- for the wrong document type

---

#### protected final void setCharacterAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)

Applies the given attributes to character
content. If there is a selection, the attributes
are applied to the selection range. If there
is no selection, the attributes are applied to
the input attribute set which defines the attributes
for any new text that gets inserted.

**Parameters:**
- editor

- the editor
- attr

- the attributes
- replace

- if true, then replace the existing attributes first

---

#### protected final void setParagraphAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)

Applies the given attributes to paragraphs. If
there is a selection, the attributes are applied
to the paragraphs that intersect the selection.
if there is no selection, the attributes are applied
to the paragraph at the current caret position.

**Parameters:**
- editor

- the editor
- attr

- the attributes
- replace

- if true, replace the existing attributes first

---

### Additional Sections

#### Class StyledEditorKit.StyledTextAction

java.lang.Object

- javax.swing.AbstractAction
- - javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction

javax.swing.AbstractAction

- javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction

javax.swing.text.TextAction

- javax.swing.text.StyledEditorKit.StyledTextAction

javax.swing.text.StyledEditorKit.StyledTextAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Direct Known Subclasses:** HTMLEditorKit.HTMLTextAction

,

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.UnderlineAction

**Enclosing class:** StyledEditorKit

```java
public abstract static class
StyledEditorKit.StyledTextAction

extends
TextAction
```

An action that assumes it's being fired on a JEditorPane
with a StyledEditorKit (or subclass) installed. This has
some convenience methods for causing character or paragraph
level attribute changes. The convenience methods will
throw an IllegalArgumentException if the assumption of
a StyledDocument, a JEditorPane, or a StyledEditorKit
fail to be true.

The component that gets acted upon by the action
will be the source of the ActionEvent if the source
can be narrowed to a JEditorPane type. If the source
can't be narrowed, the most recently focused text
component is changed. If neither of these are the
case, the action cannot be performed.

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

public abstract static class

StyledEditorKit.StyledTextAction

extends

TextAction

An action that assumes it's being fired on a JEditorPane
with a StyledEditorKit (or subclass) installed. This has
some convenience methods for causing character or paragraph
level attribute changes. The convenience methods will
throw an IllegalArgumentException if the assumption of
a StyledDocument, a JEditorPane, or a StyledEditorKit
fail to be true.

The component that gets acted upon by the action
will be the source of the ActionEvent if the source
can be narrowed to a JEditorPane type. If the source
can't be narrowed, the most recently focused text
component is changed. If neither of these are the
case, the action cannot be performed.

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

The component that gets acted upon by the action
will be the source of the ActionEvent if the source
can be narrowed to a JEditorPane type. If the source
can't be narrowed, the most recently focused text
component is changed. If neither of these are the
case, the action cannot be performed.

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

StyledTextAction

​(

String

nm)

Creates a new StyledTextAction from a string action name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

JEditorPane

getEditor

​(

ActionEvent

e)

Gets the target editor for an action.

protected

StyledDocument

getStyledDocument

​(

JEditorPane

e)

Gets the document associated with an editor pane.

protected

StyledEditorKit

getStyledEditorKit

​(

JEditorPane

e)

Gets the editor kit associated with an editor pane.

protected void

setCharacterAttributes

​(

JEditorPane

editor,

AttributeSet

attr,
boolean replace)

Applies the given attributes to character
content.

protected void

setParagraphAttributes

​(

JEditorPane

editor,

AttributeSet

attr,
boolean replace)

Applies the given attributes to paragraphs.

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

- Methods declared in interface java.awt.event.

ActionListener

actionPerformed

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

StyledTextAction

​(

String

nm)

Creates a new StyledTextAction from a string action name.

---

#### Constructor Summary

Creates a new StyledTextAction from a string action name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

JEditorPane

getEditor

​(

ActionEvent

e)

Gets the target editor for an action.

protected

StyledDocument

getStyledDocument

​(

JEditorPane

e)

Gets the document associated with an editor pane.

protected

StyledEditorKit

getStyledEditorKit

​(

JEditorPane

e)

Gets the editor kit associated with an editor pane.

protected void

setCharacterAttributes

​(

JEditorPane

editor,

AttributeSet

attr,
boolean replace)

Applies the given attributes to character
content.

protected void

setParagraphAttributes

​(

JEditorPane

editor,

AttributeSet

attr,
boolean replace)

Applies the given attributes to paragraphs.

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

- Methods declared in interface java.awt.event.

ActionListener

actionPerformed

---

#### Method Summary

Gets the target editor for an action.

Gets the document associated with an editor pane.

Gets the editor kit associated with an editor pane.

Applies the given attributes to character
content.

Applies the given attributes to paragraphs.

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

Methods declared in interface java.awt.event.

ActionListener

actionPerformed

---

#### Methods declared in interface java.awt.event. ActionListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StyledTextAction

```java
public StyledTextAction​(
String
nm)
```

Creates a new StyledTextAction from a string action name.

**Parameters:** nm

- the name of the action

============ METHOD DETAIL ==========

- Method Detail

- getEditor

```java
protected final
JEditorPane
getEditor​(
ActionEvent
e)
```

Gets the target editor for an action.

**Parameters:** e

- the action event
**Returns:** the editor

- getStyledDocument

```java
protected final
StyledDocument
getStyledDocument​(
JEditorPane
e)
```

Gets the document associated with an editor pane.

**Parameters:** e

- the editor
**Returns:** the document
**Throws:** IllegalArgumentException

- for the wrong document type

- getStyledEditorKit

```java
protected final
StyledEditorKit
getStyledEditorKit​(
JEditorPane
e)
```

Gets the editor kit associated with an editor pane.

**Parameters:** e

- the editor pane
**Returns:** the kit
**Throws:** IllegalArgumentException

- for the wrong document type

- setCharacterAttributes

```java
protected final void setCharacterAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)
```

Applies the given attributes to character
content. If there is a selection, the attributes
are applied to the selection range. If there
is no selection, the attributes are applied to
the input attribute set which defines the attributes
for any new text that gets inserted.

**Parameters:** editor

- the editor
**Parameters:** attr

- the attributes
**Parameters:** replace

- if true, then replace the existing attributes first

- setParagraphAttributes

```java
protected final void setParagraphAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)
```

Applies the given attributes to paragraphs. If
there is a selection, the attributes are applied
to the paragraphs that intersect the selection.
if there is no selection, the attributes are applied
to the paragraph at the current caret position.

**Parameters:** editor

- the editor
**Parameters:** attr

- the attributes
**Parameters:** replace

- if true, replace the existing attributes first

Constructor Detail

- StyledTextAction

```java
public StyledTextAction​(
String
nm)
```

Creates a new StyledTextAction from a string action name.

**Parameters:** nm

- the name of the action

---

#### Constructor Detail

StyledTextAction

```java
public StyledTextAction​(
String
nm)
```

Creates a new StyledTextAction from a string action name.

**Parameters:** nm

- the name of the action

---

#### StyledTextAction

public StyledTextAction​(

String

nm)

Creates a new StyledTextAction from a string action name.

Method Detail

- getEditor

```java
protected final
JEditorPane
getEditor​(
ActionEvent
e)
```

Gets the target editor for an action.

**Parameters:** e

- the action event
**Returns:** the editor

- getStyledDocument

```java
protected final
StyledDocument
getStyledDocument​(
JEditorPane
e)
```

Gets the document associated with an editor pane.

**Parameters:** e

- the editor
**Returns:** the document
**Throws:** IllegalArgumentException

- for the wrong document type

- getStyledEditorKit

```java
protected final
StyledEditorKit
getStyledEditorKit​(
JEditorPane
e)
```

Gets the editor kit associated with an editor pane.

**Parameters:** e

- the editor pane
**Returns:** the kit
**Throws:** IllegalArgumentException

- for the wrong document type

- setCharacterAttributes

```java
protected final void setCharacterAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)
```

Applies the given attributes to character
content. If there is a selection, the attributes
are applied to the selection range. If there
is no selection, the attributes are applied to
the input attribute set which defines the attributes
for any new text that gets inserted.

**Parameters:** editor

- the editor
**Parameters:** attr

- the attributes
**Parameters:** replace

- if true, then replace the existing attributes first

- setParagraphAttributes

```java
protected final void setParagraphAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)
```

Applies the given attributes to paragraphs. If
there is a selection, the attributes are applied
to the paragraphs that intersect the selection.
if there is no selection, the attributes are applied
to the paragraph at the current caret position.

**Parameters:** editor

- the editor
**Parameters:** attr

- the attributes
**Parameters:** replace

- if true, replace the existing attributes first

---

#### Method Detail

getEditor

```java
protected final
JEditorPane
getEditor​(
ActionEvent
e)
```

Gets the target editor for an action.

**Parameters:** e

- the action event
**Returns:** the editor

---

#### getEditor

protected final

JEditorPane

getEditor​(

ActionEvent

e)

Gets the target editor for an action.

getStyledDocument

```java
protected final
StyledDocument
getStyledDocument​(
JEditorPane
e)
```

Gets the document associated with an editor pane.

**Parameters:** e

- the editor
**Returns:** the document
**Throws:** IllegalArgumentException

- for the wrong document type

---

#### getStyledDocument

protected final

StyledDocument

getStyledDocument​(

JEditorPane

e)

Gets the document associated with an editor pane.

getStyledEditorKit

```java
protected final
StyledEditorKit
getStyledEditorKit​(
JEditorPane
e)
```

Gets the editor kit associated with an editor pane.

**Parameters:** e

- the editor pane
**Returns:** the kit
**Throws:** IllegalArgumentException

- for the wrong document type

---

#### getStyledEditorKit

protected final

StyledEditorKit

getStyledEditorKit​(

JEditorPane

e)

Gets the editor kit associated with an editor pane.

setCharacterAttributes

```java
protected final void setCharacterAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)
```

Applies the given attributes to character
content. If there is a selection, the attributes
are applied to the selection range. If there
is no selection, the attributes are applied to
the input attribute set which defines the attributes
for any new text that gets inserted.

**Parameters:** editor

- the editor
**Parameters:** attr

- the attributes
**Parameters:** replace

- if true, then replace the existing attributes first

---

#### setCharacterAttributes

protected final void setCharacterAttributes​(

JEditorPane

editor,

AttributeSet

attr,
boolean replace)

Applies the given attributes to character
content. If there is a selection, the attributes
are applied to the selection range. If there
is no selection, the attributes are applied to
the input attribute set which defines the attributes
for any new text that gets inserted.

setParagraphAttributes

```java
protected final void setParagraphAttributes​(
JEditorPane
editor,

AttributeSet
attr,
boolean replace)
```

Applies the given attributes to paragraphs. If
there is a selection, the attributes are applied
to the paragraphs that intersect the selection.
if there is no selection, the attributes are applied
to the paragraph at the current caret position.

**Parameters:** editor

- the editor
**Parameters:** attr

- the attributes
**Parameters:** replace

- if true, replace the existing attributes first

---

#### setParagraphAttributes

protected final void setParagraphAttributes​(

JEditorPane

editor,

AttributeSet

attr,
boolean replace)

Applies the given attributes to paragraphs. If
there is a selection, the attributes are applied
to the paragraphs that intersect the selection.
if there is no selection, the attributes are applied
to the paragraph at the current caret position.

---

