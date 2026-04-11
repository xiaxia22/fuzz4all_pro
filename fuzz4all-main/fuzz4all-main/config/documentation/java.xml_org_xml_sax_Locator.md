# Interface Locator

**Source:** `java.xml\org\xml\sax\Locator.html`

### Class Description

```java
public interface
Locator
```

Interface for associating a SAX event with a document location.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX parser provides location information to the SAX
application, it does so by implementing this interface and then
passing an instance to the application using the content
handler's

setDocumentLocator

method. The application can use the
object to obtain the location of any other SAX event
in the XML source document.

Note that the results returned by the object will be valid only
during the scope of each callback method: the application
will receive unpredictable results if it attempts to use the
locator at any other time, or after parsing completes.

SAX parsers are not required to supply a locator, but they are
very strongly encouraged to do so. If the parser supplies a
locator, it must do so before reporting any other document events.
If no locator has been set by the time the application receives
the

startDocument

event, the application should assume that a locator is not
available.

**All Known Subinterfaces:** Locator2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getPublicId()

Return the public identifier for the current document event.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

**Returns:**
- A string containing the public identifier, or
null if none is available.

**See Also:**
- getSystemId()

---

#### String
getSystemId()

Return the system identifier for the current document event.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application. For example, a file
name must always be provided as a

file:...

URL, and other
kinds of relative URI are also resolved against their bases.

**Returns:**
- A string containing the system identifier, or null
if none is available.

**See Also:**
- getPublicId()

---

#### int getLineNumber()

Return the line number where the current document event ends.
Lines are delimited by line ends, which are defined in
the XML specification.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
In some cases, these "line" numbers match what would be displayed
as columns, and in others they may not match the source text
due to internal entity expansion.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first line is line 1.

**Returns:**
- The line number, or -1 if none is available.

**See Also:**
- getColumnNumber()

---

#### int getColumnNumber()

Return the column number where the current document event ends.
This is one-based number of Java

char

values since
the last line end.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
For example, when lines contain combining character sequences, wide
characters, surrogate pairs, or bi-directional text, the value may
not correspond to the column in a text editor's display.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first column in each line is column 1.

**Returns:**
- The column number, or -1 if none is available.

**See Also:**
- getLineNumber()

---

### Additional Sections

#### Interface Locator

**All Known Subinterfaces:** Locator2

**All Known Implementing Classes:** Locator2Impl

,

LocatorImpl

```java
public interface
Locator
```

Interface for associating a SAX event with a document location.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX parser provides location information to the SAX
application, it does so by implementing this interface and then
passing an instance to the application using the content
handler's

setDocumentLocator

method. The application can use the
object to obtain the location of any other SAX event
in the XML source document.

Note that the results returned by the object will be valid only
during the scope of each callback method: the application
will receive unpredictable results if it attempts to use the
locator at any other time, or after parsing completes.

SAX parsers are not required to supply a locator, but they are
very strongly encouraged to do so. If the parser supplies a
locator, it must do so before reporting any other document events.
If no locator has been set by the time the application receives
the

startDocument

event, the application should assume that a locator is not
available.

**Since:** 1.4, SAX 1.0
**See Also:** ContentHandler.setDocumentLocator(org.xml.sax.Locator)

public interface

Locator

Interface for associating a SAX event with a document location.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX parser provides location information to the SAX
application, it does so by implementing this interface and then
passing an instance to the application using the content
handler's

setDocumentLocator

method. The application can use the
object to obtain the location of any other SAX event
in the XML source document.

Note that the results returned by the object will be valid only
during the scope of each callback method: the application
will receive unpredictable results if it attempts to use the
locator at any other time, or after parsing completes.

SAX parsers are not required to supply a locator, but they are
very strongly encouraged to do so. If the parser supplies a
locator, it must do so before reporting any other document events.
If no locator has been set by the time the application receives
the

startDocument

event, the application should assume that a locator is not
available.

If a SAX parser provides location information to the SAX
application, it does so by implementing this interface and then
passing an instance to the application using the content
handler's

setDocumentLocator

method. The application can use the
object to obtain the location of any other SAX event
in the XML source document.

Note that the results returned by the object will be valid only
during the scope of each callback method: the application
will receive unpredictable results if it attempts to use the
locator at any other time, or after parsing completes.

SAX parsers are not required to supply a locator, but they are
very strongly encouraged to do so. If the parser supplies a
locator, it must do so before reporting any other document events.
If no locator has been set by the time the application receives
the

startDocument

event, the application should assume that a locator is not
available.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Return the column number where the current document event ends.

int

getLineNumber

()

Return the line number where the current document event ends.

String

getPublicId

()

Return the public identifier for the current document event.

String

getSystemId

()

Return the system identifier for the current document event.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Return the column number where the current document event ends.

int

getLineNumber

()

Return the line number where the current document event ends.

String

getPublicId

()

Return the public identifier for the current document event.

String

getSystemId

()

Return the system identifier for the current document event.

---

#### Method Summary

Return the column number where the current document event ends.

Return the line number where the current document event ends.

Return the public identifier for the current document event.

Return the system identifier for the current document event.

============ METHOD DETAIL ==========

- Method Detail

- getPublicId

```java
String
getPublicId()
```

Return the public identifier for the current document event.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

**Returns:** A string containing the public identifier, or
null if none is available.
**See Also:** getSystemId()

- getSystemId

```java
String
getSystemId()
```

Return the system identifier for the current document event.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application. For example, a file
name must always be provided as a

file:...

URL, and other
kinds of relative URI are also resolved against their bases.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** getPublicId()

- getLineNumber

```java
int getLineNumber()
```

Return the line number where the current document event ends.
Lines are delimited by line ends, which are defined in
the XML specification.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
In some cases, these "line" numbers match what would be displayed
as columns, and in others they may not match the source text
due to internal entity expansion.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first line is line 1.

**Returns:** The line number, or -1 if none is available.
**See Also:** getColumnNumber()

- getColumnNumber

```java
int getColumnNumber()
```

Return the column number where the current document event ends.
This is one-based number of Java

char

values since
the last line end.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
For example, when lines contain combining character sequences, wide
characters, surrogate pairs, or bi-directional text, the value may
not correspond to the column in a text editor's display.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first column in each line is column 1.

**Returns:** The column number, or -1 if none is available.
**See Also:** getLineNumber()

Method Detail

- getPublicId

```java
String
getPublicId()
```

Return the public identifier for the current document event.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

**Returns:** A string containing the public identifier, or
null if none is available.
**See Also:** getSystemId()

- getSystemId

```java
String
getSystemId()
```

Return the system identifier for the current document event.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application. For example, a file
name must always be provided as a

file:...

URL, and other
kinds of relative URI are also resolved against their bases.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** getPublicId()

- getLineNumber

```java
int getLineNumber()
```

Return the line number where the current document event ends.
Lines are delimited by line ends, which are defined in
the XML specification.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
In some cases, these "line" numbers match what would be displayed
as columns, and in others they may not match the source text
due to internal entity expansion.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first line is line 1.

**Returns:** The line number, or -1 if none is available.
**See Also:** getColumnNumber()

- getColumnNumber

```java
int getColumnNumber()
```

Return the column number where the current document event ends.
This is one-based number of Java

char

values since
the last line end.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
For example, when lines contain combining character sequences, wide
characters, surrogate pairs, or bi-directional text, the value may
not correspond to the column in a text editor's display.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first column in each line is column 1.

**Returns:** The column number, or -1 if none is available.
**See Also:** getLineNumber()

---

#### Method Detail

getPublicId

```java
String
getPublicId()
```

Return the public identifier for the current document event.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

**Returns:** A string containing the public identifier, or
null if none is available.
**See Also:** getSystemId()

---

#### getPublicId

String

getPublicId()

Return the public identifier for the current document event.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

getSystemId

```java
String
getSystemId()
```

Return the system identifier for the current document event.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application. For example, a file
name must always be provided as a

file:...

URL, and other
kinds of relative URI are also resolved against their bases.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** getPublicId()

---

#### getSystemId

String

getSystemId()

Return the system identifier for the current document event.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application. For example, a file
name must always be provided as a

file:...

URL, and other
kinds of relative URI are also resolved against their bases.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup
triggering the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application. For example, a file
name must always be provided as a

file:...

URL, and other
kinds of relative URI are also resolved against their bases.

getLineNumber

```java
int getLineNumber()
```

Return the line number where the current document event ends.
Lines are delimited by line ends, which are defined in
the XML specification.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
In some cases, these "line" numbers match what would be displayed
as columns, and in others they may not match the source text
due to internal entity expansion.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first line is line 1.

**Returns:** The line number, or -1 if none is available.
**See Also:** getColumnNumber()

---

#### getLineNumber

int getLineNumber()

Return the line number where the current document event ends.
Lines are delimited by line ends, which are defined in
the XML specification.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
In some cases, these "line" numbers match what would be displayed
as columns, and in others they may not match the source text
due to internal entity expansion.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first line is line 1.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
In some cases, these "line" numbers match what would be displayed
as columns, and in others they may not match the source text
due to internal entity expansion.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first line is line 1.

getColumnNumber

```java
int getColumnNumber()
```

Return the column number where the current document event ends.
This is one-based number of Java

char

values since
the last line end.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
For example, when lines contain combining character sequences, wide
characters, surrogate pairs, or bi-directional text, the value may
not correspond to the column in a text editor's display.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first column in each line is column 1.

**Returns:** The column number, or -1 if none is available.
**See Also:** getLineNumber()

---

#### getColumnNumber

int getColumnNumber()

Return the column number where the current document event ends.
This is one-based number of Java

char

values since
the last line end.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
For example, when lines contain combining character sequences, wide
characters, surrogate pairs, or bi-directional text, the value may
not correspond to the column in a text editor's display.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first column in each line is column 1.

Warning:

The return value from the method
is intended only as an approximation for the sake of diagnostics;
it is not intended to provide sufficient information
to edit the character content of the original XML document.
For example, when lines contain combining character sequences, wide
characters, surrogate pairs, or bi-directional text, the value may
not correspond to the column in a text editor's display.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup triggering the event appears.

If possible, the SAX driver should provide the line position
of the first character after the text associated with the document
event. The first column in each line is column 1.

---

