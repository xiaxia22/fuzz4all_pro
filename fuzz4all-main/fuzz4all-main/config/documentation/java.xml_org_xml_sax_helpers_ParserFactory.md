# Class ParserFactory

**Source:** `java.xml\org\xml\sax\helpers\ParserFactory.html`

### Class Description

```java
@Deprecated
(
since
="1.5")
public class
ParserFactory

extends
Object
```

Java-specific class for dynamically loading SAX parsers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

Note:

This class is designed to work with the now-deprecated
SAX1

Parser

class. SAX2 applications should use

XMLReaderFactory

instead.

ParserFactory is not part of the platform-independent definition
of SAX; it is an additional convenience class designed
specifically for Java XML application writers. SAX applications
can use the static methods in this class to allocate a SAX parser
dynamically at run-time based either on the value of the
`org.xml.sax.parser' system property or on a string containing the class
name.

Note that the application still requires an XML parser that
implements SAX1.

**Since:** 1.4, SAX 1.0

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Parser
makeParser()
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

NullPointerException
,

ClassCastException

Create a new SAX parser using the `org.xml.sax.parser' system property.

The named class must exist and must implement the

Parser

interface.

**Throws:**
- NullPointerException

- There is no value
for the `org.xml.sax.parser' system property.
- ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
- IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
- InstantiationException

- The SAX parser class was
found but could not be instantiated.
- ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.

**See Also:**
- makeParser(java.lang.String)

,

Parser

---

#### public static
Parser
makeParser​(
String
className)
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

ClassCastException

Create a new SAX parser object using the class name provided.

The named class must exist and must implement the

Parser

interface.

**Parameters:**
- className

- A string containing the name of the
SAX parser class.

**Throws:**
- ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
- IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
- InstantiationException

- The SAX parser class was
found but could not be instantiated.
- ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.

**See Also:**
- makeParser()

,

Parser

---

### Additional Sections

#### Class ParserFactory

java.lang.Object

- org.xml.sax.helpers.ParserFactory

org.xml.sax.helpers.ParserFactory

```java
@Deprecated
(
since
="1.5")
public class
ParserFactory

extends
Object
```

Deprecated.

This class works with the deprecated

Parser

interface.

Java-specific class for dynamically loading SAX parsers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

Note:

This class is designed to work with the now-deprecated
SAX1

Parser

class. SAX2 applications should use

XMLReaderFactory

instead.

ParserFactory is not part of the platform-independent definition
of SAX; it is an additional convenience class designed
specifically for Java XML application writers. SAX applications
can use the static methods in this class to allocate a SAX parser
dynamically at run-time based either on the value of the
`org.xml.sax.parser' system property or on a string containing the class
name.

Note that the application still requires an XML parser that
implements SAX1.

**Since:** 1.4, SAX 1.0

@Deprecated

(

since

="1.5")
public class

ParserFactory

extends

Object

Java-specific class for dynamically loading SAX parsers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

Note:

This class is designed to work with the now-deprecated
SAX1

Parser

class. SAX2 applications should use

XMLReaderFactory

instead.

ParserFactory is not part of the platform-independent definition
of SAX; it is an additional convenience class designed
specifically for Java XML application writers. SAX applications
can use the static methods in this class to allocate a SAX parser
dynamically at run-time based either on the value of the
`org.xml.sax.parser' system property or on a string containing the class
name.

Note that the application still requires an XML parser that
implements SAX1.

Note:

This class is designed to work with the now-deprecated
SAX1

Parser

class. SAX2 applications should use

XMLReaderFactory

instead.

ParserFactory is not part of the platform-independent definition
of SAX; it is an additional convenience class designed
specifically for Java XML application writers. SAX applications
can use the static methods in this class to allocate a SAX parser
dynamically at run-time based either on the value of the
`org.xml.sax.parser' system property or on a string containing the class
name.

Note that the application still requires an XML parser that
implements SAX1.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Parser

makeParser

()

Deprecated.

Create a new SAX parser using the `org.xml.sax.parser' system property.

static

Parser

makeParser

​(

String

className)

Deprecated.

Create a new SAX parser object using the class name provided.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Parser

makeParser

()

Deprecated.

Create a new SAX parser using the `org.xml.sax.parser' system property.

static

Parser

makeParser

​(

String

className)

Deprecated.

Create a new SAX parser object using the class name provided.

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

Deprecated.

Create a new SAX parser using the `org.xml.sax.parser' system property.

Create a new SAX parser object using the class name provided.

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

============ METHOD DETAIL ==========

- Method Detail

- makeParser

```java
public static
Parser
makeParser()
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

NullPointerException
,

ClassCastException
```

Deprecated.

Create a new SAX parser using the `org.xml.sax.parser' system property.

The named class must exist and must implement the

Parser

interface.

**Throws:** NullPointerException

- There is no value
for the `org.xml.sax.parser' system property.
**Throws:** ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
**Throws:** IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
**Throws:** InstantiationException

- The SAX parser class was
found but could not be instantiated.
**Throws:** ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.
**See Also:** makeParser(java.lang.String)

,

Parser

- makeParser

```java
public static
Parser
makeParser​(
String
className)
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

ClassCastException
```

Deprecated.

Create a new SAX parser object using the class name provided.

The named class must exist and must implement the

Parser

interface.

**Parameters:** className

- A string containing the name of the
SAX parser class.
**Throws:** ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
**Throws:** IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
**Throws:** InstantiationException

- The SAX parser class was
found but could not be instantiated.
**Throws:** ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.
**See Also:** makeParser()

,

Parser

Method Detail

- makeParser

```java
public static
Parser
makeParser()
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

NullPointerException
,

ClassCastException
```

Deprecated.

Create a new SAX parser using the `org.xml.sax.parser' system property.

The named class must exist and must implement the

Parser

interface.

**Throws:** NullPointerException

- There is no value
for the `org.xml.sax.parser' system property.
**Throws:** ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
**Throws:** IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
**Throws:** InstantiationException

- The SAX parser class was
found but could not be instantiated.
**Throws:** ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.
**See Also:** makeParser(java.lang.String)

,

Parser

- makeParser

```java
public static
Parser
makeParser​(
String
className)
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

ClassCastException
```

Deprecated.

Create a new SAX parser object using the class name provided.

The named class must exist and must implement the

Parser

interface.

**Parameters:** className

- A string containing the name of the
SAX parser class.
**Throws:** ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
**Throws:** IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
**Throws:** InstantiationException

- The SAX parser class was
found but could not be instantiated.
**Throws:** ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.
**See Also:** makeParser()

,

Parser

---

#### Method Detail

makeParser

```java
public static
Parser
makeParser()
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

NullPointerException
,

ClassCastException
```

Deprecated.

Create a new SAX parser using the `org.xml.sax.parser' system property.

The named class must exist and must implement the

Parser

interface.

**Throws:** NullPointerException

- There is no value
for the `org.xml.sax.parser' system property.
**Throws:** ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
**Throws:** IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
**Throws:** InstantiationException

- The SAX parser class was
found but could not be instantiated.
**Throws:** ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.
**See Also:** makeParser(java.lang.String)

,

Parser

---

#### makeParser

public static

Parser

makeParser()
throws

ClassNotFoundException

,

IllegalAccessException

,

InstantiationException

,

NullPointerException

,

ClassCastException

Create a new SAX parser using the `org.xml.sax.parser' system property.

The named class must exist and must implement the

Parser

interface.

The named class must exist and must implement the

Parser

interface.

makeParser

```java
public static
Parser
makeParser​(
String
className)
throws
ClassNotFoundException
,

IllegalAccessException
,

InstantiationException
,

ClassCastException
```

Deprecated.

Create a new SAX parser object using the class name provided.

The named class must exist and must implement the

Parser

interface.

**Parameters:** className

- A string containing the name of the
SAX parser class.
**Throws:** ClassNotFoundException

- The SAX parser
class was not found (check your CLASSPATH).
**Throws:** IllegalAccessException

- The SAX parser class was
found, but you do not have permission to load
it.
**Throws:** InstantiationException

- The SAX parser class was
found but could not be instantiated.
**Throws:** ClassCastException

- The SAX parser class
was found and instantiated, but does not implement
org.xml.sax.Parser.
**See Also:** makeParser()

,

Parser

---

#### makeParser

public static

Parser

makeParser​(

String

className)
throws

ClassNotFoundException

,

IllegalAccessException

,

InstantiationException

,

ClassCastException

Create a new SAX parser object using the class name provided.

The named class must exist and must implement the

Parser

interface.

The named class must exist and must implement the

Parser

interface.

---

