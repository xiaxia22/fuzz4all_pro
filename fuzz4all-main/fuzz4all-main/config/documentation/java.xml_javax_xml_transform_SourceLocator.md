# Interface SourceLocator

**Source:** `java.xml\javax\xml\transform\SourceLocator.html`

### Class Description

```java
public interface
SourceLocator
```

This interface is primarily for the purposes of reporting where
an error occurred in the XML source or transformation instructions.

**All Known Subinterfaces:** DOMLocator

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
entity or of the external parsed entity in which the markup that
triggered the event appears.

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
entity or of the external parsed entity in which the markup that
triggered the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Returns:**
- A string containing the system identifier, or null
if none is available.

**See Also:**
- getPublicId()

---

#### int getLineNumber()

Return the line number where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup that triggered the event appears.

**Returns:**
- The line number, or -1 if none is available.

**See Also:**
- getColumnNumber()

---

#### int getColumnNumber()

Return the character position where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup that triggered the event appears.

**Returns:**
- The column number, or -1 if none is available.

**See Also:**
- getLineNumber()

---

### Additional Sections

#### Interface SourceLocator

**All Known Subinterfaces:** DOMLocator

```java
public interface
SourceLocator
```

This interface is primarily for the purposes of reporting where
an error occurred in the XML source or transformation instructions.

**Since:** 1.4

public interface

SourceLocator

This interface is primarily for the purposes of reporting where
an error occurred in the XML source or transformation instructions.

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

Return the character position where the current document event ends.

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

Return the character position where the current document event ends.

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

Return the character position where the current document event ends.

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
entity or of the external parsed entity in which the markup that
triggered the event appears.

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
entity or of the external parsed entity in which the markup that
triggered the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** getPublicId()

- getLineNumber

```java
int getLineNumber()
```

Return the line number where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup that triggered the event appears.

**Returns:** The line number, or -1 if none is available.
**See Also:** getColumnNumber()

- getColumnNumber

```java
int getColumnNumber()
```

Return the character position where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup that triggered the event appears.

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
entity or of the external parsed entity in which the markup that
triggered the event appears.

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
entity or of the external parsed entity in which the markup that
triggered the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** getPublicId()

- getLineNumber

```java
int getLineNumber()
```

Return the line number where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup that triggered the event appears.

**Returns:** The line number, or -1 if none is available.
**See Also:** getColumnNumber()

- getColumnNumber

```java
int getColumnNumber()
```

Return the character position where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup that triggered the event appears.

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
entity or of the external parsed entity in which the markup that
triggered the event appears.

**Returns:** A string containing the public identifier, or
null if none is available.
**See Also:** getSystemId()

---

#### getPublicId

String

getPublicId()

Return the public identifier for the current document event.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup that
triggered the event appears.

The return value is the public identifier of the document
entity or of the external parsed entity in which the markup that
triggered the event appears.

getSystemId

```java
String
getSystemId()
```

Return the system identifier for the current document event.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup that
triggered the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** getPublicId()

---

#### getSystemId

String

getSystemId()

Return the system identifier for the current document event.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup that
triggered the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

The return value is the system identifier of the document
entity or of the external parsed entity in which the markup that
triggered the event appears.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

getLineNumber

```java
int getLineNumber()
```

Return the line number where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup that triggered the event appears.

**Returns:** The line number, or -1 if none is available.
**See Also:** getColumnNumber()

---

#### getLineNumber

int getLineNumber()

Return the line number where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup that triggered the event appears.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the line number
in the document entity or external parsed entity where the
markup that triggered the event appears.

getColumnNumber

```java
int getColumnNumber()
```

Return the character position where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup that triggered the event appears.

**Returns:** The column number, or -1 if none is available.
**See Also:** getLineNumber()

---

#### getColumnNumber

int getColumnNumber()

Return the character position where the current document event ends.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup that triggered the event appears.

Warning:

The return value from the method
is intended only as an approximation for the sake of error
reporting; it is not intended to provide sufficient information
to edit the character content of the original XML document.

The return value is an approximation of the column number
in the document entity or external parsed entity where the
markup that triggered the event appears.

---

