# Class HTMLEditorKit.InsertHTMLTextAction

**Source:** `java.desktop\javax\swing\text\html\HTMLEditorKit.InsertHTMLTextAction.html`

### Class Description

```java
public static class
HTMLEditorKit.InsertHTMLTextAction

extends
HTMLEditorKit.HTMLTextAction
```

InsertHTMLTextAction can be used to insert an arbitrary string of HTML
into an existing HTML document. At least two HTML.Tags need to be
supplied. The first Tag, parentTag, identifies the parent in
the document to add the elements to. The second tag, addTag,
identifies the first tag that should be added to the document as
seen in the HTML string. One important thing to remember, is that
the parser is going to generate all the appropriate tags, even if
they aren't in the HTML string passed in.

For example, lets say you wanted to create an action to insert
a table into the body. The parentTag would be HTML.Tag.BODY,
addTag would be HTML.Tag.TABLE, and the string could be something
like <table><tr><td></td></tr></table>.

There is also an option to supply an alternate parentTag and
addTag. These will be checked for if there is no parentTag at
offset.

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

#### protected
String
html

HTML to insert.

---

#### protected
HTML.Tag
parentTag

Tag to check for in the document.

---

#### protected
HTML.Tag
addTag

Tag in HTML to start adding tags from.

---

#### protected
HTML.Tag
alternateParentTag

Alternate Tag to check for in the document if parentTag is
not found.

---

#### protected
HTML.Tag
alternateAddTag

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

---

### Constructor Details

#### public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)

Creates a new InsertHTMLTextAction.

**Parameters:**
- name

- a name of the action
- html

- an HTML string
- parentTag

- a parent tag
- addTag

- the first tag to start inserting into document

---

#### public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag,

HTML.Tag
alternateParentTag,

HTML.Tag
alternateAddTag)

Creates a new InsertHTMLTextAction.

**Parameters:**
- name

- a name of the action
- html

- an HTML string
- parentTag

- a parent tag
- addTag

- the first tag to start inserting into document
- alternateParentTag

- an alternative parent tag
- alternateAddTag

- an alternative tag

---

### Method Details

#### protected void insertHTML​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
addTag)

A cover for HTMLEditorKit.insertHTML. If an exception it
thrown it is wrapped in a RuntimeException and thrown.

**Parameters:**
- editor

- an instance of JEditorPane
- doc

- the document to insert into
- offset

- the offset to insert HTML at
- html

- an HTML string
- popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
- pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
- addTag

- the first tag to start inserting into document

---

#### protected void insertAtBoundary​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:**
- editor

- an instance of JEditorPane
- doc

- an instance of HTMLDocument
- offset

- an offset to start from
- insertElement

- an instance of Element
- html

- an HTML string
- parentTag

- a parent tag
- addTag

- the first tag to start inserting into document

**Since:**
- 1.3

---

#### @Deprecated

protected void insertAtBoundry​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:**
- editor

- an instance of JEditorPane
- doc

- an instance of HTMLDocument
- offset

- an offset to start from
- insertElement

- an instance of Element
- html

- an HTML string
- parentTag

- a parent tag
- addTag

- the first tag to start inserting into document

---

#### public void actionPerformed​(
ActionEvent
ae)

Inserts the HTML into the document.

**Parameters:**
- ae

- the event

---

### Additional Sections

#### Class HTMLEditorKit.InsertHTMLTextAction

java.lang.Object

- javax.swing.AbstractAction
- - javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.html.HTMLEditorKit.HTMLTextAction
- - javax.swing.text.html.HTMLEditorKit.InsertHTMLTextAction

javax.swing.AbstractAction

- javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.html.HTMLEditorKit.HTMLTextAction
- - javax.swing.text.html.HTMLEditorKit.InsertHTMLTextAction

javax.swing.text.TextAction

- javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.html.HTMLEditorKit.HTMLTextAction
- - javax.swing.text.html.HTMLEditorKit.InsertHTMLTextAction

javax.swing.text.StyledEditorKit.StyledTextAction

- javax.swing.text.html.HTMLEditorKit.HTMLTextAction
- - javax.swing.text.html.HTMLEditorKit.InsertHTMLTextAction

javax.swing.text.html.HTMLEditorKit.HTMLTextAction

- javax.swing.text.html.HTMLEditorKit.InsertHTMLTextAction

javax.swing.text.html.HTMLEditorKit.InsertHTMLTextAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Enclosing class:** HTMLEditorKit

```java
public static class
HTMLEditorKit.InsertHTMLTextAction

extends
HTMLEditorKit.HTMLTextAction
```

InsertHTMLTextAction can be used to insert an arbitrary string of HTML
into an existing HTML document. At least two HTML.Tags need to be
supplied. The first Tag, parentTag, identifies the parent in
the document to add the elements to. The second tag, addTag,
identifies the first tag that should be added to the document as
seen in the HTML string. One important thing to remember, is that
the parser is going to generate all the appropriate tags, even if
they aren't in the HTML string passed in.

For example, lets say you wanted to create an action to insert
a table into the body. The parentTag would be HTML.Tag.BODY,
addTag would be HTML.Tag.TABLE, and the string could be something
like <table><tr><td></td></tr></table>.

There is also an option to supply an alternate parentTag and
addTag. These will be checked for if there is no parentTag at
offset.

**See Also:** Serialized Form

public static class

HTMLEditorKit.InsertHTMLTextAction

extends

HTMLEditorKit.HTMLTextAction

InsertHTMLTextAction can be used to insert an arbitrary string of HTML
into an existing HTML document. At least two HTML.Tags need to be
supplied. The first Tag, parentTag, identifies the parent in
the document to add the elements to. The second tag, addTag,
identifies the first tag that should be added to the document as
seen in the HTML string. One important thing to remember, is that
the parser is going to generate all the appropriate tags, even if
they aren't in the HTML string passed in.

For example, lets say you wanted to create an action to insert
a table into the body. The parentTag would be HTML.Tag.BODY,
addTag would be HTML.Tag.TABLE, and the string could be something
like <table><tr><td></td></tr></table>.

There is also an option to supply an alternate parentTag and
addTag. These will be checked for if there is no parentTag at
offset.

For example, lets say you wanted to create an action to insert
a table into the body. The parentTag would be HTML.Tag.BODY,
addTag would be HTML.Tag.TABLE, and the string could be something
like <table><tr><td></td></tr></table>.

There is also an option to supply an alternate parentTag and
addTag. These will be checked for if there is no parentTag at
offset.

There is also an option to supply an alternate parentTag and
addTag. These will be checked for if there is no parentTag at
offset.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

HTML.Tag

addTag

Tag in HTML to start adding tags from.

protected

HTML.Tag

alternateAddTag

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

protected

HTML.Tag

alternateParentTag

Alternate Tag to check for in the document if parentTag is
not found.

protected

String

html

HTML to insert.

protected

HTML.Tag

parentTag

Tag to check for in the document.

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

InsertHTMLTextAction

​(

String

name,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

Creates a new InsertHTMLTextAction.

InsertHTMLTextAction

​(

String

name,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag,

HTML.Tag

alternateParentTag,

HTML.Tag

alternateAddTag)

Creates a new InsertHTMLTextAction.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

ae)

Inserts the HTML into the document.

protected void

insertAtBoundary

​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

Element

insertElement,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

This is invoked when inserting at a boundary.

protected void

insertAtBoundry

​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

Element

insertElement,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

Deprecated.

As of Java 2 platform v1.3, use insertAtBoundary

protected void

insertHTML

​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

String

html,
int popDepth,
int pushDepth,

HTML.Tag

addTag)

A cover for HTMLEditorKit.insertHTML.

- Methods declared in class javax.swing.text.html.

HTMLEditorKit.HTMLTextAction

elementCountToTag

,

findElementMatchingTag

,

getElementsAt

,

getHTMLDocument

,

getHTMLEditorKit

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

Fields

Modifier and Type

Field

Description

protected

HTML.Tag

addTag

Tag in HTML to start adding tags from.

protected

HTML.Tag

alternateAddTag

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

protected

HTML.Tag

alternateParentTag

Alternate Tag to check for in the document if parentTag is
not found.

protected

String

html

HTML to insert.

protected

HTML.Tag

parentTag

Tag to check for in the document.

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

Tag in HTML to start adding tags from.

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

Alternate Tag to check for in the document if parentTag is
not found.

HTML to insert.

Tag to check for in the document.

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

InsertHTMLTextAction

​(

String

name,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

Creates a new InsertHTMLTextAction.

InsertHTMLTextAction

​(

String

name,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag,

HTML.Tag

alternateParentTag,

HTML.Tag

alternateAddTag)

Creates a new InsertHTMLTextAction.

---

#### Constructor Summary

Creates a new InsertHTMLTextAction.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

ae)

Inserts the HTML into the document.

protected void

insertAtBoundary

​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

Element

insertElement,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

This is invoked when inserting at a boundary.

protected void

insertAtBoundry

​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

Element

insertElement,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

Deprecated.

As of Java 2 platform v1.3, use insertAtBoundary

protected void

insertHTML

​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

String

html,
int popDepth,
int pushDepth,

HTML.Tag

addTag)

A cover for HTMLEditorKit.insertHTML.

- Methods declared in class javax.swing.text.html.

HTMLEditorKit.HTMLTextAction

elementCountToTag

,

findElementMatchingTag

,

getElementsAt

,

getHTMLDocument

,

getHTMLEditorKit

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

Inserts the HTML into the document.

This is invoked when inserting at a boundary.

Deprecated.

As of Java 2 platform v1.3, use insertAtBoundary

A cover for HTMLEditorKit.insertHTML.

Methods declared in class javax.swing.text.html.

HTMLEditorKit.HTMLTextAction

elementCountToTag

,

findElementMatchingTag

,

getElementsAt

,

getHTMLDocument

,

getHTMLEditorKit

---

#### Methods declared in class javax.swing.text.html. HTMLEditorKit.HTMLTextAction

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

============ FIELD DETAIL ===========

- Field Detail

- html

```java
protected
String
html
```

HTML to insert.

- parentTag

```java
protected
HTML.Tag
parentTag
```

Tag to check for in the document.

- addTag

```java
protected
HTML.Tag
addTag
```

Tag in HTML to start adding tags from.

- alternateParentTag

```java
protected
HTML.Tag
alternateParentTag
```

Alternate Tag to check for in the document if parentTag is
not found.

- alternateAddTag

```java
protected
HTML.Tag
alternateAddTag
```

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InsertHTMLTextAction

```java
public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

Creates a new InsertHTMLTextAction.

**Parameters:** name

- a name of the action
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document

- InsertHTMLTextAction

```java
public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag,

HTML.Tag
alternateParentTag,

HTML.Tag
alternateAddTag)
```

Creates a new InsertHTMLTextAction.

**Parameters:** name

- a name of the action
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document
**Parameters:** alternateParentTag

- an alternative parent tag
**Parameters:** alternateAddTag

- an alternative tag

============ METHOD DETAIL ==========

- Method Detail

- insertHTML

```java
protected void insertHTML​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
addTag)
```

A cover for HTMLEditorKit.insertHTML. If an exception it
thrown it is wrapped in a RuntimeException and thrown.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- the document to insert into
**Parameters:** offset

- the offset to insert HTML at
**Parameters:** html

- an HTML string
**Parameters:** popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
**Parameters:** pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
**Parameters:** addTag

- the first tag to start inserting into document

- insertAtBoundary

```java
protected void insertAtBoundary​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** insertElement

- an instance of Element
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document
**Since:** 1.3

- insertAtBoundry

```java
@Deprecated

protected void insertAtBoundry​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

Deprecated.

As of Java 2 platform v1.3, use insertAtBoundary

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** insertElement

- an instance of Element
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
ae)
```

Inserts the HTML into the document.

**Parameters:** ae

- the event

Field Detail

- html

```java
protected
String
html
```

HTML to insert.

- parentTag

```java
protected
HTML.Tag
parentTag
```

Tag to check for in the document.

- addTag

```java
protected
HTML.Tag
addTag
```

Tag in HTML to start adding tags from.

- alternateParentTag

```java
protected
HTML.Tag
alternateParentTag
```

Alternate Tag to check for in the document if parentTag is
not found.

- alternateAddTag

```java
protected
HTML.Tag
alternateAddTag
```

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

---

#### Field Detail

html

```java
protected
String
html
```

HTML to insert.

---

#### html

protected

String

html

HTML to insert.

parentTag

```java
protected
HTML.Tag
parentTag
```

Tag to check for in the document.

---

#### parentTag

protected

HTML.Tag

parentTag

Tag to check for in the document.

addTag

```java
protected
HTML.Tag
addTag
```

Tag in HTML to start adding tags from.

---

#### addTag

protected

HTML.Tag

addTag

Tag in HTML to start adding tags from.

alternateParentTag

```java
protected
HTML.Tag
alternateParentTag
```

Alternate Tag to check for in the document if parentTag is
not found.

---

#### alternateParentTag

protected

HTML.Tag

alternateParentTag

Alternate Tag to check for in the document if parentTag is
not found.

alternateAddTag

```java
protected
HTML.Tag
alternateAddTag
```

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

---

#### alternateAddTag

protected

HTML.Tag

alternateAddTag

Alternate tag in HTML to start adding tags from if parentTag
is not found and alternateParentTag is found.

Constructor Detail

- InsertHTMLTextAction

```java
public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

Creates a new InsertHTMLTextAction.

**Parameters:** name

- a name of the action
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document

- InsertHTMLTextAction

```java
public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag,

HTML.Tag
alternateParentTag,

HTML.Tag
alternateAddTag)
```

Creates a new InsertHTMLTextAction.

**Parameters:** name

- a name of the action
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document
**Parameters:** alternateParentTag

- an alternative parent tag
**Parameters:** alternateAddTag

- an alternative tag

---

#### Constructor Detail

InsertHTMLTextAction

```java
public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

Creates a new InsertHTMLTextAction.

**Parameters:** name

- a name of the action
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document

---

#### InsertHTMLTextAction

public InsertHTMLTextAction​(

String

name,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

Creates a new InsertHTMLTextAction.

InsertHTMLTextAction

```java
public InsertHTMLTextAction​(
String
name,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag,

HTML.Tag
alternateParentTag,

HTML.Tag
alternateAddTag)
```

Creates a new InsertHTMLTextAction.

**Parameters:** name

- a name of the action
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document
**Parameters:** alternateParentTag

- an alternative parent tag
**Parameters:** alternateAddTag

- an alternative tag

---

#### InsertHTMLTextAction

public InsertHTMLTextAction​(

String

name,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag,

HTML.Tag

alternateParentTag,

HTML.Tag

alternateAddTag)

Creates a new InsertHTMLTextAction.

Method Detail

- insertHTML

```java
protected void insertHTML​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
addTag)
```

A cover for HTMLEditorKit.insertHTML. If an exception it
thrown it is wrapped in a RuntimeException and thrown.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- the document to insert into
**Parameters:** offset

- the offset to insert HTML at
**Parameters:** html

- an HTML string
**Parameters:** popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
**Parameters:** pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
**Parameters:** addTag

- the first tag to start inserting into document

- insertAtBoundary

```java
protected void insertAtBoundary​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** insertElement

- an instance of Element
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document
**Since:** 1.3

- insertAtBoundry

```java
@Deprecated

protected void insertAtBoundry​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

Deprecated.

As of Java 2 platform v1.3, use insertAtBoundary

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** insertElement

- an instance of Element
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
ae)
```

Inserts the HTML into the document.

**Parameters:** ae

- the event

---

#### Method Detail

insertHTML

```java
protected void insertHTML​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

String
html,
int popDepth,
int pushDepth,

HTML.Tag
addTag)
```

A cover for HTMLEditorKit.insertHTML. If an exception it
thrown it is wrapped in a RuntimeException and thrown.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- the document to insert into
**Parameters:** offset

- the offset to insert HTML at
**Parameters:** html

- an HTML string
**Parameters:** popDepth

- the number of ElementSpec.EndTagTypes to generate
before inserting
**Parameters:** pushDepth

- the number of ElementSpec.StartTagTypes with a direction
of ElementSpec.JoinNextDirection that should be generated
before inserting, but after the end tags have been generated
**Parameters:** addTag

- the first tag to start inserting into document

---

#### insertHTML

protected void insertHTML​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

String

html,
int popDepth,
int pushDepth,

HTML.Tag

addTag)

A cover for HTMLEditorKit.insertHTML. If an exception it
thrown it is wrapped in a RuntimeException and thrown.

insertAtBoundary

```java
protected void insertAtBoundary​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** insertElement

- an instance of Element
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document
**Since:** 1.3

---

#### insertAtBoundary

protected void insertAtBoundary​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

Element

insertElement,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

insertAtBoundry

```java
@Deprecated

protected void insertAtBoundry​(
JEditorPane
editor,

HTMLDocument
doc,
int offset,

Element
insertElement,

String
html,

HTML.Tag
parentTag,

HTML.Tag
addTag)
```

Deprecated.

As of Java 2 platform v1.3, use insertAtBoundary

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

**Parameters:** editor

- an instance of JEditorPane
**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** insertElement

- an instance of Element
**Parameters:** html

- an HTML string
**Parameters:** parentTag

- a parent tag
**Parameters:** addTag

- the first tag to start inserting into document

---

#### insertAtBoundry

@Deprecated

protected void insertAtBoundry​(

JEditorPane

editor,

HTMLDocument

doc,
int offset,

Element

insertElement,

String

html,

HTML.Tag

parentTag,

HTML.Tag

addTag)

This is invoked when inserting at a boundary. It determines
the number of pops, and then the number of pushes that need
to be performed, and then invokes insertHTML.

actionPerformed

```java
public void actionPerformed​(
ActionEvent
ae)
```

Inserts the HTML into the document.

**Parameters:** ae

- the event

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

ae)

Inserts the HTML into the document.

---

