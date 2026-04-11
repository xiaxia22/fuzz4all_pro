# Class EditorKit

**Source:** `java.desktop\javax\swing\text\EditorKit.html`

### Class Description

```java
public abstract class
EditorKit

extends
Object

implements
Cloneable
,
Serializable
```

Establishes the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text content. The EditorKit acts as a factory for some
kind of policy. For example, an implementation
of html and rtf can be provided that is replaceable
with other implementations.

A kit can safely store editing state as an instance
of the kit will be dedicated to a text component.
New kits will normally be created by cloning a
prototype kit. The kit will have its

setComponent

method called to establish
its relationship with a JTextComponent.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public EditorKit()

Construct an EditorKit.

---

### Method Details

#### public
Object
clone()

Creates a copy of the editor kit. This is implemented
to use

Object.clone()

. If the kit cannot be cloned,
null is returned.

**Overrides:**
- clone

in class

Object

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### public void install​(
JEditorPane
c)

Called when the kit is being installed into the
a JEditorPane.

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

**Parameters:**
- c

- the JEditorPane

---

#### public abstract
String
getContentType()

Gets the MIME type of the data that this
kit represents support for.

**Returns:**
- the type

---

#### public abstract
ViewFactory
getViewFactory()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

**Returns:**
- the factory

---

#### public abstract
Action
[] getActions()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Returns:**
- the set of actions

---

#### public abstract
Caret
createCaret()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Returns:**
- the caret

---

#### public abstract
Document
createDefaultDocument()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Returns:**
- the model

---

#### public abstract void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Parameters:**
- in

- The stream to read from
- doc

- The destination for the insertion.
- pos

- The location in the document to place the
content >= 0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### public abstract void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Parameters:**
- out

- The stream to write to
- doc

- The source for the write.
- pos

- The location in the document to fetch the
content from >= 0.
- len

- The amount to write out >= 0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### public abstract void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Since actual text editing is unicode based, this would
generally be the preferred way to read in the data.
Some types of content are stored in an 8-bit form however,
and will favor the InputStream.

**Parameters:**
- in

- The stream to read from
- doc

- The destination for the insertion.
- pos

- The location in the document to place the
content >= 0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### public abstract void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

Since actual text editing is unicode based, this would
generally be the preferred way to write the data.
Some types of content are stored in an 8-bit form however,
and will favor the OutputStream.

**Parameters:**
- out

- The stream to write to
- doc

- The source for the write.
- pos

- The location in the document to fetch the
content >= 0.
- len

- The amount to write out >= 0.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

### Additional Sections

#### Class EditorKit

java.lang.Object

- javax.swing.text.EditorKit

javax.swing.text.EditorKit

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** DefaultEditorKit

```java
public abstract class
EditorKit

extends
Object

implements
Cloneable
,
Serializable
```

Establishes the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text content. The EditorKit acts as a factory for some
kind of policy. For example, an implementation
of html and rtf can be provided that is replaceable
with other implementations.

A kit can safely store editing state as an instance
of the kit will be dedicated to a text component.
New kits will normally be created by cloning a
prototype kit. The kit will have its

setComponent

method called to establish
its relationship with a JTextComponent.

**See Also:** Serialized Form

public abstract class

EditorKit

extends

Object

implements

Cloneable

,

Serializable

Establishes the set of things needed by a text component
to be a reasonably functioning editor for some

type

of text content. The EditorKit acts as a factory for some
kind of policy. For example, an implementation
of html and rtf can be provided that is replaceable
with other implementations.

A kit can safely store editing state as an instance
of the kit will be dedicated to a text component.
New kits will normally be created by cloning a
prototype kit. The kit will have its

setComponent

method called to establish
its relationship with a JTextComponent.

A kit can safely store editing state as an instance
of the kit will be dedicated to a text component.
New kits will normally be created by cloning a
prototype kit. The kit will have its

setComponent

method called to establish
its relationship with a JTextComponent.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EditorKit

()

Construct an EditorKit.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the editor kit.

abstract

Caret

createCaret

()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

abstract

Document

createDefaultDocument

()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

void

deinstall

​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane.

abstract

Action

[]

getActions

()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

abstract

String

getContentType

()

Gets the MIME type of the data that this
kit represents support for.

abstract

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

Called when the kit is being installed into the
a JEditorPane.

abstract void

read

​(

InputStream

in,

Document

doc,
int pos)

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

abstract void

read

​(

Reader

in,

Document

doc,
int pos)

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

abstract void

write

​(

OutputStream

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

abstract void

write

​(

Writer

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

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

Constructor Summary

Constructors

Constructor

Description

EditorKit

()

Construct an EditorKit.

---

#### Constructor Summary

Construct an EditorKit.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the editor kit.

abstract

Caret

createCaret

()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

abstract

Document

createDefaultDocument

()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

void

deinstall

​(

JEditorPane

c)

Called when the kit is being removed from the
JEditorPane.

abstract

Action

[]

getActions

()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

abstract

String

getContentType

()

Gets the MIME type of the data that this
kit represents support for.

abstract

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

Called when the kit is being installed into the
a JEditorPane.

abstract void

read

​(

InputStream

in,

Document

doc,
int pos)

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

abstract void

read

​(

Reader

in,

Document

doc,
int pos)

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

abstract void

write

​(

OutputStream

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

abstract void

write

​(

Writer

out,

Document

doc,
int pos,
int len)

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

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

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

Creates an uninitialized text storage model
that is appropriate for this type of editor.

Called when the kit is being removed from the
JEditorPane.

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

Gets the MIME type of the data that this
kit represents support for.

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

Called when the kit is being installed into the
a JEditorPane.

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

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

- EditorKit

```java
public EditorKit()
```

Construct an EditorKit.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Creates a copy of the editor kit. This is implemented
to use

Object.clone()

. If the kit cannot be cloned,
null is returned.

**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into the
a JEditorPane.

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

**Parameters:** c

- the JEditorPane

- getContentType

```java
public abstract
String
getContentType()
```

Gets the MIME type of the data that this
kit represents support for.

**Returns:** the type

- getViewFactory

```java
public abstract
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

**Returns:** the factory

- getActions

```java
public abstract
Action
[] getActions()
```

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Returns:** the set of actions

- createCaret

```java
public abstract
Caret
createCaret()
```

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Returns:** the caret

- createDefaultDocument

```java
public abstract
Document
createDefaultDocument()
```

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Returns:** the model

- read

```java
public abstract void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public abstract void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content from >= 0.
**Parameters:** len

- The amount to write out >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- read

```java
public abstract void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Since actual text editing is unicode based, this would
generally be the preferred way to read in the data.
Some types of content are stored in an 8-bit form however,
and will favor the InputStream.

**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public abstract void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

Since actual text editing is unicode based, this would
generally be the preferred way to write the data.
Some types of content are stored in an 8-bit form however,
and will favor the OutputStream.

**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content >= 0.
**Parameters:** len

- The amount to write out >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

Constructor Detail

- EditorKit

```java
public EditorKit()
```

Construct an EditorKit.

---

#### Constructor Detail

EditorKit

```java
public EditorKit()
```

Construct an EditorKit.

---

#### EditorKit

public EditorKit()

Construct an EditorKit.

Method Detail

- clone

```java
public
Object
clone()
```

Creates a copy of the editor kit. This is implemented
to use

Object.clone()

. If the kit cannot be cloned,
null is returned.

**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into the
a JEditorPane.

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

**Parameters:** c

- the JEditorPane

- getContentType

```java
public abstract
String
getContentType()
```

Gets the MIME type of the data that this
kit represents support for.

**Returns:** the type

- getViewFactory

```java
public abstract
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

**Returns:** the factory

- getActions

```java
public abstract
Action
[] getActions()
```

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Returns:** the set of actions

- createCaret

```java
public abstract
Caret
createCaret()
```

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Returns:** the caret

- createDefaultDocument

```java
public abstract
Document
createDefaultDocument()
```

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Returns:** the model

- read

```java
public abstract void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public abstract void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content from >= 0.
**Parameters:** len

- The amount to write out >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- read

```java
public abstract void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Since actual text editing is unicode based, this would
generally be the preferred way to read in the data.
Some types of content are stored in an 8-bit form however,
and will favor the InputStream.

**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- write

```java
public abstract void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

Since actual text editing is unicode based, this would
generally be the preferred way to write the data.
Some types of content are stored in an 8-bit form however,
and will favor the OutputStream.

**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content >= 0.
**Parameters:** len

- The amount to write out >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### Method Detail

clone

```java
public
Object
clone()
```

Creates a copy of the editor kit. This is implemented
to use

Object.clone()

. If the kit cannot be cloned,
null is returned.

**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a copy of the editor kit. This is implemented
to use

Object.clone()

. If the kit cannot be cloned,
null is returned.

install

```java
public void install​(
JEditorPane
c)
```

Called when the kit is being installed into the
a JEditorPane.

**Parameters:** c

- the JEditorPane

---

#### install

public void install​(

JEditorPane

c)

Called when the kit is being installed into the
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

getContentType

```java
public abstract
String
getContentType()
```

Gets the MIME type of the data that this
kit represents support for.

**Returns:** the type

---

#### getContentType

public abstract

String

getContentType()

Gets the MIME type of the data that this
kit represents support for.

getViewFactory

```java
public abstract
ViewFactory
getViewFactory()
```

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

**Returns:** the factory

---

#### getViewFactory

public abstract

ViewFactory

getViewFactory()

Fetches a factory that is suitable for producing
views of any models that are produced by this
kit.

getActions

```java
public abstract
Action
[] getActions()
```

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

**Returns:** the set of actions

---

#### getActions

public abstract

Action

[] getActions()

Fetches the set of commands that can be used
on a text component that is using a model and
view produced by this kit.

createCaret

```java
public abstract
Caret
createCaret()
```

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

**Returns:** the caret

---

#### createCaret

public abstract

Caret

createCaret()

Fetches a caret that can navigate through views
produced by the associated ViewFactory.

createDefaultDocument

```java
public abstract
Document
createDefaultDocument()
```

Creates an uninitialized text storage model
that is appropriate for this type of editor.

**Returns:** the model

---

#### createDefaultDocument

public abstract

Document

createDefaultDocument()

Creates an uninitialized text storage model
that is appropriate for this type of editor.

read

```java
public abstract void read​(
InputStream
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### read

public abstract void read​(

InputStream

in,

Document

doc,
int pos)
throws

IOException

,

BadLocationException

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

write

```java
public abstract void write​(
OutputStream
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content from >= 0.
**Parameters:** len

- The amount to write out >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### write

public abstract void write​(

OutputStream

out,

Document

doc,
int pos,
int len)
throws

IOException

,

BadLocationException

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

read

```java
public abstract void read​(
Reader
in,

Document
doc,
int pos)
throws
IOException
,

BadLocationException
```

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Since actual text editing is unicode based, this would
generally be the preferred way to read in the data.
Some types of content are stored in an 8-bit form however,
and will favor the InputStream.

**Parameters:** in

- The stream to read from
**Parameters:** doc

- The destination for the insertion.
**Parameters:** pos

- The location in the document to place the
content >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### read

public abstract void read​(

Reader

in,

Document

doc,
int pos)
throws

IOException

,

BadLocationException

Inserts content from the given stream which is expected
to be in a format appropriate for this kind of content
handler.

Since actual text editing is unicode based, this would
generally be the preferred way to read in the data.
Some types of content are stored in an 8-bit form however,
and will favor the InputStream.

Since actual text editing is unicode based, this would
generally be the preferred way to read in the data.
Some types of content are stored in an 8-bit form however,
and will favor the InputStream.

write

```java
public abstract void write​(
Writer
out,

Document
doc,
int pos,
int len)
throws
IOException
,

BadLocationException
```

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

Since actual text editing is unicode based, this would
generally be the preferred way to write the data.
Some types of content are stored in an 8-bit form however,
and will favor the OutputStream.

**Parameters:** out

- The stream to write to
**Parameters:** doc

- The source for the write.
**Parameters:** pos

- The location in the document to fetch the
content >= 0.
**Parameters:** len

- The amount to write out >= 0.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### write

public abstract void write​(

Writer

out,

Document

doc,
int pos,
int len)
throws

IOException

,

BadLocationException

Writes content from a document to the given stream
in a format appropriate for this kind of content handler.

Since actual text editing is unicode based, this would
generally be the preferred way to write the data.
Some types of content are stored in an 8-bit form however,
and will favor the OutputStream.

Since actual text editing is unicode based, this would
generally be the preferred way to write the data.
Some types of content are stored in an 8-bit form however,
and will favor the OutputStream.

---

