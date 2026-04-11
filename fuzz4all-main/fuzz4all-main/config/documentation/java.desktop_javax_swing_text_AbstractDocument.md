# Class AbstractDocument

**Source:** `java.desktop\javax\swing\text\AbstractDocument.html`

### Class Description

```java
public abstract class
AbstractDocument

extends
Object

implements
Document
,
Serializable
```

An implementation of the document interface to serve as a
basis for implementing various kinds of documents. At this
level there is very little policy, so there is a corresponding
increase in difficulty of use.

This class implements a locking mechanism for the document. It
allows multiple readers or one writer, and writers must wait until
all observers of the document have been notified of a previous
change before beginning another mutation to the document. The
read lock is acquired and released using the

render

method. A write lock is acquired by the methods that mutate the
document, and are held for the duration of the method call.
Notification is done on the thread that produced the mutation,
and the thread has full read access to the document for the
duration of the notification, but other readers are kept out
until the notification has finished. The notification is a
beans event notification which does not allow any further
mutations until all listeners have been notified.

Any models subclassed from this class and used in conjunction
with a text component that has a look and feel implementation
that is derived from BasicTextUI may be safely updated
asynchronously, because all access to the View hierarchy
is serialized by BasicTextUI if the document is of type

AbstractDocument

. The locking assumes that an
independent thread will access the View hierarchy only from
the DocumentListener methods, and that there will be only
one event thread active at a time.

If concurrency support is desired, there are the following
additional implications. The code path for any DocumentListener
implementation and any UndoListener implementation must be threadsafe,
and not access the component lock if trying to be safe from deadlocks.
The

repaint

and

revalidate

methods
on JComponent are safe.

AbstractDocument models an implied break at the end of the document.
Among other things this allows you to position the caret after the last
character. As a result of this,

getLength

returns one less
than the length of the Content. If you create your own Content, be
sure and initialize it to have an additional character. Refer to
StringContent and GapContent for examples of this. Another implication
of this is that Elements that model the implied end character will have
an endOffset == (getLength() + 1). For example, in DefaultStyledDocument

getParagraphElement(getLength()).getEndOffset() == getLength() + 1

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

**All Implemented Interfaces:** Serializable

,

Document

---

### Field Details

#### protected
EventListenerList
listenerList

The event listener list for the document.

---

#### protected static final
String
BAD_LOCATION

Error message to indicate a bad location.

**See Also:**
- Constant Field Values

---

#### public static final
String
ParagraphElementName

Name of elements used to represent paragraphs

**See Also:**
- Constant Field Values

---

#### public static final
String
ContentElementName

Name of elements used to represent content

**See Also:**
- Constant Field Values

---

#### public static final
String
SectionElementName

Name of elements used to hold sections (lines/paragraphs).

**See Also:**
- Constant Field Values

---

#### public static final
String
BidiElementName

Name of elements used to hold a unidirectional run

**See Also:**
- Constant Field Values

---

#### public static final
String
ElementNameAttribute

Name of the attribute used to specify element
names.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected AbstractDocument​(
AbstractDocument.Content
data)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:**
- data

- the content

---

#### protected AbstractDocument​(
AbstractDocument.Content
data,

AbstractDocument.AttributeContext
context)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:**
- data

- the content
- context

- the attribute context

---

### Method Details

#### public
Dictionary
<
Object
,​
Object
> getDocumentProperties()

Supports managing a set of properties. Callers
can use the

documentProperties

dictionary
to annotate the document with document-wide properties.

**Returns:**
- a non-

null

Dictionary

**See Also:**
- setDocumentProperties(java.util.Dictionary<java.lang.Object, java.lang.Object>)

---

#### public void setDocumentProperties​(
Dictionary
<
Object
,​
Object
> x)

Replaces the document properties dictionary for this document.

**Parameters:**
- x

- the new dictionary

**See Also:**
- getDocumentProperties()

---

#### protected void fireInsertUpdate​(
DocumentEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event

**See Also:**
- EventListenerList

---

#### protected void fireChangedUpdate​(
DocumentEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event

**See Also:**
- EventListenerList

---

#### protected void fireRemoveUpdate​(
DocumentEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event

**See Also:**
- EventListenerList

---

#### protected void fireUndoableEditUpdate​(
UndoableEditEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:**
- e

- the event

**See Also:**
- EventListenerList

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a
document

d

for its document listeners with the following code:

```java
DocumentListener[] mls = (DocumentListener[])(d.getListeners(DocumentListener.class));
```

If no such listeners exist, this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- getDocumentListeners()

,

getUndoableEditListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the listener type

---

#### public int getAsynchronousLoadPriority()

Gets the asynchronous loading priority. If less than zero,
the document should not be loaded asynchronously.

**Returns:**
- the asynchronous loading priority, or

-1

if the document should not be loaded asynchronously

---

#### public void setAsynchronousLoadPriority​(int p)

Sets the asynchronous loading priority.

**Parameters:**
- p

- the new asynchronous loading priority; a value
less than zero indicates that the document should not be
loaded asynchronously

---

#### public void setDocumentFilter​(
DocumentFilter
filter)

Sets the

DocumentFilter

. The

DocumentFilter

is passed

insert

and

remove

to conditionally
allow inserting/deleting of the text. A

null

value
indicates that no filtering will occur.

**Parameters:**
- filter

- the

DocumentFilter

used to constrain text

**See Also:**
- getDocumentFilter()

**Since:**
- 1.4

---

#### public
DocumentFilter
getDocumentFilter()

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal. A

null

return value
implies no filtering is to occur.

**Returns:**
- the DocumentFilter

**See Also:**
- setDocumentFilter(javax.swing.text.DocumentFilter)

**Since:**
- 1.4

---

#### public void render​(
Runnable
r)

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

This is implemented to acquire a read lock for the duration
of the runnables execution. There may be multiple runnables
executing at the same time, and all writers will be blocked
while there are active rendering runnables. If the runnable
throws an exception, its lock will be safely released.
There is no protection against a runnable that never exits,
which will effectively leave the document locked for it's
lifetime.

If the given runnable attempts to make any mutations in
this implementation, a deadlock will occur. There is
no tracking of individual rendering threads to enable
detecting this situation, but a subclass could incur
the overhead of tracking them and throwing an error.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- render

in interface

Document

**Parameters:**
- r

- the renderer to execute

---

#### public int getLength()

Returns the length of the data. This is the number of
characters of content that represents the users data.

**Specified by:**
- getLength

in interface

Document

**Returns:**
- the length >= 0

**See Also:**
- Document.getLength()

---

#### public void addDocumentListener​(
DocumentListener
listener)

Adds a document listener for notification of any changes.

**Specified by:**
- addDocumentListener

in interface

Document

**Parameters:**
- listener

- the

DocumentListener

to add

**See Also:**
- Document.addDocumentListener(javax.swing.event.DocumentListener)

---

#### public void removeDocumentListener​(
DocumentListener
listener)

Removes a document listener.

**Specified by:**
- removeDocumentListener

in interface

Document

**Parameters:**
- listener

- the

DocumentListener

to remove

**See Also:**
- Document.removeDocumentListener(javax.swing.event.DocumentListener)

---

#### public
DocumentListener
[] getDocumentListeners()

Returns an array of all the document listeners
registered on this document.

**Returns:**
- all of this document's

DocumentListener

s
or an empty array if no document listeners are
currently registered

**See Also:**
- addDocumentListener(javax.swing.event.DocumentListener)

,

removeDocumentListener(javax.swing.event.DocumentListener)

**Since:**
- 1.4

---

#### public void addUndoableEditListener​(
UndoableEditListener
listener)

Adds an undo listener for notification of any changes.
Undo/Redo operations performed on the

UndoableEdit

will cause the appropriate DocumentEvent to be fired to keep
the view(s) in sync with the model.

**Specified by:**
- addUndoableEditListener

in interface

Document

**Parameters:**
- listener

- the

UndoableEditListener

to add

**See Also:**
- Document.addUndoableEditListener(javax.swing.event.UndoableEditListener)

---

#### public void removeUndoableEditListener​(
UndoableEditListener
listener)

Removes an undo listener.

**Specified by:**
- removeUndoableEditListener

in interface

Document

**Parameters:**
- listener

- the

UndoableEditListener

to remove

**See Also:**
- Document.removeDocumentListener(javax.swing.event.DocumentListener)

---

#### public
UndoableEditListener
[] getUndoableEditListeners()

Returns an array of all the undoable edit listeners
registered on this document.

**Returns:**
- all of this document's

UndoableEditListener

s
or an empty array if no undoable edit listeners are
currently registered

**See Also:**
- addUndoableEditListener(javax.swing.event.UndoableEditListener)

,

removeUndoableEditListener(javax.swing.event.UndoableEditListener)

**Since:**
- 1.4

---

#### public final
Object
getProperty​(
Object
key)

A convenience method for looking up a property value. It is
equivalent to:

```java
getDocumentProperties().get(key);
```

**Specified by:**
- getProperty

in interface

Document

**Parameters:**
- key

- the non-

null

property key

**Returns:**
- the value of this property or

null

**See Also:**
- getDocumentProperties()

---

#### public final void putProperty​(
Object
key,

Object
value)

A convenience method for storing up a property value. It is
equivalent to:

```java
getDocumentProperties().put(key, value);
```

If

value

is

null

this method will
remove the property.

**Specified by:**
- putProperty

in interface

Document

**Parameters:**
- key

- the non-

null

key
- value

- the property value

**See Also:**
- getDocumentProperties()

---

#### public void remove​(int offs,
int len)
throws
BadLocationException

Removes some content from the document.
Removing content causes a write lock to be held while the
actual changes are taking place. Observers are notified
of the change on the thread that called this method.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- remove

in interface

Document

**Parameters:**
- offs

- the starting offset >= 0
- len

- the number of characters to remove >= 0

**Throws:**
- BadLocationException

- the given remove position is not a valid
position within the document

**See Also:**
- Document.remove(int, int)

---

#### public void replace​(int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.
It is up to the implementation as to how this is implemented, some
implementations may treat this as two distinct operations: a remove
followed by an insert, others may treat the replace as one atomic
operation.

**Parameters:**
- offset

- index of child element
- length

- length of text to delete, may be 0 indicating don't
delete anything
- text

- text to insert,

null

indicates no text to insert
- attrs

- AttributeSet indicating attributes of inserted text,

null

is legal, and typically treated as an empty attributeset,
but exact interpretation is left to the subclass

**Throws:**
- BadLocationException

- the given position is not a valid
position within the document

**Since:**
- 1.4

---

#### public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- insertString

in interface

Document

**Parameters:**
- offs

- the starting offset >= 0
- str

- the string to insert; does nothing with null/empty strings
- a

- the attributes for the inserted content

**Throws:**
- BadLocationException

- the given insert position is not a valid
position within the document

**See Also:**
- Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

---

#### public
String
getText​(int offset,
int length)
throws
BadLocationException

Gets a sequence of text from the document.

**Specified by:**
- getText

in interface

Document

**Parameters:**
- offset

- the starting offset >= 0
- length

- the number of characters to retrieve >= 0

**Returns:**
- the text

**Throws:**
- BadLocationException

- the range given includes a position
that is not a valid position within the document

**See Also:**
- Document.getText(int, int)

---

#### public void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do something with text
nleft -= text.count;
offs += text.count;
}
```

**Specified by:**
- getText

in interface

Document

**Parameters:**
- offset

- the starting offset >= 0
- length

- the number of characters to retrieve >= 0
- txt

- the Segment object to retrieve the text into

**Throws:**
- BadLocationException

- the range given includes a position
that is not a valid position within the document

---

#### public
Position
createPosition​(int offs)
throws
BadLocationException

Returns a position that will track change as the document
is altered.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- createPosition

in interface

Document

**Parameters:**
- offs

- the position in the model >= 0

**Returns:**
- the position

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

**See Also:**
- Document.createPosition(int)

---

#### public final
Position
getStartPosition()

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Specified by:**
- getStartPosition

in interface

Document

**Returns:**
- the position

---

#### public final
Position
getEndPosition()

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Specified by:**
- getEndPosition

in interface

Document

**Returns:**
- the position

---

#### public
Element
[] getRootElements()

Gets all root elements defined. Typically, there
will only be one so the default implementation
is to return the default root element.

**Specified by:**
- getRootElements

in interface

Document

**Returns:**
- the root element

---

#### public abstract
Element
getDefaultRootElement()

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

**Specified by:**
- getDefaultRootElement

in interface

Document

**Returns:**
- the root element

**See Also:**
- Document.getDefaultRootElement()

---

#### public
Element
getBidiRootElement()

Returns the root element of the bidirectional structure for this
document. Its children represent character runs with a given
Unicode bidi level.

**Returns:**
- the root element of the bidirectional structure for this
document

---

#### public abstract
Element
getParagraphElement​(int pos)

Get the paragraph element containing the given position. Sub-classes
must define for themselves what exactly constitutes a paragraph. They
should keep in mind however that a paragraph should at least be the
unit of text over which to run the Unicode bidirectional algorithm.

**Parameters:**
- pos

- the starting offset >= 0

**Returns:**
- the element

---

#### protected final
AbstractDocument.AttributeContext
getAttributeContext()

Fetches the context for managing attributes. This
method effectively establishes the strategy used
for compressing AttributeSet information.

**Returns:**
- the context

---

#### protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)

Updates document structure as a result of text insertion. This
will happen within a write lock. If a subclass of
this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:**
- chng

- a description of the change
- attr

- the attributes for the change

---

#### protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)

Updates any document structure as a result of text removal. This
method is called before the text is actually removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:**
- chng

- a description of the change

---

#### protected void postRemoveUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)

Updates any document structure as a result of text removal. This
method is called after the text has been removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:**
- chng

- a description of the change

---

#### public void dump​(
PrintStream
out)

Gives a diagnostic dump.

**Parameters:**
- out

- the output stream

---

#### protected final
AbstractDocument.Content
getContent()

Gets the content for the document.

**Returns:**
- the content

---

#### protected
Element
createLeafElement​(
Element
parent,

AttributeSet
a,
int p0,
int p1)

Creates a document leaf element.
Hook through which elements are created to represent the
document structure. Because this implementation keeps
structure and content separate, elements grow automatically
when content is extended so splits of existing elements
follow. The document itself gets to decide how to generate
elements to give flexibility in the type of elements used.

**Parameters:**
- parent

- the parent element
- a

- the attributes for the element
- p0

- the beginning of the range >= 0
- p1

- the end of the range >= p0

**Returns:**
- the new element

---

#### protected
Element
createBranchElement​(
Element
parent,

AttributeSet
a)

Creates a document branch element, that can contain other elements.

**Parameters:**
- parent

- the parent element
- a

- the attributes

**Returns:**
- the element

---

#### protected final
Thread
getCurrentWriter()

Fetches the current writing thread if there is one.
This can be used to distinguish whether a method is
being called as part of an existing modification or
if a lock needs to be acquired and a new transaction
started.

**Returns:**
- the thread actively modifying the document
or

null

if there are no modifications in progress

---

#### protected final void writeLock()

Acquires a lock to begin mutating the document this lock
protects. There can be no writing, notification of changes, or
reading going on in order to gain the lock. Additionally a thread is
allowed to gain more than one

writeLock

,
as long as it doesn't attempt to gain additional

writeLock

s
from within document notification. Attempting to gain a

writeLock

from within a DocumentListener notification will
result in an

IllegalStateException

. The ability
to obtain more than one

writeLock

per thread allows
subclasses to gain a writeLock, perform a number of operations, then
release the lock.

Calls to

writeLock

must be balanced with calls to

writeUnlock

, else the

Document

will be left in a locked state so that no
reading or writing can be done.

**Throws:**
- IllegalStateException

- thrown on illegal lock
attempt. If the document is implemented properly, this can
only happen if a document listener attempts to mutate the
document. This situation violates the bean event model
where order of delivery is not guaranteed and all listeners
should be notified before further mutations are allowed.

---

#### protected final void writeUnlock()

Releases a write lock previously obtained via

writeLock

.
After decrementing the lock count if there are no outstanding locks
this will allow a new writer, or readers.

**See Also:**
- writeLock()

---

#### public final void readLock()

Acquires a lock to begin reading some state from the
document. There can be multiple readers at the same time.
Writing blocks the readers until notification of the change
to the listeners has been completed. This method should
be used very carefully to avoid unintended compromise
of the document. It should always be balanced with a

readUnlock

.

**See Also:**
- readUnlock()

---

#### public final void readUnlock()

Does a read unlock. This signals that one
of the readers is done. If there are no more readers
then writing can begin again. This should be balanced
with a readLock, and should occur in a finally statement
so that the balance is guaranteed. The following is an
example.

```java
readLock();
try {
// do something
} finally {
readUnlock();
}
```

**See Also:**
- readLock()

---

### Additional Sections

#### Class AbstractDocument

java.lang.Object

- javax.swing.text.AbstractDocument

javax.swing.text.AbstractDocument

**All Implemented Interfaces:** Serializable

,

Document

**Direct Known Subclasses:** DefaultStyledDocument

,

PlainDocument

```java
public abstract class
AbstractDocument

extends
Object

implements
Document
,
Serializable
```

An implementation of the document interface to serve as a
basis for implementing various kinds of documents. At this
level there is very little policy, so there is a corresponding
increase in difficulty of use.

This class implements a locking mechanism for the document. It
allows multiple readers or one writer, and writers must wait until
all observers of the document have been notified of a previous
change before beginning another mutation to the document. The
read lock is acquired and released using the

render

method. A write lock is acquired by the methods that mutate the
document, and are held for the duration of the method call.
Notification is done on the thread that produced the mutation,
and the thread has full read access to the document for the
duration of the notification, but other readers are kept out
until the notification has finished. The notification is a
beans event notification which does not allow any further
mutations until all listeners have been notified.

Any models subclassed from this class and used in conjunction
with a text component that has a look and feel implementation
that is derived from BasicTextUI may be safely updated
asynchronously, because all access to the View hierarchy
is serialized by BasicTextUI if the document is of type

AbstractDocument

. The locking assumes that an
independent thread will access the View hierarchy only from
the DocumentListener methods, and that there will be only
one event thread active at a time.

If concurrency support is desired, there are the following
additional implications. The code path for any DocumentListener
implementation and any UndoListener implementation must be threadsafe,
and not access the component lock if trying to be safe from deadlocks.
The

repaint

and

revalidate

methods
on JComponent are safe.

AbstractDocument models an implied break at the end of the document.
Among other things this allows you to position the caret after the last
character. As a result of this,

getLength

returns one less
than the length of the Content. If you create your own Content, be
sure and initialize it to have an additional character. Refer to
StringContent and GapContent for examples of this. Another implication
of this is that Elements that model the implied end character will have
an endOffset == (getLength() + 1). For example, in DefaultStyledDocument

getParagraphElement(getLength()).getEndOffset() == getLength() + 1

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

**See Also:** Serialized Form

public abstract class

AbstractDocument

extends

Object

implements

Document

,

Serializable

An implementation of the document interface to serve as a
basis for implementing various kinds of documents. At this
level there is very little policy, so there is a corresponding
increase in difficulty of use.

This class implements a locking mechanism for the document. It
allows multiple readers or one writer, and writers must wait until
all observers of the document have been notified of a previous
change before beginning another mutation to the document. The
read lock is acquired and released using the

render

method. A write lock is acquired by the methods that mutate the
document, and are held for the duration of the method call.
Notification is done on the thread that produced the mutation,
and the thread has full read access to the document for the
duration of the notification, but other readers are kept out
until the notification has finished. The notification is a
beans event notification which does not allow any further
mutations until all listeners have been notified.

Any models subclassed from this class and used in conjunction
with a text component that has a look and feel implementation
that is derived from BasicTextUI may be safely updated
asynchronously, because all access to the View hierarchy
is serialized by BasicTextUI if the document is of type

AbstractDocument

. The locking assumes that an
independent thread will access the View hierarchy only from
the DocumentListener methods, and that there will be only
one event thread active at a time.

If concurrency support is desired, there are the following
additional implications. The code path for any DocumentListener
implementation and any UndoListener implementation must be threadsafe,
and not access the component lock if trying to be safe from deadlocks.
The

repaint

and

revalidate

methods
on JComponent are safe.

AbstractDocument models an implied break at the end of the document.
Among other things this allows you to position the caret after the last
character. As a result of this,

getLength

returns one less
than the length of the Content. If you create your own Content, be
sure and initialize it to have an additional character. Refer to
StringContent and GapContent for examples of this. Another implication
of this is that Elements that model the implied end character will have
an endOffset == (getLength() + 1). For example, in DefaultStyledDocument

getParagraphElement(getLength()).getEndOffset() == getLength() + 1

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

This class implements a locking mechanism for the document. It
allows multiple readers or one writer, and writers must wait until
all observers of the document have been notified of a previous
change before beginning another mutation to the document. The
read lock is acquired and released using the

render

method. A write lock is acquired by the methods that mutate the
document, and are held for the duration of the method call.
Notification is done on the thread that produced the mutation,
and the thread has full read access to the document for the
duration of the notification, but other readers are kept out
until the notification has finished. The notification is a
beans event notification which does not allow any further
mutations until all listeners have been notified.

Any models subclassed from this class and used in conjunction
with a text component that has a look and feel implementation
that is derived from BasicTextUI may be safely updated
asynchronously, because all access to the View hierarchy
is serialized by BasicTextUI if the document is of type

AbstractDocument

. The locking assumes that an
independent thread will access the View hierarchy only from
the DocumentListener methods, and that there will be only
one event thread active at a time.

If concurrency support is desired, there are the following
additional implications. The code path for any DocumentListener
implementation and any UndoListener implementation must be threadsafe,
and not access the component lock if trying to be safe from deadlocks.
The

repaint

and

revalidate

methods
on JComponent are safe.

AbstractDocument models an implied break at the end of the document.
Among other things this allows you to position the caret after the last
character. As a result of this,

getLength

returns one less
than the length of the Content. If you create your own Content, be
sure and initialize it to have an additional character. Refer to
StringContent and GapContent for examples of this. Another implication
of this is that Elements that model the implied end character will have
an endOffset == (getLength() + 1). For example, in DefaultStyledDocument

getParagraphElement(getLength()).getEndOffset() == getLength() + 1

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

Any models subclassed from this class and used in conjunction
with a text component that has a look and feel implementation
that is derived from BasicTextUI may be safely updated
asynchronously, because all access to the View hierarchy
is serialized by BasicTextUI if the document is of type

AbstractDocument

. The locking assumes that an
independent thread will access the View hierarchy only from
the DocumentListener methods, and that there will be only
one event thread active at a time.

If concurrency support is desired, there are the following
additional implications. The code path for any DocumentListener
implementation and any UndoListener implementation must be threadsafe,
and not access the component lock if trying to be safe from deadlocks.
The

repaint

and

revalidate

methods
on JComponent are safe.

AbstractDocument models an implied break at the end of the document.
Among other things this allows you to position the caret after the last
character. As a result of this,

getLength

returns one less
than the length of the Content. If you create your own Content, be
sure and initialize it to have an additional character. Refer to
StringContent and GapContent for examples of this. Another implication
of this is that Elements that model the implied end character will have
an endOffset == (getLength() + 1). For example, in DefaultStyledDocument

getParagraphElement(getLength()).getEndOffset() == getLength() + 1

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

If concurrency support is desired, there are the following
additional implications. The code path for any DocumentListener
implementation and any UndoListener implementation must be threadsafe,
and not access the component lock if trying to be safe from deadlocks.
The

repaint

and

revalidate

methods
on JComponent are safe.

AbstractDocument models an implied break at the end of the document.
Among other things this allows you to position the caret after the last
character. As a result of this,

getLength

returns one less
than the length of the Content. If you create your own Content, be
sure and initialize it to have an additional character. Refer to
StringContent and GapContent for examples of this. Another implication
of this is that Elements that model the implied end character will have
an endOffset == (getLength() + 1). For example, in DefaultStyledDocument

getParagraphElement(getLength()).getEndOffset() == getLength() + 1

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

AbstractDocument models an implied break at the end of the document.
Among other things this allows you to position the caret after the last
character. As a result of this,

getLength

returns one less
than the length of the Content. If you create your own Content, be
sure and initialize it to have an additional character. Refer to
StringContent and GapContent for examples of this. Another implication
of this is that Elements that model the implied end character will have
an endOffset == (getLength() + 1). For example, in DefaultStyledDocument

getParagraphElement(getLength()).getEndOffset() == getLength() + 1

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

Nested Classes

Modifier and Type

Class

Description

class

AbstractDocument.AbstractElement

Implements the abstract part of an element.

static interface

AbstractDocument.AttributeContext

An interface that can be used to allow MutableAttributeSet
implementations to use pluggable attribute compression
techniques.

class

AbstractDocument.BranchElement

Implements a composite element that contains other elements.

static interface

AbstractDocument.Content

Interface to describe a sequence of character content that
can be edited.

class

AbstractDocument.DefaultDocumentEvent

Stores document changes as the document is being
modified.

static class

AbstractDocument.ElementEdit

An implementation of ElementChange that can be added to the document
event.

class

AbstractDocument.LeafElement

Implements an element that directly represents content of
some kind.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

String

BAD_LOCATION

Error message to indicate a bad location.

static

String

BidiElementName

Name of elements used to hold a unidirectional run

static

String

ContentElementName

Name of elements used to represent content

static

String

ElementNameAttribute

Name of the attribute used to specify element
names.

protected

EventListenerList

listenerList

The event listener list for the document.

static

String

ParagraphElementName

Name of elements used to represent paragraphs

static

String

SectionElementName

Name of elements used to hold sections (lines/paragraphs).

- Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractDocument

​(

AbstractDocument.Content

data)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

protected

AbstractDocument

​(

AbstractDocument.Content

data,

AbstractDocument.AttributeContext

context)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDocumentListener

​(

DocumentListener

listener)

Adds a document listener for notification of any changes.

void

addUndoableEditListener

​(

UndoableEditListener

listener)

Adds an undo listener for notification of any changes.

protected

Element

createBranchElement

​(

Element

parent,

AttributeSet

a)

Creates a document branch element, that can contain other elements.

protected

Element

createLeafElement

​(

Element

parent,

AttributeSet

a,
int p0,
int p1)

Creates a document leaf element.

Position

createPosition

​(int offs)

Returns a position that will track change as the document
is altered.

void

dump

​(

PrintStream

out)

Gives a diagnostic dump.

protected void

fireChangedUpdate

​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireInsertUpdate

​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireRemoveUpdate

​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireUndoableEditUpdate

​(

UndoableEditEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

int

getAsynchronousLoadPriority

()

Gets the asynchronous loading priority.

protected

AbstractDocument.AttributeContext

getAttributeContext

()

Fetches the context for managing attributes.

Element

getBidiRootElement

()

Returns the root element of the bidirectional structure for this
document.

protected

AbstractDocument.Content

getContent

()

Gets the content for the document.

protected

Thread

getCurrentWriter

()

Fetches the current writing thread if there is one.

abstract

Element

getDefaultRootElement

()

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

DocumentFilter

getDocumentFilter

()

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal.

DocumentListener

[]

getDocumentListeners

()

Returns an array of all the document listeners
registered on this document.

Dictionary

<

Object

,​

Object

>

getDocumentProperties

()

Supports managing a set of properties.

Position

getEndPosition

()

Returns a position that represents the end of the document.

int

getLength

()

Returns the length of the data.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

abstract

Element

getParagraphElement

​(int pos)

Get the paragraph element containing the given position.

Object

getProperty

​(

Object

key)

A convenience method for looking up a property value.

Element

[]

getRootElements

()

Gets all root elements defined.

Position

getStartPosition

()

Returns a position that represents the start of the document.

String

getText

​(int offset,
int length)

Gets a sequence of text from the document.

void

getText

​(int offset,
int length,

Segment

txt)

Fetches the text contained within the given portion
of the document.

UndoableEditListener

[]

getUndoableEditListeners

()

Returns an array of all the undoable edit listeners
registered on this document.

void

insertString

​(int offs,

String

str,

AttributeSet

a)

Inserts some content into the document.

protected void

insertUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion.

protected void

postRemoveUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal.

void

putProperty

​(

Object

key,

Object

value)

A convenience method for storing up a property value.

void

readLock

()

Acquires a lock to begin reading some state from the
document.

void

readUnlock

()

Does a read unlock.

void

remove

​(int offs,
int len)

Removes some content from the document.

void

removeDocumentListener

​(

DocumentListener

listener)

Removes a document listener.

void

removeUndoableEditListener

​(

UndoableEditListener

listener)

Removes an undo listener.

protected void

removeUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal.

void

render

​(

Runnable

r)

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.

void

replace

​(int offset,
int length,

String

text,

AttributeSet

attrs)

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

void

setAsynchronousLoadPriority

​(int p)

Sets the asynchronous loading priority.

void

setDocumentFilter

​(

DocumentFilter

filter)

Sets the

DocumentFilter

.

void

setDocumentProperties

​(

Dictionary

<

Object

,​

Object

> x)

Replaces the document properties dictionary for this document.

protected void

writeLock

()

Acquires a lock to begin mutating the document this lock
protects.

protected void

writeUnlock

()

Releases a write lock previously obtained via

writeLock

.

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

Nested Classes

Modifier and Type

Class

Description

class

AbstractDocument.AbstractElement

Implements the abstract part of an element.

static interface

AbstractDocument.AttributeContext

An interface that can be used to allow MutableAttributeSet
implementations to use pluggable attribute compression
techniques.

class

AbstractDocument.BranchElement

Implements a composite element that contains other elements.

static interface

AbstractDocument.Content

Interface to describe a sequence of character content that
can be edited.

class

AbstractDocument.DefaultDocumentEvent

Stores document changes as the document is being
modified.

static class

AbstractDocument.ElementEdit

An implementation of ElementChange that can be added to the document
event.

class

AbstractDocument.LeafElement

Implements an element that directly represents content of
some kind.

---

#### Nested Class Summary

Implements the abstract part of an element.

An interface that can be used to allow MutableAttributeSet
implementations to use pluggable attribute compression
techniques.

Implements a composite element that contains other elements.

Interface to describe a sequence of character content that
can be edited.

Stores document changes as the document is being
modified.

An implementation of ElementChange that can be added to the document
event.

Implements an element that directly represents content of
some kind.

Field Summary

Fields

Modifier and Type

Field

Description

protected static

String

BAD_LOCATION

Error message to indicate a bad location.

static

String

BidiElementName

Name of elements used to hold a unidirectional run

static

String

ContentElementName

Name of elements used to represent content

static

String

ElementNameAttribute

Name of the attribute used to specify element
names.

protected

EventListenerList

listenerList

The event listener list for the document.

static

String

ParagraphElementName

Name of elements used to represent paragraphs

static

String

SectionElementName

Name of elements used to hold sections (lines/paragraphs).

- Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

---

#### Field Summary

Error message to indicate a bad location.

Name of elements used to hold a unidirectional run

Name of elements used to represent content

Name of the attribute used to specify element
names.

The event listener list for the document.

Name of elements used to represent paragraphs

Name of elements used to hold sections (lines/paragraphs).

Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

---

#### Fields declared in interface javax.swing.text. Document

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractDocument

​(

AbstractDocument.Content

data)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

protected

AbstractDocument

​(

AbstractDocument.Content

data,

AbstractDocument.AttributeContext

context)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

---

#### Constructor Summary

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addDocumentListener

​(

DocumentListener

listener)

Adds a document listener for notification of any changes.

void

addUndoableEditListener

​(

UndoableEditListener

listener)

Adds an undo listener for notification of any changes.

protected

Element

createBranchElement

​(

Element

parent,

AttributeSet

a)

Creates a document branch element, that can contain other elements.

protected

Element

createLeafElement

​(

Element

parent,

AttributeSet

a,
int p0,
int p1)

Creates a document leaf element.

Position

createPosition

​(int offs)

Returns a position that will track change as the document
is altered.

void

dump

​(

PrintStream

out)

Gives a diagnostic dump.

protected void

fireChangedUpdate

​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireInsertUpdate

​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireRemoveUpdate

​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireUndoableEditUpdate

​(

UndoableEditEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

int

getAsynchronousLoadPriority

()

Gets the asynchronous loading priority.

protected

AbstractDocument.AttributeContext

getAttributeContext

()

Fetches the context for managing attributes.

Element

getBidiRootElement

()

Returns the root element of the bidirectional structure for this
document.

protected

AbstractDocument.Content

getContent

()

Gets the content for the document.

protected

Thread

getCurrentWriter

()

Fetches the current writing thread if there is one.

abstract

Element

getDefaultRootElement

()

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

DocumentFilter

getDocumentFilter

()

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal.

DocumentListener

[]

getDocumentListeners

()

Returns an array of all the document listeners
registered on this document.

Dictionary

<

Object

,​

Object

>

getDocumentProperties

()

Supports managing a set of properties.

Position

getEndPosition

()

Returns a position that represents the end of the document.

int

getLength

()

Returns the length of the data.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

abstract

Element

getParagraphElement

​(int pos)

Get the paragraph element containing the given position.

Object

getProperty

​(

Object

key)

A convenience method for looking up a property value.

Element

[]

getRootElements

()

Gets all root elements defined.

Position

getStartPosition

()

Returns a position that represents the start of the document.

String

getText

​(int offset,
int length)

Gets a sequence of text from the document.

void

getText

​(int offset,
int length,

Segment

txt)

Fetches the text contained within the given portion
of the document.

UndoableEditListener

[]

getUndoableEditListeners

()

Returns an array of all the undoable edit listeners
registered on this document.

void

insertString

​(int offs,

String

str,

AttributeSet

a)

Inserts some content into the document.

protected void

insertUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion.

protected void

postRemoveUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal.

void

putProperty

​(

Object

key,

Object

value)

A convenience method for storing up a property value.

void

readLock

()

Acquires a lock to begin reading some state from the
document.

void

readUnlock

()

Does a read unlock.

void

remove

​(int offs,
int len)

Removes some content from the document.

void

removeDocumentListener

​(

DocumentListener

listener)

Removes a document listener.

void

removeUndoableEditListener

​(

UndoableEditListener

listener)

Removes an undo listener.

protected void

removeUpdate

​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal.

void

render

​(

Runnable

r)

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.

void

replace

​(int offset,
int length,

String

text,

AttributeSet

attrs)

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

void

setAsynchronousLoadPriority

​(int p)

Sets the asynchronous loading priority.

void

setDocumentFilter

​(

DocumentFilter

filter)

Sets the

DocumentFilter

.

void

setDocumentProperties

​(

Dictionary

<

Object

,​

Object

> x)

Replaces the document properties dictionary for this document.

protected void

writeLock

()

Acquires a lock to begin mutating the document this lock
protects.

protected void

writeUnlock

()

Releases a write lock previously obtained via

writeLock

.

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

Adds a document listener for notification of any changes.

Adds an undo listener for notification of any changes.

Creates a document branch element, that can contain other elements.

Creates a document leaf element.

Returns a position that will track change as the document
is altered.

Gives a diagnostic dump.

Notifies all listeners that have registered interest for
notification on this event type.

Gets the asynchronous loading priority.

Fetches the context for managing attributes.

Returns the root element of the bidirectional structure for this
document.

Gets the content for the document.

Fetches the current writing thread if there is one.

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal.

Returns an array of all the document listeners
registered on this document.

Supports managing a set of properties.

Returns a position that represents the end of the document.

Returns the length of the data.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

Get the paragraph element containing the given position.

A convenience method for looking up a property value.

Gets all root elements defined.

Returns a position that represents the start of the document.

Gets a sequence of text from the document.

Fetches the text contained within the given portion
of the document.

Returns an array of all the undoable edit listeners
registered on this document.

Inserts some content into the document.

Updates document structure as a result of text insertion.

Updates any document structure as a result of text removal.

A convenience method for storing up a property value.

Acquires a lock to begin reading some state from the
document.

Does a read unlock.

Removes some content from the document.

Removes a document listener.

Removes an undo listener.

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

Sets the asynchronous loading priority.

Sets the

DocumentFilter

.

Replaces the document properties dictionary for this document.

Acquires a lock to begin mutating the document this lock
protects.

Releases a write lock previously obtained via

writeLock

.

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

============ FIELD DETAIL ===========

- Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The event listener list for the document.

- BAD_LOCATION

```java
protected static final
String
BAD_LOCATION
```

Error message to indicate a bad location.

**See Also:** Constant Field Values

- ParagraphElementName

```java
public static final
String
ParagraphElementName
```

Name of elements used to represent paragraphs

**See Also:** Constant Field Values

- ContentElementName

```java
public static final
String
ContentElementName
```

Name of elements used to represent content

**See Also:** Constant Field Values

- SectionElementName

```java
public static final
String
SectionElementName
```

Name of elements used to hold sections (lines/paragraphs).

**See Also:** Constant Field Values

- BidiElementName

```java
public static final
String
BidiElementName
```

Name of elements used to hold a unidirectional run

**See Also:** Constant Field Values

- ElementNameAttribute

```java
public static final
String
ElementNameAttribute
```

Name of the attribute used to specify element
names.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractDocument

```java
protected AbstractDocument​(
AbstractDocument.Content
data)
```

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:** data

- the content

- AbstractDocument

```java
protected AbstractDocument​(
AbstractDocument.Content
data,

AbstractDocument.AttributeContext
context)
```

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:** data

- the content
**Parameters:** context

- the attribute context

============ METHOD DETAIL ==========

- Method Detail

- getDocumentProperties

```java
public
Dictionary
<
Object
,​
Object
> getDocumentProperties()
```

Supports managing a set of properties. Callers
can use the

documentProperties

dictionary
to annotate the document with document-wide properties.

**Returns:** a non-

null

Dictionary
**See Also:** setDocumentProperties(java.util.Dictionary<java.lang.Object, java.lang.Object>)

- setDocumentProperties

```java
public void setDocumentProperties​(
Dictionary
<
Object
,​
Object
> x)
```

Replaces the document properties dictionary for this document.

**Parameters:** x

- the new dictionary
**See Also:** getDocumentProperties()

- fireInsertUpdate

```java
protected void fireInsertUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- fireChangedUpdate

```java
protected void fireChangedUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- fireRemoveUpdate

```java
protected void fireRemoveUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- fireUndoableEditUpdate

```java
protected void fireUndoableEditUpdate​(
UndoableEditEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a
document

d

for its document listeners with the following code:

```java
DocumentListener[] mls = (DocumentListener[])(d.getListeners(DocumentListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getDocumentListeners()

,

getUndoableEditListeners()

- getAsynchronousLoadPriority

```java
public int getAsynchronousLoadPriority()
```

Gets the asynchronous loading priority. If less than zero,
the document should not be loaded asynchronously.

**Returns:** the asynchronous loading priority, or

-1

if the document should not be loaded asynchronously

- setAsynchronousLoadPriority

```java
public void setAsynchronousLoadPriority​(int p)
```

Sets the asynchronous loading priority.

**Parameters:** p

- the new asynchronous loading priority; a value
less than zero indicates that the document should not be
loaded asynchronously

- setDocumentFilter

```java
public void setDocumentFilter​(
DocumentFilter
filter)
```

Sets the

DocumentFilter

. The

DocumentFilter

is passed

insert

and

remove

to conditionally
allow inserting/deleting of the text. A

null

value
indicates that no filtering will occur.

**Parameters:** filter

- the

DocumentFilter

used to constrain text
**Since:** 1.4
**See Also:** getDocumentFilter()

- getDocumentFilter

```java
public
DocumentFilter
getDocumentFilter()
```

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal. A

null

return value
implies no filtering is to occur.

**Returns:** the DocumentFilter
**Since:** 1.4
**See Also:** setDocumentFilter(javax.swing.text.DocumentFilter)

- render

```java
public void render​(
Runnable
r)
```

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

This is implemented to acquire a read lock for the duration
of the runnables execution. There may be multiple runnables
executing at the same time, and all writers will be blocked
while there are active rendering runnables. If the runnable
throws an exception, its lock will be safely released.
There is no protection against a runnable that never exits,
which will effectively leave the document locked for it's
lifetime.

If the given runnable attempts to make any mutations in
this implementation, a deadlock will occur. There is
no tracking of individual rendering threads to enable
detecting this situation, but a subclass could incur
the overhead of tracking them and throwing an error.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** render

in interface

Document
**Parameters:** r

- the renderer to execute

- getLength

```java
public int getLength()
```

Returns the length of the data. This is the number of
characters of content that represents the users data.

**Specified by:** getLength

in interface

Document
**Returns:** the length >= 0
**See Also:** Document.getLength()

- addDocumentListener

```java
public void addDocumentListener​(
DocumentListener
listener)
```

Adds a document listener for notification of any changes.

**Specified by:** addDocumentListener

in interface

Document
**Parameters:** listener

- the

DocumentListener

to add
**See Also:** Document.addDocumentListener(javax.swing.event.DocumentListener)

- removeDocumentListener

```java
public void removeDocumentListener​(
DocumentListener
listener)
```

Removes a document listener.

**Specified by:** removeDocumentListener

in interface

Document
**Parameters:** listener

- the

DocumentListener

to remove
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

- getDocumentListeners

```java
public
DocumentListener
[] getDocumentListeners()
```

Returns an array of all the document listeners
registered on this document.

**Returns:** all of this document's

DocumentListener

s
or an empty array if no document listeners are
currently registered
**Since:** 1.4
**See Also:** addDocumentListener(javax.swing.event.DocumentListener)

,

removeDocumentListener(javax.swing.event.DocumentListener)

- addUndoableEditListener

```java
public void addUndoableEditListener​(
UndoableEditListener
listener)
```

Adds an undo listener for notification of any changes.
Undo/Redo operations performed on the

UndoableEdit

will cause the appropriate DocumentEvent to be fired to keep
the view(s) in sync with the model.

**Specified by:** addUndoableEditListener

in interface

Document
**Parameters:** listener

- the

UndoableEditListener

to add
**See Also:** Document.addUndoableEditListener(javax.swing.event.UndoableEditListener)

- removeUndoableEditListener

```java
public void removeUndoableEditListener​(
UndoableEditListener
listener)
```

Removes an undo listener.

**Specified by:** removeUndoableEditListener

in interface

Document
**Parameters:** listener

- the

UndoableEditListener

to remove
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

- getUndoableEditListeners

```java
public
UndoableEditListener
[] getUndoableEditListeners()
```

Returns an array of all the undoable edit listeners
registered on this document.

**Returns:** all of this document's

UndoableEditListener

s
or an empty array if no undoable edit listeners are
currently registered
**Since:** 1.4
**See Also:** addUndoableEditListener(javax.swing.event.UndoableEditListener)

,

removeUndoableEditListener(javax.swing.event.UndoableEditListener)

- getProperty

```java
public final
Object
getProperty​(
Object
key)
```

A convenience method for looking up a property value. It is
equivalent to:

```java
getDocumentProperties().get(key);
```

**Specified by:** getProperty

in interface

Document
**Parameters:** key

- the non-

null

property key
**Returns:** the value of this property or

null
**See Also:** getDocumentProperties()

- putProperty

```java
public final void putProperty​(
Object
key,

Object
value)
```

A convenience method for storing up a property value. It is
equivalent to:

```java
getDocumentProperties().put(key, value);
```

If

value

is

null

this method will
remove the property.

**Specified by:** putProperty

in interface

Document
**Parameters:** key

- the non-

null

key
**Parameters:** value

- the property value
**See Also:** getDocumentProperties()

- remove

```java
public void remove​(int offs,
int len)
throws
BadLocationException
```

Removes some content from the document.
Removing content causes a write lock to be held while the
actual changes are taking place. Observers are notified
of the change on the thread that called this method.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** remove

in interface

Document
**Parameters:** offs

- the starting offset >= 0
**Parameters:** len

- the number of characters to remove >= 0
**Throws:** BadLocationException

- the given remove position is not a valid
position within the document
**See Also:** Document.remove(int, int)

- replace

```java
public void replace​(int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException
```

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.
It is up to the implementation as to how this is implemented, some
implementations may treat this as two distinct operations: a remove
followed by an insert, others may treat the replace as one atomic
operation.

**Parameters:** offset

- index of child element
**Parameters:** length

- length of text to delete, may be 0 indicating don't
delete anything
**Parameters:** text

- text to insert,

null

indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,

null

is legal, and typically treated as an empty attributeset,
but exact interpretation is left to the subclass
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Since:** 1.4

- insertString

```java
public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** insertString

in interface

Document
**Parameters:** offs

- the starting offset >= 0
**Parameters:** str

- the string to insert; does nothing with null/empty strings
**Parameters:** a

- the attributes for the inserted content
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

- getText

```java
public
String
getText​(int offset,
int length)
throws
BadLocationException
```

Gets a sequence of text from the document.

**Specified by:** getText

in interface

Document
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the number of characters to retrieve >= 0
**Returns:** the text
**Throws:** BadLocationException

- the range given includes a position
that is not a valid position within the document
**See Also:** Document.getText(int, int)

- getText

```java
public void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do something with text
nleft -= text.count;
offs += text.count;
}
```

**Specified by:** getText

in interface

Document
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the number of characters to retrieve >= 0
**Parameters:** txt

- the Segment object to retrieve the text into
**Throws:** BadLocationException

- the range given includes a position
that is not a valid position within the document

- createPosition

```java
public
Position
createPosition​(int offs)
throws
BadLocationException
```

Returns a position that will track change as the document
is altered.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** createPosition

in interface

Document
**Parameters:** offs

- the position in the model >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** Document.createPosition(int)

- getStartPosition

```java
public final
Position
getStartPosition()
```

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Specified by:** getStartPosition

in interface

Document
**Returns:** the position

- getEndPosition

```java
public final
Position
getEndPosition()
```

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Specified by:** getEndPosition

in interface

Document
**Returns:** the position

- getRootElements

```java
public
Element
[] getRootElements()
```

Gets all root elements defined. Typically, there
will only be one so the default implementation
is to return the default root element.

**Specified by:** getRootElements

in interface

Document
**Returns:** the root element

- getDefaultRootElement

```java
public abstract
Element
getDefaultRootElement()
```

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

**Specified by:** getDefaultRootElement

in interface

Document
**Returns:** the root element
**See Also:** Document.getDefaultRootElement()

- getBidiRootElement

```java
public
Element
getBidiRootElement()
```

Returns the root element of the bidirectional structure for this
document. Its children represent character runs with a given
Unicode bidi level.

**Returns:** the root element of the bidirectional structure for this
document

- getParagraphElement

```java
public abstract
Element
getParagraphElement​(int pos)
```

Get the paragraph element containing the given position. Sub-classes
must define for themselves what exactly constitutes a paragraph. They
should keep in mind however that a paragraph should at least be the
unit of text over which to run the Unicode bidirectional algorithm.

**Parameters:** pos

- the starting offset >= 0
**Returns:** the element

- getAttributeContext

```java
protected final
AbstractDocument.AttributeContext
getAttributeContext()
```

Fetches the context for managing attributes. This
method effectively establishes the strategy used
for compressing AttributeSet information.

**Returns:** the context

- insertUpdate

```java
protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)
```

Updates document structure as a result of text insertion. This
will happen within a write lock. If a subclass of
this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change
**Parameters:** attr

- the attributes for the change

- removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal. This
method is called before the text is actually removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change

- postRemoveUpdate

```java
protected void postRemoveUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal. This
method is called after the text has been removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change

- dump

```java
public void dump​(
PrintStream
out)
```

Gives a diagnostic dump.

**Parameters:** out

- the output stream

- getContent

```java
protected final
AbstractDocument.Content
getContent()
```

Gets the content for the document.

**Returns:** the content

- createLeafElement

```java
protected
Element
createLeafElement​(
Element
parent,

AttributeSet
a,
int p0,
int p1)
```

Creates a document leaf element.
Hook through which elements are created to represent the
document structure. Because this implementation keeps
structure and content separate, elements grow automatically
when content is extended so splits of existing elements
follow. The document itself gets to decide how to generate
elements to give flexibility in the type of elements used.

**Parameters:** parent

- the parent element
**Parameters:** a

- the attributes for the element
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Returns:** the new element

- createBranchElement

```java
protected
Element
createBranchElement​(
Element
parent,

AttributeSet
a)
```

Creates a document branch element, that can contain other elements.

**Parameters:** parent

- the parent element
**Parameters:** a

- the attributes
**Returns:** the element

- getCurrentWriter

```java
protected final
Thread
getCurrentWriter()
```

Fetches the current writing thread if there is one.
This can be used to distinguish whether a method is
being called as part of an existing modification or
if a lock needs to be acquired and a new transaction
started.

**Returns:** the thread actively modifying the document
or

null

if there are no modifications in progress

- writeLock

```java
protected final void writeLock()
```

Acquires a lock to begin mutating the document this lock
protects. There can be no writing, notification of changes, or
reading going on in order to gain the lock. Additionally a thread is
allowed to gain more than one

writeLock

,
as long as it doesn't attempt to gain additional

writeLock

s
from within document notification. Attempting to gain a

writeLock

from within a DocumentListener notification will
result in an

IllegalStateException

. The ability
to obtain more than one

writeLock

per thread allows
subclasses to gain a writeLock, perform a number of operations, then
release the lock.

Calls to

writeLock

must be balanced with calls to

writeUnlock

, else the

Document

will be left in a locked state so that no
reading or writing can be done.

**Throws:** IllegalStateException

- thrown on illegal lock
attempt. If the document is implemented properly, this can
only happen if a document listener attempts to mutate the
document. This situation violates the bean event model
where order of delivery is not guaranteed and all listeners
should be notified before further mutations are allowed.

- writeUnlock

```java
protected final void writeUnlock()
```

Releases a write lock previously obtained via

writeLock

.
After decrementing the lock count if there are no outstanding locks
this will allow a new writer, or readers.

**See Also:** writeLock()

- readLock

```java
public final void readLock()
```

Acquires a lock to begin reading some state from the
document. There can be multiple readers at the same time.
Writing blocks the readers until notification of the change
to the listeners has been completed. This method should
be used very carefully to avoid unintended compromise
of the document. It should always be balanced with a

readUnlock

.

**See Also:** readUnlock()

- readUnlock

```java
public final void readUnlock()
```

Does a read unlock. This signals that one
of the readers is done. If there are no more readers
then writing can begin again. This should be balanced
with a readLock, and should occur in a finally statement
so that the balance is guaranteed. The following is an
example.

```java
readLock();
try {
// do something
} finally {
readUnlock();
}
```

**See Also:** readLock()

Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The event listener list for the document.

- BAD_LOCATION

```java
protected static final
String
BAD_LOCATION
```

Error message to indicate a bad location.

**See Also:** Constant Field Values

- ParagraphElementName

```java
public static final
String
ParagraphElementName
```

Name of elements used to represent paragraphs

**See Also:** Constant Field Values

- ContentElementName

```java
public static final
String
ContentElementName
```

Name of elements used to represent content

**See Also:** Constant Field Values

- SectionElementName

```java
public static final
String
SectionElementName
```

Name of elements used to hold sections (lines/paragraphs).

**See Also:** Constant Field Values

- BidiElementName

```java
public static final
String
BidiElementName
```

Name of elements used to hold a unidirectional run

**See Also:** Constant Field Values

- ElementNameAttribute

```java
public static final
String
ElementNameAttribute
```

Name of the attribute used to specify element
names.

**See Also:** Constant Field Values

---

#### Field Detail

listenerList

```java
protected
EventListenerList
listenerList
```

The event listener list for the document.

---

#### listenerList

protected

EventListenerList

listenerList

The event listener list for the document.

BAD_LOCATION

```java
protected static final
String
BAD_LOCATION
```

Error message to indicate a bad location.

**See Also:** Constant Field Values

---

#### BAD_LOCATION

protected static final

String

BAD_LOCATION

Error message to indicate a bad location.

ParagraphElementName

```java
public static final
String
ParagraphElementName
```

Name of elements used to represent paragraphs

**See Also:** Constant Field Values

---

#### ParagraphElementName

public static final

String

ParagraphElementName

Name of elements used to represent paragraphs

ContentElementName

```java
public static final
String
ContentElementName
```

Name of elements used to represent content

**See Also:** Constant Field Values

---

#### ContentElementName

public static final

String

ContentElementName

Name of elements used to represent content

SectionElementName

```java
public static final
String
SectionElementName
```

Name of elements used to hold sections (lines/paragraphs).

**See Also:** Constant Field Values

---

#### SectionElementName

public static final

String

SectionElementName

Name of elements used to hold sections (lines/paragraphs).

BidiElementName

```java
public static final
String
BidiElementName
```

Name of elements used to hold a unidirectional run

**See Also:** Constant Field Values

---

#### BidiElementName

public static final

String

BidiElementName

Name of elements used to hold a unidirectional run

ElementNameAttribute

```java
public static final
String
ElementNameAttribute
```

Name of the attribute used to specify element
names.

**See Also:** Constant Field Values

---

#### ElementNameAttribute

public static final

String

ElementNameAttribute

Name of the attribute used to specify element
names.

Constructor Detail

- AbstractDocument

```java
protected AbstractDocument​(
AbstractDocument.Content
data)
```

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:** data

- the content

- AbstractDocument

```java
protected AbstractDocument​(
AbstractDocument.Content
data,

AbstractDocument.AttributeContext
context)
```

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:** data

- the content
**Parameters:** context

- the attribute context

---

#### Constructor Detail

AbstractDocument

```java
protected AbstractDocument​(
AbstractDocument.Content
data)
```

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:** data

- the content

---

#### AbstractDocument

protected AbstractDocument​(

AbstractDocument.Content

data)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

AbstractDocument

```java
protected AbstractDocument​(
AbstractDocument.Content
data,

AbstractDocument.AttributeContext
context)
```

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

**Parameters:** data

- the content
**Parameters:** context

- the attribute context

---

#### AbstractDocument

protected AbstractDocument​(

AbstractDocument.Content

data,

AbstractDocument.AttributeContext

context)

Constructs a new

AbstractDocument

, wrapped around some
specified content storage mechanism.

Method Detail

- getDocumentProperties

```java
public
Dictionary
<
Object
,​
Object
> getDocumentProperties()
```

Supports managing a set of properties. Callers
can use the

documentProperties

dictionary
to annotate the document with document-wide properties.

**Returns:** a non-

null

Dictionary
**See Also:** setDocumentProperties(java.util.Dictionary<java.lang.Object, java.lang.Object>)

- setDocumentProperties

```java
public void setDocumentProperties​(
Dictionary
<
Object
,​
Object
> x)
```

Replaces the document properties dictionary for this document.

**Parameters:** x

- the new dictionary
**See Also:** getDocumentProperties()

- fireInsertUpdate

```java
protected void fireInsertUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- fireChangedUpdate

```java
protected void fireChangedUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- fireRemoveUpdate

```java
protected void fireRemoveUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- fireUndoableEditUpdate

```java
protected void fireUndoableEditUpdate​(
UndoableEditEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a
document

d

for its document listeners with the following code:

```java
DocumentListener[] mls = (DocumentListener[])(d.getListeners(DocumentListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getDocumentListeners()

,

getUndoableEditListeners()

- getAsynchronousLoadPriority

```java
public int getAsynchronousLoadPriority()
```

Gets the asynchronous loading priority. If less than zero,
the document should not be loaded asynchronously.

**Returns:** the asynchronous loading priority, or

-1

if the document should not be loaded asynchronously

- setAsynchronousLoadPriority

```java
public void setAsynchronousLoadPriority​(int p)
```

Sets the asynchronous loading priority.

**Parameters:** p

- the new asynchronous loading priority; a value
less than zero indicates that the document should not be
loaded asynchronously

- setDocumentFilter

```java
public void setDocumentFilter​(
DocumentFilter
filter)
```

Sets the

DocumentFilter

. The

DocumentFilter

is passed

insert

and

remove

to conditionally
allow inserting/deleting of the text. A

null

value
indicates that no filtering will occur.

**Parameters:** filter

- the

DocumentFilter

used to constrain text
**Since:** 1.4
**See Also:** getDocumentFilter()

- getDocumentFilter

```java
public
DocumentFilter
getDocumentFilter()
```

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal. A

null

return value
implies no filtering is to occur.

**Returns:** the DocumentFilter
**Since:** 1.4
**See Also:** setDocumentFilter(javax.swing.text.DocumentFilter)

- render

```java
public void render​(
Runnable
r)
```

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

This is implemented to acquire a read lock for the duration
of the runnables execution. There may be multiple runnables
executing at the same time, and all writers will be blocked
while there are active rendering runnables. If the runnable
throws an exception, its lock will be safely released.
There is no protection against a runnable that never exits,
which will effectively leave the document locked for it's
lifetime.

If the given runnable attempts to make any mutations in
this implementation, a deadlock will occur. There is
no tracking of individual rendering threads to enable
detecting this situation, but a subclass could incur
the overhead of tracking them and throwing an error.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** render

in interface

Document
**Parameters:** r

- the renderer to execute

- getLength

```java
public int getLength()
```

Returns the length of the data. This is the number of
characters of content that represents the users data.

**Specified by:** getLength

in interface

Document
**Returns:** the length >= 0
**See Also:** Document.getLength()

- addDocumentListener

```java
public void addDocumentListener​(
DocumentListener
listener)
```

Adds a document listener for notification of any changes.

**Specified by:** addDocumentListener

in interface

Document
**Parameters:** listener

- the

DocumentListener

to add
**See Also:** Document.addDocumentListener(javax.swing.event.DocumentListener)

- removeDocumentListener

```java
public void removeDocumentListener​(
DocumentListener
listener)
```

Removes a document listener.

**Specified by:** removeDocumentListener

in interface

Document
**Parameters:** listener

- the

DocumentListener

to remove
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

- getDocumentListeners

```java
public
DocumentListener
[] getDocumentListeners()
```

Returns an array of all the document listeners
registered on this document.

**Returns:** all of this document's

DocumentListener

s
or an empty array if no document listeners are
currently registered
**Since:** 1.4
**See Also:** addDocumentListener(javax.swing.event.DocumentListener)

,

removeDocumentListener(javax.swing.event.DocumentListener)

- addUndoableEditListener

```java
public void addUndoableEditListener​(
UndoableEditListener
listener)
```

Adds an undo listener for notification of any changes.
Undo/Redo operations performed on the

UndoableEdit

will cause the appropriate DocumentEvent to be fired to keep
the view(s) in sync with the model.

**Specified by:** addUndoableEditListener

in interface

Document
**Parameters:** listener

- the

UndoableEditListener

to add
**See Also:** Document.addUndoableEditListener(javax.swing.event.UndoableEditListener)

- removeUndoableEditListener

```java
public void removeUndoableEditListener​(
UndoableEditListener
listener)
```

Removes an undo listener.

**Specified by:** removeUndoableEditListener

in interface

Document
**Parameters:** listener

- the

UndoableEditListener

to remove
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

- getUndoableEditListeners

```java
public
UndoableEditListener
[] getUndoableEditListeners()
```

Returns an array of all the undoable edit listeners
registered on this document.

**Returns:** all of this document's

UndoableEditListener

s
or an empty array if no undoable edit listeners are
currently registered
**Since:** 1.4
**See Also:** addUndoableEditListener(javax.swing.event.UndoableEditListener)

,

removeUndoableEditListener(javax.swing.event.UndoableEditListener)

- getProperty

```java
public final
Object
getProperty​(
Object
key)
```

A convenience method for looking up a property value. It is
equivalent to:

```java
getDocumentProperties().get(key);
```

**Specified by:** getProperty

in interface

Document
**Parameters:** key

- the non-

null

property key
**Returns:** the value of this property or

null
**See Also:** getDocumentProperties()

- putProperty

```java
public final void putProperty​(
Object
key,

Object
value)
```

A convenience method for storing up a property value. It is
equivalent to:

```java
getDocumentProperties().put(key, value);
```

If

value

is

null

this method will
remove the property.

**Specified by:** putProperty

in interface

Document
**Parameters:** key

- the non-

null

key
**Parameters:** value

- the property value
**See Also:** getDocumentProperties()

- remove

```java
public void remove​(int offs,
int len)
throws
BadLocationException
```

Removes some content from the document.
Removing content causes a write lock to be held while the
actual changes are taking place. Observers are notified
of the change on the thread that called this method.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** remove

in interface

Document
**Parameters:** offs

- the starting offset >= 0
**Parameters:** len

- the number of characters to remove >= 0
**Throws:** BadLocationException

- the given remove position is not a valid
position within the document
**See Also:** Document.remove(int, int)

- replace

```java
public void replace​(int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException
```

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.
It is up to the implementation as to how this is implemented, some
implementations may treat this as two distinct operations: a remove
followed by an insert, others may treat the replace as one atomic
operation.

**Parameters:** offset

- index of child element
**Parameters:** length

- length of text to delete, may be 0 indicating don't
delete anything
**Parameters:** text

- text to insert,

null

indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,

null

is legal, and typically treated as an empty attributeset,
but exact interpretation is left to the subclass
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Since:** 1.4

- insertString

```java
public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** insertString

in interface

Document
**Parameters:** offs

- the starting offset >= 0
**Parameters:** str

- the string to insert; does nothing with null/empty strings
**Parameters:** a

- the attributes for the inserted content
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

- getText

```java
public
String
getText​(int offset,
int length)
throws
BadLocationException
```

Gets a sequence of text from the document.

**Specified by:** getText

in interface

Document
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the number of characters to retrieve >= 0
**Returns:** the text
**Throws:** BadLocationException

- the range given includes a position
that is not a valid position within the document
**See Also:** Document.getText(int, int)

- getText

```java
public void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do something with text
nleft -= text.count;
offs += text.count;
}
```

**Specified by:** getText

in interface

Document
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the number of characters to retrieve >= 0
**Parameters:** txt

- the Segment object to retrieve the text into
**Throws:** BadLocationException

- the range given includes a position
that is not a valid position within the document

- createPosition

```java
public
Position
createPosition​(int offs)
throws
BadLocationException
```

Returns a position that will track change as the document
is altered.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** createPosition

in interface

Document
**Parameters:** offs

- the position in the model >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** Document.createPosition(int)

- getStartPosition

```java
public final
Position
getStartPosition()
```

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Specified by:** getStartPosition

in interface

Document
**Returns:** the position

- getEndPosition

```java
public final
Position
getEndPosition()
```

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Specified by:** getEndPosition

in interface

Document
**Returns:** the position

- getRootElements

```java
public
Element
[] getRootElements()
```

Gets all root elements defined. Typically, there
will only be one so the default implementation
is to return the default root element.

**Specified by:** getRootElements

in interface

Document
**Returns:** the root element

- getDefaultRootElement

```java
public abstract
Element
getDefaultRootElement()
```

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

**Specified by:** getDefaultRootElement

in interface

Document
**Returns:** the root element
**See Also:** Document.getDefaultRootElement()

- getBidiRootElement

```java
public
Element
getBidiRootElement()
```

Returns the root element of the bidirectional structure for this
document. Its children represent character runs with a given
Unicode bidi level.

**Returns:** the root element of the bidirectional structure for this
document

- getParagraphElement

```java
public abstract
Element
getParagraphElement​(int pos)
```

Get the paragraph element containing the given position. Sub-classes
must define for themselves what exactly constitutes a paragraph. They
should keep in mind however that a paragraph should at least be the
unit of text over which to run the Unicode bidirectional algorithm.

**Parameters:** pos

- the starting offset >= 0
**Returns:** the element

- getAttributeContext

```java
protected final
AbstractDocument.AttributeContext
getAttributeContext()
```

Fetches the context for managing attributes. This
method effectively establishes the strategy used
for compressing AttributeSet information.

**Returns:** the context

- insertUpdate

```java
protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)
```

Updates document structure as a result of text insertion. This
will happen within a write lock. If a subclass of
this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change
**Parameters:** attr

- the attributes for the change

- removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal. This
method is called before the text is actually removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change

- postRemoveUpdate

```java
protected void postRemoveUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal. This
method is called after the text has been removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change

- dump

```java
public void dump​(
PrintStream
out)
```

Gives a diagnostic dump.

**Parameters:** out

- the output stream

- getContent

```java
protected final
AbstractDocument.Content
getContent()
```

Gets the content for the document.

**Returns:** the content

- createLeafElement

```java
protected
Element
createLeafElement​(
Element
parent,

AttributeSet
a,
int p0,
int p1)
```

Creates a document leaf element.
Hook through which elements are created to represent the
document structure. Because this implementation keeps
structure and content separate, elements grow automatically
when content is extended so splits of existing elements
follow. The document itself gets to decide how to generate
elements to give flexibility in the type of elements used.

**Parameters:** parent

- the parent element
**Parameters:** a

- the attributes for the element
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Returns:** the new element

- createBranchElement

```java
protected
Element
createBranchElement​(
Element
parent,

AttributeSet
a)
```

Creates a document branch element, that can contain other elements.

**Parameters:** parent

- the parent element
**Parameters:** a

- the attributes
**Returns:** the element

- getCurrentWriter

```java
protected final
Thread
getCurrentWriter()
```

Fetches the current writing thread if there is one.
This can be used to distinguish whether a method is
being called as part of an existing modification or
if a lock needs to be acquired and a new transaction
started.

**Returns:** the thread actively modifying the document
or

null

if there are no modifications in progress

- writeLock

```java
protected final void writeLock()
```

Acquires a lock to begin mutating the document this lock
protects. There can be no writing, notification of changes, or
reading going on in order to gain the lock. Additionally a thread is
allowed to gain more than one

writeLock

,
as long as it doesn't attempt to gain additional

writeLock

s
from within document notification. Attempting to gain a

writeLock

from within a DocumentListener notification will
result in an

IllegalStateException

. The ability
to obtain more than one

writeLock

per thread allows
subclasses to gain a writeLock, perform a number of operations, then
release the lock.

Calls to

writeLock

must be balanced with calls to

writeUnlock

, else the

Document

will be left in a locked state so that no
reading or writing can be done.

**Throws:** IllegalStateException

- thrown on illegal lock
attempt. If the document is implemented properly, this can
only happen if a document listener attempts to mutate the
document. This situation violates the bean event model
where order of delivery is not guaranteed and all listeners
should be notified before further mutations are allowed.

- writeUnlock

```java
protected final void writeUnlock()
```

Releases a write lock previously obtained via

writeLock

.
After decrementing the lock count if there are no outstanding locks
this will allow a new writer, or readers.

**See Also:** writeLock()

- readLock

```java
public final void readLock()
```

Acquires a lock to begin reading some state from the
document. There can be multiple readers at the same time.
Writing blocks the readers until notification of the change
to the listeners has been completed. This method should
be used very carefully to avoid unintended compromise
of the document. It should always be balanced with a

readUnlock

.

**See Also:** readUnlock()

- readUnlock

```java
public final void readUnlock()
```

Does a read unlock. This signals that one
of the readers is done. If there are no more readers
then writing can begin again. This should be balanced
with a readLock, and should occur in a finally statement
so that the balance is guaranteed. The following is an
example.

```java
readLock();
try {
// do something
} finally {
readUnlock();
}
```

**See Also:** readLock()

---

#### Method Detail

getDocumentProperties

```java
public
Dictionary
<
Object
,​
Object
> getDocumentProperties()
```

Supports managing a set of properties. Callers
can use the

documentProperties

dictionary
to annotate the document with document-wide properties.

**Returns:** a non-

null

Dictionary
**See Also:** setDocumentProperties(java.util.Dictionary<java.lang.Object, java.lang.Object>)

---

#### getDocumentProperties

public

Dictionary

<

Object

,​

Object

> getDocumentProperties()

Supports managing a set of properties. Callers
can use the

documentProperties

dictionary
to annotate the document with document-wide properties.

setDocumentProperties

```java
public void setDocumentProperties​(
Dictionary
<
Object
,​
Object
> x)
```

Replaces the document properties dictionary for this document.

**Parameters:** x

- the new dictionary
**See Also:** getDocumentProperties()

---

#### setDocumentProperties

public void setDocumentProperties​(

Dictionary

<

Object

,​

Object

> x)

Replaces the document properties dictionary for this document.

fireInsertUpdate

```java
protected void fireInsertUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

---

#### fireInsertUpdate

protected void fireInsertUpdate​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

fireChangedUpdate

```java
protected void fireChangedUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

---

#### fireChangedUpdate

protected void fireChangedUpdate​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

fireRemoveUpdate

```java
protected void fireRemoveUpdate​(
DocumentEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

---

#### fireRemoveUpdate

protected void fireRemoveUpdate​(

DocumentEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

fireUndoableEditUpdate

```java
protected void fireUndoableEditUpdate​(
UndoableEditEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

**Parameters:** e

- the event
**See Also:** EventListenerList

---

#### fireUndoableEditUpdate

protected void fireUndoableEditUpdate​(

UndoableEditEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a
document

d

for its document listeners with the following code:

```java
DocumentListener[] mls = (DocumentListener[])(d.getListeners(DocumentListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getDocumentListeners()

,

getUndoableEditListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this document.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a
document

d

for its document listeners with the following code:

```java
DocumentListener[] mls = (DocumentListener[])(d.getListeners(DocumentListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a
document

d

for its document listeners with the following code:

```java
DocumentListener[] mls = (DocumentListener[])(d.getListeners(DocumentListener.class));
```

If no such listeners exist, this method returns an empty array.

DocumentListener[] mls = (DocumentListener[])(d.getListeners(DocumentListener.class));

getAsynchronousLoadPriority

```java
public int getAsynchronousLoadPriority()
```

Gets the asynchronous loading priority. If less than zero,
the document should not be loaded asynchronously.

**Returns:** the asynchronous loading priority, or

-1

if the document should not be loaded asynchronously

---

#### getAsynchronousLoadPriority

public int getAsynchronousLoadPriority()

Gets the asynchronous loading priority. If less than zero,
the document should not be loaded asynchronously.

setAsynchronousLoadPriority

```java
public void setAsynchronousLoadPriority​(int p)
```

Sets the asynchronous loading priority.

**Parameters:** p

- the new asynchronous loading priority; a value
less than zero indicates that the document should not be
loaded asynchronously

---

#### setAsynchronousLoadPriority

public void setAsynchronousLoadPriority​(int p)

Sets the asynchronous loading priority.

setDocumentFilter

```java
public void setDocumentFilter​(
DocumentFilter
filter)
```

Sets the

DocumentFilter

. The

DocumentFilter

is passed

insert

and

remove

to conditionally
allow inserting/deleting of the text. A

null

value
indicates that no filtering will occur.

**Parameters:** filter

- the

DocumentFilter

used to constrain text
**Since:** 1.4
**See Also:** getDocumentFilter()

---

#### setDocumentFilter

public void setDocumentFilter​(

DocumentFilter

filter)

Sets the

DocumentFilter

. The

DocumentFilter

is passed

insert

and

remove

to conditionally
allow inserting/deleting of the text. A

null

value
indicates that no filtering will occur.

getDocumentFilter

```java
public
DocumentFilter
getDocumentFilter()
```

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal. A

null

return value
implies no filtering is to occur.

**Returns:** the DocumentFilter
**Since:** 1.4
**See Also:** setDocumentFilter(javax.swing.text.DocumentFilter)

---

#### getDocumentFilter

public

DocumentFilter

getDocumentFilter()

Returns the

DocumentFilter

that is responsible for
filtering of insertion/removal. A

null

return value
implies no filtering is to occur.

render

```java
public void render​(
Runnable
r)
```

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

This is implemented to acquire a read lock for the duration
of the runnables execution. There may be multiple runnables
executing at the same time, and all writers will be blocked
while there are active rendering runnables. If the runnable
throws an exception, its lock will be safely released.
There is no protection against a runnable that never exits,
which will effectively leave the document locked for it's
lifetime.

If the given runnable attempts to make any mutations in
this implementation, a deadlock will occur. There is
no tracking of individual rendering threads to enable
detecting this situation, but a subclass could incur
the overhead of tracking them and throwing an error.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** render

in interface

Document
**Parameters:** r

- the renderer to execute

---

#### render

public void render​(

Runnable

r)

This allows the model to be safely rendered in the presence
of currency, if the model supports being updated asynchronously.
The given runnable will be executed in a way that allows it
to safely read the model with no changes while the runnable
is being executed. The runnable itself may

not

make any mutations.

This is implemented to acquire a read lock for the duration
of the runnables execution. There may be multiple runnables
executing at the same time, and all writers will be blocked
while there are active rendering runnables. If the runnable
throws an exception, its lock will be safely released.
There is no protection against a runnable that never exits,
which will effectively leave the document locked for it's
lifetime.

If the given runnable attempts to make any mutations in
this implementation, a deadlock will occur. There is
no tracking of individual rendering threads to enable
detecting this situation, but a subclass could incur
the overhead of tracking them and throwing an error.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This is implemented to acquire a read lock for the duration
of the runnables execution. There may be multiple runnables
executing at the same time, and all writers will be blocked
while there are active rendering runnables. If the runnable
throws an exception, its lock will be safely released.
There is no protection against a runnable that never exits,
which will effectively leave the document locked for it's
lifetime.

If the given runnable attempts to make any mutations in
this implementation, a deadlock will occur. There is
no tracking of individual rendering threads to enable
detecting this situation, but a subclass could incur
the overhead of tracking them and throwing an error.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

If the given runnable attempts to make any mutations in
this implementation, a deadlock will occur. There is
no tracking of individual rendering threads to enable
detecting this situation, but a subclass could incur
the overhead of tracking them and throwing an error.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

getLength

```java
public int getLength()
```

Returns the length of the data. This is the number of
characters of content that represents the users data.

**Specified by:** getLength

in interface

Document
**Returns:** the length >= 0
**See Also:** Document.getLength()

---

#### getLength

public int getLength()

Returns the length of the data. This is the number of
characters of content that represents the users data.

addDocumentListener

```java
public void addDocumentListener​(
DocumentListener
listener)
```

Adds a document listener for notification of any changes.

**Specified by:** addDocumentListener

in interface

Document
**Parameters:** listener

- the

DocumentListener

to add
**See Also:** Document.addDocumentListener(javax.swing.event.DocumentListener)

---

#### addDocumentListener

public void addDocumentListener​(

DocumentListener

listener)

Adds a document listener for notification of any changes.

removeDocumentListener

```java
public void removeDocumentListener​(
DocumentListener
listener)
```

Removes a document listener.

**Specified by:** removeDocumentListener

in interface

Document
**Parameters:** listener

- the

DocumentListener

to remove
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

---

#### removeDocumentListener

public void removeDocumentListener​(

DocumentListener

listener)

Removes a document listener.

getDocumentListeners

```java
public
DocumentListener
[] getDocumentListeners()
```

Returns an array of all the document listeners
registered on this document.

**Returns:** all of this document's

DocumentListener

s
or an empty array if no document listeners are
currently registered
**Since:** 1.4
**See Also:** addDocumentListener(javax.swing.event.DocumentListener)

,

removeDocumentListener(javax.swing.event.DocumentListener)

---

#### getDocumentListeners

public

DocumentListener

[] getDocumentListeners()

Returns an array of all the document listeners
registered on this document.

addUndoableEditListener

```java
public void addUndoableEditListener​(
UndoableEditListener
listener)
```

Adds an undo listener for notification of any changes.
Undo/Redo operations performed on the

UndoableEdit

will cause the appropriate DocumentEvent to be fired to keep
the view(s) in sync with the model.

**Specified by:** addUndoableEditListener

in interface

Document
**Parameters:** listener

- the

UndoableEditListener

to add
**See Also:** Document.addUndoableEditListener(javax.swing.event.UndoableEditListener)

---

#### addUndoableEditListener

public void addUndoableEditListener​(

UndoableEditListener

listener)

Adds an undo listener for notification of any changes.
Undo/Redo operations performed on the

UndoableEdit

will cause the appropriate DocumentEvent to be fired to keep
the view(s) in sync with the model.

removeUndoableEditListener

```java
public void removeUndoableEditListener​(
UndoableEditListener
listener)
```

Removes an undo listener.

**Specified by:** removeUndoableEditListener

in interface

Document
**Parameters:** listener

- the

UndoableEditListener

to remove
**See Also:** Document.removeDocumentListener(javax.swing.event.DocumentListener)

---

#### removeUndoableEditListener

public void removeUndoableEditListener​(

UndoableEditListener

listener)

Removes an undo listener.

getUndoableEditListeners

```java
public
UndoableEditListener
[] getUndoableEditListeners()
```

Returns an array of all the undoable edit listeners
registered on this document.

**Returns:** all of this document's

UndoableEditListener

s
or an empty array if no undoable edit listeners are
currently registered
**Since:** 1.4
**See Also:** addUndoableEditListener(javax.swing.event.UndoableEditListener)

,

removeUndoableEditListener(javax.swing.event.UndoableEditListener)

---

#### getUndoableEditListeners

public

UndoableEditListener

[] getUndoableEditListeners()

Returns an array of all the undoable edit listeners
registered on this document.

getProperty

```java
public final
Object
getProperty​(
Object
key)
```

A convenience method for looking up a property value. It is
equivalent to:

```java
getDocumentProperties().get(key);
```

**Specified by:** getProperty

in interface

Document
**Parameters:** key

- the non-

null

property key
**Returns:** the value of this property or

null
**See Also:** getDocumentProperties()

---

#### getProperty

public final

Object

getProperty​(

Object

key)

A convenience method for looking up a property value. It is
equivalent to:

```java
getDocumentProperties().get(key);
```

getDocumentProperties().get(key);

putProperty

```java
public final void putProperty​(
Object
key,

Object
value)
```

A convenience method for storing up a property value. It is
equivalent to:

```java
getDocumentProperties().put(key, value);
```

If

value

is

null

this method will
remove the property.

**Specified by:** putProperty

in interface

Document
**Parameters:** key

- the non-

null

key
**Parameters:** value

- the property value
**See Also:** getDocumentProperties()

---

#### putProperty

public final void putProperty​(

Object

key,

Object

value)

A convenience method for storing up a property value. It is
equivalent to:

```java
getDocumentProperties().put(key, value);
```

If

value

is

null

this method will
remove the property.

getDocumentProperties().put(key, value);

remove

```java
public void remove​(int offs,
int len)
throws
BadLocationException
```

Removes some content from the document.
Removing content causes a write lock to be held while the
actual changes are taking place. Observers are notified
of the change on the thread that called this method.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** remove

in interface

Document
**Parameters:** offs

- the starting offset >= 0
**Parameters:** len

- the number of characters to remove >= 0
**Throws:** BadLocationException

- the given remove position is not a valid
position within the document
**See Also:** Document.remove(int, int)

---

#### remove

public void remove​(int offs,
int len)
throws

BadLocationException

Removes some content from the document.
Removing content causes a write lock to be held while the
actual changes are taking place. Observers are notified
of the change on the thread that called this method.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

replace

```java
public void replace​(int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException
```

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.
It is up to the implementation as to how this is implemented, some
implementations may treat this as two distinct operations: a remove
followed by an insert, others may treat the replace as one atomic
operation.

**Parameters:** offset

- index of child element
**Parameters:** length

- length of text to delete, may be 0 indicating don't
delete anything
**Parameters:** text

- text to insert,

null

indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,

null

is legal, and typically treated as an empty attributeset,
but exact interpretation is left to the subclass
**Throws:** BadLocationException

- the given position is not a valid
position within the document
**Since:** 1.4

---

#### replace

public void replace​(int offset,
int length,

String

text,

AttributeSet

attrs)
throws

BadLocationException

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.
It is up to the implementation as to how this is implemented, some
implementations may treat this as two distinct operations: a remove
followed by an insert, others may treat the replace as one atomic
operation.

insertString

```java
public void insertString​(int offs,

String
str,

AttributeSet
a)
throws
BadLocationException
```

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** insertString

in interface

Document
**Parameters:** offs

- the starting offset >= 0
**Parameters:** str

- the string to insert; does nothing with null/empty strings
**Parameters:** a

- the attributes for the inserted content
**Throws:** BadLocationException

- the given insert position is not a valid
position within the document
**See Also:** Document.insertString(int, java.lang.String, javax.swing.text.AttributeSet)

---

#### insertString

public void insertString​(int offs,

String

str,

AttributeSet

a)
throws

BadLocationException

Inserts some content into the document.
Inserting content causes a write lock to be held while the
actual changes are taking place, followed by notification
to the observers on the thread that grabbed the write lock.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

getText

```java
public
String
getText​(int offset,
int length)
throws
BadLocationException
```

Gets a sequence of text from the document.

**Specified by:** getText

in interface

Document
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the number of characters to retrieve >= 0
**Returns:** the text
**Throws:** BadLocationException

- the range given includes a position
that is not a valid position within the document
**See Also:** Document.getText(int, int)

---

#### getText

public

String

getText​(int offset,
int length)
throws

BadLocationException

Gets a sequence of text from the document.

getText

```java
public void getText​(int offset,
int length,

Segment
txt)
throws
BadLocationException
```

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do something with text
nleft -= text.count;
offs += text.count;
}
```

**Specified by:** getText

in interface

Document
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the number of characters to retrieve >= 0
**Parameters:** txt

- the Segment object to retrieve the text into
**Throws:** BadLocationException

- the range given includes a position
that is not a valid position within the document

---

#### getText

public void getText​(int offset,
int length,

Segment

txt)
throws

BadLocationException

Fetches the text contained within the given portion
of the document.

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do something with text
nleft -= text.count;
offs += text.count;
}
```

If the partialReturn property on the txt parameter is false, the
data returned in the Segment will be the entire length requested and
may or may not be a copy depending upon how the data was stored.
If the partialReturn property is true, only the amount of text that
can be returned without creating a copy is returned. Using partial
returns will give better performance for situations where large
parts of the document are being scanned. The following is an example
of using the partial return to access the entire document:

```java
int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do something with text
nleft -= text.count;
offs += text.count;
}
```

int nleft = doc.getDocumentLength();
Segment text = new Segment();
int offs = 0;
text.setPartialReturn(true);
while (nleft > 0) {
doc.getText(offs, nleft, text);
// do something with text
nleft -= text.count;
offs += text.count;
}

createPosition

```java
public
Position
createPosition​(int offs)
throws
BadLocationException
```

Returns a position that will track change as the document
is altered.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** createPosition

in interface

Document
**Parameters:** offs

- the position in the model >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** Document.createPosition(int)

---

#### createPosition

public

Position

createPosition​(int offs)
throws

BadLocationException

Returns a position that will track change as the document
is altered.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

getStartPosition

```java
public final
Position
getStartPosition()
```

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

**Specified by:** getStartPosition

in interface

Document
**Returns:** the position

---

#### getStartPosition

public final

Position

getStartPosition()

Returns a position that represents the start of the document. The
position returned can be counted on to track change and stay
located at the beginning of the document.

getEndPosition

```java
public final
Position
getEndPosition()
```

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

**Specified by:** getEndPosition

in interface

Document
**Returns:** the position

---

#### getEndPosition

public final

Position

getEndPosition()

Returns a position that represents the end of the document. The
position returned can be counted on to track change and stay
located at the end of the document.

getRootElements

```java
public
Element
[] getRootElements()
```

Gets all root elements defined. Typically, there
will only be one so the default implementation
is to return the default root element.

**Specified by:** getRootElements

in interface

Document
**Returns:** the root element

---

#### getRootElements

public

Element

[] getRootElements()

Gets all root elements defined. Typically, there
will only be one so the default implementation
is to return the default root element.

getDefaultRootElement

```java
public abstract
Element
getDefaultRootElement()
```

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

**Specified by:** getDefaultRootElement

in interface

Document
**Returns:** the root element
**See Also:** Document.getDefaultRootElement()

---

#### getDefaultRootElement

public abstract

Element

getDefaultRootElement()

Returns the root element that views should be based upon
unless some other mechanism for assigning views to element
structures is provided.

getBidiRootElement

```java
public
Element
getBidiRootElement()
```

Returns the root element of the bidirectional structure for this
document. Its children represent character runs with a given
Unicode bidi level.

**Returns:** the root element of the bidirectional structure for this
document

---

#### getBidiRootElement

public

Element

getBidiRootElement()

Returns the root element of the bidirectional structure for this
document. Its children represent character runs with a given
Unicode bidi level.

getParagraphElement

```java
public abstract
Element
getParagraphElement​(int pos)
```

Get the paragraph element containing the given position. Sub-classes
must define for themselves what exactly constitutes a paragraph. They
should keep in mind however that a paragraph should at least be the
unit of text over which to run the Unicode bidirectional algorithm.

**Parameters:** pos

- the starting offset >= 0
**Returns:** the element

---

#### getParagraphElement

public abstract

Element

getParagraphElement​(int pos)

Get the paragraph element containing the given position. Sub-classes
must define for themselves what exactly constitutes a paragraph. They
should keep in mind however that a paragraph should at least be the
unit of text over which to run the Unicode bidirectional algorithm.

getAttributeContext

```java
protected final
AbstractDocument.AttributeContext
getAttributeContext()
```

Fetches the context for managing attributes. This
method effectively establishes the strategy used
for compressing AttributeSet information.

**Returns:** the context

---

#### getAttributeContext

protected final

AbstractDocument.AttributeContext

getAttributeContext()

Fetches the context for managing attributes. This
method effectively establishes the strategy used
for compressing AttributeSet information.

insertUpdate

```java
protected void insertUpdate​(
AbstractDocument.DefaultDocumentEvent
chng,

AttributeSet
attr)
```

Updates document structure as a result of text insertion. This
will happen within a write lock. If a subclass of
this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change
**Parameters:** attr

- the attributes for the change

---

#### insertUpdate

protected void insertUpdate​(

AbstractDocument.DefaultDocumentEvent

chng,

AttributeSet

attr)

Updates document structure as a result of text insertion. This
will happen within a write lock. If a subclass of
this class reimplements this method, it should delegate to the
superclass as well.

removeUpdate

```java
protected void removeUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal. This
method is called before the text is actually removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change

---

#### removeUpdate

protected void removeUpdate​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal. This
method is called before the text is actually removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

postRemoveUpdate

```java
protected void postRemoveUpdate​(
AbstractDocument.DefaultDocumentEvent
chng)
```

Updates any document structure as a result of text removal. This
method is called after the text has been removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

**Parameters:** chng

- a description of the change

---

#### postRemoveUpdate

protected void postRemoveUpdate​(

AbstractDocument.DefaultDocumentEvent

chng)

Updates any document structure as a result of text removal. This
method is called after the text has been removed from the Content.
This will happen within a write lock. If a subclass
of this class reimplements this method, it should delegate to the
superclass as well.

dump

```java
public void dump​(
PrintStream
out)
```

Gives a diagnostic dump.

**Parameters:** out

- the output stream

---

#### dump

public void dump​(

PrintStream

out)

Gives a diagnostic dump.

getContent

```java
protected final
AbstractDocument.Content
getContent()
```

Gets the content for the document.

**Returns:** the content

---

#### getContent

protected final

AbstractDocument.Content

getContent()

Gets the content for the document.

createLeafElement

```java
protected
Element
createLeafElement​(
Element
parent,

AttributeSet
a,
int p0,
int p1)
```

Creates a document leaf element.
Hook through which elements are created to represent the
document structure. Because this implementation keeps
structure and content separate, elements grow automatically
when content is extended so splits of existing elements
follow. The document itself gets to decide how to generate
elements to give flexibility in the type of elements used.

**Parameters:** parent

- the parent element
**Parameters:** a

- the attributes for the element
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Returns:** the new element

---

#### createLeafElement

protected

Element

createLeafElement​(

Element

parent,

AttributeSet

a,
int p0,
int p1)

Creates a document leaf element.
Hook through which elements are created to represent the
document structure. Because this implementation keeps
structure and content separate, elements grow automatically
when content is extended so splits of existing elements
follow. The document itself gets to decide how to generate
elements to give flexibility in the type of elements used.

createBranchElement

```java
protected
Element
createBranchElement​(
Element
parent,

AttributeSet
a)
```

Creates a document branch element, that can contain other elements.

**Parameters:** parent

- the parent element
**Parameters:** a

- the attributes
**Returns:** the element

---

#### createBranchElement

protected

Element

createBranchElement​(

Element

parent,

AttributeSet

a)

Creates a document branch element, that can contain other elements.

getCurrentWriter

```java
protected final
Thread
getCurrentWriter()
```

Fetches the current writing thread if there is one.
This can be used to distinguish whether a method is
being called as part of an existing modification or
if a lock needs to be acquired and a new transaction
started.

**Returns:** the thread actively modifying the document
or

null

if there are no modifications in progress

---

#### getCurrentWriter

protected final

Thread

getCurrentWriter()

Fetches the current writing thread if there is one.
This can be used to distinguish whether a method is
being called as part of an existing modification or
if a lock needs to be acquired and a new transaction
started.

writeLock

```java
protected final void writeLock()
```

Acquires a lock to begin mutating the document this lock
protects. There can be no writing, notification of changes, or
reading going on in order to gain the lock. Additionally a thread is
allowed to gain more than one

writeLock

,
as long as it doesn't attempt to gain additional

writeLock

s
from within document notification. Attempting to gain a

writeLock

from within a DocumentListener notification will
result in an

IllegalStateException

. The ability
to obtain more than one

writeLock

per thread allows
subclasses to gain a writeLock, perform a number of operations, then
release the lock.

Calls to

writeLock

must be balanced with calls to

writeUnlock

, else the

Document

will be left in a locked state so that no
reading or writing can be done.

**Throws:** IllegalStateException

- thrown on illegal lock
attempt. If the document is implemented properly, this can
only happen if a document listener attempts to mutate the
document. This situation violates the bean event model
where order of delivery is not guaranteed and all listeners
should be notified before further mutations are allowed.

---

#### writeLock

protected final void writeLock()

Acquires a lock to begin mutating the document this lock
protects. There can be no writing, notification of changes, or
reading going on in order to gain the lock. Additionally a thread is
allowed to gain more than one

writeLock

,
as long as it doesn't attempt to gain additional

writeLock

s
from within document notification. Attempting to gain a

writeLock

from within a DocumentListener notification will
result in an

IllegalStateException

. The ability
to obtain more than one

writeLock

per thread allows
subclasses to gain a writeLock, perform a number of operations, then
release the lock.

Calls to

writeLock

must be balanced with calls to

writeUnlock

, else the

Document

will be left in a locked state so that no
reading or writing can be done.

Calls to

writeLock

must be balanced with calls to

writeUnlock

, else the

Document

will be left in a locked state so that no
reading or writing can be done.

writeUnlock

```java
protected final void writeUnlock()
```

Releases a write lock previously obtained via

writeLock

.
After decrementing the lock count if there are no outstanding locks
this will allow a new writer, or readers.

**See Also:** writeLock()

---

#### writeUnlock

protected final void writeUnlock()

Releases a write lock previously obtained via

writeLock

.
After decrementing the lock count if there are no outstanding locks
this will allow a new writer, or readers.

readLock

```java
public final void readLock()
```

Acquires a lock to begin reading some state from the
document. There can be multiple readers at the same time.
Writing blocks the readers until notification of the change
to the listeners has been completed. This method should
be used very carefully to avoid unintended compromise
of the document. It should always be balanced with a

readUnlock

.

**See Also:** readUnlock()

---

#### readLock

public final void readLock()

Acquires a lock to begin reading some state from the
document. There can be multiple readers at the same time.
Writing blocks the readers until notification of the change
to the listeners has been completed. This method should
be used very carefully to avoid unintended compromise
of the document. It should always be balanced with a

readUnlock

.

readUnlock

```java
public final void readUnlock()
```

Does a read unlock. This signals that one
of the readers is done. If there are no more readers
then writing can begin again. This should be balanced
with a readLock, and should occur in a finally statement
so that the balance is guaranteed. The following is an
example.

```java
readLock();
try {
// do something
} finally {
readUnlock();
}
```

**See Also:** readLock()

---

#### readUnlock

public final void readUnlock()

Does a read unlock. This signals that one
of the readers is done. If there are no more readers
then writing can begin again. This should be balanced
with a readLock, and should occur in a finally statement
so that the balance is guaranteed. The following is an
example.

```java
readLock();
try {
// do something
} finally {
readUnlock();
}
```

readLock();
try {
// do something
} finally {
readUnlock();
}

---

