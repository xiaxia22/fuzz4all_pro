# Class JEditorPane

**Source:** `java.desktop\javax\swing\JEditorPane.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UIClassID",

description
="A text component to edit various types of content.")
public class
JEditorPane

extends
JTextComponent
```

A text component to edit various kinds of content.
You can find how-to information and examples of using editor panes in

Using Text Components

,
a section in

The Java Tutorial.

This component uses implementations of the

EditorKit

to accomplish its behavior. It effectively
morphs into the proper kind of text editor for the kind
of content it is given. The content type that editor is bound
to at any given time is determined by the

EditorKit

currently
installed. If the content is set to a new URL, its type is used
to determine the

EditorKit

that should be used to
load the content.

By default, the following types of content are known:

There are several ways to load content into this component.

- The

setText

method can be used to initialize
the component from a string. In this case the current

EditorKit

will be used, and the content type will be
expected to be of this type.

The

read

method can be used to initialize the
component from a

Reader

. Note that if the content type is HTML,
relative references (e.g. for things like images) can't be resolved
unless the <base> tag is used or the

Base

property
on

HTMLDocument

is set.
In this case the current

EditorKit

will be used,
and the content type will be expected to be of this type.

The

setPage

method can be used to initialize
the component from a URL. In this case, the content type will be
determined from the URL, and the registered

EditorKit

for that content type will be set.

Some kinds of content may provide hyperlink support by generating
hyperlink events. The HTML

EditorKit

will generate
hyperlink events if the

JEditorPane

is

not editable

(

JEditorPane.setEditable(false);

has been called).
If HTML frames are embedded in the document, the typical response would be
to change a portion of the current document. The following code
fragment is a possible hyperlink listener implementation, that treats
HTML frame events specially, and simply displays any other activated
hyperlinks.

```java
class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}
```

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

Scrollable

---

### Field Details

#### public static final
String
W3C_LENGTH_UNITS

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

By default this is not enabled; to enable
it set the client

property

with this name
to

Boolean.TRUE

.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
HONOR_DISPLAY_PROPERTIES

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

The default varies based on the look and feel;
to enable it set the client

property

with
this name to

Boolean.TRUE

.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

### Constructor Details

#### public JEditorPane()

Creates a new

JEditorPane

.
The document model is set to

null

.

---

#### public JEditorPane​(
URL
initialPage)
throws
IOException

Creates a

JEditorPane

based on a specified URL for input.

**Parameters:**
- initialPage

- the URL

**Throws:**
- IOException

- if the URL is

null

or cannot be accessed

---

#### public JEditorPane​(
String
url)
throws
IOException

Creates a

JEditorPane

based on a string containing
a URL specification.

**Parameters:**
- url

- the URL

**Throws:**
- IOException

- if the URL is

null

or
cannot be accessed

---

#### public JEditorPane​(
String
type,

String
text)

Creates a

JEditorPane

that has been initialized
to the given text. This is a convenience constructor that calls the

setContentType

and

setText

methods.

**Parameters:**
- type

- mime type of the given text
- text

- the text to initialize with; may be

null

**Throws:**
- NullPointerException

- if the

type

parameter
is

null

---

### Method Details

#### public void addHyperlinkListener​(
HyperlinkListener
listener)

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

**Parameters:**
- listener

- the listener

---

#### public void removeHyperlinkListener​(
HyperlinkListener
listener)

Removes a hyperlink listener.

**Parameters:**
- listener

- the listener

---

#### @BeanProperty
(
bound
=false)
public
HyperlinkListener
[] getHyperlinkListeners()

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

**Returns:**
- all of the

HyperLinkListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void fireHyperlinkUpdate​(
HyperlinkEvent
e)

Notifies all listeners that have registered interest for
notification on this event type. This is normally called
by the currently installed

EditorKit

if a content type
that supports hyperlinks is currently active and there
was activity with a link. The listener list is processed
last to first.

**Parameters:**
- e

- the event

**See Also:**
- EventListenerList

---

#### @BeanProperty
(
expert
=true,

description
="the URL used to set content")
public void setPage​(
URL
page)
throws
IOException

Sets the current URL being displayed. The content type of the
pane is set, and if the editor kit for the pane is
non-

null

, then
a new default document is created and the URL is read into it.
If the URL contains and reference location, the location will
be scrolled to by calling the

scrollToReference

method. If the desired URL is the one currently being displayed,
the document will not be reloaded. To force a document
reload it is necessary to clear the stream description property
of the document. The following code shows how this can be done:

```java
Document doc = jEditorPane.getDocument();
doc.putProperty(Document.StreamDescriptionProperty, null);
```

If the desired URL is not the one currently being
displayed, the

getStream

method is called to
give subclasses control over the stream provided.

This may load either synchronously or asynchronously
depending upon the document returned by the

EditorKit

.
If the

Document

is of type

AbstractDocument

and has a value returned by

AbstractDocument.getAsynchronousLoadPriority

that is greater than or equal to zero, the page will be
loaded on a separate thread using that priority.

If the document is loaded synchronously, it will be
filled in with the stream prior to being installed into
the editor with a call to

setDocument

, which
is bound and will fire a property change event. If an

IOException

is thrown the partially loaded
document will
be discarded and neither the document or page property
change events will be fired. If the document is
successfully loaded and installed, a view will be
built for it by the UI which will then be scrolled if
necessary, and then the page property change event
will be fired.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

**Parameters:**
- page

- the URL of the page

**Throws:**
- IOException

- for a

null

or invalid
page specification, or exception from the stream being read

**See Also:**
- getPage()

---

#### public void read​(
InputStream
in,

Object
desc)
throws
IOException

This method initializes from a stream. If the kit is
set to be of type

HTMLEditorKit

, and the

desc

parameter is an

HTMLDocument

,
then it invokes the

HTMLEditorKit

to initiate
the read. Otherwise it calls the superclass
method which loads the model as plain text.

**Parameters:**
- in

- the stream from which to read
- desc

- an object describing the stream

**Throws:**
- IOException

- as thrown by the stream being
used to initialize

**See Also:**
- JTextComponent.read(java.io.Reader, java.lang.Object)

,

JTextComponent.setDocument(javax.swing.text.Document)

---

#### protected
InputStream
getStream​(
URL
page)
throws
IOException

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method. By
default, this simply opens the URL and returns the
stream. This can be reimplemented to do useful things
like fetch the stream from a cache, monitor the progress
of the stream, etc.

This method is expected to have the side effect of
establishing the content type, and therefore setting the
appropriate

EditorKit

to use for loading the stream.

If this the stream was an http connection, redirects
will be followed and the resulting URL will be set as
the

Document.StreamDescriptionProperty

so that relative
URL's can be properly resolved.

**Parameters:**
- page

- the URL of the page

**Returns:**
- a stream for the URL which is about to be loaded

**Throws:**
- IOException

- if an I/O problem occurs

---

#### public void scrollToReference​(
String
reference)

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed). By default, this
method only knows how to locate a reference in an
HTMLDocument. The implementation calls the

scrollRectToVisible

method to
accomplish the actual scrolling. If scrolling to a
reference location is needed for document types other
than HTML, this method should be reimplemented.
This method will have no effect if the component
is not visible.

**Parameters:**
- reference

- the named location to scroll to

---

#### public
URL
getPage()

Gets the current URL being displayed. If a URL was
not specified in the creation of the document, this
will return

null

, and relative URL's will not be
resolved.

**Returns:**
- the URL, or

null

if none

---

#### public void setPage​(
String
url)
throws
IOException

Sets the current URL being displayed.

**Parameters:**
- url

- the URL for display

**Throws:**
- IOException

- for a

null

or invalid URL
specification

---

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Gets the class ID for the UI.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "EditorPaneUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### protected
EditorKit
createDefaultEditorKit()

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

**Returns:**
- the editor kit

---

#### public
EditorKit
getEditorKit()

Fetches the currently installed kit for handling content.

createDefaultEditorKit

is called to set up a default
if necessary.

**Returns:**
- the editor kit

---

#### public final
String
getContentType()

Gets the type of content that this editor
is currently set to deal with. This is
defined to be the type associated with the
currently installed

EditorKit

.

**Returns:**
- the content type,

null

if no editor kit set

---

#### @BeanProperty
(
bound
=false,

description
="the type of content")
public final void setContentType​(
String
type)

Sets the type of content that this editor
handles. This calls

getEditorKitForContentType

,
and then

setEditorKit

if an editor kit can
be successfully located. This is mostly convenience method
that can be used as an alternative to calling

setEditorKit

directly.

If there is a charset definition specified as a parameter
of the content type specification, it will be used when
loading input streams using the associated

EditorKit

.
For example if the type is specified as

text/html; charset=EUC-JP

the content
will be loaded using the

EditorKit

registered for

text/html

and the Reader provided to
the

EditorKit

to load unicode into the document will
use the

EUC-JP

charset for translating
to unicode. If the type is not recognized, the content
will be loaded using the

EditorKit

registered
for plain text,

text/plain

.

**Parameters:**
- type

- the non-

null

mime type for the content editing
support

**Throws:**
- NullPointerException

- if the

type

parameter
is

null

**See Also:**
- getContentType()

---

#### @BeanProperty
(
expert
=true,

description
="the currently installed kit for handling content")
public void setEditorKit​(
EditorKit
kit)

Sets the currently installed kit for handling
content. This is the bound property that
establishes the content type of the editor.
Any old kit is first deinstalled, then if kit is
non-

null

,
the new kit is installed, and a default document created for it.
A

PropertyChange

event ("editorKit") is always fired when

setEditorKit

is called.

NOTE: This has the side effect of changing the model,
because the

EditorKit

is the source of how a
particular type
of content is modeled. This method will cause

setDocument

to be called on behalf of the caller to ensure integrity
of the internal state.

**Parameters:**
- kit

- the desired editor behavior

**See Also:**
- getEditorKit()

---

#### public
EditorKit
getEditorKitForContentType​(
String
type)

Fetches the editor kit to use for the given type
of content. This is called when a type is requested
that doesn't match the currently installed type.
If the component doesn't have an

EditorKit

registered
for the given type, it will try to create an

EditorKit

from the default

EditorKit

registry.
If that fails, a

PlainEditorKit

is used on the
assumption that all text documents can be represented
as plain text.

This method can be reimplemented to use some
other kind of type registry. This can
be reimplemented to use the Java Activation
Framework, for example.

**Parameters:**
- type

- the non-

null

content type

**Returns:**
- the editor kit

---

#### public void setEditorKitForContentType​(
String
type,

EditorKit
k)

Directly sets the editor kit to use for the given type. A
look-and-feel implementation might use this in conjunction
with

createEditorKitForContentType

to install handlers for
content types with a look-and-feel bias.

**Parameters:**
- type

- the non-

null

content type
- k

- the editor kit to be set

---

#### public void replaceSelection​(
String
content)

Replaces the currently selected content with new content
represented by the given string. If there is no selection
this amounts to an insert of the given text. If there
is no replacement text (i.e. the content string is empty
or

null

) this amounts to a removal of the
current selection. The replacement text will have the
attributes currently defined for input. If the component is not
editable, beep and return.

**Overrides:**
- replaceSelection

in class

JTextComponent

**Parameters:**
- content

- the content to replace the selection with. This
value can be

null

---

#### public static
EditorKit
createEditorKitForContentType​(
String
type)

Creates a handler for the given type from the default registry
of editor kits. The registry is created if necessary. If the
registered class has not yet been loaded, an attempt
is made to dynamically load the prototype of the kit for the
given type. If the type was registered with a

ClassLoader

,
that

ClassLoader

will be used to load the prototype.
If there was no registered

ClassLoader

,

Class.forName

will be used to load the prototype.

Once a prototype

EditorKit

instance is successfully
located, it is cloned and the clone is returned.

**Parameters:**
- type

- the content type

**Returns:**
- the editor kit, or

null

if there is nothing
registered for the given type

---

#### public static void registerEditorKitForContentType​(
String
type,

String
classname)

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed, and can be safely changed before attempted uses
to avoid loading unwanted classes. The prototype

EditorKit

will be loaded with

Class.forName

when registered with this method.

**Parameters:**
- type

- the non-

null

content type
- classname

- the class to load later

---

#### public static void registerEditorKitForContentType​(
String
type,

String
classname,

ClassLoader
loader)

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed using the given

ClassLoader

,
and can be safely changed
before attempted uses to avoid loading unwanted classes.

**Parameters:**
- type

- the non-

null

content type
- classname

- the class to load later
- loader

- the

ClassLoader

to use to load the name

---

#### public static
String
getEditorKitClassNameForContentType​(
String
type)

Returns the currently registered

EditorKit

class name for the
type

type

.

**Parameters:**
- type

- the non-

null

content type

**Returns:**
- a

String

containing the

EditorKit

class name
for

type

**Since:**
- 1.3

---

#### public
Dimension
getPreferredSize()

Returns the preferred size for the

JEditorPane

.
The preferred size for

JEditorPane

is slightly altered
from the preferred size of the superclass. If the size
of the viewport has become smaller than the minimum size
of the component, the scrollable definition for tracking
width or height will turn to false. The default viewport
layout will give the preferred size, and that is not desired
in the case where the scrollable is tracking. In that case
the

normal

preferred size is adjusted to the
minimum size. This allows things like HTML tables to
shrink down to their minimum size and then be laid out at
their minimum size, refusing to shrink any further.

**Overrides:**
- getPreferredSize

in class

JComponent

**Returns:**
- a

Dimension

containing the preferred size

**See Also:**
- JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### @BeanProperty
(
bound
=false,

description
="the text of this component")
public void setText​(
String
t)

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor. For example, if the type is set to

text/html

the string should be specified in terms of HTML.

This is implemented to remove the contents of the current document,
and replace them by parsing the given string using the current

EditorKit

. This gives the semantics of the
superclass by not changing
out the model, while supporting the content type currently set on
this component. The assumption is that the previous content is
relatively
small, and that the previous content doesn't have side effects.
Both of those assumptions can be violated and cause undesirable results.
To avoid this, create a new document,

getEditorKit().createDefaultDocument()

, and replace the
existing

Document

with the new one. You are then assured the
previous

Document

won't have any lingering state.

- Leaving the existing model in place means that the old view will be
torn down, and a new view created, where replacing the document would
avoid the tear down of the old view.

Some formats (such as HTML) can install things into the document that
can influence future contents. HTML can have style information embedded
that would influence the next content installed unexpectedly.

An alternative way to load this component with a string would be to
create a StringReader and call the read method. In this case the model
would be replaced after it was initialized with the contents of the
string.

**Overrides:**
- setText

in class

JTextComponent

**Parameters:**
- t

- the new text to be set; if

null

the old
text will be deleted

**See Also:**
- getText()

---

#### public
String
getText()

Returns the text contained in this

TextComponent

in terms of the
content type of this editor. If an exception is thrown while
attempting to retrieve the text,

null

will be returned.
This is implemented to call

JTextComponent.write

with
a

StringWriter

.

**Overrides:**
- getText

in class

JTextComponent

**Returns:**
- the text

**See Also:**
- setText(java.lang.String)

---

#### @BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

**Specified by:**
- getScrollableTracksViewportWidth

in interface

Scrollable

**Overrides:**
- getScrollableTracksViewportWidth

in class

JTextComponent

**Returns:**
- true if a viewport should force the Scrollables width to
match its own, false otherwise

---

#### @BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

**Specified by:**
- getScrollableTracksViewportHeight

in interface

Scrollable

**Overrides:**
- getScrollableTracksViewportHeight

in class

JTextComponent

**Returns:**
- true if a viewport should force the

Scrollable

's height to match its own,
false otherwise

---

#### protected
String
paramString()

Returns a string representation of this

JEditorPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JTextComponent

**Returns:**
- a string representation of this

JEditorPane

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JEditorPane.
For editor panes, the AccessibleContext takes the form of an
AccessibleJEditorPane.
A new AccessibleJEditorPane instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

JTextComponent

**Returns:**
- an AccessibleJEditorPane that serves as the
AccessibleContext of this JEditorPane

---

### Additional Sections

#### Class JEditorPane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.text.JTextComponent
- - javax.swing.JEditorPane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.text.JTextComponent
- - javax.swing.JEditorPane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.text.JTextComponent
- - javax.swing.JEditorPane

javax.swing.JComponent

- javax.swing.text.JTextComponent
- - javax.swing.JEditorPane

javax.swing.text.JTextComponent

- javax.swing.JEditorPane

javax.swing.JEditorPane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

Scrollable

**Direct Known Subclasses:** JTextPane

```java
@JavaBean
(
defaultProperty
="UIClassID",

description
="A text component to edit various types of content.")
public class
JEditorPane

extends
JTextComponent
```

A text component to edit various kinds of content.
You can find how-to information and examples of using editor panes in

Using Text Components

,
a section in

The Java Tutorial.

This component uses implementations of the

EditorKit

to accomplish its behavior. It effectively
morphs into the proper kind of text editor for the kind
of content it is given. The content type that editor is bound
to at any given time is determined by the

EditorKit

currently
installed. If the content is set to a new URL, its type is used
to determine the

EditorKit

that should be used to
load the content.

By default, the following types of content are known:

There are several ways to load content into this component.

- The

setText

method can be used to initialize
the component from a string. In this case the current

EditorKit

will be used, and the content type will be
expected to be of this type.

The

read

method can be used to initialize the
component from a

Reader

. Note that if the content type is HTML,
relative references (e.g. for things like images) can't be resolved
unless the <base> tag is used or the

Base

property
on

HTMLDocument

is set.
In this case the current

EditorKit

will be used,
and the content type will be expected to be of this type.

The

setPage

method can be used to initialize
the component from a URL. In this case, the content type will be
determined from the URL, and the registered

EditorKit

for that content type will be set.

Some kinds of content may provide hyperlink support by generating
hyperlink events. The HTML

EditorKit

will generate
hyperlink events if the

JEditorPane

is

not editable

(

JEditorPane.setEditable(false);

has been called).
If HTML frames are embedded in the document, the typical response would be
to change a portion of the current document. The following code
fragment is a possible hyperlink listener implementation, that treats
HTML frame events specially, and simply displays any other activated
hyperlinks.

```java
class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}
```

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**Since:** 1.2
**See Also:** Serialized Form

@JavaBean

(

defaultProperty

="UIClassID",

description

="A text component to edit various types of content.")
public class

JEditorPane

extends

JTextComponent

A text component to edit various kinds of content.
You can find how-to information and examples of using editor panes in

Using Text Components

,
a section in

The Java Tutorial.

This component uses implementations of the

EditorKit

to accomplish its behavior. It effectively
morphs into the proper kind of text editor for the kind
of content it is given. The content type that editor is bound
to at any given time is determined by the

EditorKit

currently
installed. If the content is set to a new URL, its type is used
to determine the

EditorKit

that should be used to
load the content.

By default, the following types of content are known:

There are several ways to load content into this component.

- The

setText

method can be used to initialize
the component from a string. In this case the current

EditorKit

will be used, and the content type will be
expected to be of this type.

The

read

method can be used to initialize the
component from a

Reader

. Note that if the content type is HTML,
relative references (e.g. for things like images) can't be resolved
unless the <base> tag is used or the

Base

property
on

HTMLDocument

is set.
In this case the current

EditorKit

will be used,
and the content type will be expected to be of this type.

The

setPage

method can be used to initialize
the component from a URL. In this case, the content type will be
determined from the URL, and the registered

EditorKit

for that content type will be set.

Some kinds of content may provide hyperlink support by generating
hyperlink events. The HTML

EditorKit

will generate
hyperlink events if the

JEditorPane

is

not editable

(

JEditorPane.setEditable(false);

has been called).
If HTML frames are embedded in the document, the typical response would be
to change a portion of the current document. The following code
fragment is a possible hyperlink listener implementation, that treats
HTML frame events specially, and simply displays any other activated
hyperlinks.

```java
class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}
```

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

This component uses implementations of the

EditorKit

to accomplish its behavior. It effectively
morphs into the proper kind of text editor for the kind
of content it is given. The content type that editor is bound
to at any given time is determined by the

EditorKit

currently
installed. If the content is set to a new URL, its type is used
to determine the

EditorKit

that should be used to
load the content.

By default, the following types of content are known:

There are several ways to load content into this component.

- The

setText

method can be used to initialize
the component from a string. In this case the current

EditorKit

will be used, and the content type will be
expected to be of this type.

The

read

method can be used to initialize the
component from a

Reader

. Note that if the content type is HTML,
relative references (e.g. for things like images) can't be resolved
unless the <base> tag is used or the

Base

property
on

HTMLDocument

is set.
In this case the current

EditorKit

will be used,
and the content type will be expected to be of this type.

The

setPage

method can be used to initialize
the component from a URL. In this case, the content type will be
determined from the URL, and the registered

EditorKit

for that content type will be set.

Some kinds of content may provide hyperlink support by generating
hyperlink events. The HTML

EditorKit

will generate
hyperlink events if the

JEditorPane

is

not editable

(

JEditorPane.setEditable(false);

has been called).
If HTML frames are embedded in the document, the typical response would be
to change a portion of the current document. The following code
fragment is a possible hyperlink listener implementation, that treats
HTML frame events specially, and simply displays any other activated
hyperlinks.

```java
class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}
```

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

By default, the following types of content are known:

There are several ways to load content into this component.

- The

setText

method can be used to initialize
the component from a string. In this case the current

EditorKit

will be used, and the content type will be
expected to be of this type.

The

read

method can be used to initialize the
component from a

Reader

. Note that if the content type is HTML,
relative references (e.g. for things like images) can't be resolved
unless the <base> tag is used or the

Base

property
on

HTMLDocument

is set.
In this case the current

EditorKit

will be used,
and the content type will be expected to be of this type.

The

setPage

method can be used to initialize
the component from a URL. In this case, the content type will be
determined from the URL, and the registered

EditorKit

for that content type will be set.

Some kinds of content may provide hyperlink support by generating
hyperlink events. The HTML

EditorKit

will generate
hyperlink events if the

JEditorPane

is

not editable

(

JEditorPane.setEditable(false);

has been called).
If HTML frames are embedded in the document, the typical response would be
to change a portion of the current document. The following code
fragment is a possible hyperlink listener implementation, that treats
HTML frame events specially, and simply displays any other activated
hyperlinks.

```java
class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}
```

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

There are several ways to load content into this component.

- The

setText

method can be used to initialize
the component from a string. In this case the current

EditorKit

will be used, and the content type will be
expected to be of this type.

The

read

method can be used to initialize the
component from a

Reader

. Note that if the content type is HTML,
relative references (e.g. for things like images) can't be resolved
unless the <base> tag is used or the

Base

property
on

HTMLDocument

is set.
In this case the current

EditorKit

will be used,
and the content type will be expected to be of this type.

The

setPage

method can be used to initialize
the component from a URL. In this case, the content type will be
determined from the URL, and the registered

EditorKit

for that content type will be set.

Some kinds of content may provide hyperlink support by generating
hyperlink events. The HTML

EditorKit

will generate
hyperlink events if the

JEditorPane

is

not editable

(

JEditorPane.setEditable(false);

has been called).
If HTML frames are embedded in the document, the typical response would be
to change a portion of the current document. The following code
fragment is a possible hyperlink listener implementation, that treats
HTML frame events specially, and simply displays any other activated
hyperlinks.

```java
class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}
```

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

The

setText

method can be used to initialize
the component from a string. In this case the current

EditorKit

will be used, and the content type will be
expected to be of this type.

The

read

method can be used to initialize the
component from a

Reader

. Note that if the content type is HTML,
relative references (e.g. for things like images) can't be resolved
unless the <base> tag is used or the

Base

property
on

HTMLDocument

is set.
In this case the current

EditorKit

will be used,
and the content type will be expected to be of this type.

The

setPage

method can be used to initialize
the component from a URL. In this case, the content type will be
determined from the URL, and the registered

EditorKit

for that content type will be set.

Some kinds of content may provide hyperlink support by generating
hyperlink events. The HTML

EditorKit

will generate
hyperlink events if the

JEditorPane

is

not editable

(

JEditorPane.setEditable(false);

has been called).
If HTML frames are embedded in the document, the typical response would be
to change a portion of the current document. The following code
fragment is a possible hyperlink listener implementation, that treats
HTML frame events specially, and simply displays any other activated
hyperlinks.

```java
class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}
```

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

class Hyperactive implements HyperlinkListener {

public void hyperlinkUpdate(HyperlinkEvent e) {
if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
JEditorPane pane = (JEditorPane) e.getSource();
if (e instanceof HTMLFrameHyperlinkEvent) {
HTMLFrameHyperlinkEvent evt = (HTMLFrameHyperlinkEvent)e;
HTMLDocument doc = (HTMLDocument)pane.getDocument();
doc.processHTMLFrameHyperlinkEvent(evt);
} else {
try {
pane.setPage(e.getURL());
} catch (Throwable t) {
t.printStackTrace();
}
}
}
}
}

For information on customizing how

text/html

is rendered please see

W3C_LENGTH_UNITS

and

HONOR_DISPLAY_PROPERTIES

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

Culturally dependent information in some documents is handled through
a mechanism called character encoding. Character encoding is an
unambiguous mapping of the members of a character set (letters, ideographs,
digits, symbols, or control functions) to specific numeric code values. It
represents the way the file is stored. Example character encodings are
ISO-8859-1, ISO-8859-5, Shift-jis, Euc-jp, and UTF-8. When the file is
passed to an user agent (

JEditorPane

) it is converted to
the document character set (ISO-10646 aka Unicode).

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

There are multiple ways to get a character set mapping to happen
with

JEditorPane

.

- One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

One way is to specify the character set as a parameter of the MIME
type. This will be established by a call to the

setContentType

method. If the content
is loaded by the

setPage

method the content
type will have been set according to the specification of the URL.
It the file is loaded directly, the content type would be expected to
have been set prior to loading.

Another way the character set can be specified is in the document itself.
This requires reading the document prior to determining the character set
that is desired. To handle this, it is expected that the

EditorKit

.read operation throw a

ChangedCharSetException

which will
be caught. The read is then restarted with a new Reader that uses
the character set specified in the

ChangedCharSetException

(which is an

IOException

).

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

protected class

JEditorPane.AccessibleJEditorPane

This class implements accessibility support for the

JEditorPane

class.

protected class

JEditorPane.AccessibleJEditorPaneHTML

This class provides support for

AccessibleHypertext

,
and is used in instances where the

EditorKit

installed in this

JEditorPane

is an instance of

HTMLEditorKit

.

protected class

JEditorPane.JEditorPaneAccessibleHypertextSupport

What's returned by

AccessibleJEditorPaneHTML.getAccessibleText

.

- Nested classes/interfaces declared in class javax.swing.text.

JTextComponent

JTextComponent.AccessibleJTextComponent

,

JTextComponent.DropLocation

,

JTextComponent.KeyBinding

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

HONOR_DISPLAY_PROPERTIES

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

static

String

W3C_LENGTH_UNITS

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

- Fields declared in class javax.swing.text.

JTextComponent

DEFAULT_KEYMAP

,

FOCUS_ACCELERATOR_KEY

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JEditorPane

()

Creates a new

JEditorPane

.

JEditorPane

​(

String

url)

Creates a

JEditorPane

based on a string containing
a URL specification.

JEditorPane

​(

String

type,

String

text)

Creates a

JEditorPane

that has been initialized
to the given text.

JEditorPane

​(

URL

initialPage)

Creates a

JEditorPane

based on a specified URL for input.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addHyperlinkListener

​(

HyperlinkListener

listener)

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

protected

EditorKit

createDefaultEditorKit

()

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

static

EditorKit

createEditorKitForContentType

​(

String

type)

Creates a handler for the given type from the default registry
of editor kits.

void

fireHyperlinkUpdate

​(

HyperlinkEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JEditorPane.

String

getContentType

()

Gets the type of content that this editor
is currently set to deal with.

EditorKit

getEditorKit

()

Fetches the currently installed kit for handling content.

static

String

getEditorKitClassNameForContentType

​(

String

type)

Returns the currently registered

EditorKit

class name for the
type

type

.

EditorKit

getEditorKitForContentType

​(

String

type)

Fetches the editor kit to use for the given type
of content.

HyperlinkListener

[]

getHyperlinkListeners

()

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

URL

getPage

()

Gets the current URL being displayed.

Dimension

getPreferredSize

()

Returns the preferred size for the

JEditorPane

.

boolean

getScrollableTracksViewportHeight

()

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

boolean

getScrollableTracksViewportWidth

()

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

protected

InputStream

getStream

​(

URL

page)

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method.

String

getText

()

Returns the text contained in this

TextComponent

in terms of the
content type of this editor.

String

getUIClassID

()

Gets the class ID for the UI.

protected

String

paramString

()

Returns a string representation of this

JEditorPane

.

void

read

​(

InputStream

in,

Object

desc)

This method initializes from a stream.

static void

registerEditorKitForContentType

​(

String

type,

String

classname)

Establishes the default bindings of

type

to

classname

.

static void

registerEditorKitForContentType

​(

String

type,

String

classname,

ClassLoader

loader)

Establishes the default bindings of

type

to

classname

.

void

removeHyperlinkListener

​(

HyperlinkListener

listener)

Removes a hyperlink listener.

void

replaceSelection

​(

String

content)

Replaces the currently selected content with new content
represented by the given string.

void

scrollToReference

​(

String

reference)

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed).

void

setContentType

​(

String

type)

Sets the type of content that this editor
handles.

void

setEditorKit

​(

EditorKit

kit)

Sets the currently installed kit for handling
content.

void

setEditorKitForContentType

​(

String

type,

EditorKit

k)

Directly sets the editor kit to use for the given type.

void

setPage

​(

String

url)

Sets the current URL being displayed.

void

setPage

​(

URL

page)

Sets the current URL being displayed.

void

setText

​(

String

t)

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor.

- Methods declared in class javax.swing.text.

JTextComponent

addCaretListener

,

addKeymap

,

copy

,

cut

,

fireCaretUpdate

,

getActions

,

getCaret

,

getCaretColor

,

getCaretListeners

,

getCaretPosition

,

getDisabledTextColor

,

getDocument

,

getDragEnabled

,

getDropLocation

,

getDropMode

,

getFocusAccelerator

,

getHighlighter

,

getKeymap

,

getKeymap

,

getMargin

,

getNavigationFilter

,

getPreferredScrollableViewportSize

,

getPrintable

,

getScrollableBlockIncrement

,

getScrollableUnitIncrement

,

getSelectedText

,

getSelectedTextColor

,

getSelectionColor

,

getSelectionEnd

,

getSelectionStart

,

getText

,

getToolTipText

,

getUI

,

isEditable

,

loadKeymap

,

modelToView

,

modelToView2D

,

moveCaretPosition

,

paste

,

print

,

print

,

print

,

read

,

removeCaretListener

,

removeKeymap

,

restoreComposedText

,

saveComposedText

,

select

,

selectAll

,

setCaret

,

setCaretColor

,

setCaretPosition

,

setDisabledTextColor

,

setDocument

,

setDragEnabled

,

setDropMode

,

setEditable

,

setFocusAccelerator

,

setHighlighter

,

setKeymap

,

setMargin

,

setNavigationFilter

,

setSelectedTextColor

,

setSelectionColor

,

setSelectionEnd

,

setSelectionStart

,

setUI

,

updateUI

,

viewToModel

,

viewToModel2D

,

write

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

protected class

JEditorPane.AccessibleJEditorPane

This class implements accessibility support for the

JEditorPane

class.

protected class

JEditorPane.AccessibleJEditorPaneHTML

This class provides support for

AccessibleHypertext

,
and is used in instances where the

EditorKit

installed in this

JEditorPane

is an instance of

HTMLEditorKit

.

protected class

JEditorPane.JEditorPaneAccessibleHypertextSupport

What's returned by

AccessibleJEditorPaneHTML.getAccessibleText

.

- Nested classes/interfaces declared in class javax.swing.text.

JTextComponent

JTextComponent.AccessibleJTextComponent

,

JTextComponent.DropLocation

,

JTextComponent.KeyBinding

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

This class implements accessibility support for the

JEditorPane

class.

This class provides support for

AccessibleHypertext

,
and is used in instances where the

EditorKit

installed in this

JEditorPane

is an instance of

HTMLEditorKit

.

What's returned by

AccessibleJEditorPaneHTML.getAccessibleText

.

Nested classes/interfaces declared in class javax.swing.text.

JTextComponent

JTextComponent.AccessibleJTextComponent

,

JTextComponent.DropLocation

,

JTextComponent.KeyBinding

---

#### Nested classes/interfaces declared in class javax.swing.text. JTextComponent

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

static

String

HONOR_DISPLAY_PROPERTIES

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

static

String

W3C_LENGTH_UNITS

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

- Fields declared in class javax.swing.text.

JTextComponent

DEFAULT_KEYMAP

,

FOCUS_ACCELERATOR_KEY

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

Fields declared in class javax.swing.text.

JTextComponent

DEFAULT_KEYMAP

,

FOCUS_ACCELERATOR_KEY

---

#### Fields declared in class javax.swing.text. JTextComponent

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

JEditorPane

()

Creates a new

JEditorPane

.

JEditorPane

​(

String

url)

Creates a

JEditorPane

based on a string containing
a URL specification.

JEditorPane

​(

String

type,

String

text)

Creates a

JEditorPane

that has been initialized
to the given text.

JEditorPane

​(

URL

initialPage)

Creates a

JEditorPane

based on a specified URL for input.

---

#### Constructor Summary

Creates a new

JEditorPane

.

Creates a

JEditorPane

based on a string containing
a URL specification.

Creates a

JEditorPane

that has been initialized
to the given text.

Creates a

JEditorPane

based on a specified URL for input.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addHyperlinkListener

​(

HyperlinkListener

listener)

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

protected

EditorKit

createDefaultEditorKit

()

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

static

EditorKit

createEditorKitForContentType

​(

String

type)

Creates a handler for the given type from the default registry
of editor kits.

void

fireHyperlinkUpdate

​(

HyperlinkEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JEditorPane.

String

getContentType

()

Gets the type of content that this editor
is currently set to deal with.

EditorKit

getEditorKit

()

Fetches the currently installed kit for handling content.

static

String

getEditorKitClassNameForContentType

​(

String

type)

Returns the currently registered

EditorKit

class name for the
type

type

.

EditorKit

getEditorKitForContentType

​(

String

type)

Fetches the editor kit to use for the given type
of content.

HyperlinkListener

[]

getHyperlinkListeners

()

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

URL

getPage

()

Gets the current URL being displayed.

Dimension

getPreferredSize

()

Returns the preferred size for the

JEditorPane

.

boolean

getScrollableTracksViewportHeight

()

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

boolean

getScrollableTracksViewportWidth

()

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

protected

InputStream

getStream

​(

URL

page)

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method.

String

getText

()

Returns the text contained in this

TextComponent

in terms of the
content type of this editor.

String

getUIClassID

()

Gets the class ID for the UI.

protected

String

paramString

()

Returns a string representation of this

JEditorPane

.

void

read

​(

InputStream

in,

Object

desc)

This method initializes from a stream.

static void

registerEditorKitForContentType

​(

String

type,

String

classname)

Establishes the default bindings of

type

to

classname

.

static void

registerEditorKitForContentType

​(

String

type,

String

classname,

ClassLoader

loader)

Establishes the default bindings of

type

to

classname

.

void

removeHyperlinkListener

​(

HyperlinkListener

listener)

Removes a hyperlink listener.

void

replaceSelection

​(

String

content)

Replaces the currently selected content with new content
represented by the given string.

void

scrollToReference

​(

String

reference)

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed).

void

setContentType

​(

String

type)

Sets the type of content that this editor
handles.

void

setEditorKit

​(

EditorKit

kit)

Sets the currently installed kit for handling
content.

void

setEditorKitForContentType

​(

String

type,

EditorKit

k)

Directly sets the editor kit to use for the given type.

void

setPage

​(

String

url)

Sets the current URL being displayed.

void

setPage

​(

URL

page)

Sets the current URL being displayed.

void

setText

​(

String

t)

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor.

- Methods declared in class javax.swing.text.

JTextComponent

addCaretListener

,

addKeymap

,

copy

,

cut

,

fireCaretUpdate

,

getActions

,

getCaret

,

getCaretColor

,

getCaretListeners

,

getCaretPosition

,

getDisabledTextColor

,

getDocument

,

getDragEnabled

,

getDropLocation

,

getDropMode

,

getFocusAccelerator

,

getHighlighter

,

getKeymap

,

getKeymap

,

getMargin

,

getNavigationFilter

,

getPreferredScrollableViewportSize

,

getPrintable

,

getScrollableBlockIncrement

,

getScrollableUnitIncrement

,

getSelectedText

,

getSelectedTextColor

,

getSelectionColor

,

getSelectionEnd

,

getSelectionStart

,

getText

,

getToolTipText

,

getUI

,

isEditable

,

loadKeymap

,

modelToView

,

modelToView2D

,

moveCaretPosition

,

paste

,

print

,

print

,

print

,

read

,

removeCaretListener

,

removeKeymap

,

restoreComposedText

,

saveComposedText

,

select

,

selectAll

,

setCaret

,

setCaretColor

,

setCaretPosition

,

setDisabledTextColor

,

setDocument

,

setDragEnabled

,

setDropMode

,

setEditable

,

setFocusAccelerator

,

setHighlighter

,

setKeymap

,

setMargin

,

setNavigationFilter

,

setSelectedTextColor

,

setSelectionColor

,

setSelectionEnd

,

setSelectionStart

,

setUI

,

updateUI

,

viewToModel

,

viewToModel2D

,

write

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

wait

,

wait

,

wait

---

#### Method Summary

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

Creates a handler for the given type from the default registry
of editor kits.

Notifies all listeners that have registered interest for
notification on this event type.

Gets the AccessibleContext associated with this JEditorPane.

Gets the type of content that this editor
is currently set to deal with.

Fetches the currently installed kit for handling content.

Returns the currently registered

EditorKit

class name for the
type

type

.

Fetches the editor kit to use for the given type
of content.

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

Gets the current URL being displayed.

Returns the preferred size for the

JEditorPane

.

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method.

Returns the text contained in this

TextComponent

in terms of the
content type of this editor.

Gets the class ID for the UI.

Returns a string representation of this

JEditorPane

.

This method initializes from a stream.

Establishes the default bindings of

type

to

classname

.

Removes a hyperlink listener.

Replaces the currently selected content with new content
represented by the given string.

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed).

Sets the type of content that this editor
handles.

Sets the currently installed kit for handling
content.

Directly sets the editor kit to use for the given type.

Sets the current URL being displayed.

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor.

Methods declared in class javax.swing.text.

JTextComponent

addCaretListener

,

addKeymap

,

copy

,

cut

,

fireCaretUpdate

,

getActions

,

getCaret

,

getCaretColor

,

getCaretListeners

,

getCaretPosition

,

getDisabledTextColor

,

getDocument

,

getDragEnabled

,

getDropLocation

,

getDropMode

,

getFocusAccelerator

,

getHighlighter

,

getKeymap

,

getKeymap

,

getMargin

,

getNavigationFilter

,

getPreferredScrollableViewportSize

,

getPrintable

,

getScrollableBlockIncrement

,

getScrollableUnitIncrement

,

getSelectedText

,

getSelectedTextColor

,

getSelectionColor

,

getSelectionEnd

,

getSelectionStart

,

getText

,

getToolTipText

,

getUI

,

isEditable

,

loadKeymap

,

modelToView

,

modelToView2D

,

moveCaretPosition

,

paste

,

print

,

print

,

print

,

read

,

removeCaretListener

,

removeKeymap

,

restoreComposedText

,

saveComposedText

,

select

,

selectAll

,

setCaret

,

setCaretColor

,

setCaretPosition

,

setDisabledTextColor

,

setDocument

,

setDragEnabled

,

setDropMode

,

setEditable

,

setFocusAccelerator

,

setHighlighter

,

setKeymap

,

setMargin

,

setNavigationFilter

,

setSelectedTextColor

,

setSelectionColor

,

setSelectionEnd

,

setSelectionStart

,

setUI

,

updateUI

,

viewToModel

,

viewToModel2D

,

write

---

#### Methods declared in class javax.swing.text. JTextComponent

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- W3C_LENGTH_UNITS

```java
public static final
String
W3C_LENGTH_UNITS
```

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

By default this is not enabled; to enable
it set the client

property

with this name
to

Boolean.TRUE

.

**Since:** 1.5
**See Also:** Constant Field Values

- HONOR_DISPLAY_PROPERTIES

```java
public static final
String
HONOR_DISPLAY_PROPERTIES
```

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

The default varies based on the look and feel;
to enable it set the client

property

with
this name to

Boolean.TRUE

.

**Since:** 1.5
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JEditorPane

```java
public JEditorPane()
```

Creates a new

JEditorPane

.
The document model is set to

null

.

- JEditorPane

```java
public JEditorPane​(
URL
initialPage)
throws
IOException
```

Creates a

JEditorPane

based on a specified URL for input.

**Parameters:** initialPage

- the URL
**Throws:** IOException

- if the URL is

null

or cannot be accessed

- JEditorPane

```java
public JEditorPane​(
String
url)
throws
IOException
```

Creates a

JEditorPane

based on a string containing
a URL specification.

**Parameters:** url

- the URL
**Throws:** IOException

- if the URL is

null

or
cannot be accessed

- JEditorPane

```java
public JEditorPane​(
String
type,

String
text)
```

Creates a

JEditorPane

that has been initialized
to the given text. This is a convenience constructor that calls the

setContentType

and

setText

methods.

**Parameters:** type

- mime type of the given text
**Parameters:** text

- the text to initialize with; may be

null
**Throws:** NullPointerException

- if the

type

parameter
is

null

============ METHOD DETAIL ==========

- Method Detail

- addHyperlinkListener

```java
public void addHyperlinkListener​(
HyperlinkListener
listener)
```

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

**Parameters:** listener

- the listener

- removeHyperlinkListener

```java
public void removeHyperlinkListener​(
HyperlinkListener
listener)
```

Removes a hyperlink listener.

**Parameters:** listener

- the listener

- getHyperlinkListeners

```java
@BeanProperty
(
bound
=false)
public
HyperlinkListener
[] getHyperlinkListeners()
```

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

**Returns:** all of the

HyperLinkListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireHyperlinkUpdate

```java
public void fireHyperlinkUpdate​(
HyperlinkEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. This is normally called
by the currently installed

EditorKit

if a content type
that supports hyperlinks is currently active and there
was activity with a link. The listener list is processed
last to first.

**Parameters:** e

- the event
**See Also:** EventListenerList

- setPage

```java
@BeanProperty
(
expert
=true,

description
="the URL used to set content")
public void setPage​(
URL
page)
throws
IOException
```

Sets the current URL being displayed. The content type of the
pane is set, and if the editor kit for the pane is
non-

null

, then
a new default document is created and the URL is read into it.
If the URL contains and reference location, the location will
be scrolled to by calling the

scrollToReference

method. If the desired URL is the one currently being displayed,
the document will not be reloaded. To force a document
reload it is necessary to clear the stream description property
of the document. The following code shows how this can be done:

```java
Document doc = jEditorPane.getDocument();
doc.putProperty(Document.StreamDescriptionProperty, null);
```

If the desired URL is not the one currently being
displayed, the

getStream

method is called to
give subclasses control over the stream provided.

This may load either synchronously or asynchronously
depending upon the document returned by the

EditorKit

.
If the

Document

is of type

AbstractDocument

and has a value returned by

AbstractDocument.getAsynchronousLoadPriority

that is greater than or equal to zero, the page will be
loaded on a separate thread using that priority.

If the document is loaded synchronously, it will be
filled in with the stream prior to being installed into
the editor with a call to

setDocument

, which
is bound and will fire a property change event. If an

IOException

is thrown the partially loaded
document will
be discarded and neither the document or page property
change events will be fired. If the document is
successfully loaded and installed, a view will be
built for it by the UI which will then be scrolled if
necessary, and then the page property change event
will be fired.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

**Parameters:** page

- the URL of the page
**Throws:** IOException

- for a

null

or invalid
page specification, or exception from the stream being read
**See Also:** getPage()

- read

```java
public void read​(
InputStream
in,

Object
desc)
throws
IOException
```

This method initializes from a stream. If the kit is
set to be of type

HTMLEditorKit

, and the

desc

parameter is an

HTMLDocument

,
then it invokes the

HTMLEditorKit

to initiate
the read. Otherwise it calls the superclass
method which loads the model as plain text.

**Parameters:** in

- the stream from which to read
**Parameters:** desc

- an object describing the stream
**Throws:** IOException

- as thrown by the stream being
used to initialize
**See Also:** JTextComponent.read(java.io.Reader, java.lang.Object)

,

JTextComponent.setDocument(javax.swing.text.Document)

- getStream

```java
protected
InputStream
getStream​(
URL
page)
throws
IOException
```

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method. By
default, this simply opens the URL and returns the
stream. This can be reimplemented to do useful things
like fetch the stream from a cache, monitor the progress
of the stream, etc.

This method is expected to have the side effect of
establishing the content type, and therefore setting the
appropriate

EditorKit

to use for loading the stream.

If this the stream was an http connection, redirects
will be followed and the resulting URL will be set as
the

Document.StreamDescriptionProperty

so that relative
URL's can be properly resolved.

**Parameters:** page

- the URL of the page
**Returns:** a stream for the URL which is about to be loaded
**Throws:** IOException

- if an I/O problem occurs

- scrollToReference

```java
public void scrollToReference​(
String
reference)
```

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed). By default, this
method only knows how to locate a reference in an
HTMLDocument. The implementation calls the

scrollRectToVisible

method to
accomplish the actual scrolling. If scrolling to a
reference location is needed for document types other
than HTML, this method should be reimplemented.
This method will have no effect if the component
is not visible.

**Parameters:** reference

- the named location to scroll to

- getPage

```java
public
URL
getPage()
```

Gets the current URL being displayed. If a URL was
not specified in the creation of the document, this
will return

null

, and relative URL's will not be
resolved.

**Returns:** the URL, or

null

if none

- setPage

```java
public void setPage​(
String
url)
throws
IOException
```

Sets the current URL being displayed.

**Parameters:** url

- the URL for display
**Throws:** IOException

- for a

null

or invalid URL
specification

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Gets the class ID for the UI.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "EditorPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- createDefaultEditorKit

```java
protected
EditorKit
createDefaultEditorKit()
```

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

**Returns:** the editor kit

- getEditorKit

```java
public
EditorKit
getEditorKit()
```

Fetches the currently installed kit for handling content.

createDefaultEditorKit

is called to set up a default
if necessary.

**Returns:** the editor kit

- getContentType

```java
public final
String
getContentType()
```

Gets the type of content that this editor
is currently set to deal with. This is
defined to be the type associated with the
currently installed

EditorKit

.

**Returns:** the content type,

null

if no editor kit set

- setContentType

```java
@BeanProperty
(
bound
=false,

description
="the type of content")
public final void setContentType​(
String
type)
```

Sets the type of content that this editor
handles. This calls

getEditorKitForContentType

,
and then

setEditorKit

if an editor kit can
be successfully located. This is mostly convenience method
that can be used as an alternative to calling

setEditorKit

directly.

If there is a charset definition specified as a parameter
of the content type specification, it will be used when
loading input streams using the associated

EditorKit

.
For example if the type is specified as

text/html; charset=EUC-JP

the content
will be loaded using the

EditorKit

registered for

text/html

and the Reader provided to
the

EditorKit

to load unicode into the document will
use the

EUC-JP

charset for translating
to unicode. If the type is not recognized, the content
will be loaded using the

EditorKit

registered
for plain text,

text/plain

.

**Parameters:** type

- the non-

null

mime type for the content editing
support
**Throws:** NullPointerException

- if the

type

parameter
is

null
**See Also:** getContentType()

- setEditorKit

```java
@BeanProperty
(
expert
=true,

description
="the currently installed kit for handling content")
public void setEditorKit​(
EditorKit
kit)
```

Sets the currently installed kit for handling
content. This is the bound property that
establishes the content type of the editor.
Any old kit is first deinstalled, then if kit is
non-

null

,
the new kit is installed, and a default document created for it.
A

PropertyChange

event ("editorKit") is always fired when

setEditorKit

is called.

NOTE: This has the side effect of changing the model,
because the

EditorKit

is the source of how a
particular type
of content is modeled. This method will cause

setDocument

to be called on behalf of the caller to ensure integrity
of the internal state.

**Parameters:** kit

- the desired editor behavior
**See Also:** getEditorKit()

- getEditorKitForContentType

```java
public
EditorKit
getEditorKitForContentType​(
String
type)
```

Fetches the editor kit to use for the given type
of content. This is called when a type is requested
that doesn't match the currently installed type.
If the component doesn't have an

EditorKit

registered
for the given type, it will try to create an

EditorKit

from the default

EditorKit

registry.
If that fails, a

PlainEditorKit

is used on the
assumption that all text documents can be represented
as plain text.

This method can be reimplemented to use some
other kind of type registry. This can
be reimplemented to use the Java Activation
Framework, for example.

**Parameters:** type

- the non-

null

content type
**Returns:** the editor kit

- setEditorKitForContentType

```java
public void setEditorKitForContentType​(
String
type,

EditorKit
k)
```

Directly sets the editor kit to use for the given type. A
look-and-feel implementation might use this in conjunction
with

createEditorKitForContentType

to install handlers for
content types with a look-and-feel bias.

**Parameters:** type

- the non-

null

content type
**Parameters:** k

- the editor kit to be set

- replaceSelection

```java
public void replaceSelection​(
String
content)
```

Replaces the currently selected content with new content
represented by the given string. If there is no selection
this amounts to an insert of the given text. If there
is no replacement text (i.e. the content string is empty
or

null

) this amounts to a removal of the
current selection. The replacement text will have the
attributes currently defined for input. If the component is not
editable, beep and return.

**Overrides:** replaceSelection

in class

JTextComponent
**Parameters:** content

- the content to replace the selection with. This
value can be

null

- createEditorKitForContentType

```java
public static
EditorKit
createEditorKitForContentType​(
String
type)
```

Creates a handler for the given type from the default registry
of editor kits. The registry is created if necessary. If the
registered class has not yet been loaded, an attempt
is made to dynamically load the prototype of the kit for the
given type. If the type was registered with a

ClassLoader

,
that

ClassLoader

will be used to load the prototype.
If there was no registered

ClassLoader

,

Class.forName

will be used to load the prototype.

Once a prototype

EditorKit

instance is successfully
located, it is cloned and the clone is returned.

**Parameters:** type

- the content type
**Returns:** the editor kit, or

null

if there is nothing
registered for the given type

- registerEditorKitForContentType

```java
public static void registerEditorKitForContentType​(
String
type,

String
classname)
```

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed, and can be safely changed before attempted uses
to avoid loading unwanted classes. The prototype

EditorKit

will be loaded with

Class.forName

when registered with this method.

**Parameters:** type

- the non-

null

content type
**Parameters:** classname

- the class to load later

- registerEditorKitForContentType

```java
public static void registerEditorKitForContentType​(
String
type,

String
classname,

ClassLoader
loader)
```

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed using the given

ClassLoader

,
and can be safely changed
before attempted uses to avoid loading unwanted classes.

**Parameters:** type

- the non-

null

content type
**Parameters:** classname

- the class to load later
**Parameters:** loader

- the

ClassLoader

to use to load the name

- getEditorKitClassNameForContentType

```java
public static
String
getEditorKitClassNameForContentType​(
String
type)
```

Returns the currently registered

EditorKit

class name for the
type

type

.

**Parameters:** type

- the non-

null

content type
**Returns:** a

String

containing the

EditorKit

class name
for

type
**Since:** 1.3

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size for the

JEditorPane

.
The preferred size for

JEditorPane

is slightly altered
from the preferred size of the superclass. If the size
of the viewport has become smaller than the minimum size
of the component, the scrollable definition for tracking
width or height will turn to false. The default viewport
layout will give the preferred size, and that is not desired
in the case where the scrollable is tracking. In that case
the

normal

preferred size is adjusted to the
minimum size. This allows things like HTML tables to
shrink down to their minimum size and then be laid out at
their minimum size, refusing to shrink any further.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** a

Dimension

containing the preferred size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

- setText

```java
@BeanProperty
(
bound
=false,

description
="the text of this component")
public void setText​(
String
t)
```

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor. For example, if the type is set to

text/html

the string should be specified in terms of HTML.

This is implemented to remove the contents of the current document,
and replace them by parsing the given string using the current

EditorKit

. This gives the semantics of the
superclass by not changing
out the model, while supporting the content type currently set on
this component. The assumption is that the previous content is
relatively
small, and that the previous content doesn't have side effects.
Both of those assumptions can be violated and cause undesirable results.
To avoid this, create a new document,

getEditorKit().createDefaultDocument()

, and replace the
existing

Document

with the new one. You are then assured the
previous

Document

won't have any lingering state.

- Leaving the existing model in place means that the old view will be
torn down, and a new view created, where replacing the document would
avoid the tear down of the old view.

Some formats (such as HTML) can install things into the document that
can influence future contents. HTML can have style information embedded
that would influence the next content installed unexpectedly.

An alternative way to load this component with a string would be to
create a StringReader and call the read method. In this case the model
would be replaced after it was initialized with the contents of the
string.

**Overrides:** setText

in class

JTextComponent
**Parameters:** t

- the new text to be set; if

null

the old
text will be deleted
**See Also:** getText()

- getText

```java
public
String
getText()
```

Returns the text contained in this

TextComponent

in terms of the
content type of this editor. If an exception is thrown while
attempting to retrieve the text,

null

will be returned.
This is implemented to call

JTextComponent.write

with
a

StringWriter

.

**Overrides:** getText

in class

JTextComponent
**Returns:** the text
**See Also:** setText(java.lang.String)

- getScrollableTracksViewportWidth

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()
```

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Overrides:** getScrollableTracksViewportWidth

in class

JTextComponent
**Returns:** true if a viewport should force the Scrollables width to
match its own, false otherwise

- getScrollableTracksViewportHeight

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()
```

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Overrides:** getScrollableTracksViewportHeight

in class

JTextComponent
**Returns:** true if a viewport should force the

Scrollable

's height to match its own,
false otherwise

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JEditorPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JTextComponent
**Returns:** a string representation of this

JEditorPane

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JEditorPane.
For editor panes, the AccessibleContext takes the form of an
AccessibleJEditorPane.
A new AccessibleJEditorPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JTextComponent
**Returns:** an AccessibleJEditorPane that serves as the
AccessibleContext of this JEditorPane

Field Detail

- W3C_LENGTH_UNITS

```java
public static final
String
W3C_LENGTH_UNITS
```

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

By default this is not enabled; to enable
it set the client

property

with this name
to

Boolean.TRUE

.

**Since:** 1.5
**See Also:** Constant Field Values

- HONOR_DISPLAY_PROPERTIES

```java
public static final
String
HONOR_DISPLAY_PROPERTIES
```

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

The default varies based on the look and feel;
to enable it set the client

property

with
this name to

Boolean.TRUE

.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### Field Detail

W3C_LENGTH_UNITS

```java
public static final
String
W3C_LENGTH_UNITS
```

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

By default this is not enabled; to enable
it set the client

property

with this name
to

Boolean.TRUE

.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### W3C_LENGTH_UNITS

public static final

String

W3C_LENGTH_UNITS

Key for a client property used to indicate whether

w3c compliant

length units are used for html rendering.

By default this is not enabled; to enable
it set the client

property

with this name
to

Boolean.TRUE

.

By default this is not enabled; to enable
it set the client

property

with this name
to

Boolean.TRUE

.

HONOR_DISPLAY_PROPERTIES

```java
public static final
String
HONOR_DISPLAY_PROPERTIES
```

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

The default varies based on the look and feel;
to enable it set the client

property

with
this name to

Boolean.TRUE

.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### HONOR_DISPLAY_PROPERTIES

public static final

String

HONOR_DISPLAY_PROPERTIES

Key for a client property used to indicate whether
the default font and foreground color from the component are
used if a font or foreground color is not specified in the styled
text.

The default varies based on the look and feel;
to enable it set the client

property

with
this name to

Boolean.TRUE

.

The default varies based on the look and feel;
to enable it set the client

property

with
this name to

Boolean.TRUE

.

Constructor Detail

- JEditorPane

```java
public JEditorPane()
```

Creates a new

JEditorPane

.
The document model is set to

null

.

- JEditorPane

```java
public JEditorPane​(
URL
initialPage)
throws
IOException
```

Creates a

JEditorPane

based on a specified URL for input.

**Parameters:** initialPage

- the URL
**Throws:** IOException

- if the URL is

null

or cannot be accessed

- JEditorPane

```java
public JEditorPane​(
String
url)
throws
IOException
```

Creates a

JEditorPane

based on a string containing
a URL specification.

**Parameters:** url

- the URL
**Throws:** IOException

- if the URL is

null

or
cannot be accessed

- JEditorPane

```java
public JEditorPane​(
String
type,

String
text)
```

Creates a

JEditorPane

that has been initialized
to the given text. This is a convenience constructor that calls the

setContentType

and

setText

methods.

**Parameters:** type

- mime type of the given text
**Parameters:** text

- the text to initialize with; may be

null
**Throws:** NullPointerException

- if the

type

parameter
is

null

---

#### Constructor Detail

JEditorPane

```java
public JEditorPane()
```

Creates a new

JEditorPane

.
The document model is set to

null

.

---

#### JEditorPane

public JEditorPane()

Creates a new

JEditorPane

.
The document model is set to

null

.

JEditorPane

```java
public JEditorPane​(
URL
initialPage)
throws
IOException
```

Creates a

JEditorPane

based on a specified URL for input.

**Parameters:** initialPage

- the URL
**Throws:** IOException

- if the URL is

null

or cannot be accessed

---

#### JEditorPane

public JEditorPane​(

URL

initialPage)
throws

IOException

Creates a

JEditorPane

based on a specified URL for input.

JEditorPane

```java
public JEditorPane​(
String
url)
throws
IOException
```

Creates a

JEditorPane

based on a string containing
a URL specification.

**Parameters:** url

- the URL
**Throws:** IOException

- if the URL is

null

or
cannot be accessed

---

#### JEditorPane

public JEditorPane​(

String

url)
throws

IOException

Creates a

JEditorPane

based on a string containing
a URL specification.

JEditorPane

```java
public JEditorPane​(
String
type,

String
text)
```

Creates a

JEditorPane

that has been initialized
to the given text. This is a convenience constructor that calls the

setContentType

and

setText

methods.

**Parameters:** type

- mime type of the given text
**Parameters:** text

- the text to initialize with; may be

null
**Throws:** NullPointerException

- if the

type

parameter
is

null

---

#### JEditorPane

public JEditorPane​(

String

type,

String

text)

Creates a

JEditorPane

that has been initialized
to the given text. This is a convenience constructor that calls the

setContentType

and

setText

methods.

Method Detail

- addHyperlinkListener

```java
public void addHyperlinkListener​(
HyperlinkListener
listener)
```

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

**Parameters:** listener

- the listener

- removeHyperlinkListener

```java
public void removeHyperlinkListener​(
HyperlinkListener
listener)
```

Removes a hyperlink listener.

**Parameters:** listener

- the listener

- getHyperlinkListeners

```java
@BeanProperty
(
bound
=false)
public
HyperlinkListener
[] getHyperlinkListeners()
```

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

**Returns:** all of the

HyperLinkListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireHyperlinkUpdate

```java
public void fireHyperlinkUpdate​(
HyperlinkEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. This is normally called
by the currently installed

EditorKit

if a content type
that supports hyperlinks is currently active and there
was activity with a link. The listener list is processed
last to first.

**Parameters:** e

- the event
**See Also:** EventListenerList

- setPage

```java
@BeanProperty
(
expert
=true,

description
="the URL used to set content")
public void setPage​(
URL
page)
throws
IOException
```

Sets the current URL being displayed. The content type of the
pane is set, and if the editor kit for the pane is
non-

null

, then
a new default document is created and the URL is read into it.
If the URL contains and reference location, the location will
be scrolled to by calling the

scrollToReference

method. If the desired URL is the one currently being displayed,
the document will not be reloaded. To force a document
reload it is necessary to clear the stream description property
of the document. The following code shows how this can be done:

```java
Document doc = jEditorPane.getDocument();
doc.putProperty(Document.StreamDescriptionProperty, null);
```

If the desired URL is not the one currently being
displayed, the

getStream

method is called to
give subclasses control over the stream provided.

This may load either synchronously or asynchronously
depending upon the document returned by the

EditorKit

.
If the

Document

is of type

AbstractDocument

and has a value returned by

AbstractDocument.getAsynchronousLoadPriority

that is greater than or equal to zero, the page will be
loaded on a separate thread using that priority.

If the document is loaded synchronously, it will be
filled in with the stream prior to being installed into
the editor with a call to

setDocument

, which
is bound and will fire a property change event. If an

IOException

is thrown the partially loaded
document will
be discarded and neither the document or page property
change events will be fired. If the document is
successfully loaded and installed, a view will be
built for it by the UI which will then be scrolled if
necessary, and then the page property change event
will be fired.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

**Parameters:** page

- the URL of the page
**Throws:** IOException

- for a

null

or invalid
page specification, or exception from the stream being read
**See Also:** getPage()

- read

```java
public void read​(
InputStream
in,

Object
desc)
throws
IOException
```

This method initializes from a stream. If the kit is
set to be of type

HTMLEditorKit

, and the

desc

parameter is an

HTMLDocument

,
then it invokes the

HTMLEditorKit

to initiate
the read. Otherwise it calls the superclass
method which loads the model as plain text.

**Parameters:** in

- the stream from which to read
**Parameters:** desc

- an object describing the stream
**Throws:** IOException

- as thrown by the stream being
used to initialize
**See Also:** JTextComponent.read(java.io.Reader, java.lang.Object)

,

JTextComponent.setDocument(javax.swing.text.Document)

- getStream

```java
protected
InputStream
getStream​(
URL
page)
throws
IOException
```

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method. By
default, this simply opens the URL and returns the
stream. This can be reimplemented to do useful things
like fetch the stream from a cache, monitor the progress
of the stream, etc.

This method is expected to have the side effect of
establishing the content type, and therefore setting the
appropriate

EditorKit

to use for loading the stream.

If this the stream was an http connection, redirects
will be followed and the resulting URL will be set as
the

Document.StreamDescriptionProperty

so that relative
URL's can be properly resolved.

**Parameters:** page

- the URL of the page
**Returns:** a stream for the URL which is about to be loaded
**Throws:** IOException

- if an I/O problem occurs

- scrollToReference

```java
public void scrollToReference​(
String
reference)
```

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed). By default, this
method only knows how to locate a reference in an
HTMLDocument. The implementation calls the

scrollRectToVisible

method to
accomplish the actual scrolling. If scrolling to a
reference location is needed for document types other
than HTML, this method should be reimplemented.
This method will have no effect if the component
is not visible.

**Parameters:** reference

- the named location to scroll to

- getPage

```java
public
URL
getPage()
```

Gets the current URL being displayed. If a URL was
not specified in the creation of the document, this
will return

null

, and relative URL's will not be
resolved.

**Returns:** the URL, or

null

if none

- setPage

```java
public void setPage​(
String
url)
throws
IOException
```

Sets the current URL being displayed.

**Parameters:** url

- the URL for display
**Throws:** IOException

- for a

null

or invalid URL
specification

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Gets the class ID for the UI.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "EditorPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- createDefaultEditorKit

```java
protected
EditorKit
createDefaultEditorKit()
```

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

**Returns:** the editor kit

- getEditorKit

```java
public
EditorKit
getEditorKit()
```

Fetches the currently installed kit for handling content.

createDefaultEditorKit

is called to set up a default
if necessary.

**Returns:** the editor kit

- getContentType

```java
public final
String
getContentType()
```

Gets the type of content that this editor
is currently set to deal with. This is
defined to be the type associated with the
currently installed

EditorKit

.

**Returns:** the content type,

null

if no editor kit set

- setContentType

```java
@BeanProperty
(
bound
=false,

description
="the type of content")
public final void setContentType​(
String
type)
```

Sets the type of content that this editor
handles. This calls

getEditorKitForContentType

,
and then

setEditorKit

if an editor kit can
be successfully located. This is mostly convenience method
that can be used as an alternative to calling

setEditorKit

directly.

If there is a charset definition specified as a parameter
of the content type specification, it will be used when
loading input streams using the associated

EditorKit

.
For example if the type is specified as

text/html; charset=EUC-JP

the content
will be loaded using the

EditorKit

registered for

text/html

and the Reader provided to
the

EditorKit

to load unicode into the document will
use the

EUC-JP

charset for translating
to unicode. If the type is not recognized, the content
will be loaded using the

EditorKit

registered
for plain text,

text/plain

.

**Parameters:** type

- the non-

null

mime type for the content editing
support
**Throws:** NullPointerException

- if the

type

parameter
is

null
**See Also:** getContentType()

- setEditorKit

```java
@BeanProperty
(
expert
=true,

description
="the currently installed kit for handling content")
public void setEditorKit​(
EditorKit
kit)
```

Sets the currently installed kit for handling
content. This is the bound property that
establishes the content type of the editor.
Any old kit is first deinstalled, then if kit is
non-

null

,
the new kit is installed, and a default document created for it.
A

PropertyChange

event ("editorKit") is always fired when

setEditorKit

is called.

NOTE: This has the side effect of changing the model,
because the

EditorKit

is the source of how a
particular type
of content is modeled. This method will cause

setDocument

to be called on behalf of the caller to ensure integrity
of the internal state.

**Parameters:** kit

- the desired editor behavior
**See Also:** getEditorKit()

- getEditorKitForContentType

```java
public
EditorKit
getEditorKitForContentType​(
String
type)
```

Fetches the editor kit to use for the given type
of content. This is called when a type is requested
that doesn't match the currently installed type.
If the component doesn't have an

EditorKit

registered
for the given type, it will try to create an

EditorKit

from the default

EditorKit

registry.
If that fails, a

PlainEditorKit

is used on the
assumption that all text documents can be represented
as plain text.

This method can be reimplemented to use some
other kind of type registry. This can
be reimplemented to use the Java Activation
Framework, for example.

**Parameters:** type

- the non-

null

content type
**Returns:** the editor kit

- setEditorKitForContentType

```java
public void setEditorKitForContentType​(
String
type,

EditorKit
k)
```

Directly sets the editor kit to use for the given type. A
look-and-feel implementation might use this in conjunction
with

createEditorKitForContentType

to install handlers for
content types with a look-and-feel bias.

**Parameters:** type

- the non-

null

content type
**Parameters:** k

- the editor kit to be set

- replaceSelection

```java
public void replaceSelection​(
String
content)
```

Replaces the currently selected content with new content
represented by the given string. If there is no selection
this amounts to an insert of the given text. If there
is no replacement text (i.e. the content string is empty
or

null

) this amounts to a removal of the
current selection. The replacement text will have the
attributes currently defined for input. If the component is not
editable, beep and return.

**Overrides:** replaceSelection

in class

JTextComponent
**Parameters:** content

- the content to replace the selection with. This
value can be

null

- createEditorKitForContentType

```java
public static
EditorKit
createEditorKitForContentType​(
String
type)
```

Creates a handler for the given type from the default registry
of editor kits. The registry is created if necessary. If the
registered class has not yet been loaded, an attempt
is made to dynamically load the prototype of the kit for the
given type. If the type was registered with a

ClassLoader

,
that

ClassLoader

will be used to load the prototype.
If there was no registered

ClassLoader

,

Class.forName

will be used to load the prototype.

Once a prototype

EditorKit

instance is successfully
located, it is cloned and the clone is returned.

**Parameters:** type

- the content type
**Returns:** the editor kit, or

null

if there is nothing
registered for the given type

- registerEditorKitForContentType

```java
public static void registerEditorKitForContentType​(
String
type,

String
classname)
```

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed, and can be safely changed before attempted uses
to avoid loading unwanted classes. The prototype

EditorKit

will be loaded with

Class.forName

when registered with this method.

**Parameters:** type

- the non-

null

content type
**Parameters:** classname

- the class to load later

- registerEditorKitForContentType

```java
public static void registerEditorKitForContentType​(
String
type,

String
classname,

ClassLoader
loader)
```

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed using the given

ClassLoader

,
and can be safely changed
before attempted uses to avoid loading unwanted classes.

**Parameters:** type

- the non-

null

content type
**Parameters:** classname

- the class to load later
**Parameters:** loader

- the

ClassLoader

to use to load the name

- getEditorKitClassNameForContentType

```java
public static
String
getEditorKitClassNameForContentType​(
String
type)
```

Returns the currently registered

EditorKit

class name for the
type

type

.

**Parameters:** type

- the non-

null

content type
**Returns:** a

String

containing the

EditorKit

class name
for

type
**Since:** 1.3

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size for the

JEditorPane

.
The preferred size for

JEditorPane

is slightly altered
from the preferred size of the superclass. If the size
of the viewport has become smaller than the minimum size
of the component, the scrollable definition for tracking
width or height will turn to false. The default viewport
layout will give the preferred size, and that is not desired
in the case where the scrollable is tracking. In that case
the

normal

preferred size is adjusted to the
minimum size. This allows things like HTML tables to
shrink down to their minimum size and then be laid out at
their minimum size, refusing to shrink any further.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** a

Dimension

containing the preferred size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

- setText

```java
@BeanProperty
(
bound
=false,

description
="the text of this component")
public void setText​(
String
t)
```

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor. For example, if the type is set to

text/html

the string should be specified in terms of HTML.

This is implemented to remove the contents of the current document,
and replace them by parsing the given string using the current

EditorKit

. This gives the semantics of the
superclass by not changing
out the model, while supporting the content type currently set on
this component. The assumption is that the previous content is
relatively
small, and that the previous content doesn't have side effects.
Both of those assumptions can be violated and cause undesirable results.
To avoid this, create a new document,

getEditorKit().createDefaultDocument()

, and replace the
existing

Document

with the new one. You are then assured the
previous

Document

won't have any lingering state.

- Leaving the existing model in place means that the old view will be
torn down, and a new view created, where replacing the document would
avoid the tear down of the old view.

Some formats (such as HTML) can install things into the document that
can influence future contents. HTML can have style information embedded
that would influence the next content installed unexpectedly.

An alternative way to load this component with a string would be to
create a StringReader and call the read method. In this case the model
would be replaced after it was initialized with the contents of the
string.

**Overrides:** setText

in class

JTextComponent
**Parameters:** t

- the new text to be set; if

null

the old
text will be deleted
**See Also:** getText()

- getText

```java
public
String
getText()
```

Returns the text contained in this

TextComponent

in terms of the
content type of this editor. If an exception is thrown while
attempting to retrieve the text,

null

will be returned.
This is implemented to call

JTextComponent.write

with
a

StringWriter

.

**Overrides:** getText

in class

JTextComponent
**Returns:** the text
**See Also:** setText(java.lang.String)

- getScrollableTracksViewportWidth

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()
```

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Overrides:** getScrollableTracksViewportWidth

in class

JTextComponent
**Returns:** true if a viewport should force the Scrollables width to
match its own, false otherwise

- getScrollableTracksViewportHeight

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()
```

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Overrides:** getScrollableTracksViewportHeight

in class

JTextComponent
**Returns:** true if a viewport should force the

Scrollable

's height to match its own,
false otherwise

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JEditorPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JTextComponent
**Returns:** a string representation of this

JEditorPane

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JEditorPane.
For editor panes, the AccessibleContext takes the form of an
AccessibleJEditorPane.
A new AccessibleJEditorPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JTextComponent
**Returns:** an AccessibleJEditorPane that serves as the
AccessibleContext of this JEditorPane

---

#### Method Detail

addHyperlinkListener

```java
public void addHyperlinkListener​(
HyperlinkListener
listener)
```

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

**Parameters:** listener

- the listener

---

#### addHyperlinkListener

public void addHyperlinkListener​(

HyperlinkListener

listener)

Adds a hyperlink listener for notification of any changes, for example
when a link is selected and entered.

removeHyperlinkListener

```java
public void removeHyperlinkListener​(
HyperlinkListener
listener)
```

Removes a hyperlink listener.

**Parameters:** listener

- the listener

---

#### removeHyperlinkListener

public void removeHyperlinkListener​(

HyperlinkListener

listener)

Removes a hyperlink listener.

getHyperlinkListeners

```java
@BeanProperty
(
bound
=false)
public
HyperlinkListener
[] getHyperlinkListeners()
```

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

**Returns:** all of the

HyperLinkListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getHyperlinkListeners

@BeanProperty

(

bound

=false)
public

HyperlinkListener

[] getHyperlinkListeners()

Returns an array of all the

HyperLinkListener

s added
to this JEditorPane with addHyperlinkListener().

fireHyperlinkUpdate

```java
public void fireHyperlinkUpdate​(
HyperlinkEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type. This is normally called
by the currently installed

EditorKit

if a content type
that supports hyperlinks is currently active and there
was activity with a link. The listener list is processed
last to first.

**Parameters:** e

- the event
**See Also:** EventListenerList

---

#### fireHyperlinkUpdate

public void fireHyperlinkUpdate​(

HyperlinkEvent

e)

Notifies all listeners that have registered interest for
notification on this event type. This is normally called
by the currently installed

EditorKit

if a content type
that supports hyperlinks is currently active and there
was activity with a link. The listener list is processed
last to first.

setPage

```java
@BeanProperty
(
expert
=true,

description
="the URL used to set content")
public void setPage​(
URL
page)
throws
IOException
```

Sets the current URL being displayed. The content type of the
pane is set, and if the editor kit for the pane is
non-

null

, then
a new default document is created and the URL is read into it.
If the URL contains and reference location, the location will
be scrolled to by calling the

scrollToReference

method. If the desired URL is the one currently being displayed,
the document will not be reloaded. To force a document
reload it is necessary to clear the stream description property
of the document. The following code shows how this can be done:

```java
Document doc = jEditorPane.getDocument();
doc.putProperty(Document.StreamDescriptionProperty, null);
```

If the desired URL is not the one currently being
displayed, the

getStream

method is called to
give subclasses control over the stream provided.

This may load either synchronously or asynchronously
depending upon the document returned by the

EditorKit

.
If the

Document

is of type

AbstractDocument

and has a value returned by

AbstractDocument.getAsynchronousLoadPriority

that is greater than or equal to zero, the page will be
loaded on a separate thread using that priority.

If the document is loaded synchronously, it will be
filled in with the stream prior to being installed into
the editor with a call to

setDocument

, which
is bound and will fire a property change event. If an

IOException

is thrown the partially loaded
document will
be discarded and neither the document or page property
change events will be fired. If the document is
successfully loaded and installed, a view will be
built for it by the UI which will then be scrolled if
necessary, and then the page property change event
will be fired.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

**Parameters:** page

- the URL of the page
**Throws:** IOException

- for a

null

or invalid
page specification, or exception from the stream being read
**See Also:** getPage()

---

#### setPage

@BeanProperty

(

expert

=true,

description

="the URL used to set content")
public void setPage​(

URL

page)
throws

IOException

Sets the current URL being displayed. The content type of the
pane is set, and if the editor kit for the pane is
non-

null

, then
a new default document is created and the URL is read into it.
If the URL contains and reference location, the location will
be scrolled to by calling the

scrollToReference

method. If the desired URL is the one currently being displayed,
the document will not be reloaded. To force a document
reload it is necessary to clear the stream description property
of the document. The following code shows how this can be done:

```java
Document doc = jEditorPane.getDocument();
doc.putProperty(Document.StreamDescriptionProperty, null);
```

If the desired URL is not the one currently being
displayed, the

getStream

method is called to
give subclasses control over the stream provided.

This may load either synchronously or asynchronously
depending upon the document returned by the

EditorKit

.
If the

Document

is of type

AbstractDocument

and has a value returned by

AbstractDocument.getAsynchronousLoadPriority

that is greater than or equal to zero, the page will be
loaded on a separate thread using that priority.

If the document is loaded synchronously, it will be
filled in with the stream prior to being installed into
the editor with a call to

setDocument

, which
is bound and will fire a property change event. If an

IOException

is thrown the partially loaded
document will
be discarded and neither the document or page property
change events will be fired. If the document is
successfully loaded and installed, a view will be
built for it by the UI which will then be scrolled if
necessary, and then the page property change event
will be fired.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

Document doc = jEditorPane.getDocument();
doc.putProperty(Document.StreamDescriptionProperty, null);

This may load either synchronously or asynchronously
depending upon the document returned by the

EditorKit

.
If the

Document

is of type

AbstractDocument

and has a value returned by

AbstractDocument.getAsynchronousLoadPriority

that is greater than or equal to zero, the page will be
loaded on a separate thread using that priority.

If the document is loaded synchronously, it will be
filled in with the stream prior to being installed into
the editor with a call to

setDocument

, which
is bound and will fire a property change event. If an

IOException

is thrown the partially loaded
document will
be discarded and neither the document or page property
change events will be fired. If the document is
successfully loaded and installed, a view will be
built for it by the UI which will then be scrolled if
necessary, and then the page property change event
will be fired.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

If the document is loaded synchronously, it will be
filled in with the stream prior to being installed into
the editor with a call to

setDocument

, which
is bound and will fire a property change event. If an

IOException

is thrown the partially loaded
document will
be discarded and neither the document or page property
change events will be fired. If the document is
successfully loaded and installed, a view will be
built for it by the UI which will then be scrolled if
necessary, and then the page property change event
will be fired.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

If the document is loaded asynchronously, the document
will be installed into the editor immediately using a
call to

setDocument

which will fire a
document property change event, then a thread will be
created which will begin doing the actual loading.
In this case, the page property change event will not be
fired by the call to this method directly, but rather will be
fired when the thread doing the loading has finished.
It will also be fired on the event-dispatch thread.
Since the calling thread can not throw an

IOException

in the event of failure on the other thread, the page
property change event will be fired when the other
thread is done whether the load was successful or not.

read

```java
public void read​(
InputStream
in,

Object
desc)
throws
IOException
```

This method initializes from a stream. If the kit is
set to be of type

HTMLEditorKit

, and the

desc

parameter is an

HTMLDocument

,
then it invokes the

HTMLEditorKit

to initiate
the read. Otherwise it calls the superclass
method which loads the model as plain text.

**Parameters:** in

- the stream from which to read
**Parameters:** desc

- an object describing the stream
**Throws:** IOException

- as thrown by the stream being
used to initialize
**See Also:** JTextComponent.read(java.io.Reader, java.lang.Object)

,

JTextComponent.setDocument(javax.swing.text.Document)

---

#### read

public void read​(

InputStream

in,

Object

desc)
throws

IOException

This method initializes from a stream. If the kit is
set to be of type

HTMLEditorKit

, and the

desc

parameter is an

HTMLDocument

,
then it invokes the

HTMLEditorKit

to initiate
the read. Otherwise it calls the superclass
method which loads the model as plain text.

getStream

```java
protected
InputStream
getStream​(
URL
page)
throws
IOException
```

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method. By
default, this simply opens the URL and returns the
stream. This can be reimplemented to do useful things
like fetch the stream from a cache, monitor the progress
of the stream, etc.

This method is expected to have the side effect of
establishing the content type, and therefore setting the
appropriate

EditorKit

to use for loading the stream.

If this the stream was an http connection, redirects
will be followed and the resulting URL will be set as
the

Document.StreamDescriptionProperty

so that relative
URL's can be properly resolved.

**Parameters:** page

- the URL of the page
**Returns:** a stream for the URL which is about to be loaded
**Throws:** IOException

- if an I/O problem occurs

---

#### getStream

protected

InputStream

getStream​(

URL

page)
throws

IOException

Fetches a stream for the given URL, which is about to
be loaded by the

setPage

method. By
default, this simply opens the URL and returns the
stream. This can be reimplemented to do useful things
like fetch the stream from a cache, monitor the progress
of the stream, etc.

This method is expected to have the side effect of
establishing the content type, and therefore setting the
appropriate

EditorKit

to use for loading the stream.

If this the stream was an http connection, redirects
will be followed and the resulting URL will be set as
the

Document.StreamDescriptionProperty

so that relative
URL's can be properly resolved.

This method is expected to have the side effect of
establishing the content type, and therefore setting the
appropriate

EditorKit

to use for loading the stream.

If this the stream was an http connection, redirects
will be followed and the resulting URL will be set as
the

Document.StreamDescriptionProperty

so that relative
URL's can be properly resolved.

If this the stream was an http connection, redirects
will be followed and the resulting URL will be set as
the

Document.StreamDescriptionProperty

so that relative
URL's can be properly resolved.

scrollToReference

```java
public void scrollToReference​(
String
reference)
```

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed). By default, this
method only knows how to locate a reference in an
HTMLDocument. The implementation calls the

scrollRectToVisible

method to
accomplish the actual scrolling. If scrolling to a
reference location is needed for document types other
than HTML, this method should be reimplemented.
This method will have no effect if the component
is not visible.

**Parameters:** reference

- the named location to scroll to

---

#### scrollToReference

public void scrollToReference​(

String

reference)

Scrolls the view to the given reference location
(that is, the value returned by the

URL.getRef

method for the URL being displayed). By default, this
method only knows how to locate a reference in an
HTMLDocument. The implementation calls the

scrollRectToVisible

method to
accomplish the actual scrolling. If scrolling to a
reference location is needed for document types other
than HTML, this method should be reimplemented.
This method will have no effect if the component
is not visible.

getPage

```java
public
URL
getPage()
```

Gets the current URL being displayed. If a URL was
not specified in the creation of the document, this
will return

null

, and relative URL's will not be
resolved.

**Returns:** the URL, or

null

if none

---

#### getPage

public

URL

getPage()

Gets the current URL being displayed. If a URL was
not specified in the creation of the document, this
will return

null

, and relative URL's will not be
resolved.

setPage

```java
public void setPage​(
String
url)
throws
IOException
```

Sets the current URL being displayed.

**Parameters:** url

- the URL for display
**Throws:** IOException

- for a

null

or invalid URL
specification

---

#### setPage

public void setPage​(

String

url)
throws

IOException

Sets the current URL being displayed.

getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Gets the class ID for the UI.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "EditorPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false)
public

String

getUIClassID()

Gets the class ID for the UI.

createDefaultEditorKit

```java
protected
EditorKit
createDefaultEditorKit()
```

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

**Returns:** the editor kit

---

#### createDefaultEditorKit

protected

EditorKit

createDefaultEditorKit()

Creates the default editor kit (

PlainEditorKit

) for when
the component is first created.

getEditorKit

```java
public
EditorKit
getEditorKit()
```

Fetches the currently installed kit for handling content.

createDefaultEditorKit

is called to set up a default
if necessary.

**Returns:** the editor kit

---

#### getEditorKit

public

EditorKit

getEditorKit()

Fetches the currently installed kit for handling content.

createDefaultEditorKit

is called to set up a default
if necessary.

getContentType

```java
public final
String
getContentType()
```

Gets the type of content that this editor
is currently set to deal with. This is
defined to be the type associated with the
currently installed

EditorKit

.

**Returns:** the content type,

null

if no editor kit set

---

#### getContentType

public final

String

getContentType()

Gets the type of content that this editor
is currently set to deal with. This is
defined to be the type associated with the
currently installed

EditorKit

.

setContentType

```java
@BeanProperty
(
bound
=false,

description
="the type of content")
public final void setContentType​(
String
type)
```

Sets the type of content that this editor
handles. This calls

getEditorKitForContentType

,
and then

setEditorKit

if an editor kit can
be successfully located. This is mostly convenience method
that can be used as an alternative to calling

setEditorKit

directly.

If there is a charset definition specified as a parameter
of the content type specification, it will be used when
loading input streams using the associated

EditorKit

.
For example if the type is specified as

text/html; charset=EUC-JP

the content
will be loaded using the

EditorKit

registered for

text/html

and the Reader provided to
the

EditorKit

to load unicode into the document will
use the

EUC-JP

charset for translating
to unicode. If the type is not recognized, the content
will be loaded using the

EditorKit

registered
for plain text,

text/plain

.

**Parameters:** type

- the non-

null

mime type for the content editing
support
**Throws:** NullPointerException

- if the

type

parameter
is

null
**See Also:** getContentType()

---

#### setContentType

@BeanProperty

(

bound

=false,

description

="the type of content")
public final void setContentType​(

String

type)

Sets the type of content that this editor
handles. This calls

getEditorKitForContentType

,
and then

setEditorKit

if an editor kit can
be successfully located. This is mostly convenience method
that can be used as an alternative to calling

setEditorKit

directly.

If there is a charset definition specified as a parameter
of the content type specification, it will be used when
loading input streams using the associated

EditorKit

.
For example if the type is specified as

text/html; charset=EUC-JP

the content
will be loaded using the

EditorKit

registered for

text/html

and the Reader provided to
the

EditorKit

to load unicode into the document will
use the

EUC-JP

charset for translating
to unicode. If the type is not recognized, the content
will be loaded using the

EditorKit

registered
for plain text,

text/plain

.

If there is a charset definition specified as a parameter
of the content type specification, it will be used when
loading input streams using the associated

EditorKit

.
For example if the type is specified as

text/html; charset=EUC-JP

the content
will be loaded using the

EditorKit

registered for

text/html

and the Reader provided to
the

EditorKit

to load unicode into the document will
use the

EUC-JP

charset for translating
to unicode. If the type is not recognized, the content
will be loaded using the

EditorKit

registered
for plain text,

text/plain

.

setEditorKit

```java
@BeanProperty
(
expert
=true,

description
="the currently installed kit for handling content")
public void setEditorKit​(
EditorKit
kit)
```

Sets the currently installed kit for handling
content. This is the bound property that
establishes the content type of the editor.
Any old kit is first deinstalled, then if kit is
non-

null

,
the new kit is installed, and a default document created for it.
A

PropertyChange

event ("editorKit") is always fired when

setEditorKit

is called.

NOTE: This has the side effect of changing the model,
because the

EditorKit

is the source of how a
particular type
of content is modeled. This method will cause

setDocument

to be called on behalf of the caller to ensure integrity
of the internal state.

**Parameters:** kit

- the desired editor behavior
**See Also:** getEditorKit()

---

#### setEditorKit

@BeanProperty

(

expert

=true,

description

="the currently installed kit for handling content")
public void setEditorKit​(

EditorKit

kit)

Sets the currently installed kit for handling
content. This is the bound property that
establishes the content type of the editor.
Any old kit is first deinstalled, then if kit is
non-

null

,
the new kit is installed, and a default document created for it.
A

PropertyChange

event ("editorKit") is always fired when

setEditorKit

is called.

NOTE: This has the side effect of changing the model,
because the

EditorKit

is the source of how a
particular type
of content is modeled. This method will cause

setDocument

to be called on behalf of the caller to ensure integrity
of the internal state.

NOTE: This has the side effect of changing the model,
because the

EditorKit

is the source of how a
particular type
of content is modeled. This method will cause

setDocument

to be called on behalf of the caller to ensure integrity
of the internal state.

getEditorKitForContentType

```java
public
EditorKit
getEditorKitForContentType​(
String
type)
```

Fetches the editor kit to use for the given type
of content. This is called when a type is requested
that doesn't match the currently installed type.
If the component doesn't have an

EditorKit

registered
for the given type, it will try to create an

EditorKit

from the default

EditorKit

registry.
If that fails, a

PlainEditorKit

is used on the
assumption that all text documents can be represented
as plain text.

This method can be reimplemented to use some
other kind of type registry. This can
be reimplemented to use the Java Activation
Framework, for example.

**Parameters:** type

- the non-

null

content type
**Returns:** the editor kit

---

#### getEditorKitForContentType

public

EditorKit

getEditorKitForContentType​(

String

type)

Fetches the editor kit to use for the given type
of content. This is called when a type is requested
that doesn't match the currently installed type.
If the component doesn't have an

EditorKit

registered
for the given type, it will try to create an

EditorKit

from the default

EditorKit

registry.
If that fails, a

PlainEditorKit

is used on the
assumption that all text documents can be represented
as plain text.

This method can be reimplemented to use some
other kind of type registry. This can
be reimplemented to use the Java Activation
Framework, for example.

This method can be reimplemented to use some
other kind of type registry. This can
be reimplemented to use the Java Activation
Framework, for example.

setEditorKitForContentType

```java
public void setEditorKitForContentType​(
String
type,

EditorKit
k)
```

Directly sets the editor kit to use for the given type. A
look-and-feel implementation might use this in conjunction
with

createEditorKitForContentType

to install handlers for
content types with a look-and-feel bias.

**Parameters:** type

- the non-

null

content type
**Parameters:** k

- the editor kit to be set

---

#### setEditorKitForContentType

public void setEditorKitForContentType​(

String

type,

EditorKit

k)

Directly sets the editor kit to use for the given type. A
look-and-feel implementation might use this in conjunction
with

createEditorKitForContentType

to install handlers for
content types with a look-and-feel bias.

replaceSelection

```java
public void replaceSelection​(
String
content)
```

Replaces the currently selected content with new content
represented by the given string. If there is no selection
this amounts to an insert of the given text. If there
is no replacement text (i.e. the content string is empty
or

null

) this amounts to a removal of the
current selection. The replacement text will have the
attributes currently defined for input. If the component is not
editable, beep and return.

**Overrides:** replaceSelection

in class

JTextComponent
**Parameters:** content

- the content to replace the selection with. This
value can be

null

---

#### replaceSelection

public void replaceSelection​(

String

content)

Replaces the currently selected content with new content
represented by the given string. If there is no selection
this amounts to an insert of the given text. If there
is no replacement text (i.e. the content string is empty
or

null

) this amounts to a removal of the
current selection. The replacement text will have the
attributes currently defined for input. If the component is not
editable, beep and return.

createEditorKitForContentType

```java
public static
EditorKit
createEditorKitForContentType​(
String
type)
```

Creates a handler for the given type from the default registry
of editor kits. The registry is created if necessary. If the
registered class has not yet been loaded, an attempt
is made to dynamically load the prototype of the kit for the
given type. If the type was registered with a

ClassLoader

,
that

ClassLoader

will be used to load the prototype.
If there was no registered

ClassLoader

,

Class.forName

will be used to load the prototype.

Once a prototype

EditorKit

instance is successfully
located, it is cloned and the clone is returned.

**Parameters:** type

- the content type
**Returns:** the editor kit, or

null

if there is nothing
registered for the given type

---

#### createEditorKitForContentType

public static

EditorKit

createEditorKitForContentType​(

String

type)

Creates a handler for the given type from the default registry
of editor kits. The registry is created if necessary. If the
registered class has not yet been loaded, an attempt
is made to dynamically load the prototype of the kit for the
given type. If the type was registered with a

ClassLoader

,
that

ClassLoader

will be used to load the prototype.
If there was no registered

ClassLoader

,

Class.forName

will be used to load the prototype.

Once a prototype

EditorKit

instance is successfully
located, it is cloned and the clone is returned.

Once a prototype

EditorKit

instance is successfully
located, it is cloned and the clone is returned.

registerEditorKitForContentType

```java
public static void registerEditorKitForContentType​(
String
type,

String
classname)
```

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed, and can be safely changed before attempted uses
to avoid loading unwanted classes. The prototype

EditorKit

will be loaded with

Class.forName

when registered with this method.

**Parameters:** type

- the non-

null

content type
**Parameters:** classname

- the class to load later

---

#### registerEditorKitForContentType

public static void registerEditorKitForContentType​(

String

type,

String

classname)

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed, and can be safely changed before attempted uses
to avoid loading unwanted classes. The prototype

EditorKit

will be loaded with

Class.forName

when registered with this method.

registerEditorKitForContentType

```java
public static void registerEditorKitForContentType​(
String
type,

String
classname,

ClassLoader
loader)
```

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed using the given

ClassLoader

,
and can be safely changed
before attempted uses to avoid loading unwanted classes.

**Parameters:** type

- the non-

null

content type
**Parameters:** classname

- the class to load later
**Parameters:** loader

- the

ClassLoader

to use to load the name

---

#### registerEditorKitForContentType

public static void registerEditorKitForContentType​(

String

type,

String

classname,

ClassLoader

loader)

Establishes the default bindings of

type

to

classname

.
The class will be dynamically loaded later when actually
needed using the given

ClassLoader

,
and can be safely changed
before attempted uses to avoid loading unwanted classes.

getEditorKitClassNameForContentType

```java
public static
String
getEditorKitClassNameForContentType​(
String
type)
```

Returns the currently registered

EditorKit

class name for the
type

type

.

**Parameters:** type

- the non-

null

content type
**Returns:** a

String

containing the

EditorKit

class name
for

type
**Since:** 1.3

---

#### getEditorKitClassNameForContentType

public static

String

getEditorKitClassNameForContentType​(

String

type)

Returns the currently registered

EditorKit

class name for the
type

type

.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size for the

JEditorPane

.
The preferred size for

JEditorPane

is slightly altered
from the preferred size of the superclass. If the size
of the viewport has become smaller than the minimum size
of the component, the scrollable definition for tracking
width or height will turn to false. The default viewport
layout will give the preferred size, and that is not desired
in the case where the scrollable is tracking. In that case
the

normal

preferred size is adjusted to the
minimum size. This allows things like HTML tables to
shrink down to their minimum size and then be laid out at
their minimum size, refusing to shrink any further.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** a

Dimension

containing the preferred size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Returns the preferred size for the

JEditorPane

.
The preferred size for

JEditorPane

is slightly altered
from the preferred size of the superclass. If the size
of the viewport has become smaller than the minimum size
of the component, the scrollable definition for tracking
width or height will turn to false. The default viewport
layout will give the preferred size, and that is not desired
in the case where the scrollable is tracking. In that case
the

normal

preferred size is adjusted to the
minimum size. This allows things like HTML tables to
shrink down to their minimum size and then be laid out at
their minimum size, refusing to shrink any further.

setText

```java
@BeanProperty
(
bound
=false,

description
="the text of this component")
public void setText​(
String
t)
```

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor. For example, if the type is set to

text/html

the string should be specified in terms of HTML.

This is implemented to remove the contents of the current document,
and replace them by parsing the given string using the current

EditorKit

. This gives the semantics of the
superclass by not changing
out the model, while supporting the content type currently set on
this component. The assumption is that the previous content is
relatively
small, and that the previous content doesn't have side effects.
Both of those assumptions can be violated and cause undesirable results.
To avoid this, create a new document,

getEditorKit().createDefaultDocument()

, and replace the
existing

Document

with the new one. You are then assured the
previous

Document

won't have any lingering state.

- Leaving the existing model in place means that the old view will be
torn down, and a new view created, where replacing the document would
avoid the tear down of the old view.

Some formats (such as HTML) can install things into the document that
can influence future contents. HTML can have style information embedded
that would influence the next content installed unexpectedly.

An alternative way to load this component with a string would be to
create a StringReader and call the read method. In this case the model
would be replaced after it was initialized with the contents of the
string.

**Overrides:** setText

in class

JTextComponent
**Parameters:** t

- the new text to be set; if

null

the old
text will be deleted
**See Also:** getText()

---

#### setText

@BeanProperty

(

bound

=false,

description

="the text of this component")
public void setText​(

String

t)

Sets the text of this

TextComponent

to the specified
content,
which is expected to be in the format of the content type of
this editor. For example, if the type is set to

text/html

the string should be specified in terms of HTML.

This is implemented to remove the contents of the current document,
and replace them by parsing the given string using the current

EditorKit

. This gives the semantics of the
superclass by not changing
out the model, while supporting the content type currently set on
this component. The assumption is that the previous content is
relatively
small, and that the previous content doesn't have side effects.
Both of those assumptions can be violated and cause undesirable results.
To avoid this, create a new document,

getEditorKit().createDefaultDocument()

, and replace the
existing

Document

with the new one. You are then assured the
previous

Document

won't have any lingering state.

- Leaving the existing model in place means that the old view will be
torn down, and a new view created, where replacing the document would
avoid the tear down of the old view.

Some formats (such as HTML) can install things into the document that
can influence future contents. HTML can have style information embedded
that would influence the next content installed unexpectedly.

An alternative way to load this component with a string would be to
create a StringReader and call the read method. In this case the model
would be replaced after it was initialized with the contents of the
string.

This is implemented to remove the contents of the current document,
and replace them by parsing the given string using the current

EditorKit

. This gives the semantics of the
superclass by not changing
out the model, while supporting the content type currently set on
this component. The assumption is that the previous content is
relatively
small, and that the previous content doesn't have side effects.
Both of those assumptions can be violated and cause undesirable results.
To avoid this, create a new document,

getEditorKit().createDefaultDocument()

, and replace the
existing

Document

with the new one. You are then assured the
previous

Document

won't have any lingering state.

- Leaving the existing model in place means that the old view will be
torn down, and a new view created, where replacing the document would
avoid the tear down of the old view.

Some formats (such as HTML) can install things into the document that
can influence future contents. HTML can have style information embedded
that would influence the next content installed unexpectedly.

An alternative way to load this component with a string would be to
create a StringReader and call the read method. In this case the model
would be replaced after it was initialized with the contents of the
string.

Leaving the existing model in place means that the old view will be
torn down, and a new view created, where replacing the document would
avoid the tear down of the old view.

Some formats (such as HTML) can install things into the document that
can influence future contents. HTML can have style information embedded
that would influence the next content installed unexpectedly.

An alternative way to load this component with a string would be to
create a StringReader and call the read method. In this case the model
would be replaced after it was initialized with the contents of the
string.

getText

```java
public
String
getText()
```

Returns the text contained in this

TextComponent

in terms of the
content type of this editor. If an exception is thrown while
attempting to retrieve the text,

null

will be returned.
This is implemented to call

JTextComponent.write

with
a

StringWriter

.

**Overrides:** getText

in class

JTextComponent
**Returns:** the text
**See Also:** setText(java.lang.String)

---

#### getText

public

String

getText()

Returns the text contained in this

TextComponent

in terms of the
content type of this editor. If an exception is thrown while
attempting to retrieve the text,

null

will be returned.
This is implemented to call

JTextComponent.write

with
a

StringWriter

.

getScrollableTracksViewportWidth

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()
```

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Overrides:** getScrollableTracksViewportWidth

in class

JTextComponent
**Returns:** true if a viewport should force the Scrollables width to
match its own, false otherwise

---

#### getScrollableTracksViewportWidth

@BeanProperty

(

bound

=false)
public boolean getScrollableTracksViewportWidth()

Returns true if a viewport should always force the width of this

Scrollable

to match the width of the viewport.

getScrollableTracksViewportHeight

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()
```

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Overrides:** getScrollableTracksViewportHeight

in class

JTextComponent
**Returns:** true if a viewport should force the

Scrollable

's height to match its own,
false otherwise

---

#### getScrollableTracksViewportHeight

@BeanProperty

(

bound

=false)
public boolean getScrollableTracksViewportHeight()

Returns true if a viewport should always force the height of this

Scrollable

to match the height of the viewport.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JEditorPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JTextComponent
**Returns:** a string representation of this

JEditorPane

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JEditorPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JEditorPane.
For editor panes, the AccessibleContext takes the form of an
AccessibleJEditorPane.
A new AccessibleJEditorPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JTextComponent
**Returns:** an AccessibleJEditorPane that serves as the
AccessibleContext of this JEditorPane

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JEditorPane.
For editor panes, the AccessibleContext takes the form of an
AccessibleJEditorPane.
A new AccessibleJEditorPane instance is created if necessary.

---

