# Class LocatorImpl

**Source:** `java.xml\org\xml\sax\helpers\LocatorImpl.html`

### Class Description

```java
public class
LocatorImpl

extends
Object

implements
Locator
```

Provide an optional convenience implementation of Locator.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class is available mainly for application writers, who
can use it to make a persistent snapshot of a locator at any
point during a document parse:

```java
Locator locator;
Locator startloc;

public void setLocator (Locator locator)
{
// note the locator
this.locator = locator;
}

public void startDocument ()
{
// save the location of the start of the document
// for future use.
Locator startloc = new LocatorImpl(locator);
}
```

Normally, parser writers will not use this class, since it
is more efficient to provide location information only when
requested, rather than constantly updating a Locator object.

**All Implemented Interfaces:** Locator

---

### Field Details

*No entries found.*

### Constructor Details

#### public LocatorImpl()

Zero-argument constructor.

This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

---

#### public LocatorImpl​(
Locator
locator)

Copy constructor.

Create a persistent copy of the current state of a locator.
When the original locator changes, this copy will still keep
the original values (and it can be used outside the scope of
DocumentHandler methods).

**Parameters:**
- locator

- The locator to copy.

---

### Method Details

#### public
String
getPublicId()

Return the saved public identifier.

**Specified by:**
- getPublicId

in interface

Locator

**Returns:**
- The public identifier as a string, or null if none
is available.

**See Also:**
- Locator.getPublicId()

,

setPublicId(java.lang.String)

---

#### public
String
getSystemId()

Return the saved system identifier.

**Specified by:**
- getSystemId

in interface

Locator

**Returns:**
- The system identifier as a string, or null if none
is available.

**See Also:**
- Locator.getSystemId()

,

setSystemId(java.lang.String)

---

#### public int getLineNumber()

Return the saved line number (1-based).

**Specified by:**
- getLineNumber

in interface

Locator

**Returns:**
- The line number as an integer, or -1 if none is available.

**See Also:**
- Locator.getLineNumber()

,

setLineNumber(int)

---

#### public int getColumnNumber()

Return the saved column number (1-based).

**Specified by:**
- getColumnNumber

in interface

Locator

**Returns:**
- The column number as an integer, or -1 if none is available.

**See Also:**
- Locator.getColumnNumber()

,

setColumnNumber(int)

---

#### public void setPublicId​(
String
publicId)

Set the public identifier for this locator.

**Parameters:**
- publicId

- The new public identifier, or null
if none is available.

**See Also:**
- getPublicId()

---

#### public void setSystemId​(
String
systemId)

Set the system identifier for this locator.

**Parameters:**
- systemId

- The new system identifier, or null
if none is available.

**See Also:**
- getSystemId()

---

#### public void setLineNumber​(int lineNumber)

Set the line number for this locator (1-based).

**Parameters:**
- lineNumber

- The line number, or -1 if none is available.

**See Also:**
- getLineNumber()

---

#### public void setColumnNumber​(int columnNumber)

Set the column number for this locator (1-based).

**Parameters:**
- columnNumber

- The column number, or -1 if none is available.

**See Also:**
- getColumnNumber()

---

### Additional Sections

#### Class LocatorImpl

java.lang.Object

- org.xml.sax.helpers.LocatorImpl

org.xml.sax.helpers.LocatorImpl

**All Implemented Interfaces:** Locator

**Direct Known Subclasses:** Locator2Impl

```java
public class
LocatorImpl

extends
Object

implements
Locator
```

Provide an optional convenience implementation of Locator.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class is available mainly for application writers, who
can use it to make a persistent snapshot of a locator at any
point during a document parse:

```java
Locator locator;
Locator startloc;

public void setLocator (Locator locator)
{
// note the locator
this.locator = locator;
}

public void startDocument ()
{
// save the location of the start of the document
// for future use.
Locator startloc = new LocatorImpl(locator);
}
```

Normally, parser writers will not use this class, since it
is more efficient to provide location information only when
requested, rather than constantly updating a Locator object.

**Since:** 1.4, SAX 1.0
**See Also:** Locator

public class

LocatorImpl

extends

Object

implements

Locator

Provide an optional convenience implementation of Locator.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class is available mainly for application writers, who
can use it to make a persistent snapshot of a locator at any
point during a document parse:

```java
Locator locator;
Locator startloc;

public void setLocator (Locator locator)
{
// note the locator
this.locator = locator;
}

public void startDocument ()
{
// save the location of the start of the document
// for future use.
Locator startloc = new LocatorImpl(locator);
}
```

Normally, parser writers will not use this class, since it
is more efficient to provide location information only when
requested, rather than constantly updating a Locator object.

This class is available mainly for application writers, who
can use it to make a persistent snapshot of a locator at any
point during a document parse:

Locator locator;
Locator startloc;

public void setLocator (Locator locator)
{
// note the locator
this.locator = locator;
}

public void startDocument ()
{
// save the location of the start of the document
// for future use.
Locator startloc = new LocatorImpl(locator);
}

Normally, parser writers will not use this class, since it
is more efficient to provide location information only when
requested, rather than constantly updating a Locator object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LocatorImpl

()

Zero-argument constructor.

LocatorImpl

​(

Locator

locator)

Copy constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Return the saved column number (1-based).

int

getLineNumber

()

Return the saved line number (1-based).

String

getPublicId

()

Return the saved public identifier.

String

getSystemId

()

Return the saved system identifier.

void

setColumnNumber

​(int columnNumber)

Set the column number for this locator (1-based).

void

setLineNumber

​(int lineNumber)

Set the line number for this locator (1-based).

void

setPublicId

​(

String

publicId)

Set the public identifier for this locator.

void

setSystemId

​(

String

systemId)

Set the system identifier for this locator.

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

Constructor Summary

Constructors

Constructor

Description

LocatorImpl

()

Zero-argument constructor.

LocatorImpl

​(

Locator

locator)

Copy constructor.

---

#### Constructor Summary

Zero-argument constructor.

Copy constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Return the saved column number (1-based).

int

getLineNumber

()

Return the saved line number (1-based).

String

getPublicId

()

Return the saved public identifier.

String

getSystemId

()

Return the saved system identifier.

void

setColumnNumber

​(int columnNumber)

Set the column number for this locator (1-based).

void

setLineNumber

​(int lineNumber)

Set the line number for this locator (1-based).

void

setPublicId

​(

String

publicId)

Set the public identifier for this locator.

void

setSystemId

​(

String

systemId)

Set the system identifier for this locator.

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

Return the saved column number (1-based).

Return the saved line number (1-based).

Return the saved public identifier.

Return the saved system identifier.

Set the column number for this locator (1-based).

Set the line number for this locator (1-based).

Set the public identifier for this locator.

Set the system identifier for this locator.

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

- LocatorImpl

```java
public LocatorImpl()
```

Zero-argument constructor.

This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

- LocatorImpl

```java
public LocatorImpl​(
Locator
locator)
```

Copy constructor.

Create a persistent copy of the current state of a locator.
When the original locator changes, this copy will still keep
the original values (and it can be used outside the scope of
DocumentHandler methods).

**Parameters:** locator

- The locator to copy.

============ METHOD DETAIL ==========

- Method Detail

- getPublicId

```java
public
String
getPublicId()
```

Return the saved public identifier.

**Specified by:** getPublicId

in interface

Locator
**Returns:** The public identifier as a string, or null if none
is available.
**See Also:** Locator.getPublicId()

,

setPublicId(java.lang.String)

- getSystemId

```java
public
String
getSystemId()
```

Return the saved system identifier.

**Specified by:** getSystemId

in interface

Locator
**Returns:** The system identifier as a string, or null if none
is available.
**See Also:** Locator.getSystemId()

,

setSystemId(java.lang.String)

- getLineNumber

```java
public int getLineNumber()
```

Return the saved line number (1-based).

**Specified by:** getLineNumber

in interface

Locator
**Returns:** The line number as an integer, or -1 if none is available.
**See Also:** Locator.getLineNumber()

,

setLineNumber(int)

- getColumnNumber

```java
public int getColumnNumber()
```

Return the saved column number (1-based).

**Specified by:** getColumnNumber

in interface

Locator
**Returns:** The column number as an integer, or -1 if none is available.
**See Also:** Locator.getColumnNumber()

,

setColumnNumber(int)

- setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this locator.

**Parameters:** publicId

- The new public identifier, or null
if none is available.
**See Also:** getPublicId()

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this locator.

**Parameters:** systemId

- The new system identifier, or null
if none is available.
**See Also:** getSystemId()

- setLineNumber

```java
public void setLineNumber​(int lineNumber)
```

Set the line number for this locator (1-based).

**Parameters:** lineNumber

- The line number, or -1 if none is available.
**See Also:** getLineNumber()

- setColumnNumber

```java
public void setColumnNumber​(int columnNumber)
```

Set the column number for this locator (1-based).

**Parameters:** columnNumber

- The column number, or -1 if none is available.
**See Also:** getColumnNumber()

Constructor Detail

- LocatorImpl

```java
public LocatorImpl()
```

Zero-argument constructor.

This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

- LocatorImpl

```java
public LocatorImpl​(
Locator
locator)
```

Copy constructor.

Create a persistent copy of the current state of a locator.
When the original locator changes, this copy will still keep
the original values (and it can be used outside the scope of
DocumentHandler methods).

**Parameters:** locator

- The locator to copy.

---

#### Constructor Detail

LocatorImpl

```java
public LocatorImpl()
```

Zero-argument constructor.

This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

---

#### LocatorImpl

public LocatorImpl()

Zero-argument constructor.

This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

LocatorImpl

```java
public LocatorImpl​(
Locator
locator)
```

Copy constructor.

Create a persistent copy of the current state of a locator.
When the original locator changes, this copy will still keep
the original values (and it can be used outside the scope of
DocumentHandler methods).

**Parameters:** locator

- The locator to copy.

---

#### LocatorImpl

public LocatorImpl​(

Locator

locator)

Copy constructor.

Create a persistent copy of the current state of a locator.
When the original locator changes, this copy will still keep
the original values (and it can be used outside the scope of
DocumentHandler methods).

Create a persistent copy of the current state of a locator.
When the original locator changes, this copy will still keep
the original values (and it can be used outside the scope of
DocumentHandler methods).

Method Detail

- getPublicId

```java
public
String
getPublicId()
```

Return the saved public identifier.

**Specified by:** getPublicId

in interface

Locator
**Returns:** The public identifier as a string, or null if none
is available.
**See Also:** Locator.getPublicId()

,

setPublicId(java.lang.String)

- getSystemId

```java
public
String
getSystemId()
```

Return the saved system identifier.

**Specified by:** getSystemId

in interface

Locator
**Returns:** The system identifier as a string, or null if none
is available.
**See Also:** Locator.getSystemId()

,

setSystemId(java.lang.String)

- getLineNumber

```java
public int getLineNumber()
```

Return the saved line number (1-based).

**Specified by:** getLineNumber

in interface

Locator
**Returns:** The line number as an integer, or -1 if none is available.
**See Also:** Locator.getLineNumber()

,

setLineNumber(int)

- getColumnNumber

```java
public int getColumnNumber()
```

Return the saved column number (1-based).

**Specified by:** getColumnNumber

in interface

Locator
**Returns:** The column number as an integer, or -1 if none is available.
**See Also:** Locator.getColumnNumber()

,

setColumnNumber(int)

- setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this locator.

**Parameters:** publicId

- The new public identifier, or null
if none is available.
**See Also:** getPublicId()

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this locator.

**Parameters:** systemId

- The new system identifier, or null
if none is available.
**See Also:** getSystemId()

- setLineNumber

```java
public void setLineNumber​(int lineNumber)
```

Set the line number for this locator (1-based).

**Parameters:** lineNumber

- The line number, or -1 if none is available.
**See Also:** getLineNumber()

- setColumnNumber

```java
public void setColumnNumber​(int columnNumber)
```

Set the column number for this locator (1-based).

**Parameters:** columnNumber

- The column number, or -1 if none is available.
**See Also:** getColumnNumber()

---

#### Method Detail

getPublicId

```java
public
String
getPublicId()
```

Return the saved public identifier.

**Specified by:** getPublicId

in interface

Locator
**Returns:** The public identifier as a string, or null if none
is available.
**See Also:** Locator.getPublicId()

,

setPublicId(java.lang.String)

---

#### getPublicId

public

String

getPublicId()

Return the saved public identifier.

getSystemId

```java
public
String
getSystemId()
```

Return the saved system identifier.

**Specified by:** getSystemId

in interface

Locator
**Returns:** The system identifier as a string, or null if none
is available.
**See Also:** Locator.getSystemId()

,

setSystemId(java.lang.String)

---

#### getSystemId

public

String

getSystemId()

Return the saved system identifier.

getLineNumber

```java
public int getLineNumber()
```

Return the saved line number (1-based).

**Specified by:** getLineNumber

in interface

Locator
**Returns:** The line number as an integer, or -1 if none is available.
**See Also:** Locator.getLineNumber()

,

setLineNumber(int)

---

#### getLineNumber

public int getLineNumber()

Return the saved line number (1-based).

getColumnNumber

```java
public int getColumnNumber()
```

Return the saved column number (1-based).

**Specified by:** getColumnNumber

in interface

Locator
**Returns:** The column number as an integer, or -1 if none is available.
**See Also:** Locator.getColumnNumber()

,

setColumnNumber(int)

---

#### getColumnNumber

public int getColumnNumber()

Return the saved column number (1-based).

setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this locator.

**Parameters:** publicId

- The new public identifier, or null
if none is available.
**See Also:** getPublicId()

---

#### setPublicId

public void setPublicId​(

String

publicId)

Set the public identifier for this locator.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this locator.

**Parameters:** systemId

- The new system identifier, or null
if none is available.
**See Also:** getSystemId()

---

#### setSystemId

public void setSystemId​(

String

systemId)

Set the system identifier for this locator.

setLineNumber

```java
public void setLineNumber​(int lineNumber)
```

Set the line number for this locator (1-based).

**Parameters:** lineNumber

- The line number, or -1 if none is available.
**See Also:** getLineNumber()

---

#### setLineNumber

public void setLineNumber​(int lineNumber)

Set the line number for this locator (1-based).

setColumnNumber

```java
public void setColumnNumber​(int columnNumber)
```

Set the column number for this locator (1-based).

**Parameters:** columnNumber

- The column number, or -1 if none is available.
**See Also:** getColumnNumber()

---

#### setColumnNumber

public void setColumnNumber​(int columnNumber)

Set the column number for this locator (1-based).

---

