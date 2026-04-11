# Class StyledEditorKit

**Source:** `java.desktop\javax\swing\text\StyledEditorKit.html`

### Class Description

```java
public class
StyledEditorKit

extends
DefaultEditorKit
```

This is the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text document. This implementation provides a default
implementation which treats text as styled text and
provides a minimal set of actions for editing styled text.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public StyledEditorKit()

Creates a new EditorKit used for styled documents.

---

### Method Details

#### public
MutableAttributeSet
getInputAttributes()

Gets the input attributes for the pane. When
the caret moves and there is no selection, the
input attributes are automatically mutated to
reflect the character attributes of the current
caret location. The styled editing actions
use the input attributes to carry out their
actions.

**Returns:**
- the attribute set

---

#### public
Element
getCharacterAttributeRun()

Fetches the element representing the current
run of character attributes for the caret.

**Returns:**
- the element

---

#### public
Action
[] getActions()

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:**
- getActions

in class

DefaultEditorKit

**Returns:**
- the command list

---

#### public
Document
createDefaultDocument()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:**
- createDefaultDocument

in class

DefaultEditorKit

**Returns:**
- the model

---

#### public void install​(
JEditorPane
c)

Called when the kit is being installed into
a JEditorPane.

**Overrides:**
- install

in class

EditorKit

**Parameters:**
- c

- the JEditorPane

---

#### public void deinstall​(
JEditorPane
c)

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:**
- deinstall

in class

EditorKit

**Parameters:**
- c

- the JEditorPane

---

#### public
ViewFactory
getViewFactory()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. This is implemented to return View implementations
for the following kinds of elements:

- AbstractDocument.ContentElementName

AbstractDocument.ParagraphElementName

AbstractDocument.SectionElementName

StyleConstants.ComponentElementName

StyleConstants.IconElementName

**Overrides:**
- getViewFactory

in class

DefaultEditorKit

**Returns:**
- the factory

---

#### public
Object
clone()

Creates a copy of the editor kit.

**Overrides:**
- clone

in class

EditorKit

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Parameters:**
- element

- the element
- set

- the attributes

---

### Additional Sections

#### Class StyledEditorKit

java.lang.Object

- javax.swing.text.EditorKit
- - javax.swing.text.DefaultEditorKit
- - javax.swing.text.StyledEditorKit

javax.swing.text.EditorKit

- javax.swing.text.DefaultEditorKit
- - javax.swing.text.StyledEditorKit

javax.swing.text.DefaultEditorKit

- javax.swing.text.StyledEditorKit

javax.swing.text.StyledEditorKit

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** HTMLEditorKit

,

RTFEditorKit

```java
public class
StyledEditorKit

extends
DefaultEditorKit
```

This is the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text document. This implementation provides a default
implementation which treats text as styled text and
provides a minimal set of actions for editing styled text.

**See Also:** Serialized Form

public class

StyledEditorKit

extends

DefaultEditorKit

This is the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text document. This implementation provides a default
implementation which treats text as styled text and
provides a minimal set of actions for editing styled text.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

StyledEditorKit.AlignmentAction

An action to set paragraph alignment.

static class

StyledEditorKit.BoldAction

An action to toggle the bold attribute.

static class

StyledEditorKit.FontFamilyAction

An action to set the font family in the associated
JEditorPane.

static class

StyledEditorKit.FontSizeAction

An action to set the font size in the associated
JEditorPane.

static class

StyledEditorKit.ForegroundAction

An action to set foreground color.

static class

StyledEditorKit.ItalicAction

An action to toggle the italic attribute.

static class

StyledEditorKit.StyledTextAction

An action that assumes it's being fired on a JEditorPane
with a StyledEditorKit (or subclass) installed.

static class

StyledEditorKit.UnderlineAction

An action to toggle the underline attribute.

- Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StyledEditorKit

()

Creates a new EditorKit used for styled documents.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the editor kit.

Document

createDefaultDocument

()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

protected void

createInputAttributes

​(

Element

element,

MutableAttributeSet

set)

Copies the key/values in

element

s AttributeSet into

set

.

void

deinstall

​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane.

Action

[]

getActions

()

Fetches the command list for the editor.

Element

getCharacterAttributeRun

()

Fetches the element representing the current
run of character attributes for the caret.

MutableAttributeSet

getInputAttributes

()

Gets the input attributes for the pane.

ViewFactory

getViewFactory

()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

void

install

​(

JEditorPane

c)

Called when the kit is being installed into
a JEditorPane.

- Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

,

getContentType

,

read

,

read

,

write

,

write

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

StyledEditorKit.AlignmentAction

An action to set paragraph alignment.

static class

StyledEditorKit.BoldAction

An action to toggle the bold attribute.

static class

StyledEditorKit.FontFamilyAction

An action to set the font family in the associated
JEditorPane.

static class

StyledEditorKit.FontSizeAction

An action to set the font size in the associated
JEditorPane.

static class

StyledEditorKit.ForegroundAction

An action to set foreground color.

static class

StyledEditorKit.ItalicAction

An action to toggle the italic attribute.

static class

StyledEditorKit.StyledTextAction

An action that assumes it's being fired on a JEditorPane
with a StyledEditorKit (or subclass) installed.

static class

StyledEditorKit.UnderlineAction

An action to toggle the underline attribute.

- Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

---

#### Nested Class Summary

An action to set paragraph alignment.

An action to toggle the bold attribute.

An action to set the font family in the associated
JEditorPane.

An action to set the font size in the associated
JEditorPane.

An action to set foreground color.

An action to toggle the italic attribute.

An action that assumes it's being fired on a JEditorPane
with a StyledEditorKit (or subclass) installed.

An action to toggle the underline attribute.

Nested classes/interfaces declared in class javax.swing.text.

DefaultEditorKit

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

---

#### Nested classes/interfaces declared in class javax.swing.text. DefaultEditorKit

Field Summary

- Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

---

#### Field Summary

Fields declared in class javax.swing.text.

DefaultEditorKit

backwardAction

,

beepAction

,

beginAction

,

beginLineAction

,

beginParagraphAction

,

beginWordAction

,

copyAction

,

cutAction

,

defaultKeyTypedAction

,

deleteNextCharAction

,

deleteNextWordAction

,

deletePrevCharAction

,

deletePrevWordAction

,

downAction

,

endAction

,

endLineAction

,

EndOfLineStringProperty

,

endParagraphAction

,

endWordAction

,

forwardAction

,

insertBreakAction

,

insertContentAction

,

insertTabAction

,

nextWordAction

,

pageDownAction

,

pageUpAction

,

pasteAction

,

previousWordAction

,

readOnlyAction

,

selectAllAction

,

selectionBackwardAction

,

selectionBeginAction

,

selectionBeginLineAction

,

selectionBeginParagraphAction

,

selectionBeginWordAction

,

selectionDownAction

,

selectionEndAction

,

selectionEndLineAction

,

selectionEndParagraphAction

,

selectionEndWordAction

,

selectionForwardAction

,

selectionNextWordAction

,

selectionPreviousWordAction

,

selectionUpAction

,

selectLineAction

,

selectParagraphAction

,

selectWordAction

,

upAction

,

writableAction

---

#### Fields declared in class javax.swing.text. DefaultEditorKit

Constructor Summary

Constructors

Constructor

Description

StyledEditorKit

()

Creates a new EditorKit used for styled documents.

---

#### Constructor Summary

Creates a new EditorKit used for styled documents.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the editor kit.

Document

createDefaultDocument

()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

protected void

createInputAttributes

​(

Element

element,

MutableAttributeSet

set)

Copies the key/values in

element

s AttributeSet into

set

.

void

deinstall

​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane.

Action

[]

getActions

()

Fetches the command list for the editor.

Element

getCharacterAttributeRun

()

Fetches the element representing the current
run of character attributes for the caret.

MutableAttributeSet

getInputAttributes

()

Gets the input attributes for the pane.

ViewFactory

getViewFactory

()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

void

install

​(

JEditorPane

c)

Called when the kit is being installed into
a JEditorPane.

- Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

,

getContentType

,

read

,

read

,

write

,

write

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

---

#### Method Summary

Creates a copy of the editor kit.

Creates an uninitialized text storage model
that is appropriate for this type of editor.

Copies the key/values in

element

s AttributeSet into

set

.

Called when the kit is being removed from the
JEditorPane.

Fetches the command list for the editor.

Fetches the element representing the current
run of character attributes for the caret.

Gets the input attributes for the pane.

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

Called when the kit is being installed into
a JEditorPane.

Methods declared in class javax.swing.text.

DefaultEditorKit

createCaret

,

getContentType

,

read

,

read

,

write

,

write

---

#### Methods declared in class javax.swing.text. DefaultEditorKit

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StyledEditorKit

```java
public StyledEditorKit()
```

Creates a new EditorKit used for styled documents.

============ METHOD DETAIL ==========

- Method Detail

- getInputAttributes

```java
public
MutableAttributeSet
getInputAttributes()
```

Gets the input attributes for the pane. When
the caret moves and there is no selection, the
input attributes are automatically mutated to
reflect the character attributes of the current
caret location. The styled editing actions
use the input attributes to carry out their
actions.

**Returns:** the attribute set

- getCharacterAttributeRun

```java
public
Element
getCharacterAttributeRun()
```

Fetches the element representing the current
run of character attributes for the caret.

**Returns:** the element

- getActions

```java
public
Action
[] getActions()
```

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:** getActions

in class

DefaultEditorKit
**Returns:** the command list

- createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:** createDefaultDocument

in class

DefaultEditorKit
**Returns:** the model

- install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into
a JEditorPane.

**Overrides:** install

in class

EditorKit
**Parameters:** c

- the JEditorPane

- deinstall

```java
public void deinstall​(
JEditorPane
c)
```

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:** deinstall

in class

EditorKit
**Parameters:** c

- the JEditorPane

- getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. This is implemented to return View implementations
for the following kinds of elements:

- AbstractDocument.ContentElementName

AbstractDocument.ParagraphElementName

AbstractDocument.SectionElementName

StyleConstants.ComponentElementName

StyleConstants.IconElementName

**Overrides:** getViewFactory

in class

DefaultEditorKit
**Returns:** the factory

- clone

```java
public
Object
clone()
```

Creates a copy of the editor kit.

**Overrides:** clone

in class

EditorKit
**Returns:** the copy
**See Also:** Cloneable

- createInputAttributes

```java
protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)
```

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Parameters:** element

- the element
**Parameters:** set

- the attributes

Constructor Detail

- StyledEditorKit

```java
public StyledEditorKit()
```

Creates a new EditorKit used for styled documents.

---

#### Constructor Detail

StyledEditorKit

```java
public StyledEditorKit()
```

Creates a new EditorKit used for styled documents.

---

#### StyledEditorKit

public StyledEditorKit()

Creates a new EditorKit used for styled documents.

Method Detail

- getInputAttributes

```java
public
MutableAttributeSet
getInputAttributes()
```

Gets the input attributes for the pane. When
the caret moves and there is no selection, the
input attributes are automatically mutated to
reflect the character attributes of the current
caret location. The styled editing actions
use the input attributes to carry out their
actions.

**Returns:** the attribute set

- getCharacterAttributeRun

```java
public
Element
getCharacterAttributeRun()
```

Fetches the element representing the current
run of character attributes for the caret.

**Returns:** the element

- getActions

```java
public
Action
[] getActions()
```

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:** getActions

in class

DefaultEditorKit
**Returns:** the command list

- createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:** createDefaultDocument

in class

DefaultEditorKit
**Returns:** the model

- install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into
a JEditorPane.

**Overrides:** install

in class

EditorKit
**Parameters:** c

- the JEditorPane

- deinstall

```java
public void deinstall​(
JEditorPane
c)
```

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:** deinstall

in class

EditorKit
**Parameters:** c

- the JEditorPane

- getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. This is implemented to return View implementations
for the following kinds of elements:

- AbstractDocument.ContentElementName

AbstractDocument.ParagraphElementName

AbstractDocument.SectionElementName

StyleConstants.ComponentElementName

StyleConstants.IconElementName

**Overrides:** getViewFactory

in class

DefaultEditorKit
**Returns:** the factory

- clone

```java
public
Object
clone()
```

Creates a copy of the editor kit.

**Overrides:** clone

in class

EditorKit
**Returns:** the copy
**See Also:** Cloneable

- createInputAttributes

```java
protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)
```

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Parameters:** element

- the element
**Parameters:** set

- the attributes

---

#### Method Detail

getInputAttributes

```java
public
MutableAttributeSet
getInputAttributes()
```

Gets the input attributes for the pane. When
the caret moves and there is no selection, the
input attributes are automatically mutated to
reflect the character attributes of the current
caret location. The styled editing actions
use the input attributes to carry out their
actions.

**Returns:** the attribute set

---

#### getInputAttributes

public

MutableAttributeSet

getInputAttributes()

Gets the input attributes for the pane. When
the caret moves and there is no selection, the
input attributes are automatically mutated to
reflect the character attributes of the current
caret location. The styled editing actions
use the input attributes to carry out their
actions.

getCharacterAttributeRun

```java
public
Element
getCharacterAttributeRun()
```

Fetches the element representing the current
run of character attributes for the caret.

**Returns:** the element

---

#### getCharacterAttributeRun

public

Element

getCharacterAttributeRun()

Fetches the element representing the current
run of character attributes for the caret.

getActions

```java
public
Action
[] getActions()
```

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

**Overrides:** getActions

in class

DefaultEditorKit
**Returns:** the command list

---

#### getActions

public

Action

[] getActions()

Fetches the command list for the editor. This is
the list of commands supported by the superclass
augmented by the collection of commands defined
locally for style operations.

createDefaultDocument

```java
public
Document
createDefaultDocument()
```

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Overrides:** createDefaultDocument

in class

DefaultEditorKit
**Returns:** the model

---

#### createDefaultDocument

public

Document

createDefaultDocument()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into
a JEditorPane.

**Overrides:** install

in class

EditorKit
**Parameters:** c

- the JEditorPane

---

#### install

public void install​(

JEditorPane

c)

Called when the kit is being installed into
a JEditorPane.

deinstall

```java
public void deinstall​(
JEditorPane
c)
```

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

**Overrides:** deinstall

in class

EditorKit
**Parameters:** c

- the JEditorPane

---

#### deinstall

public void deinstall​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane. This is used to unregister any
listeners that were attached.

getViewFactory

```java
public
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. This is implemented to return View implementations
for the following kinds of elements:

- AbstractDocument.ContentElementName

AbstractDocument.ParagraphElementName

AbstractDocument.SectionElementName

StyleConstants.ComponentElementName

StyleConstants.IconElementName

**Overrides:** getViewFactory

in class

DefaultEditorKit
**Returns:** the factory

---

#### getViewFactory

public

ViewFactory

getViewFactory()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit. This is implemented to return View implementations
for the following kinds of elements:

- AbstractDocument.ContentElementName

AbstractDocument.ParagraphElementName

AbstractDocument.SectionElementName

StyleConstants.ComponentElementName

StyleConstants.IconElementName

AbstractDocument.ContentElementName

AbstractDocument.ParagraphElementName

AbstractDocument.SectionElementName

StyleConstants.ComponentElementName

StyleConstants.IconElementName

clone

```java
public
Object
clone()
```

Creates a copy of the editor kit.

**Overrides:** clone

in class

EditorKit
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a copy of the editor kit.

createInputAttributes

```java
protected void createInputAttributes​(
Element
element,

MutableAttributeSet
set)
```

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

**Parameters:** element

- the element
**Parameters:** set

- the attributes

---

#### createInputAttributes

protected void createInputAttributes​(

Element

element,

MutableAttributeSet

set)

Copies the key/values in

element

s AttributeSet into

set

. This does not copy component, icon, or element
names attributes. Subclasses may wish to refine what is and what
isn't copied here. But be sure to first remove all the attributes that
are in

set

.

This is called anytime the caret moves over a different location.

This is called anytime the caret moves over a different location.

---

