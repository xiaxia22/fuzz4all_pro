# Class Locator2Impl

**Source:** `java.xml\org\xml\sax\ext\Locator2Impl.html`

### Class Description

```java
public class
Locator2Impl

extends
LocatorImpl

implements
Locator2
```

SAX2 extension helper for holding additional Entity information,
implementing the

Locator2

interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

This is not part of core-only SAX2 distributions.

**All Implemented Interfaces:** Locator2

,

Locator

---

### Field Details

*No entries found.*

### Constructor Details

#### public Locator2Impl()

Construct a new, empty Locator2Impl object.
This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

---

#### public Locator2Impl​(
Locator
locator)

Copy an existing Locator or Locator2 object.
If the object implements Locator2, values of the

encoding

and

version

strings are copied,
otherwise they set to

null

.

**Parameters:**
- locator

- The existing Locator object.

---

### Method Details

#### public
String
getXMLVersion()

Returns the current value of the version property.

**Specified by:**
- getXMLVersion

in interface

Locator2

**Returns:**
- Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.

**See Also:**
- setXMLVersion(java.lang.String)

---

#### public
String
getEncoding()

Returns the current value of the encoding property.

**Specified by:**
- getEncoding

in interface

Locator2

**Returns:**
- Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.

**See Also:**
- setEncoding(java.lang.String)

---

#### public void setXMLVersion​(
String
version)

Assigns the current value of the version property.

**Parameters:**
- version

- the new "version" value

**See Also:**
- getXMLVersion()

---

#### public void setEncoding​(
String
encoding)

Assigns the current value of the encoding property.

**Parameters:**
- encoding

- the new "encoding" value

**See Also:**
- getEncoding()

---

### Additional Sections

#### Class Locator2Impl

java.lang.Object

- org.xml.sax.helpers.LocatorImpl
- - org.xml.sax.ext.Locator2Impl

org.xml.sax.helpers.LocatorImpl

- org.xml.sax.ext.Locator2Impl

org.xml.sax.ext.Locator2Impl

**All Implemented Interfaces:** Locator2

,

Locator

```java
public class
Locator2Impl

extends
LocatorImpl

implements
Locator2
```

SAX2 extension helper for holding additional Entity information,
implementing the

Locator2

interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

This is not part of core-only SAX2 distributions.

**Since:** 1.5, SAX 2.0.2

public class

Locator2Impl

extends

LocatorImpl

implements

Locator2

SAX2 extension helper for holding additional Entity information,
implementing the

Locator2

interface.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

This is not part of core-only SAX2 distributions.

This is not part of core-only SAX2 distributions.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Locator2Impl

()

Construct a new, empty Locator2Impl object.

Locator2Impl

​(

Locator

locator)

Copy an existing Locator or Locator2 object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getEncoding

()

Returns the current value of the encoding property.

String

getXMLVersion

()

Returns the current value of the version property.

void

setEncoding

​(

String

encoding)

Assigns the current value of the encoding property.

void

setXMLVersion

​(

String

version)

Assigns the current value of the version property.

- Methods declared in class org.xml.sax.helpers.

LocatorImpl

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

,

setColumnNumber

,

setLineNumber

,

setPublicId

,

setSystemId

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

- Methods declared in interface org.xml.sax.

Locator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

Constructor Summary

Constructors

Constructor

Description

Locator2Impl

()

Construct a new, empty Locator2Impl object.

Locator2Impl

​(

Locator

locator)

Copy an existing Locator or Locator2 object.

---

#### Constructor Summary

Construct a new, empty Locator2Impl object.

Copy an existing Locator or Locator2 object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getEncoding

()

Returns the current value of the encoding property.

String

getXMLVersion

()

Returns the current value of the version property.

void

setEncoding

​(

String

encoding)

Assigns the current value of the encoding property.

void

setXMLVersion

​(

String

version)

Assigns the current value of the version property.

- Methods declared in class org.xml.sax.helpers.

LocatorImpl

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

,

setColumnNumber

,

setLineNumber

,

setPublicId

,

setSystemId

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

- Methods declared in interface org.xml.sax.

Locator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

---

#### Method Summary

Returns the current value of the encoding property.

Returns the current value of the version property.

Assigns the current value of the encoding property.

Assigns the current value of the version property.

Methods declared in class org.xml.sax.helpers.

LocatorImpl

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

,

setColumnNumber

,

setLineNumber

,

setPublicId

,

setSystemId

---

#### Methods declared in class org.xml.sax.helpers. LocatorImpl

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

Methods declared in interface org.xml.sax.

Locator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

---

#### Methods declared in interface org.xml.sax. Locator

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Locator2Impl

```java
public Locator2Impl()
```

Construct a new, empty Locator2Impl object.
This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

- Locator2Impl

```java
public Locator2Impl​(
Locator
locator)
```

Copy an existing Locator or Locator2 object.
If the object implements Locator2, values of the

encoding

and

version

strings are copied,
otherwise they set to

null

.

**Parameters:** locator

- The existing Locator object.

============ METHOD DETAIL ==========

- Method Detail

- getXMLVersion

```java
public
String
getXMLVersion()
```

Returns the current value of the version property.

**Specified by:** getXMLVersion

in interface

Locator2
**Returns:** Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.
**See Also:** setXMLVersion(java.lang.String)

- getEncoding

```java
public
String
getEncoding()
```

Returns the current value of the encoding property.

**Specified by:** getEncoding

in interface

Locator2
**Returns:** Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.
**See Also:** setEncoding(java.lang.String)

- setXMLVersion

```java
public void setXMLVersion​(
String
version)
```

Assigns the current value of the version property.

**Parameters:** version

- the new "version" value
**See Also:** getXMLVersion()

- setEncoding

```java
public void setEncoding​(
String
encoding)
```

Assigns the current value of the encoding property.

**Parameters:** encoding

- the new "encoding" value
**See Also:** getEncoding()

Constructor Detail

- Locator2Impl

```java
public Locator2Impl()
```

Construct a new, empty Locator2Impl object.
This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

- Locator2Impl

```java
public Locator2Impl​(
Locator
locator)
```

Copy an existing Locator or Locator2 object.
If the object implements Locator2, values of the

encoding

and

version

strings are copied,
otherwise they set to

null

.

**Parameters:** locator

- The existing Locator object.

---

#### Constructor Detail

Locator2Impl

```java
public Locator2Impl()
```

Construct a new, empty Locator2Impl object.
This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

---

#### Locator2Impl

public Locator2Impl()

Construct a new, empty Locator2Impl object.
This will not normally be useful, since the main purpose
of this class is to make a snapshot of an existing Locator.

Locator2Impl

```java
public Locator2Impl​(
Locator
locator)
```

Copy an existing Locator or Locator2 object.
If the object implements Locator2, values of the

encoding

and

version

strings are copied,
otherwise they set to

null

.

**Parameters:** locator

- The existing Locator object.

---

#### Locator2Impl

public Locator2Impl​(

Locator

locator)

Copy an existing Locator or Locator2 object.
If the object implements Locator2, values of the

encoding

and

version

strings are copied,
otherwise they set to

null

.

Method Detail

- getXMLVersion

```java
public
String
getXMLVersion()
```

Returns the current value of the version property.

**Specified by:** getXMLVersion

in interface

Locator2
**Returns:** Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.
**See Also:** setXMLVersion(java.lang.String)

- getEncoding

```java
public
String
getEncoding()
```

Returns the current value of the encoding property.

**Specified by:** getEncoding

in interface

Locator2
**Returns:** Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.
**See Also:** setEncoding(java.lang.String)

- setXMLVersion

```java
public void setXMLVersion​(
String
version)
```

Assigns the current value of the version property.

**Parameters:** version

- the new "version" value
**See Also:** getXMLVersion()

- setEncoding

```java
public void setEncoding​(
String
encoding)
```

Assigns the current value of the encoding property.

**Parameters:** encoding

- the new "encoding" value
**See Also:** getEncoding()

---

#### Method Detail

getXMLVersion

```java
public
String
getXMLVersion()
```

Returns the current value of the version property.

**Specified by:** getXMLVersion

in interface

Locator2
**Returns:** Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.
**See Also:** setXMLVersion(java.lang.String)

---

#### getXMLVersion

public

String

getXMLVersion()

Returns the current value of the version property.

getEncoding

```java
public
String
getEncoding()
```

Returns the current value of the encoding property.

**Specified by:** getEncoding

in interface

Locator2
**Returns:** Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.
**See Also:** setEncoding(java.lang.String)

---

#### getEncoding

public

String

getEncoding()

Returns the current value of the encoding property.

setXMLVersion

```java
public void setXMLVersion​(
String
version)
```

Assigns the current value of the version property.

**Parameters:** version

- the new "version" value
**See Also:** getXMLVersion()

---

#### setXMLVersion

public void setXMLVersion​(

String

version)

Assigns the current value of the version property.

setEncoding

```java
public void setEncoding​(
String
encoding)
```

Assigns the current value of the encoding property.

**Parameters:** encoding

- the new "encoding" value
**See Also:** getEncoding()

---

#### setEncoding

public void setEncoding​(

String

encoding)

Assigns the current value of the encoding property.

---

